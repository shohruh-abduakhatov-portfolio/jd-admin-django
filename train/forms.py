from django import forms


class CreateTrainForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    nameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameUzb'}), label='Uzb Name', max_length=255, required=True)
    nameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameRus'}), label='Rus Name', max_length=255 ,required=True)
    nameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEng'}), label='Eng Name', max_length=255, required=True)
    nameFra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameFra'}), label='Fra Name', max_length=255, required=True)
    nameEsp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEsp'}), label='Esp Name', max_length=255, required=True)
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}), label='Code', max_length=255, required=True)
    brand = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brand'}), label='Brand', max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, train_id=False):
        if train_id:
            return {
                'nameUzb': self['nameUzb'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFra': self['nameFra'].value(),
                'nameEsp': self['nameEsp'].value(),
                'code': self['code'].value(),
                'brand': self['brand'].value(),
                'show': self['show'].value(),
                'id': self['identifier'].value()
            }
        else:
            return {
                'nameUzb': self['nameUzb'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFra': self['nameFra'].value(),
                'nameEsp': self['nameEsp'].value(),
                'brand': self['brand'].value(),
                'code': self['code'].value(),
                'show': self['show'].value(),
            }
