from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ProfileViewSet, UserSearchViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)
router.register('users', UserSearchViewSet)

urlpatterns = router.urls