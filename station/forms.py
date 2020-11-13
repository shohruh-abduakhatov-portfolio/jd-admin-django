import datetime

from django import forms


class CreateStationForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    code = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Code'}), label='Code', max_length=255, required=True)
    codeECR = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CodeECR'}), label='Code ECR', max_length=255,required=True)
    dor = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DOR'}), label='DOR', max_length=255,required=True)
    gos = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'GOS'}), label='GOS', max_length=255,required=True)
    nameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Uzb Name'}), label='Uzb Name', max_length=255,required=True)
    nameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rus Name'}), label='Rus Name', max_length=255,required=True)
    nameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Eng Name'}), label='Eng Name', max_length=255,required=True)
    nameFull = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}), label='Full Name', max_length=255,required=True)
    otd = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Otd'}), label='OTD', max_length=255,required=True)

    rejectDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control has-feedback', 'id': 'single_cal3', 'onkeydown':'return false'}, format='%m/%d/%Y'),  label='Reject Date', initial=datetime.date.today, required=True)

    rejectUse = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control has-feedback', 'id': 'single_cal4', 'onkeydown':'return false'}, format='%m/%d/%Y'), label='Reject Use', initial=datetime.date.today, required=True)
    sf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sf'}), label='SF', max_length=255,required=True)
    sign = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sign'}), label='Sign', max_length=255,required=True)
    startDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control has-feedback', 'id': 'single_cal5', 'onkeydown':'return false'}, format='%m/%d/%Y'), label='Start Date', initial=datetime.date.today, required=True)
    startUse = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control has-feedback', 'id': 'single_cal6', 'onkeydown':'return false'}, format='%m/%d/%Y'), label='Start Use', initial=datetime.date.today, required=True)
    type = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type'}), label='Type ', max_length=255,required=True)
    vrl = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Vrl'}), label='VRL', max_length=255,required=True)
    vrz = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Vrz'}), label='VRZ', max_length=255,required=True)
    longitude = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}), label='Longitude',
                          max_length=255, required=True)
    latitude = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}), label='Latitude',
                          max_length=255, required=True)
    address = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
                               label='Address',
                               max_length=255, required=True)
    telephone = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Telephone'}),
                               label='Telephone',
                               max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, station_id=False):
        if station_id:
            return {
                'id': self['identifier'].value(),
                'code': self['code'].value(),
                'codeECR': self['codeECR'].value(),
                'dor': self['dor'].value(),
                'gos': self['gos'].value(),
                'nameUzb': self['nameUzb'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFull': self['nameFull'].value(),
                'otd': self['otd'].value(),
                'rejectDate': self['rejectDate'].value(),
                'rejectUse': self['rejectUse'].value(),
                'sf': self['sf'].value(),
                'sign': self['sign'].value(),
                'startDate': self['startDate'].value(),
                'startUse': self['startUse'].value(),
                'type': self['type'].value(),
                'vrl': self['vrl'].value(),
                'vrz': self['vrz'].value(),
                'longitude': self['longitude'].value(),
                'latitude': self['latitude'].value(),
                'address': self['address'].value(),
                'telephone': self['telephone'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'code': self['code'].value(),
                'codeECR': self['codeECR'].value(),
                'dor': self['dor'].value(),
                'gos': self['gos'].value(),
                'nameUzb': self['nameUzb'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFull': self['nameFull'].value(),
                'otd': self['otd'].value(),
                'rejectDate': self['rejectDate'].value(),
                'rejectUse': self['rejectUse'].value(),
                'sf': self['sf'].value(),
                'sign': self['sign'].value(),
                'startDate': self['startDate'].value(),
                'startUse': self['startUse'].value(),
                'type': self['type'].value(),
                'vrl': self['vrl'].value(),
                'vrz': self['vrz'].value(),
                'longitude': self['longitude'].value(),
                'latitude': self['latitude'].value(),
                'address': self['address'].value(),
                'telephone': self['telephone'].value(),
                'show': self['show'].value()
            }

