from django.db import models

# Create your models here.
class Cartella(models.Model):
    nome_cartella = models.CharField(max_length=128, help_text="Inserire il nome della cartella")
    tempo_riproduzione = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.nome_cartella

    class Meta:
        verbose_name = "Cartella"
        verbose_name_plural = "Cartelle"
