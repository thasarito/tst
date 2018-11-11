from django.urls import path, include
from . import views
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('dictionary', views.DictionaryView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
]
