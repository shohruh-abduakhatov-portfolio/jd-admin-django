from django import forms


class CreateLabelForm(forms.Form):
    contentId = forms.CharField(widget=forms.HiddenInput, required=False)
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    labelName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LabelName'}),
                                label='LabelName', max_length=255, required=True)
    nameUzb = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameUzb'}),
                              label='NameUzb', max_length=255, required=True)
    nameRus = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameRus'}),
                              label='NameRus', max_length=255, required=True)
    nameEng = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEng'}),
                              label='NameEng', max_length=255, required=True)
    nameFra = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameFra'}),
                              label='NameFra', max_length=255, required=True)
    nameEsp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NameEsp'}),
                              label='NameEsp', max_length=255, required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, label_id=False):
        if label_id:
            return {
                'nameUzb': self['nameUzb'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFra': self['nameFra'].value(),
                'nameEsp': self['nameEsp'].value(),
                'labelId': self['identifier'].value(),
                'contentId': self['contentId'].value(),
                'labelName': self['labelName'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'nameUzb': self['nameUzb'].value(),
                'contentId': self['contentId'].value(),
                'nameRus': self['nameRus'].value(),
                'nameEng': self['nameEng'].value(),
                'nameFra': self['nameFra'].value(),
                'nameEsp': self['nameEsp'].value(),
                'labelName': self['labelName'].value(),
                'show': self['show'].value()
            }
