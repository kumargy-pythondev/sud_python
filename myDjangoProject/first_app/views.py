from django.shortcuts import render
from django.http import HttpResponse

My_dict = {'insert_me':"hello I am from Views.py", 'help_insert':"Please contact my number 201-238-3519"}
def index(request):
    return render(request,'first_app/index.html', context = My_dict)
    # return HttpResponse("Hello World!!")

def help(request):
    return render(request,'first_app/help.html', context = My_dict)