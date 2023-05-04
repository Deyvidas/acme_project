from django import forms

from .models import Birthday


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
        # fields = ['first_name', 'last_name', 'birthday']
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs=attr.get('first_name')),
            'last_name': forms.TextInput(attrs=attr.get('last_name')),
            'birthday': forms.DateInput(attrs=attr.get('birthday')),
        }
