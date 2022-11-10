import exifread
import os
import pygame
from easygui import diropenbox

in_dir = diropenbox('选择输入文件夹')
out_dir = diropenbox('选择输出文件夹')

for dirpath, dirnames, filenames in os.walk(in_dir):
    for filename in filenames:
        new_path = ''
        if filename.lower().endswith('.jpg'):
            file_path = os.path.join(dirpath, filename)
            tags = exifread.process_file(open(file_path, 'rb'))
            if 'EXIF DateTimeOriginal' in tags:
                new_dir = str(tags['EXIF DateTimeOriginal'])[
                    :7].replace(':', '.')
                new_path = os.path.join(out_dir, new_dir, filename)
                if not os.path.exists(os.path.dirname(new_path)):
                    os.makedirs(os.path.dirname(new_path))
                try:
                    os.rename(file_path, new_path)
                except FileExistsError:
                    print('文件已存在：', file_path)
                    continue
