from django.db import models

class Car(models.Model):
    merk = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    tahun = models.IntegerField()
    harga_dasar = models.DecimalField(max_digits=12, decimal_places=2)
    dana_bank = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    bunga = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.merk} {self.model} ({self.tahun})"

class Service(models.Model):
    mobil = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="services")
    tanggal = models.DateField()
    deskripsi = models.TextField()
    biaya = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Service {self.mobil} pada {self.tanggal}"
