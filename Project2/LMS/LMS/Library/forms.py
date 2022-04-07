from django import forms


class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your full-name'}))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    rep=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter Password'}))
    email=forms.CharField(max_length=30,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email'}))
    phone=forms.CharField(max_length=30,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter Phone'}))
