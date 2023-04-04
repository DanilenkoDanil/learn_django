from django.urls import path,include
from rest_framework import routers
from steam.views import AccountView

router = routers.DefaultRouter()
router.register(r'accounts', AccountView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]