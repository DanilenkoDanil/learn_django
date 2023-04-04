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


class SnippetList(APIView):
    @staticmethod
    def get(request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=200)

    @staticmethod
    def post(request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class SnippetDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)


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

