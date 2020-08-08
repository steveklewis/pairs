from django.contrib import admin

# Register your models here.

from .models import Emotion, EmotionPair, Tag

admin.site.register(Tag)
admin.site.register(Emotion)
admin.site.register(EmotionPair)
