from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register('book', views.SlambookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('book/<int:slambook_id>/answer/', views.SlambookAnswerViewSet.as_view({'get': 'list', 'post': 'create'}), name='slambook-answer'),
    path('book/<int:slambook_id>/answer/<int:book_id>', views.AnswerViewSet.as_view({'get': 'list',}), name='slambook-answer'),
]