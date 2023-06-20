from rest_framework import viewsets, filters, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializer, models, permissions


# Create your views here.
class AnswerViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    """Handle creating, updating, and deleting profiles"""
    authentication_classes = (TokenAuthentication, )
    queryset = models.AnswersTemplate.objects.all()
    serializer_class = serializer.AnswerSerializer
    permission_classes = (permissions.Answer_Permission, IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('slambook', )

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(filled_by = self.request.user)

    def get_queryset(self):
        """Return the queryset filtered by the author ID"""
        slambook_id = self.kwargs['slambook_id']
        answer_id = self.kwargs['book_id']
        return models.AnswersTemplate.objects.filter(id=answer_id, slambook_id=slambook_id)


class SlambookAnswerViewSet(viewsets.ModelViewSet):
    """Handle answers related to a slambook"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializer.AnswerSerializer
    permission_classes = (permissions.Answer_Permission, IsAuthenticated, )

    def get_queryset(self):
        slambook_id = self.kwargs['slambook_id']
        return models.AnswersTemplate.objects.filter(slambook_id=slambook_id)

    def perform_create(self, serializer):
        slambook_id = self.kwargs['slambook_id']
        slambook = models.SlambookTemplate.objects.get(id=slambook_id)
        serializer.save(filled_by=self.request.user, slambook=slambook)


class ViewUserSlambookViewSet(viewsets.ModelViewSet):
    queryset = models.SlambookTemplate.objects.all()
    serializer_class = serializer.SlamBookModelSerializer
    permission_classes = (permissions.Slambook_Permission, IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return models.SlambookTemplate.objects.filter(created_by=user_id)



class SlambookViewSet(viewsets.ModelViewSet):
    queryset = models.SlambookTemplate.objects.all()
    serializer_class = serializer.SlamBookModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.Slambook_Permission, IsAuthenticated,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'community',)

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(created_by = self.request.user)

    def get_queryset(self):
        queryset = self.queryset
        slambook_id = self.kwargs.get('pk')
        if slambook_id is not None:
            queryset = queryset.filter(id=slambook_id)
        else:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset
