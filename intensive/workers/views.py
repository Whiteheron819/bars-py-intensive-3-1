from .models import Worker
from django.http import HttpResponse


def create_workers(request):
    Worker.objects.bulk_create(
        [Worker(first_name='Пётр', last_name='Иванов'),
         Worker(first_name='Василий', last_name='Петров'),
         Worker(first_name='Иван', last_name='Васильев')]
    )
    new_workers = Worker.objects.all().values_list().order_by('-id')[:3]

    return HttpResponse(new_workers)


def main(request):
    main_workers = Worker.objects.using('default').all().values_list()

    return HttpResponse(main_workers)


def replica(request):
    replica_workers = Worker.objects.using('replica').all().values_list()

    return HttpResponse(replica_workers)


def choose_db(request):
    if Worker.objects.using('default').filter(pk=1).exists():
        workers = Worker.objects.using('default').all().values_list()
    elif Worker.objects.using('replica').filter(pk=1).exists():
        workers = Worker.objects.using('replica').all().values_list()
    else:
        workers = 'Отсутствует подключение к БД'

    return HttpResponse(workers)
