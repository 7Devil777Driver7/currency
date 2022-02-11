from accounts.views import ProfileView, UserActivateView, UserSignUpView

from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('activate/<uuid:username>', UserActivateView.as_view(), name='activate'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile')
]
