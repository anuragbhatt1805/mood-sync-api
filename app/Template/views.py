from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializer, models, permissions

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = models.Questions.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.AddQuestion, IsAuthenticated)
    serializer_class = serializer.QuestionModelSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('question_text',)


class TemplateViewSet(viewsets.ModelViewSet):
    queryset = models.Template.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateUseTemplate, IsAuthenticated)
    serializer_class = serializer.TemplateSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'description', 'author__username' )

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(is_active = True, author = self.request.user)
        serializer.save(q1 = models.Questions.objects.get(id = self.request.data['q1']))
        serializer.save(q2 = models.Questions.objects.get(id = self.request.data['q2']))
        serializer.save(q3 = models.Questions.objects.get(id = self.request.data['q3']))
        serializer.save(q4 = models.Questions.objects.get(id = self.request.data['q4']))
        serializer.save(q5 = models.Questions.objects.get(id = self.request.data['q5']))
        serializer.save(q6 = models.Questions.objects.get(id = self.request.data['q6']))
        serializer.save(q7 = models.Questions.objects.get(id = self.request.data['q7']))
        serializer.save(q8 = models.Questions.objects.get(id = self.request.data['q8']))
        serializer.save(q9 = models.Questions.objects.get(id = self.request.data['q9']))
        serializer.save(q10 = models.Questions.objects.get(id = self.request.data['q10']))
        serializer.save(q11 = models.Questions.objects.get(id = self.request.data['q11']))
        serializer.save(q12 = models.Questions.objects.get(id = self.request.data['q12']))
        serializer.save(q13 = models.Questions.objects.get(id = self.request.data['q13']))
        serializer.save(q14 = models.Questions.objects.get(id = self.request.data['q14']))
        serializer.save(q15 = models.Questions.objects.get(id = self.request.data['q15']))
        serializer.save(q16 = models.Questions.objects.get(id = self.request.data['q16']))
        serializer.save(q17 = models.Questions.objects.get(id = self.request.data['q17']))
