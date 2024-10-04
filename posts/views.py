from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
class HelloWord(View):
    def get(self,request):
        data={
            'name':'Diego',
            'apellido':'Mendoza',
            'codes':['Python','Django','React']
        }
        return render(request,'index.html',context=data)
