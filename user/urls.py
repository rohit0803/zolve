from django.urls import path

from user import views as user_views


urlpatterns = [
    path('signup', user_views.SignUp.as_view(), name='signup'),
    path('signin', user_views.SignIn.as_view(), name='signin')
]
