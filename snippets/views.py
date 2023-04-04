from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.models import STYLES_CHOICES, LANGUAGE_CHOICES
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import generics, mixins


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    

class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)


@csrf_exempt
def styles_list(request):
    if request.method == "GET":
        return JsonResponse(STYLES_CHOICES, status=200, safe=False)
    else:
        return HttpResponse('invalid method')


@csrf_exempt
def language_list(request):
    if request.method == "GET":
        return JsonResponse(LANGUAGE_CHOICES, status=200, safe=False)
    else:
        return HttpResponse('invalid method')

