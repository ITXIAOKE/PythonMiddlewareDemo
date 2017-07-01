from django.shortcuts import render

# 首页的视图函数
def index(request):
    print("index")
    raise Exception("value error")
    return render(request,'booktest/index.html')
