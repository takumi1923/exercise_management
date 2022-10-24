from django import forms
from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from .models import List,Card,Reward,RewardCreate,Reward_Recieve,Calendar,RewardTake,Ikusei_Point,Ikusei_Siyou,Ikusei_Suruze,Ikusei_Daze,Point_Limit,Point_Amari
from django.core.exceptions import ValidationError
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ("title",)




# forms.py
class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description","date","start_time","excercise_time", "list",)
    






class CardCreateFromHomeForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description","date","start_time","excercise_time", "list",)
        

class RewardForm(forms.ModelForm):
    class Meta:
        model = RewardTake
        fields = ("date","reward","point",)
       

class BS4ScheduleForm(forms.ModelForm):
    """Bootstrapに対応するためのModelForm"""

    class Meta:
        model = Calendar
        fields = ("title", "description","date","start_time","excercise_time", "list",)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'start_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'excercise_time': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            

        }

    
class IkuseiForm(forms.ModelForm):
    class Meta:
        model = Ikusei_Point
        fields = ("ikusei_point",)

    


    

class IkuseiSiyouForm(forms.ModelForm):
    class Meta:
        model = Ikusei_Siyou
        fields = ("ikusei_siyou",)

class IkuseiDazeForm(forms.ModelForm):
    class Meta:
        model = Ikusei_Daze
        fields = ("ikusei_daze",)

