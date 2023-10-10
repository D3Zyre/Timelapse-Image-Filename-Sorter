import os
from shutil import copy2
import time

def get_num_files(path, print_stats_every_x_seconds = 1):
    """
    Counts the number of files in a directory using os.walk
    set print_stats_every_x_seconds to -1 to never print
    """
    num_files = 0
    t = time.time()
    if print_stats_every_x_seconds != -1:
        print("\nChecking number of files for path "+str(path)+"...\n")
    for path, dir, file in os.walk(os.path.expanduser(path)):
        num_files += len(file)
        if time.time() - t >= print_stats_every_x_seconds and print_stats_every_x_seconds != -1:
            print("\r" + str(num_files) + " files...", end="")
            t = time.time()

    return num_files

def get_size_folder(path, print_stats_every_x_seconds = 1):
    """
    gets the size of the folder
    set print_stats_every_x_seconds to -1 to never print
    """
    size = 0
    t = time.time()
    if print_stats_every_x_seconds != -1:
        print("\nChecking size of path "+str(path)+"...\n")
    for path, dir, files in os.walk(os.path.expanduser(path)):
        size += sum([os.stat(str(path)+"/"+str(file))[6] for file in files])
        if time.time() - t >= print_stats_every_x_seconds and print_stats_every_x_seconds != -1:
            print("\r" + str(size) + " Bytes...", end="")
            t = time.time()
    
    return size

count = 0
total_size = 0
files = list()
input_path = str(input("\n\nPaste full input path here:\n\n"))
output_path = str(input("\n\nPaste full output path here:\n\n"))
total_files = get_num_files(input_path) # for stats/progress
total_total_size = get_size_folder(input_path) # for stats/progress
print("\n\nGetting Files List...\n")

for path, dir, path_files in os.walk(input_path):
    [files.append([i, os.stat(path+"/"+i).st_mtime, path]) for i in path_files]

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
    destination = os.path.expanduser(output_path+"/"+filename)
    size_of_file = os.stat(path+"/"+file)[6]
    total_size += int(size_of_file)
    current_time = time.time() - t
    try:
        print("\r{:6.2f}%         at {:.1f} files per second        {:.1f}MB/s          size: {:.1f}/{:.1f}MB        file {}/{}         {:.1f} minutes remaining...              ".format(total_size/total_total_size*100, count/current_time, total_size/current_time/1000000, total_size/1000000, total_total_size/1000000 , count, total_files, (total_total_size-total_size)/(total_size/current_time)/60), end="")
    except ZeroDivisionError:
        pass
    copy2(path+"/"+file, destination)
