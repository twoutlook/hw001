import os
from shutil import copyfile

IP = "47.96.29.69"


#django-admin startproject mysite
#sudo mv mysite site001




ALLOWED_HOSTS ="ALLOWED_HOSTS = ['"+IP+"']"
STATIC = 'STATIC_ROOT = os.path.join(BASE_DIR, "static/")'

print ("Make sure to change IP before run this py file, current IP is " + IP)



f2 = open('site001/mysite/settings2.py', 'w')

with open('site001/mysite/settings.py', 'r') as f1:
  read_data = f1.readlines()
  for s in read_data:
#    print(s)

    if s.startswith ("ALLOWED_HOSTS"):
      print(s)
      s = ALLOWED_HOSTS
      print(s)

#   else:
#     print("... "+ s)

    if s.startswith ("STATIC_ROOT"):
      print(s)
      s = "# "+s
      print(s)



    f2.write(s)

# f1.close


f2.write(STATIC)
f2.close

#copyfile(r'/home/demo/site001/mysite/settings.py',r'/home/demo/site001/mysite/settings.py.bk')
#copyfile(r'/home/demo/site001/mysite/settings2.py',r'/home/demo/site001/mysite/settings.py')

os.rename(r'/home/demo/site001/mysite/settings.py',r'/home/demo/site001/mysite/settings.py.bk')
os.rename(r'/home/demo/site001/mysite/settings2.py',r'/home/demo/site001/mysite/settings.py')
