from django.urls import path,include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router=DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet) #queryset is present so no base name required

urlpatterns = [
   path('hello-view/',views.HelloApiView.as_view()),
   path('login/',views.UserLoginApiView.as_view()),
   path('',include(router.urls))    #no prefix we wanna include all thats y no path specified
]
