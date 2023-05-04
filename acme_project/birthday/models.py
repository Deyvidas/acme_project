from django.db import models


class Birthday(models.Model):
    first_name = models.CharField(
        verbose_name='Ваше имя:',
        max_length=20,
    )

    last_name = models.CharField(
        verbose_name='Ваша фамилия:',
        help_text='Необязательное поле',
        blank=True,
        max_length=20,
    )

    birthday = models.DateField(
        verbose_name='Дата рождения:',
    )

    class Meta:
        db_table = 'birthday_birthday'

    def __str__(self):
        return self.first_name
