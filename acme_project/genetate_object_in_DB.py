
# $ python manage.py debugsqlshell

# run this commands in debugsqlshell to generate
# a objects in DB table birthday_birthday

from random import randint as r
from birthday.models import Birthday


for i in range(1, 26):
    object = Birthday.objects.create(
        first_name=f'Name{i}',
        last_name=f'Lastname{i}',
        birthday=f'{r(1950, 2023)}-{r(1, 12)}-{r(1, 27)}',
    )
    object.save()
