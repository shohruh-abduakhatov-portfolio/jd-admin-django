from django import forms


class CreateLanguageForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    languageName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LanguageName'}), label='LanguageName', max_length=255,required=True)
    languageId = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LanguageId'}), label='LanguageId', max_length=255,required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, station_id=False):
        if station_id:
            return {
                'languageName': self['languageName'].value(),
                'languageId': self['languageId'].value(),
                'id': self['identifier'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'languageName': self['languageName'].value(),
                'languageId': self['languageId'].value(),
                'show': self['show'].value()
            }
