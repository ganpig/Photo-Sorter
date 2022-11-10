import exifread
import os
from easygui import diropenbox

in_dir = diropenbox('选择输入文件夹')
out_dir = diropenbox('选择输出文件夹')

for dirpath, dirnames, filenames in os.walk(in_dir):
    pic = 1
    vid = 1
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        new_path = ''
        if filename.lower().endswith('.jpg'):
            tags = exifread.process_file(open(file_path, 'rb'))
            if 'EXIF DateTimeOriginal' in tags:
                new_name = str(tags['EXIF DateTimeOriginal']).replace(
                    ':', '').replace(' ', '_')
            else:
                new_name = str(pic).zfill(2)
                pic += 1
            new_path = os.path.join(
                dirpath.replace(in_dir, out_dir), new_name + '.jpg')
        elif filename.startswith('VID_') or filename.startswith('IMG_'):
            new_path = os.path.join(
                dirpath.replace(in_dir, out_dir), filename[4:])
        else:
            new_path = os.path.join(
                dirpath.replace(in_dir, out_dir), filename)
        print(new_path)
        new_dir = os.path.dirname(new_path)
        if not os.path.isdir(new_dir):
            os.makedirs(new_dir)
        os.system(f'copy "{file_path}" "{new_path}"')
