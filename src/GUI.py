import json
import tkinter as tk
from tkinter import Tk, Label, Button, filedialog, Text, StringVar, dialog
class FolderFileManager(tk.Frame):

    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self,self.master)
        self.configure_gui()

        # Source Folder Section

        self.label = Label(master,text="Source Folder: ")
        self.label.grid(row=4,column=1)

        self.v = StringVar(value=self.source_folder)

        self.source_folder_button = Button(master, text="Select folder to watch", command=self.select_watch_folder)
        self.source_folder_button.grid(row=4,column=0,padx=10)

        self.folder_text =  Label(master,textvariable=self.v)
        self.folder_text.grid(row=4,column=2)

        # Image Folder Section
        self.label2 = Label(master,text="Image Folder: ")
        self.label2.grid(row=7,column=1,pady=10)

        self.pictures_folder_button = Button(master,text="Select folder to place images", command=self.select_picture_folder)
        self.pictures_folder_button.grid(row=7,column=0,padx=10)

        self.v2 = StringVar(value=self.picture_folder)
        
        self.target_picture_text = Label(master,textvariable=self.v2)
        self.target_picture_text.grid(row=7,column=2,pady=10)

        # Music Folder Section
        self.label3 = Label(master,text="Music Folder: ")
        self.label3.grid(row=8,column=1,pady=10)

        self.music_folder_button = Button(master,text="Select folder to place music files", command=self.select_music_folder)
        self.music_folder_button.grid(row=8,column=0,padx=10)


        self.v3 = StringVar(value=self.music_folder)

        self.target_music_text = Label(master,textvariable=self.v3)
        self.target_music_text.grid(row=8,column=2,pady=10)

        # Documents Folder Section
        self.label4 = Label(master,text="Documents Folder: ")
        self.label4.grid(row=9,column=1,pady=10)

        self.documents_folder_button = Button(master,text="Select folder to place document files", command=self.select_documents_folder)
        self.documents_folder_button.grid(row=9,column=0,padx=10)


        self.v4 = StringVar(value=self.documents_folder)

        self.target_documents_text = Label(master,textvariable=self.v4)
        self.target_documents_text.grid(row=9,column=2,pady=10)

        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=10,column=2)

        self.save_button = Button(master,text='Save', command=self.update_configuration)
        self.save_button.grid(row=10,column=1)


    def configure_gui(self):
        self.master.title("Folder Shepherd")
        self.master.geometry("")
        self.master.resizable(False,False)
        self.master.iconbitmap(r"src\\images\\fileshepherd.ico")
        img = tk.PhotoImage(file = r"src\\images\\fileshepherd.ico")
        # self.master.tk.call('wm', 'iconphoto', self.master._w, img)


        with open('config.json') as config_file:
            data = json.load(config_file)
        self.source_folder = data['source_folder']
        self.documents_folder = data['documents_folder']
        self.picture_folder = data['pictures_folder']
        self.music_folder = data['music_folder']

    def select_watch_folder(self):
        sourcefolder = filedialog.askdirectory()
        self.v.set(sourcefolder)

    def select_picture_folder(self):
        targetfolder = filedialog.askdirectory()
        self.v2.set(targetfolder)

    def select_music_folder(self):
        targetfolder = filedialog.askdirectory()
        self.v3.set(targetfolder)

    def select_documents_folder(self):
        targetfolder = filedialog.askdirectory()
        self.v4.set(targetfolder)

    def update_configuration(self):
        print("Updating Configuration")
        jsonFile = open("config.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        tmp = data["source_folder"] 
        data["source_folder"] = self.v.get()
        data["pictures_folder"] = self.v2.get()
        data['music_folder'] = self.v3.get()
        data['documents_folder'] = self.v4.get()
        #data["mode"] = "replay"

        ## Save our changes to JSON file
        jsonFile = open("config.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()


if __name__ == '__main__':
   root = tk.Tk()
   main_app =  FolderFileManager(root)
   root.mainloop()