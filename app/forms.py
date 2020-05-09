from django import forms

class City(forms.Form):
	name = forms.CharField(max_length = 20,widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder':'Name'}))
