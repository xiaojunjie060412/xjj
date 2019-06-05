from django.contrib import admin
from .models import BookInfo, HeroInfo

# Register your models here.


class HeroInfoInLines(admin.StackedInline):
    model = HeroInfo
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']
    list_filter = ['title', 'pub_date']
    list_per_page = 20
    inlines = [HeroInfoInLines]


admin.site.register(BookInfo, BookInfoAdmin)


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'content']
    list_filter = ['name']
    search_fields = ['name', 'content']


admin.site.register(HeroInfo, HeroInfoAdmin)
