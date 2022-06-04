from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *



admin.site.register(Kitob)


@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    pass
    search_fields = ("ism","id",)
    list_display = ("id","ism","yosh","tirik")
    list_display_links = ("ism",)
    list_editable = ("yosh","tirik",)
    list_filter = ("tirik",)

@admin.register(Student)
class StudentAdmin(ModelAdmin):

    search_fields = ("ism", "id", "guruh",)
    list_editable = ("ism", "kitob_soni",)
    list_filter = ("guruh",)
    list_display = ("id", "ism", "guruh", "kitob_soni",)

@admin.register(Record)
class RecordAmin(ModelAdmin):
    search_fields = ("sana","student","kitob","qatyardi","qaytarish_sana",)
    list_filter = ("sana","student","kitob",)

admin.site.register(Kutubxonachi)



