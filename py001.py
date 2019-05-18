import os, sys
from shutil import copyfile
# https://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python
#for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):

selected_path = r'/etc/httpd/conf.d'
ext_from = r'.conf'
ext_to = r'.confbk'

print ("\n === before ===\n")
for filename in os.listdir(selected_path):
  print("    "+selected_path+"/"+filename)

print ("\n...processing")

for filename in os.listdir(selected_path):
#  print(filename)
  base_file, ext = os.path.splitext(filename)
#  print(ext)
  if ext == ext_from:
    os.rename(selected_path+"/"+filename, selected_path+"/"+base_file + ext_to)

print ("\n === after ===")
for filename in os.listdir(selected_path):
  print("    "+selected_path+"/"+filename)


#cp /root/script/etc/httpd/conf.d/site001.conf /etc/httpd/conf.d/site001.conf
#cp /root/script/etc/httpd/conf.modules.d/10-wsgi.conf /etc/httpd/conf.modules.d/10-wsgi.conf

print (" ... to copy mod_wsgi   ---by Mark, 2018-06-16 12:15, in Kunshan")
copyfile(r'/home/demo/venv001/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so',r'/etc/httpd/modules/mod_wsgi.so')


print("... to copy site001.conf ---by Mark, 2018-06-16, consider to put it in python file with other source file")
copyfile(r'etc/httpd/conf.d/site001.conf',r'/etc/httpd/conf.d/site001.conf')

print("... to copy 10-wsgi.conf")
copyfile(r'etc/httpd/conf.modules.d/10-wsgi.conf',r'/etc/httpd/conf.modules.d/10-wsgi.conf')

path0 = r'/etc/httpd/modules'
print ("\n === to check mod_wsgi.so ===")
for filename in os.listdir(path0):
  base_file, ext = os.path.splitext(filename)
  if base_file.startswith(r'mod_ws'):

    print("    "+path0+"/"+filename)


path1 = r'/etc/httpd/conf.d'
path2 = r'/etc/httpd/conf.modules.d'
print ("\n === to check conf.d ===")
for filename in os.listdir(path1):
  base_file, ext = os.path.splitext(filename)
  if ext == '.conf':
   # print("123456")
   # print(ext)
    print("    "+path1+"/"+filename)

print ("\n === to check conf.modules.d ===")

for filename in os.listdir(path2):
  base_file, ext = os.path.splitext(filename)
  if base_file == '10-wsgi' and  ext == '.conf':
    print("    "+path2+"/"+filename)

print ("\n")
