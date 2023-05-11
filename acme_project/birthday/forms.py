from django import forms
from django.core.exceptions import ValidationError

from .models import Birthday


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        attr = {
            'first_name': {
                'type': 'text',
                'placeholder': 'Имя',
                'class': 'form-control',
            },
            'last_name': {
                'type': 'text',
                'placeholder': 'Фамилия',
                'class': 'form-control',
            },
            'birthday': {
                'type': 'date',
                'class': 'form-control',
            },
        }

        model = Birthday
        fields = ['first_name', 'last_name', 'birthday', 'image']
        # fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs=attr.get('first_name')),
            'last_name': forms.TextInput(attrs=attr.get('last_name')),
            'birthday': forms.DateInput(attrs=attr.get('birthday')),
        }

    def clean_first_name(self) -> str:
        first_name = self.cleaned_data.get('first_name')
        return first_name.title()

    def clean_last_name(self) -> str:
        last_name = self.cleaned_data.get('last_name')
        return last_name.title()

    def clean(self) -> None:
        super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if f'{first_name} {last_name}' in BEATLES:
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )
