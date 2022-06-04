from django  import forms
from .models import *
class StudentForm(forms.Form):
    ism = forms.CharField(label="Ism")
    guruh = forms.CharField(label="Guruh")
    kitob_soni = forms.IntegerField(max_value=5,min_value=0,label = "kitob_soni")

class MuallifForm(forms.Form):
    ism = forms.CharField()
    yosh = forms.IntegerField()
    tirik = forms.BooleanField()
    kitob_soni = forms.IntegerField()

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class MuallifForm(forms.Form):
    ism = forms.CharField()
    yosh = forms.IntegerField()
    tirik = forms.BooleanField()
    kitob_soni = forms.IntegerField()



