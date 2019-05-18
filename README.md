# a001
## 這是設計在阿里云的CentOS7快速部署Django的方法.
## [2019-11-27]適用於hinet CentOS 7.5 eng, 64bit
新增了

### go
```
cd /home/demo
echo "You're at /home/demo, and going to be role as demo, and then, please continue to run source go2"
su demo
```

### go2
```
source venv001/bin/activate
cd site001
git pull
python manage.py migrate
deactivate
echo "going to exit, and become root again"
echo "please cd ~, back to root's dir"
echo "then, to source go3, to restart httpd"
exit
```
### go3
```
systemctl restart httpd
systemctl status httpd
```



建立一個demo 帳號，俱有 sudo 的權限
在 /home/demo 下建立 Python3.6 虛擬環境和範例 Django 應用
使用 Apache2 的 wsgi 技術


### check mod_wsgi.so

```
ldd mod_wsgi.so
ldd /etc/httpd/modules/mod_wsgi.so
        linux-vdso.so.1 =>  (0x00007ffd4f165000)
        libpython3.6m.so.1.0 => /usr/lib64/libpython3.6m.so.1.0 (0x00007f5eaa5db000)
        libpthread.so.0 => /usr/lib64/libpthread.so.0 (0x00007f5eaa3bf000)
        libc.so.6 => /usr/lib64/libc.so.6 (0x00007f5ea9ff2000)
        libdl.so.2 => /usr/lib64/libdl.so.2 (0x00007f5ea9dee000)
        libutil.so.1 => /usr/lib64/libutil.so.1 (0x00007f5ea9beb000)
        libm.so.6 => /usr/lib64/libm.so.6 (0x00007f5ea98e9000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f5eaacff000)
```


### check deploy
```

https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
python3 manage.py check --deploy
```

# hw001
# hw001
