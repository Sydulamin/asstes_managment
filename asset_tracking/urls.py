from django.contrib import admin
from django.urls import path
from asset_management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', views.company_list_create, name='company-list-create'),
    path('api/companies/<int:pk>/', views.company_retrieve_update_destroy, name='company-retrieve-update-destroy'),
    path('api/devices/', views.device_list, name='device-list'),
    path('api/devices/<int:pk>/', views.device_detail, name='device-detail'),
    path('api/checkouts/', views.checkout_list, name='checkout-list'),
    path('api/checkouts/<int:pk>/', views.checkout_detail, name='checkout-detail'),
]