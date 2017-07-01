##1，定义
>Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的健壮性，其它的MVC框架也有这个功能，名称为IoC。

##2,各个方法
Django在中间件中预置了五个方法，这五个方法的区别在于不同的阶段执行，对输入或输出进行干预，方法如下：

+ 1）初始化：无需任何参数， 服务器接收第一个请求时会被调用一次，而且只调用一次，用于确定是否启用当前中间件。

>def __init__():
    pass

+ 2）在进行url匹配之前被调用，在每个请求上调用,返回None或HttpResponse对象。

>def process_request(request):
    pass

+ 3）在url匹配之后，视图函数调用之前被调用，在每个请求上调用,返回None或HttpResponse对象。

>def process_view(request, view_func, view_args, view_kwargs):
    pass

+ 4） 视图函数之后会被调用：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象。

>def process_response(request, response):
    pass

+ 5）异常处理：当视图函数抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象。

>def process_exception(request,exception):
    pass

##3，案例加以说明
+ 1）在booktest/目录下创建middleware.py文件，代码如下：

```
from django.http import HttpResponse
from django.conf import settings


class MyMiddleWare(object):
    def __init__(self):
        print("init")

    def process_request(self,request):
        print("prcess_request")

    def process_view(self,request,view_func,*view_args,**view_kwargs):
        print("process_view")

    def process_response(self,request,response):
        print("process_response")
        return  response

    def process_exception(self,request,exception):
        print("exception")


```

+ 2）在test05/settings.py文件中，向MIDDLEWARE_CLASSES项中注册。

```
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'booktest.middleware.MyMiddleWare',
)
```

+ 3）修改booktest/views.py中视图index。

```
# 首页的视图函数
def index(request):
    print("index")
    return render(request,'booktest/index.html')
```

+ 4）运行服务器，命令行中效果如下图：

![这里写图片描述](http://upload-images.jianshu.io/upload_images/3827414-696d4ef624334ab9?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+ 5）刷新页面，命令行中效果如下图：

![这里写图片描述](http://upload-images.jianshu.io/upload_images/3827414-f69ae336bd21ea43?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

+  6）异常中间件效果：
+如果多个中间件中注册了相同的方法，则先注册的后执行。

修改视图函数如下：
```
# 首页的视图函数
def index(request):
    print("index")
    raise Exception("value error")
    return render(request,'booktest/index.html')

```

效果图如下：

![这里写图片描述](http://upload-images.jianshu.io/upload_images/3827414-485e0d764e7ae885?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
