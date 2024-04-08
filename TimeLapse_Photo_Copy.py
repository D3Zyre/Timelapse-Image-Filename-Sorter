import os
from shutil import copy2
import time

count = 0
total_size = 0
files = list()
input_path = str(input("\n\nPaste full input path here:\n\n"))
output_path = str(input("\n\nPaste full output path here:\n\n"))
if (not os.path.exists(output_path)):
    os.makedirs(output_path)

for path, dir, path_files in os.walk(input_path):
    [files.append((i, os.stat(path+"/"+i).st_mtime, path, os.stat(path+"/"+i).st_size)) for i in path_files if i.endswith((".JPG", ".jpg", ".PNG", ".png"))]
total_files = len(files) # for stats/progress
total_total_size = sum([file[3] for file in files]) # for stats/progress

print("\n\nSorting Files...\n")
files = sorted(files, key=lambda tup: tup[1], reverse=False) # sort by date, you might have to flip the true/false?
paths = [i[2] for i in files]
files = [i[0] for i in files]
print("\n\nCopying Files...\n")
n = -1
t = time.time()
for file in files:
    n += 1
    path = paths[n]
    count += 1
    filename = "G{}.{}".format(str(count).zfill(8), str(file).split(".")[-1])
    destination = os.path.abspath(output_path+"/"+filename)
    size_of_file = os.stat(path+"/"+file)[6]
    total_size += int(size_of_file)
    current_time = time.time() - t
    try:
        print("\r{:6.2f}%         at {:.1f} files per second        {:.1f}MB/s          size: {:.1f}/{:.1f}MB        file {}/{}         {:.1f} minutes remaining...              ".format(total_size/total_total_size*100, count/current_time, total_size/current_time/1000000, total_size/1000000, total_total_size/1000000 , count, total_files, (total_total_size-total_size)/(total_size/current_time)/60), end="")
    except ZeroDivisionError:
        pass
    copy2(path+"/"+file, destination)
