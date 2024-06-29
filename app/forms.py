from .models import Resum
from django import forms


GENDERCHOOSE={
    ('Male','Male'),
    ('Female','Female')

}
class ResumForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=GENDERCHOOSE,widget=forms.RadioSelect)
    class Meta:
        model=Resum
        fields="__all__"

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'date':forms.DateInput(attrs={'class':'form-control'}),
           # 'gender':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'job_city':forms.TextInput(attrs={'class':'form-control'}),
            'profile_image':forms.TextInput(attrs={'class':'form-control'}),
            'filefield':forms.TextInput(attrs={'class':'form-control'}),

        }
