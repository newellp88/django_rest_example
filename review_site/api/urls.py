from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('reviews', views.PostViewSet)


urlpatterns = router.urls