# shop
# 配置
1.ngrok
ngrok下载和基本使用
    从https://ngrok.com/  下载ngrok

    然后注册一个账号 获取官方分配一个密钥
    Install your authtoken
      ./ngrok authtoken xxxx
    Create your first secure tunnel
      ./ngrok http 80
    Open the web interface at http://localhost:4040 to inspect and replay 
    read doc  https://ngrok.com/docs 
    for instructions on advanced features like adding HTTP authentication, setting custom subdomains and more.

    使用cmd 到ngrok.exe的目录 
        ngrok -authtoken 密钥 -subdomain  二级域名 端口 
        ngrok -authtoken  xxxx -subdomain yyyy 8000  #这个二级域名也要付费才有了

    最简单的命令是 
    ngrok http 8000
下面介绍全免费的方案
使用默认配置文件
    default location of config file is  $HOME/.ngrok2/ngrok.yml.
    windows下面
     C:\Users\Administrator/.ngrok2\ngrok.yml

    authtoken: 
    tunnels:
      myshop-http:
        addr: 8000
        proto: http
        #subdomain: myshop-inspect  这个要付费才有
        inspect: false
        
    然后在console，运行
    ngrok start myshop-http
2.Rabbitmq server
celery4.x 不再支持windows
pip install celery==3.1.18

rabbitmq 支持的OS多过redis，这里在windows安装了一个 可以用

cd /d D:\RabbitMQ Server\rabbitmq_server-3.6.9\sbin
windows下面配置rabbitmq
http://www.rabbitmq.com/configure.html#customise-windows-environment
run the following command after installation on rabbit mq path:

    rabbitmq-plugins enable rabbitmq_management 
    #下面的服务启动是会失败的，如何配置为windows service看下面
    rabbitmq-service.bat start 

下面的命令，可以在console看到消息
    rabbitmq-server.bat start 

如何要运行为windows service
    RABBITMQ_BASE是用来放db和log两个目录的，
    默认是在C:\Users\Administrator\AppData\Roaming\RabbitMQ
        RABBITMQ_BASE=D:\RabbitMQ Server\rabbitmq_server-3.6.9
            rabbitmq-service.bat uninstall
            rabbitmq-service.bat install
            rabbitmq-service.bat start
             
3.paypal
Creating a PayPal account
You need to have a PayPal Business account to integrate the payment gateway into
your site. If you don't own a PayPal account yet, sign up at https://www.paypal.com/signup/account. 
Make sure that you choose a Business Account and sign up
to the PayPal Payments Standard solution, as shown in the following screenshot:


pip install django-paypal==0.3.6
http://django-paypal.readthedocs.io/en/stable/

http://developer.paypal.com
注册sandbox账号
包括business和person账号，这个是用来模拟买卖中的账号来的。
person账号初始化的balance是$9999.

4.WeasyPrint使用它的转换功能（输出pdf file）
目前为止PyGTK只支持py2.7,所以确保在python2.7的环境
否则就只能去掉WeasyPrint

# 发布运行：
因为某些app要用到static下面的静态文件，所以需要运行下面的命令
python manage.py collectstatic
开4个console

### 1.ngrok
```
ngrok start  myshop-http
```

这时候会显示外网url，以后就用这个url访问myshop购物

### 2.django myshop
```
workon myshop
cd /d e:/django_projects/shop/myshop
python manage.py runserver 0.0.0.0:8000
```

### 3.rabbitmq server
```
cd /d D:\RabbitMQ Server\rabbitmq_server-3.6.9\sbin
rabbitmq-server start
```
或者启动service

### 4.celery
```
workon myshop
cd /d e:/django_projects/shop/myshop
(myshop) e:\django_projects\shop\myshop>
celery -A myshop worker -l info
```

因为报错：pickle被rejected，所以把下面的配置注释掉了
CELERY_ACCEPT_CONTENT = ['application/json']

