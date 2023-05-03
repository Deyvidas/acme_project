from django import forms


class BirthdayForm(forms.Form):
    attr = {
        'first_name': {
            'type': 'text',
            'placeholder': 'Имя',
            'style': 'width: 25ch',
        },
        'last_name': {
            'type': 'text',
            'placeholder': 'Фамилия',
            'style': 'width: 25ch',
        },
        'birthday': {
            'type': 'date',
            'style': 'width: 25ch',
        },
    }

    first_name = forms.CharField(
        max_length=20,
        label='Ваше имя:',
        widget=forms.TextInput(attrs=attr['first_name'])
    )

    last_name = forms.CharField(
        label='Ваша фамилия:',
        required=False,
        widget=forms.TextInput(attrs=attr['last_name'])
    )

    birthday = forms.DateField(
        label='Дата рождения:',
        widget=forms.DateInput(attrs=attr['birthday'])
    )
