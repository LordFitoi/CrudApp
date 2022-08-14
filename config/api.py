from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
# from app.core.viewsets import ContactViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
# router.register("contacts", ContactViewSet)

app_name = "api"
urlpatterns = router.urls