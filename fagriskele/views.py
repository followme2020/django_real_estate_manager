from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Apartment, Resort
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from fagriskele.models import Building
from django.urls import reverse_lazy


@login_required
def index(request):
    num_apts = Apartment.objects.all().count()
    num_buildings = Building.objects.all().count()
    num_resorts = Resort.objects.all().count()
    num_resale = Apartment.objects.filter(building__resort__name='Resale Apartments').count()
    num_new_apts = num_apts - num_resale
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_apts': num_apts,
        'num_buildings': num_buildings,
        'num_resorts': num_resorts,
        'num_resale': num_resale,
        'num_new_apts': num_new_apts,
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context)


class ApartmentListView(LoginRequiredMixin, generic.ListView):
    model = Apartment
    paginate_by = 10


class ApartmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Apartment


class ApartmentCreate(LoginRequiredMixin, CreateView):
    model = Apartment
    fields = ['id', 'building', 'apartment_number', 'floor', 'bedrooms',
              'covered_gross', 'balcony', 'position', 'price_in_gbp']


class ApartmentUpdate(LoginRequiredMixin, UpdateView):
    model = Apartment
    fields = ['id', 'building', 'apartment_number', 'floor', 'bedrooms',
              'covered_gross', 'balcony', 'position', 'price_in_gbp']


class ApartmentDelete(LoginRequiredMixin, DeleteView):
    model = Apartment
    success_url = reverse_lazy('apartments')


class BuildingListView(LoginRequiredMixin, generic.ListView):
    model = Building
    paginate_by = 2


class BuildingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Building


class BuildingCreate(LoginRequiredMixin, CreateView):
    model = Building
    fields = ['id', 'name', 'building_number', 'resort']


class BuildingUpdate(LoginRequiredMixin, UpdateView):
    model = Building
    fields = ['id', 'name', 'building_number', 'resort']

