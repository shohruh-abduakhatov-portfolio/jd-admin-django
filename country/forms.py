from django import forms


class CreateCountryForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    countryNameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameUzb'}), label='NameUzb', max_length=255,required=True)
    countryNameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameRus'}), label='NameRus', max_length=255, required=True)
    countryNameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEng'}), label='NameEng', max_length=255, required=True)
    countryNameFra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameFra'}), label='NameFra', max_length=255, required=True)
    countryNameEsp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEsp'}), label='NameEsp', max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, country_id=False):
        if country_id:
            return {
                'countryId': self['identifier'].value(),
                'countryNameUzb': self['countryNameUzb'].value(),
                'countryNameRus': self['countryNameRus'].value(),
                'countryNameEng': self['countryNameEng'].value(),
                'countryNameFra': self['countryNameFra'].value(),
                'countryNameEsp': self['countryNameEsp'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'countryNameUzb': self['countryNameUzb'].value(),
                'countryNameRus': self['countryNameRus'].value(),
                'countryNameEng': self['countryNameEng'].value(),
                'countryNameFra': self['countryNameFra'].value(),
                'countryNameEsp': self['countryNameEsp'].value(),
                'show': self['show'].value()
            }
