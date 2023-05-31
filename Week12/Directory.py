import os
import shutil

os.mkdir("C:\Python_Workspace\Week12\myDir")
os.mkdir("C:\Python_Workspace\Week12\myDir\dir1")
shutil.rmtree("C:\Python_Workspace\Week12\myDir")  # 폴더 안의 모든 파일 삭제

# 파일 및 디렉토리 복사
import shutil

shutil.copy("C:/Windows/notepad.exe", "C:/Temp/myNote.exe")

# 파일 또는 디렉토리가 이미 존재하는지 확인
import os.path

print(os.path.exists("C:/Windows/notepad.exe"))
print(os.path.isfile("C:/Windows/notepad.exe"))
print(os.path.isdir("C:/Windows"))
