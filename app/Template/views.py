from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializer, models, permissions

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.AddQuestion, IsAuthenticated)
    serializer_class = serializer.DiaryModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('question_text', 'question_type',)

class TemplateViewSet(viewsets.ModelViewSet):
    queryset = models.Template.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateUseTemplate, IsAuthenticated)
    serializer_class = serializer.TemplateSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'description', 'author', )
