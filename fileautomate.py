from configparser import ExtendedInterpolation
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

# print(os.path.splitext(os.listdir(src)[0]))

# if os.path.exists(dest):
#     print("directory exists")
#     shutil.move(src, dest)
# else:
#     os.makedirs(dest)
#     print("New directory made")
#     shutil.move(src, dest)

for file in os.listdir(src):
    extension = os.path.splitext(file)[1]
    if extension == ".exe" or extension == ".msi":
        print(file + " is an installation")
    elif extension == ".mp4" or extension == ".avi" or extension == ".mov" or extension == ".mp3":
        print(file + " is a media file")
    elif extension == ".jpg" or extension == ".png" or extension == ".svg":
        print(file + " is an image file")
    elif extension == ".pdf" or extension == ".doc" or extension == ".docx" or extension == ".ppt" or extension == ".pptx":
        print(file + " is a document")
    elif extension == ".7z" or extension == ".zip":
        print(file + " is a zipped file")


