import os
import shutil

print(os.getcwd())

os.chdir(r'F:\HET\Python programs\TestPython\faltu')
print(os.getcwd())

#os.makedirs('ab/ sub-ab1')

#print(os.getcwd())

print(os.listdir())

src_files = os.listdir()
for file_name in src_files:
    full_file_name = os.path.join(r'F:\HET\Python programs\TestPython\faltu', file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name,r'F:\HET\Python programs\TestPython\faltu1' )
#for dirpath in os.walk('F:\HET\Python programs'):
 #   print('Current Path:', dirpath)
 #  print('Directories :', dirnames)
  # print('Files:', filenames)
    
#newpath=shutil.copy(r'F:\HET\Python programs\TestPython',r'F:\HET\Python programs\faltu') 

#os.chdir(newpath)
#print(os.listdir())
