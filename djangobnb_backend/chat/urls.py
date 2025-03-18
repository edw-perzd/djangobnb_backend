from django.urls import path

from . import api

urlpatterns = [
    path('', api.conversations_list, name='api_conversations_list'),
    path('start/<uuid:user_id>/', api.conversations_store, name='api_conversations_store'),
    path('<uuid:pk>/', api.conversations_detail, name='api_conversations_detail')
]
