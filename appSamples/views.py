from django.shortcuts import render
from django.views import View

class HomePage(View):
    def get(self, request):
        return render(request, 'appSamples/index.html')

class ConditionPage(View):
    def get(self, request):
        return render(request, 'appSamples/condition.html', {
            "status": True,
            "age": 30, 
            "message": "ok",
            "list_block": [12, 34, 13, 27, 80, 3, 44],
        })