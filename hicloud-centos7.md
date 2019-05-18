# Hicloud CentOS7

## 新建用戶 demo

```
sudo adduser demo
sudo passwd demo
sudo usermod -a -G demo apache
sudo usermod -a -G wheel demo
```

## 運行各安裝指令
```
sudo yum -y install tree
sudo yum -y install nano

sudo yum -y install httpd
sudo yum -y  install httpd-devel
sudo systemctl start httpd.service
sudo systemctl enable httpd.service

sudo yum -y update
sudo yum -y install yum-utils
sudo yum -y groupinstall development
sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install python36u
sudo yum -y install python36u-pip
sudo yum -y install python36u-devel

cat /etc/*release
httpd -V
python3.6 -V
```

## 建立虛擬環境並安裝wsgi

```
cd /home/demo
python3.6 -m venv venv001
source venv001/bin/activate
pip install django
pip install --upgrade pip
pip install mod_wsgi
deactivate
cd ~
ll
```

## 下載腳本並運行py001

```

git clone https://github.com/twoutlook/a001.git
cd a001

python3.6 py001.py


 rm -f /home/demo/s02-demo
 rm -f /home/demo/py002.py
cp s02-demo /home/demo/s02-demo
cp py002.py /home/demo/py002.py
chown demo:demo  /home/demo/s02-demo
chown demo:demo  /home/demo/py002.py
pwd

```


## 切換用戶demo並運行腳本

```
su demo
cd ~
source s02-demo

```

## CentOS7 Firewall 打開 80 端口
https://stackoverflow.com/questions/24729024/open-firewall-port-on-centos-7
https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7

```
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --reload

firewall-cmd --zone=public --add-port=8000/tcp --permanent
firewall-cmd --reload

sudo firewall-cmd --list-all


```

## CentOS7 Linux SE
https://linuxhint.com/how-to-disable-selinux-on-centos-7/
Temporarily Disable SELinux on CentOS 7
sudo setenforce 0

nano /etc/selinux/config


## Troubleshooting (1)No module named 'encodings'

cd /var/log/httpd
tail error_log
ModuleNotFoundError: No module named 'encodings'

這是因為 mod_wsgi.so 權限不對

chmod 755 mod_wsgi.so 

![err1](/img/wsgi.png)



