import json

from tkinter import Tk, Label, Button, filedialog, Text, StringVar
class FolderFileManager:
    def __init__(self, master):
        self.master = master
        master.title("Matt's Big Adventure")
        master.geometry('500x500')

        self.label = Label(master, text="This is our first GUI!")
        self.label.grid()

        self.folder_button = Button(master, text="Select folder to watch", command=self.select_watch_folder)
        self.folder_button.grid(row=0,column=0)
        
        self.v = StringVar()
        self.folder_text =  Label(master,textvariable=self.v)

        
        self.close_button = Button(master, text="Close", command=master.quit)


        self.close_button.grid()
        self.folder_button.grid()



    def select_watch_folder(self):
        folder_to_watch = filedialog.askdirectory()
        self.v.set(folder_to_watch)
        self.update_configuration(folder_to_watch)

    def update_configuration(self,sourcefolder):
        print("Updating Configuration")
        jsonFile = open("config.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        tmp = data["source_folders"] 
        data["source_folders"] = sourcefolder
        #data["mode"] = "replay"

        ## Save our changes to JSON file
        jsonFile = open("config.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

root = Tk()
my_gui = FolderFileManager(root)
root.mainloop()