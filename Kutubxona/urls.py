from django.contrib import admin
from django.urls import path
from mash_uchun.views import *
from app9.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/',salomlash),
    path('oquvchilar/',oquvchilar),
    path('oquvchi/<str:ism>/',oquvchi),
    path('students/',all_students),
    path('muallif/',muallif),
    path('student/<int:pk>/',student_ochir),
    path('muallif/<int:pk>/', student_ochir),
    path('kitoblar/',all_books),
    path ('student/<int:pk>/edit/',student_tahrirlash),
    path ('muallif/<int:pk>/edit/',muallif_tahrirlash),
    path ('recordlar/',all_records),


]

