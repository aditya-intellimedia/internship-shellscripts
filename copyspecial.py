import os
import shutil
import zipfile
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
        
#zf = zipfile.ZipFile("myzipfile.zip", "w")
#for dirname, subdirs, files in os.walk("mydirectory"):
 #   zf.write(dirname)
  #  for filename in files:
   #     zf.write(os.path.join(dirname, filename))
#zf.close()
#for dirpath in os.walk('F:\HET\Python programs'):
 #   print('Current Path:', dirpath)
 #  print('Directories :', dirnames)
  # print('Files:', filenames)

shutil.make_archive(r'F:\HET\Python programs\TestPython\faltu1\zipi','zip',r'F:\HET\Python programs\TestPython\faltu1')
    
#newpath=shutil.copy(r'F:\HET\Python programs\TestPython',r'F:\HET\Python programs\faltu') 

#def zipdir(path, ziph):
    # ziph is zipfile handle
 #   for root,files in os.walk(r'F:\HET\Python programs\TestPython\faltu1' ):
  #      for file in files:
   #         ziph.write(os.path.join(root, file))
    
#if __name__ == '__main__':
 #   zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
   # zipdir('tmp/', zipf)
  #  zipf.close()
            
#os.chdir(newpath)
#print(os.listdir())
