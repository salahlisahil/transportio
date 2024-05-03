from django import forms


class CommentForm(forms.Form):
    fullname = forms.CharField(label='Full Name', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Subject', max_length=200)
    comment = forms.CharField(label='Comment', widget=forms.Textarea)
