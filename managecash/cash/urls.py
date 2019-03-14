from django.urls import path

from cash.views import (
    CashListView,
    CashCreateView,
    CashEditView,
    CashDeleteView,
)

app_name = 'cash'
urlpatterns = [
    path('', CashListView.as_view(), name='index'),
    path('create', CashCreateView.as_view(), name='create'),
    path('<slug:pk>/edit', CashEditView.as_view(), name='edit'),
    path('<slug:pk>/delete', CashDeleteView.as_view(), name='delete'),
]