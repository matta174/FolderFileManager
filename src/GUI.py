import json

from tkinter import Tk, Label, Button
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Matt's Big Adventure")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.update_configuration)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def update_configuration(self):
        print("Updating Configuration")
        jsonFile = open("config.json", "r") # Open the JSON file for reading
        data = json.load(jsonFile) # Read the JSON into the buffer
        jsonFile.close() # Close the JSON file

        ## Working with buffered content
        tmp = data["source_folders"] 
        data["source_folders"] = 'C:/notreal'
        data["mode"] = "replay"

        ## Save our changes to JSON file
        jsonFile = open("config.json", "w+")
        jsonFile.write(json.dumps(data))
        jsonFile.close()

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()