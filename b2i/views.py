from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from .models import *
from .forms import predictForm
import os
import pickle
import glob


# Create your views here.


def prediction(request):
    context = {}
    if request.method == "POST":
        form = predictForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data.get("choose_image")
            modulepath = os.path.dirname(__file__)
            model = pickle.load(open(os.path.join(modulepath, "model.pkl"), "rb"))
            obj = uploadImg.objects.create(img=data)
            obj.save()
            context['obj'] = obj
            res = model(obj.img.url)
            grow = list()
            grow.append(res[0][0][1])
            grow.append(res[0][1][1])
            grow.append(res[0][2][1])
            grow.append(res[0][3][1])
            grow.append(res[0][4][1])
            context['results'] = grow
            obj.delete()

    else:
        form = predictForm()
        context['form'] = form
        file = glob.glob('''E:\\ANAND's STUFF\\new\\media\\images\\*''')
        for f in file :
            os.remove(f)
    return render(request, "prediction.html", context)
