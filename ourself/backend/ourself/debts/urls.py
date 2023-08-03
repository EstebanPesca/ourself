from django.urls import path
from .api.views import debt_list, debt_detail,debt_create,debt_update,debt_delete

urlpatterns=[
    path('list/', debt_list, name='debt-list'),
    path('list/<int:pk>/', debt_detail, name='debt-detail'),
    path('create/', debt_create, name='debt-create'),
    path('update/<int:pk>/', debt_update, name='debt-update'),
    path('delete/<int:pk>/', debt_delete, name='debt-delete'),
]