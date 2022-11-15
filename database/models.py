from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.username

class Dosen(models.Model):
    nama_dosen = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_dosen

class Data_alumni(models.Model):
#    username = models.OneToOneField(User,  null=True, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=100)
    nama_panggilan = models.CharField(max_length=50)
    npm = models.CharField('NPM', max_length=10)
    tahun_masuk = models.IntegerField()
    tahun_lulus = models.IntegerField()
    dosen_wali = models.CharField(max_length=100)
    tema_skripsi = models.CharField(max_length=200)
    kota_asal = models.CharField(max_length=200)
    kota_sekarang = models.CharField(max_length=200)
    nomor_kontak = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    media_sosial = models.CharField(max_length=200)
    jabatan_sekarang = models.CharField(max_length=100)
    nama_instansi = models.CharField(max_length=200)
    masa_kerja = models.IntegerField()
    gelar_pascasarjana = models.CharField(max_length=20)
    kampus_pascasarjana = models.CharField(max_length=200)
    tema_tesis = models.CharField(max_length=200,  null=True)
    lulus_pascasarjana = models.IntegerField()
    catatan = models.CharField(max_length=200)
    resume = models.TextField(null=True)

# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
		# fields of the model
	title = models.CharField(max_length = 200)
	description = models.TextField()
	last_modified = models.DateTimeField(auto_now_add = True)
	img = models.ImageField(upload_to = "images/")

		# renames the instances of the model
		# with their title name
	def __str__(self):
		return self.title




# Create your models here.
