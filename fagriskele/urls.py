from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apartments/', views.ApartmentListView.as_view(), name='apartments'),
    path('apartment/<int:pk>', views.ApartmentDetailView.as_view(), name='apartment-detail'),
    path('buildings/', views.BuildingListView.as_view(), name='buildings'),
    path('building/<int:pk>', views.BuildingDetailView.as_view(), name='building-detail'),
    path('building/create/', views.BuildingCreate.as_view(), name='building-create'),
    path('building/<int:pk>/update/', views.BuildingUpdate.as_view(), name='building-update'),
    path('apartment/create/', views.ApartmentCreate.as_view(), name='apartment-create'),
    path('apartment/<int:pk>/update/', views.ApartmentUpdate.as_view(), name='apartment-update'),
    path('apartment/<int:pk>/delete/', views.ApartmentDelete.as_view(), name='apartment-delete'),
]