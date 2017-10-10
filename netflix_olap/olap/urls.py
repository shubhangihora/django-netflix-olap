from rest_framework.routers import SimpleRouter
from .views import PopShowViewSet, PopMovieViewSet, ActiveUserViewSet, PopGenreViewSet, PopPlanViewSet

router =  SimpleRouter()
router.register("pop-shows", PopShowViewSet)
router.register("pop-movies", PopMovieViewSet)
router.register("active-users", ActiveUserViewSet)
router.register("pop-genres", PopGenreViewSet)
router.register("pop-plans", PopPlanViewSet)
urlpatterns = router.urls
