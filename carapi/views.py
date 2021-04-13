from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,request

from rest_framework.parsers import JSONParser

from .models import Car
from .serializers import CarSerializer

def car_by_user(request):
    query = request.GET.get('q')
    qs = Car.objects.filter(user_id=query)
    #print(qs[0].number)
    serializer = CarSerializer(qs)
    print(serializer.errors)
    return JsonResponse({"id":"serializer.data"})

def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET' and request.GET.get('q')==None:
        snippets = Car.objects.all()
        serializer = CarSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.GET.get('q'):
        query = request.GET.get('q')
        if Car.objects.filter(user_id=query):
            snippets = Car.objects.filter(user_id=query)
            serializer = CarSerializer(snippets, many=True)
            status=200
            return JsonResponse(serializer.data, safe=False)
        else:
            status=404
            return JsonResponse({"code" : status},status=404)