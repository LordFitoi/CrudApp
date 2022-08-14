from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from app.core.viewsets import EntityViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()
router.register("entity", EntityViewSet)

app_name = "api"
urlpatterns = router.urls