import os
import random
from django.shortcuts import render, redirect
from replace.models import *
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'GET':
        model = My_model.objects.all()
        context = {
            'models':model
        }
        return render(request, 'index.html', context)

    elif request.method == 'POST' and request.FILES['myfile']:
        find = request.POST['find']
        replace = request.POST['replace']
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        f1 = open(('media/' + filename), 'r')

        s = f1.read()
        f1.close()

        data = s.replace(find, replace)

        n = random.randint(0,100)

        f2 = open(('media/' + str(n) + filename), 'w')
        f2.write(data)
        f2.close()

        url = ('/media/' + str(n) + filename)
        os.remove('media/' + filename)

        My_model.objects.create(find=find, replace=replace, file=data, path=url)
        return redirect('/')

