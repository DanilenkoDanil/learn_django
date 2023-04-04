from django.urls import path
from snippets.views import styles_list, language_list
from snippets.views import SnippetList, SnippetDetail

urlpatterns = [
    path('snippets/', SnippetList.as_view()),
    path('styles', styles_list),
    path('languages', language_list),
    path('snippet/<int:pk>/', SnippetDetail.as_view())
]
