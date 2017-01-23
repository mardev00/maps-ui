from django import forms


class MapForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    longitude_val = forms.FloatField(label='Center Longitude')
    latitude_val = forms.FloatField(label='Center Latitude')
    left_longitude_val = forms.FloatField()
    left_latitude_val = forms.FloatField()  
    right_longitude_val = forms.FloatField()
    right_latitude_val = forms.FloatField()


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
    
