from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register('template', views.TemplateViewSet)
router.register('question', views.QuestionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]