from django.db import models
from django.urls import reverse

# Create your models here.
class Speaker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    speaker_info = models.TextField(max_length=2000, null= True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('speaker_detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Speech(models.Model):
    title = models.CharField(max_length=200)
    speech_date = models.DateField(null=False, blank= True)
    speeech = models.TextField(max_length=2000)
    speaker = models.ForeignKey('Speaker', on_delete = models.SET_NULL, null = True)

    class Meta:
        ordering = ['title', 'speech_date', 'speaker']

    def get_absolute_url(self):
        return reverse('speech_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

