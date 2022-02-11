from currency.views import (
    ContactUsCreateView, ContactUsView, RateCreateView, RateDeleteView, RateDetailsView, RateListView,
    RateUpdateView, SourceCreateView, SourceDeleteView, SourceListView, SourceUpdateView)

from django.urls import path

app_name = 'currency'

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('contact-us/create/', ContactUsCreateView.as_view(), name='contactus-create'),
    path('rate-list/', RateListView.as_view(), name='rate-list'),
    path('rate-list/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate-list/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('rate-list/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate-list/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('source-list/', SourceListView.as_view(), name='source-list'),
    path('source-list/create/', SourceCreateView.as_view(), name='source-create'),
    path('source-list/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source-list/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
]
