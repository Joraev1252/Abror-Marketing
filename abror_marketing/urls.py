from django.urls import path

from abror_marketing.views import abror_view

app_name = 'abror_marketing'

urlpatterns = [
    path('', abror_view, name='abror_marketing')
]
