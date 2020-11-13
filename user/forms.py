from django import forms


class CreateUserForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label='Email', min_length=6, max_length=64, required=True)
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}), label='Password', min_length=6, max_length=64, required=True)
    username = forms.CharField(widget=forms.HiddenInput, required=False)

    def as_dict(self,userId=False):
        if userId:
            return {
                'email': self['email'].value(),
                'username': self['email'].value(),
                'password': self['password'].value(),
                'userId': self['identifier'].value()
            }
        else:
            return {
                'email': self['email'].value(),
                'username': self['email'].value(),
                'password': self['password'].value()
            }
