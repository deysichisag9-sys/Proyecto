from django.urls import path
from . import views

urlpatterns = [
    # Arboles
    path("hello_forestal/", views.HelloForestal.as_view(), name="hello_forestal"),
    path("forestal_insert/", views.ForestalInsert.as_view(), name="forestal_insert"),
    path("forestal_delete/", views.ForestalDelete.as_view(), name="forestal_delete"),
    path('forestal_view/<str:action>/', views.ForestalView.as_view(), name='forestal_views'),
    path('forestal_view/<str:action>/<int:id>/', views.ForestalView.as_view(), name='forestal_views_id'),

    # Caminos
    path("caminos_view/<str:action>/", views.CaminosView.as_view(), name="caminos_views"),
    path("caminos_view/<str:action>/<int:id>/", views.CaminosView.as_view(), name="caminos_views_id"),

    # Nuevas Rutas para Parcelas
    path("parcelas_view/<str:action>/", views.ParcelasView.as_view(), name="parcelas_views"),
    path("parcelas_view/<str:action>/<int:id>/", views.ParcelasView.as_view(), name="parcelas_views_id"),
]
