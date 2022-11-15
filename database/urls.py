from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('registrasi/', views.home_view, name = 'registrasi'),
    path('data_alumni/', views.data_alumni, name = 'data_alumni'),
    path('detail_nama/<int:id>/', views.detail_alumni, name='detail_nama'),
    path('detail_angkatan/<int:tahun_masuk>/', views.detail_angkatan, name='detail_angkatan'),

    ]