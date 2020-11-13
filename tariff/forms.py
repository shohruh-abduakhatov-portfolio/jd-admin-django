from django import forms


class CreateTariffForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    tariffNameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameUzb'}), label='NameUzb', max_length=255,required=True)
    tariffNameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameRus'}), label='NameRus', max_length=255, required=True)
    tariffNameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEng'}), label='NameEng', max_length=255, required=True)
    tariffNameFra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameFra'}), label='NameFra', max_length=255, required=True)
    tariffNameEsp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEsp'}), label='NameEsp', max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, tariff_id=False):
        if tariff_id:
            return {
                'tariffNameUzb': self['tariffNameUzb'].value(),
                'tariffNameRus': self['tariffNameRus'].value(),
                'tariffNameEng': self['tariffNameEng'].value(),
                'tariffNameFra': self['tariffNameFra'].value(),
                'tariffNameEsp': self['tariffNameEsp'].value(),
                'tariffId': self['identifier'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'tariffNameUzb': self['tariffNameUzb'].value(),
                'tariffNameRus': self['tariffNameRus'].value(),
                'tariffNameEng': self['tariffNameEng'].value(),
                'tariffNameFra': self['tariffNameFra'].value(),
                'tariffNameEsp': self['tariffNameEsp'].value(),
                'show': self['show'].value()
            }
