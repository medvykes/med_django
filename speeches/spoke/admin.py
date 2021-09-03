from django.contrib import admin
from .models import Speech, Speaker
# Register your models here.

class SpeechAdmin(admin.ModelAdmin):
    list_display = ('title', 'speech_date', 'speeech', 'speaker')
    fields = [('title', 'speaker'),'speeech','speech_date']

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','speaker_info')


admin.site.register(Speech, SpeechAdmin)
admin.site.register(Speaker, SpeakerAdmin)
