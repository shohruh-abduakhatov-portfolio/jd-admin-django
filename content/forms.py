from django import forms


class CreateContentForm(forms.Form):
    identifier = forms.CharField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), label='Name', max_length=255,required=True)
    categoryId = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CategoryId'}), label='CategoryId', max_length=255,required=True)
    show = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'flat'}), initial=True, label='Show')

    def as_dict(self, content_id=False):
        if content_id:
            return {
                'name': self['name'].value(),
                'categoryId': self['categoryId'].value(),
                'contentId': self['identifier'].value(),
                'show': self['show'].value()
            }
        else:
            return {
                'name': self['name'].value(),
                'categoryId': self['categoryId'].value(),
                'show': self['show'].value()
            }

