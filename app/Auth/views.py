
from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from . import serializer, models, permissions

# Create your views here.

class UserModelViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializer.UserModelSerializer
    queryset = models.UserModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email', 'username', 'city', 'state', 'country' )

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class DiaryModelViewSet(viewsets.ModelViewSet):
    """Handle creating, updating, and deleting profiles"""
    authentication_classes = (TokenAuthentication, )
    queryset = models.DiaryModel.objects.all()
    serializer_class = serializer.DiaryModelSerializer
    permission_classes = (permissions.UpdateOwnDiary, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to logged in user"""
        serializer.save(author = self.request.user)


    def get_queryset(self):
        """Return the queryset filtered by the author ID"""
        return models.DiaryModel.objects.filter(author = self.request.user)
