from accounts import views

from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>', views.UserActivateView.as_view(), name='activate')
]
