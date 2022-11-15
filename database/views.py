from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import GeeksForm
from .models import Data_alumni

def home(request):
    return render(request,'base.html')

def data_alumni(request):
    alumni = Data_alumni.objects.all().values().order_by('nama_lengkap')
    context = {'alumni' : alumni}
    return render(request,'data_alumni.html', context)

def detail_alumni(request, id):
    detail_nama = Data_alumni.objects.all().filter(id=id)
    context = {'detail_nama' : detail_nama}
    return render(request,'detail_nama.html', context)

def detail_angkatan(request, tahun_masuk):
    detail_angkatan = Data_alumni.objects.all().filter(tahun_masuk=tahun_masuk)
    context = {'detail_angkatan' : detail_angkatan}
    return render(request,'detail_angkatan.html', context)


def home_view(request):
	context ={}

	# create object of form
	form = GeeksForm(request.POST or None, request.FILES or None)

	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()
		return HttpResponseRedirect('../data_alumni/')

	context['form']= form
	return render(request, "home.html", context)



