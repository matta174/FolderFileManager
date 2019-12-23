import sys
import time
import os
import json
import logging
import ntpath
import shutil


with open('config.json') as config_file:
    data = json.load(config_file)
source_folder = data['source_folder']
documents_folder = data['documents_folder']
picture_folder = data['pictures_folder']
music_folder = data['music_folder']
folder_to_track = source_folder
folder_destination = ""


class Utilities():
    image_dict = ['.img','.jpg','.jpeg','.png','.apng','.bmp','.gif','.ico','.cur','.jfif','.pjpeg','.pjp','.svg','.tif','.tiff','.webp']
    sound_dict = ['.3gp','.aa','.aac','.aax','.act','.aiff','.alac','.amr','.ape','.au','.awb','.dct','.dss','.dvf','.flac','.gsm','.iklax','.ivs','.m4a','.m4b','.m4p','.mmf','.mp3','.mpc','.msv','.nmf','.nsf','.ogg','.oga','.mogg','.opus','.raw','.sln','.tta','.voc','.vox','.wav','.wma','.wv','.webm','.8svx']
    document_dict = ['.doc','.docx','.xls','.xlsx','.pdf','.html','.txt','.pptx','.ppt','.pps','.odp']

    def run_on_folder(self):
        for filename in os.listdir(source_folder):
            src_path = folder_to_track + "/" + filename
            full_filename = os.path.basename(src_path)
            try:
                self.check_file_type(src_path,full_filename)
            except Exception as e: print(e)

    def on_event(self,event):
        try:
            src_path = event.src_path
            full_filename = os.path.basename(src_path)
            self.check_file_type(src_path,full_filename)
        except Exception as e: print(e)
    
    def check_file_type(self,src_path,full_filename):
        filename,file_extension= os.path.splitext(full_filename)

        if (file_extension in self.document_dict):
            new_full_filename = documents_folder + '/' + full_filename
            try:
                self.move_file(src_path, new_full_filename)
            except Exception as e: print(e)
        elif (file_extension in self.sound_dict):
            new_full_filename = music_folder + '/' + full_filename
            try:
                self.move_file(src_path,new_full_filename)
            except Exception as e: print(e)
        elif (file_extension in self.image_dict):
            new_full_filename = picture_folder + '/' + full_filename
            try:
                self.move_file(src_path,new_full_filename)
            except Exception as e: print(e)


    def move_file(self, src, file_to_move):
        try:
            shutil.move(src,file_to_move)
        except Exception as e: print(e)
