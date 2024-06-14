from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import InfoUsers
import random
from faker import Faker

class RequestDBAll(View):
    def get(self, request):
        info_all = InfoUsers.objects.all()
        print(info_all.count())
        for user in info_all:
            if user.age > 20:
                print("Имя:", user.name)
        return HttpResponse("Получение всех данных")


class RequestDbFilter(View):
    def get(self, request):
        info_filter = InfoUsers.objects.filter(
            age=10
        )
        if info_filter.exists():
            print("Исходный данные:", info_filter)
            print("Получение первого объекта в списке. Способ 1:", info_filter[0].age)
            print("Получение первого объекта в списке. Способ 2:",
                  info_filter.first().age)

            print("Получение последнего объекта в списке:",
                  info_filter.last().age)
            print("Получение кол-во:", info_filter.count())

            print("По возрастанию:", info_filter.order_by("age"))
            print("По убыванию:", info_filter.order_by("-age"))
        else:
            print("Список пустой")

        # Объекты больше заднного числа
        info_gt_filter = InfoUsers.objects.filter(
            balance__gt=200
        )
        print("Объекты больше заднного числа:", info_gt_filter)

        # Объекты меньше заднного числа
        info_lt_filter = InfoUsers.objects.filter(
            balance__lt=200
        )
        print("Объекты меньше заднного числа:", info_lt_filter)

        # Объекты больше или равно заднному числу
        info_gte_filter = InfoUsers.objects.filter(
            balance__gte=0
        )
        print("Объекты больше или равно заднному числу:", info_gte_filter)

        # Объекты меньше или равно заднному числу
        info_lte_filter = InfoUsers.objects.filter(
            balance__lte=200
        )
        print("Объекты меньше или равно заднному числу:", info_lte_filter)

        return HttpResponse("Фильтрация данных")



class RequestDbGet(View):
    def get(self, request):
        try:
            info_user = InfoUsers.objects.get(
                id=2
            )
            return HttpResponse(f"GET запрос от: {info_user.name}")
        except:
            return HttpResponse("Пользователя с таким ID нет или есть, но их много!")

class RequestDbCreate(View):
    def get(self, request):
        faker = Faker('ru_RU')
        
        for _ in range(1000):
            first_name = faker.first_name()
            balance = random.randint(1000, 6000)
            age = random.randint(16, 100)
            InfoUsers.objects.create(
                name=first_name,
                age=age,
                balance=balance,
                message=faker.text()
            )
        return HttpResponse("Создание пользователя")
    

class RequestDbUpdateOne(View):
    def get(self, request):
        InfoUsers.objects.update(
            message='-'
        )
        return HttpResponse("Обновление нескольких пользователей. Часть 1")
    
class RequestDbUpdateTwo(View):
    def get(self, request):
        InfoUsers.objects.filter(age__gte=34).update(
            message='Новое сообщение'
        )
        return HttpResponse("Обновление нескольких пользователей. Часть 2")

class RequestDbUpdateThree(View):
    def get(self, request):
        info_users = InfoUsers.objects.filter(age=50)
        for user in info_users:
            user.balance += 500
            user.save()
        return HttpResponse("Обновление нескольких пользователей. Часть 3. Финал.")

class RequestDbUpdateFour(View):
    def get(self, request):
        info_all = InfoUsers.objects.all()
        for user in info_all:
            if user.age % 2 == 0:
                user.balance -= 100
                user.save()
        return HttpResponse("Обновление нескольких пользователей. Часть 4. Точно Финал.")

class RequestDbUpdateGet(View):
    def get(self, request):
        user = InfoUsers.objects.get(id=624)
        user.balance -= 1000
        user.age -= 1
        user.save()
        return HttpResponse("Обновление одного пользователя")
    
class RequestDbDelete(View):
    def get(self, request):
        # InfoUsers.objects.filter(balance__lt=1000).delete()
        info = InfoUsers.objects.filter(balance__in=[2000, 2100, 1200]).delete()
        print(info)
        return HttpResponse("Удаление пользователя")