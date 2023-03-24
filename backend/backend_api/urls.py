# file created by nikamn

from rest_framework import routers

from .views import MovieViewSet


router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
urlpatterns = router.urls
