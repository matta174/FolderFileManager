import sys
import time
import os
import json
import logging
import ntpath
import shutil

from Utilities import Utilities
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

with open('config.json') as config_file:
    data = json.load(config_file)
source_folder = data['source_folder']
folder_to_track = source_folder

class WatchDog(PatternMatchingEventHandler):
    Utils = Utilities()
    def on_created(self,event):
        try:
            src_path = event.src_path
            full_filename = os.path.basename(src_path)
            self.Utils.check_file_type(src_path,full_filename)
        except Exception as e: print(e)



class Main():
    event_handler = WatchDog()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()