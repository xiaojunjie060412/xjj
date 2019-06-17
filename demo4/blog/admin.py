from django.contrib import admin
from .models import Classify, Article, Tag, Ads
# Register your models here.

admin.site.register(Classify)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Ads)