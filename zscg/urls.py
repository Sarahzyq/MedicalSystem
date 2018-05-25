from django.conf.urls import url,include
#from django.contrib.auth import views
from zscg import views
from rest_framework import routers

#router = routers.SimpleRouter()
router = routers.DefaultRouter()
router.register(r'PatientBasicInfo', views.PatientBasicInfoViewSet)
router.register(r'BingLi', views.BingLiViewSet)
router.register(r'Photo', views.PhotoViewSet)
router.register(r'DiagHistoryBasic', views.DiagHistoryBasicViewSet)

app_name = 'zscg'
urlpatterns = [
    url(r'^', include(router.urls)),
    url('^show', views.show,name='show'),
    url('^do_login/$', views.do_login, name='do_login'),
#    url('^PatientBasicInfo/(?P<name>.+)/$', views.PatientBasicInfoViewSet)
# url('^get_patient/$', views.get_patient)
]
