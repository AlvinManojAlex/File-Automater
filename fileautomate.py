import os
import shutil
from dotenv import load_dotenv
load_dotenv()

src = os.getenv("src_path")
dest_media = os.getenv("dest_media")
dest_img = os.getenv("dest_img")
dest_exe = os.getenv("dest_exe")
dest_zip = os.getenv("dest_zip")
dest_doc = os.getenv("dest_docs")

# src = r""
# dest_media = src +"\\Media_files"
# dest_exe = src + "\\Installation_Files"
# dest_img = src + "\\Image_Files"
# dest_zip = src + "\\Zip"
# dest_doc = src + "\\Documents"

for file in os.listdir(src):
    extension = os.path.splitext(file)[1]
    if extension == ".exe" or extension == ".msi":
        if not os.path.exists(dest_exe):
            os.makedirs(dest_exe)
        if not os.path.exists(dest_exe+"\\"+file):
            shutil.move(src+"\\"+file, dest_exe)
        else:
            os.remove(dest_exe+"\\"+file)
            shutil.move(src+"\\"+file, dest_exe)

    elif extension == ".mp4" or extension == ".avi" or extension == ".mov" or extension == ".mp3":
        if not os.path.exists(dest_media):
            os.makedirs(dest_media)
        if not os.path.exists(dest_media+"\\"+file):
            shutil.move(src+"\\"+file, dest_media)
        else:
            os.remove(dest_media+"\\"+file)
            shutil.move(src+"\\"+file, dest_media)

    elif extension == ".jpg" or extension == ".png" or extension == ".svg":
        if not os.path.exists(dest_img):
            os.makedirs(dest_img)
        if not os.path.exists(dest_img+"\\"+file):
            shutil.move(src+"\\"+file, dest_img)
        else:
            os.remove(dest_img+"\\"+file)
            shutil.move(src+"\\"+file, dest_img)

    elif extension == ".pdf" or extension == ".doc" or extension == ".docx" or extension == ".ppt" or extension == ".pptx":
        if not os.path.exists(dest_doc):
            os.makedirs(dest_doc)
        if not os.path.exists(dest_doc+"\\"+file):
            shutil.move(src+"\\"+file, dest_doc)
        else:
            os.remove(dest_doc+"\\"+file)
            shutil.move(src+"\\"+file, dest_doc)

    elif extension == ".7z" or extension == ".zip":
        if not os.path.exists(dest_zip):
            os.makedirs(dest_zip)
        if not os.path.exists(dest_zip+"\\"+file):
            shutil.move(src+"\\"+file, dest_zip)
        else:
            os.remove(dest_zip+"\\"+file)
            shutil.move(src+"\\"+file, dest_zip)
