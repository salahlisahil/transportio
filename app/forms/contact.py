from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Fullname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Mobile'}))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Company'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Write your message', 'style': 'resize: none;'}))
