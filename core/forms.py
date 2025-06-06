from django import forms
from core.models import Check_up

class CheckUpForm(forms.ModelForm):

    class Meta:
        model = Check_up
        fields = (
            'file',
            'comment',
            'phone_number',
            'accept_policy'
        )
        widgets = {
            'file': forms.FileInput(attrs={
        
            }),
            'comment' : forms.TextInput(attrs={
                'placeholder': "Nəyi yoxlamağımızı istədiyinizi qeyd edin (məsələn: qrammatika, üslub, tərcümə)"
            }),
            'phone_number' : forms.TextInput(attrs={
                'placeholder': '+994 ...'
            }),
            'accept_policy' : forms.CheckboxInput(attrs={

            })
        }