from datetime import date

from django.core.exceptions import ValidationError


def real_age(value: date) -> None:
    age = (date.today() - value).days / 365
    error_text = 'Ожидается возраст от 0 до 120 лет.'

    if not 0 <= age <= 120:
        raise ValidationError(error_text)
