from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Car, Service
from .forms import CarForm, ServiceForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    services = car.services.all()
    cicilan = 0
    if car.dana_bank and car.bunga:
        total = car.dana_bank + (car.dana_bank * car.bunga / 100)
        cicilan = total / 12
    total_service = sum(s.biaya for s in services)
    hpp = car.harga_dasar / (car.dana_bank + car.bunga) if car.dana_bank and car.bunga else car.harga_dasar
    hpp += total_service
    return render(request, 'cars/car_detail.html', {
        'car': car,
        'services': services,
        'cicilan': cicilan,
        'hpp': hpp
    })

def car_add(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)  # Added request.FILES for image upload
        if form.is_valid():
            car = form.save()
            messages.success(request, f'{car.merk} {car.model} berhasil ditambahkan!')
            return redirect('car_list')
        else:
            messages.error(request, 'Terjadi kesalahan. Silakan periksa form Anda.')
    else:
        form = CarForm()
    
    context = {
        'form': form,
        'title': 'Tambah Mobil Baru',
        'submit_text': 'Simpan Mobil',
    }
    return render(request, 'cars/car_form.html', context)

def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car_list')

def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_detail', pk=form.cleaned_data['mobil'].pk)
    else:
        form = ServiceForm()
    return render(request, 'cars/service_form.html', {'form': form})
