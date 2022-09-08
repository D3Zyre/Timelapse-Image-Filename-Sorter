# Timelapse-Image-Filename-Sorter
Copies all files in a directory (and its subdirectories), sorts them by date created, renames them in that order, starting with G00000001 (followed by whatever extension was there before), and copies to a new directory.

you'll need os, shutil, and time.

should work on any python3, but if you have problems try python3 version 3.10