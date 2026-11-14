"""
URL configuration for trufhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from turf_management.views import TurfListCreateView
from turf_management.views import TurfRetriveUpdateDeleteView

from accounts.views import AdminCreateView
from accounts.views import UserCreationView

from reservations.views import BookingCreateView
from reservations.views import BookingRetrieveUpdateDeleteView
from reservations.views import BookingSummaryView

urlpatterns = [
    path('admin/', admin.site.urls),

    #Turf
    path("turf/",TurfListCreateView.as_view()),
    path("turf/<int:pk>/",TurfRetriveUpdateDeleteView.as_view()),

    #accounts
    path("player/register/",UserCreationView.as_view()),
    path("owner/register/",AdminCreateView.as_view()),

    #Booking
    path("booking/",BookingCreateView.as_view()),
    path("booking/<int:pk>/",BookingRetrieveUpdateDeleteView.as_view()),
    path("booking/summary/",BookingSummaryView.as_view()),
]
