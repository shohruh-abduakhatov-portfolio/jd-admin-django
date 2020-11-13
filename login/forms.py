from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               label='Username', min_length=6,
                               max_length=30, required=True)
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Password'}),
        label='Password', min_length=6, max_length=64, required=True)


    def as_dict(self):
        return {
            'username': self['username'].value(),
            'password': self['password'].value()
        }
