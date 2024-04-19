import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phone.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                # id, name, price, image, release_date, lte_exists и slug
                # print (line.split(';'))
                id_, name_, image_, price_, release_date_, lte_exists_, slug_ = line
                phone = Phone(
                    name = name_,
                    price = price_,
                    image = image_,
                    release_date = release_date_,
                    lte_exists = lte_exists_,
                    slug=slugify(name_)
                )
                phone.save()
                print(line)
                pass
# def create_car(request):
#     car = Car(
#     brand=random.choice(['B1','B2','B3']),
#     model=random.choice(['M1','M2','M3']),
#     color=random.choice(['C1','C2','C3']),)
#     car.save()
#     return HttpResponse(f'Все получилось! Новая машина: {car.brand}, {car.model}')