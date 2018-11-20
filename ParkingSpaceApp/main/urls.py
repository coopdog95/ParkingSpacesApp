from django.urls import path
from .views import HomeView, ParkingSpaceView, ParkingSpaceReserveView

urlpatterns = [
	path('', HomeView.as_view(), name="index"),
	path('spaces/', ParkingSpaceView.as_view(), name="spaces"),
	path('reserve/<int:pk>/', ParkingSpaceReserveView.as_view(), name="reserve"),

]