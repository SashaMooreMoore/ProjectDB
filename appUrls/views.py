from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse


class StaticUrl(View):
    def get(self, request):
        return HttpResponse("Статичная ссылка")

class DinamicInt(View):
    def get(self, request, number):
        if number < 100:
            # return redirect("https://disk.yandex.com.am/i/_7WmGvNfd-wuxw")
            # return redirect("/url/static")
            return redirect("urlStaticUrl")
        print(type(number))
        return HttpResponse(f"Динамичное значение числа: {number}")
    
class DinamicSlug(View):
    def get(self, request, text):
        return HttpResponse(f"Динамичное значение текста: {text}")