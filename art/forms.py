from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label='Email', max_length=255, widget=forms.EmailInput(attrs={"class":"form-control"}))
    phone = forms.CharField(label='Phone (optional)', help_text='Ex: (123) 456-7890', max_length=25, required=False, widget=forms.TextInput(attrs={"class":"form-control"}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={"rows":"5", "class":"form-control"}))

class SubscriberForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))