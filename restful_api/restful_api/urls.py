from django.conf.urls import url, include
from rest_framework import routers
from restful_api.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('restful_api.waterrecord.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
