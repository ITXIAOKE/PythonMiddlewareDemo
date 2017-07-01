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

