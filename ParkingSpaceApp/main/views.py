from django.shortcuts import render, get_object_or_404
from rest_framework import filters
from django.db.models import Q
from django.views.generic import ListView, View, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse
import geopy.distance


from .models import ParkingSpace
from users.models import Profile





class HomeView(View):
	model = Profile


	def get(self, request):
		#user = get_object_or_404(User, username=self.kwargs.get('username'))
		
		return render(request, 'main/base.html', {'user':self.request.user})


class ParkingSpaceView(ListView):
	model = ParkingSpace
	template_name = 'main/spacetable.html'
	context_object_name = 'ParkingSpaces'

	def get_queryset(self):

		wanted_items = set()

		if self.request.GET.get('search'):

			search = float(self.request.GET.get('search'))

			for space in ParkingSpace.objects.filter(available=True):
				ulat = self.request.user.profile.ulatitude
				ulong = self.request.user.profile.ulongitude
				uCoord = (ulat, ulong)
				sCoord = (space.latitude, space.longitude)
				d = geopy.distance.vincenty(uCoord, sCoord).miles
				if d <= search:
					wanted_items.add(space.pk)

		return ParkingSpace.objects.filter(pk__in = wanted_items)


	

class ParkingSpaceReserveView(UpdateView):
	model = ParkingSpace
	fields = ['available']

	def get_success_url(self):
		return reverse('spaces')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)


