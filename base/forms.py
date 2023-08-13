from django import forms

class ReserveForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email address'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    guest = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'guest', 'placeholder': '# of Guests'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'message', 'cols': 20, 'rows': 7}))
