import sys
import time
import os
import json
import logging
import ntpath
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

with open('config.json') as config_file:
    data = json.load(config_file)

source_folder = data['source_folder']
documents_folder = data['documents_folder']
picture_folder = data['pictures_folder']
music_folder = data['music_folder']

class Utils(PatternMatchingEventHandler):

    # def on_any_event(self,event):
    #     print('anything' + str(event))

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
        
        full_filename = os.path.basename(src_path)
        filename,file_extension= os.path.splitext(full_filename) 
        new_full_filename = folder_destination + "/" + full_filename

        image_dict = ['.img','.jpg','.jpeg','.png','.apng','.bmp','.gif','.ico','.cur','.jfif','.pjpeg','.pjp','.svg','.tif','.tiff','.webp']
        sound_dict = ['.3gp','.aa','.aac','.aax','.act','.aiff','.alac','.amr','.ape','.au','.awb','.dct','.dss','.dvf','.flac','.gsm','.iklax','.ivs','.m4a','.m4b','.m4p','.mmf','.mp3','.mpc','.msv','.nmf','.nsf','.ogg','.oga','.mogg','.opus','.raw','.sln','.tta','.voc','.vox','.wav','.wma','.wv','.webm','.8svx']
        document_dict = ['.doc','.docx','.xls','.xlsx','.pdf','.html','.txt','.pptx','.ppt','.pps','.odp']

        if (file_extension in document_dict):
            new_full_filename = documents_folder + '/' + full_filename
            try:
                shutil.move(src_path, new_full_filename)
            except Exception as e: print(e)
        elif (file_extension in sound_dict):
            new_full_filename = music_folder + '/' + full_filename
            try:
                shutil.move(src_path,new_full_filename)
            except Exception as e: print(e)

        elif (file_extension in image_dict):
            new_full_filename = picture_folder + '/' + full_filename
            try:
                shutil.move(src_path,new_full_filename)
            except Exception as e: print(e)
        
    # def on_modified(self,event):
    #     for filename in os.listdir(folder_to_track):
    #         src = folder_to_track + "/" + filename
    #         new_destination = folder_destination + "/" + filename
    #         try:
    #             os.rename(src,new_destination)
    #         except:
    #             print('uh oh ')
    

folder_to_track = source_folder
folder_destination = ""

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