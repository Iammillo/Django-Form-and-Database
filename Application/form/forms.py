from django import forms

class NameForm(forms.Form):
    Name=forms.CharField()
    Address=forms.CharField()
    mobile=forms.CharField()
    Roll=forms.CharField()
    Available = forms.BooleanField(initial=True, required=False)
