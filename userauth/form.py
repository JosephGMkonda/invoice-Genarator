from django import forms
from .models import Profile



class ProfileForm(forms.ModelForm):

    Full_Name = forms.CharField(widget=forms.TextInput(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}), required=True)
    Address = forms.CharField(widget=forms.Textarea(attrs={'id': 'floatingInput', 'class': 'form-control mb-3'}), required=True)

    

    class Meta:
        model = Profile
        fields = ["Full_Name","Address"]