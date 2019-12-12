import sys
import time
import os
import json
import logging
import ntpath

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

with open('config.json') as config_file:
    data = json.load(config_file)

source_folders = data['source_folders']
target_folders = data['target_folders']
picture_folder = data['pictures_folder']
music_folder = data['music_folder']

class Utils(PatternMatchingEventHandler):
    
    def on_any_event(self,event):
        print('anything')

    # def on_modified(self,event):
    #     for filename in os.listdir(folder_to_track):
    #         src = folder_to_track + "/" + filename
    #         new_destination = folder_destination + "/" + filename
    #         try:
    #             os.rename(src,new_destination)
    #         except:
    #             print('uh oh ')
    
    # def on_moved(self,event):
    #     print('moved')

    # def on_deleted(self,event):
    #     print('deleted')

    def on_created(self,event):
        src_path = event.src_path
        filename, file_extension = os.path.splitext(src_path)
        filename2 = os.path.basename(src_path)
        filename3,filename4 = os.path.splitext(filename2) # ntpath.basename(event.src_path)
        new_destination = folder_destination + "/" + filename
        # for filename in os.listdir(folder_to_track):
        #     src = folder_to_track + "/" + filename
        #     new_destination = folder_destination + "/" + filename
            # try:
            #     os.rename(src,new_destination)
            # except:
            #     print('uh oh')
        if (file_extension == '.txt'):
            try:
                os.rename(src_path, new_destination)
            except:
                print('uh oh')
        elif (file_extension == '.mp4'):
            new_destination = music_folder
            try:
                os.rename(src_path,new_destination)
            except:
                print('uh oh')                
        elif (file_extension == '.jpg' or file_extension == '.png'):
            new_destination = picture_folder
            try:
                os.rename(src_path,new_destination + '/' + filename)
            except Exception as e:
                print('uh oh')
        
folder_to_track = source_folders
folder_destination = target_folders

event_handler = Utils()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()