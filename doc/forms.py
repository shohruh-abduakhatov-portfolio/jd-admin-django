from django import forms


class CreateDocForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    docNameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameUzb'}), label='NameUzb', max_length=255,required=True)
    docNameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameRus'}), label='NameRus', max_length=255, required=True)
    docNameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEng'}), label='NameEng', max_length=255, required=True)
    docNameFra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameFra'}), label='NameFra', max_length=255, required=True)
    docNameEsp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEsp'}), label='NameEsp', max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, doc_id=False):
        if doc_id:
            return {
                'docNameUzb': self['docNameUzb'].value(),
                'docNameRus': self['docNameRus'].value(),
                'docNameEng': self['docNameEng'].value(),
                'docNameFra': self['docNameFra'].value(),
                'docNameEsp': self['docNameEsp'].value(),
                'show': self['show'].value(),
                'docId': self['identifier'].value()
            }
        else:
            return {
                'docNameUzb': self['docNameUzb'].value(),
                'docNameRus': self['docNameRus'].value(),
                'docNameEng': self['docNameEng'].value(),
                'docNameFra': self['docNameFra'].value(),
                'docNameEsp': self['docNameEsp'].value(),
                'show': self['show'].value()
            }
