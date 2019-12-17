import json

from tkinter import Tk, Label, Button, filedialog, Text, StringVar, dialog
class FolderFileManager:

    def __init__(self, master):
        self.master = master
        master.title("Folder Shepherd")
        master.geometry('300x300')


        self.label = Label(master,text="Source folder: ")
        self.source_folder_button = Button(master, text="Select folder to watch", command=self.select_watch_folder)

        self.label2 = Label(master,text="Target folder: ")
        self.target_folder_button = Button(master,text="Select folder to place files", command=self.select_target_folder)
        
        self.v = StringVar()
        self.folder_text =  Label(master,textvariable=self.v)

        self.v2 = StringVar()
        self.target_folder_text = Label(master,textvariable=self.v2)
        
        
        self.close_button = Button(master, text="Close", command=master.quit)

        self.save_button = Button(master,text='Save', command=self.update_configuration)

        self.source_folder_button.grid(row=1,column=2)
        self.folder_text.grid(row=4,column=2)
        self.target_folder_text.grid(row=5,column=2)
        self.label.grid(row=4,column=1)
        self.label2.grid(row=5,column=1)
        self.save_button.grid(row=6,column=2)
        self.close_button.grid(row=7,column=2)
        self.target_folder_button.grid(row=2,column=2)
        # self.source_folder_button.grid()



    def select_watch_folder(self):
        sourcefolder = filedialog.askdirectory()
        self.v.set(sourcefolder)
        # self.update_configuration(folder_to_watch)
    def select_target_folder(self):
        targetfolder = filedialog.askdirectory()
        self.v2.set(targetfolder)

    def update_configuration(self):
        print("Updating Configuration")
        jsonFile = open("config.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        tmp = data["source_folders"] 
        data["source_folders"] = self.v.get()
        data["target_folders"] = self.v2.get()
        #data["mode"] = "replay"

        ## Save our changes to JSON file
        jsonFile = open("config.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

root = Tk()
my_gui = FolderFileManager(root)
root.mainloop()