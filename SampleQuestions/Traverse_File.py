#Directory Tree Traversal:
#Write a Python script to recursively traverse a directory tree and print out the names of all files and directories. Bonus points for implementing options to filter based on file extensions or directory depth.

import os

def traverse_file(directory, max_depth = float('inf'), file_ext, curr_depth=0)
  if (curr_depth > max_depth):
    return

for item in os.listdir(directory)
   item_path = os.path.join(directory, item)

   if os.path.isFile(item_path)
     if file_ext = None or item.endswith(file_ext)
       print (item_path)
    elif os.path.isDir(item_path)
       print(item_path)
       travesre_file(durectory, max_depth, file_ext, curr_depth =1)


#usage:
#traverse_file("/path/to/directory", 3, file_ext='.txt')
