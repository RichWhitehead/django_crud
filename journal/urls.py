from django.urls import path
from .views import HomePageView, JournalPageView

urlpatterns = [
  path('', HomePageView.as_view(), name = 'home'),
  path('Journal/<int:pk>', JournalPageView.as_view(), name = 'journal')
]