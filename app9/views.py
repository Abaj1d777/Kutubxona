from django.shortcuts import render,redirect
from .models import *
from .forms import *

def all_students(request):
    if request.method == 'POST':
        f = StudentForm(request.POST)
        if f.is_valid():
            Student.objects.create(
            ism = request.POST.get("ism"),
            guruh = request.POST["guruh"],
            kitob_soni = request.POST.get("kitob_soni"),
        )
        return redirect("/students/")
    talabalar = Student.objects.all()
    top3 = Student.objects.order_by("-kitob_soni")[:3]
    malumot = {
        "forms":StudentForm(),
        "oquvchilar": talabalar,
        "kitob_koplar" :top3
    }
    return render(request,"all_students.html",malumot)

def muallif(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            yosh=request.POST["yosh"],
            kitoblar_soni=request.POST.get("kitob_soni"),
            tirk=request.POST.get("tirik"),

        )
        return redirect("/mallif/")
    m1 = Muallif.objects.all()
    top3 = Muallif.objects.order_by("-kitoblar_soni")[:3]
    malumot = {
        "forma":MuallifForm(),
        "muallif": m1,
        "kitobi_koplar": top3
    }
    return render(request, "mualliflar.html", malumot)



def student_ochir(request,pk):
    Student.objects.filter(id = pk ).delete()
    return redirect("/students/")

def Muallif_ochir(request,pk):
    Muallif.objects.filter(id = pk).delete()
    return redirect("/muallif/")


def student_tahrirlash(request,pk):
    if request.method == 'POST':
        Student.objects.filter(id = pk).update(
            ism = request.POST.get('ism'),
            guruh = request.POST.get('guruh'),
            kitob_soni = request.POST.get('kitob_soni')
        )
        return redirect("/students/")
    data = {
        "student":Student.objects.get(id = pk)
    }
    return render(request,"students_edit.html",data)

def muallif_tahrirlash(request,pk):
    if request.method == 'POST':


        return redirect("/muallif/")
    data = {
        "muallif": Muallif.objects.get(id=pk)
    }
    return render(request, "Muallif_tahrirlash.html", data)

def all_records(request):
    if request.method == 'POST':
        g = KitobForm(request.POST)
        if g.is_valid():
            g.save()
        return redirect("/recordlar/")
    data = {
        "forma":RecordForm(),
        "record": Record.objects.all(),
        "kitob":Kitob.objects.all(),
        "student": Student.objects.all(),
    }
    return render(request,"Recordss.html",data)


def all_books(request):
    if request.method == "POST":
        f = KitobForm(request.POST)
        if f.is_valid():
            f.save()
        return redirect("/kitoblar/")

    data = {
        "forma":KitobForm(),
        "kitob":Kitob.objects.all(),
        "mualliflar":Muallif.objects.all()
            }
    return render(request,"Kitob.html",data)
























