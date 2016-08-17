from django.shortcuts import render
from django.views.generic import TemplateView
import requests

class MainView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        r = requests.get('http://127.0.0.1:8080')
        text = r.text.split('\n')
        return render(request, template_name='index.html', context={'text':text})

    def post(self,request,*args,**kwargs):
        a = request.POST["a"]
        b = request.POST["b"]
        c = request.POST['c']
        try:
            a = int(a)
            b = int(b)
            c = int(c)
        except ValueError:
            return render(request, template_name='index.html', context={'error': "Check your values"})
        r = requests.post('http://127.0.0.1:8080', data={"a": a, "b": b, "c": c})
        print(r.text.split('\n'))
        text = r.text.split('\n')
        return render(request, template_name='index.html', context={'text': text})