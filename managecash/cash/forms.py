from django import forms

from cash.models import Cash


class CashForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CashForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cash
        fields = ('title', 'price')

    def save(self, commit=True):
        cash = super(CashForm, self).save(commit=False)
        cash.user = self.user
        if commit:
            cash.save()
        return cash


class CashChangeForm(forms.ModelForm):

    class Meta:
        model = Cash
        fields = ('title', 'price')

