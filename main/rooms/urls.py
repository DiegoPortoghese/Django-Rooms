from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

#rooms_router = DefaultRouter()
#rooms_router.register(r'rooms', views.RoomViewSet)

urlpatterns = [
    #path("",include(rooms_router.urls)), # ROOM default CRUD
    path('upload/', views.RoomImageView.as_view()),
    path('upload/<int:pk>/', views.DetailRoomImageView.as_view()),
    path('', views.ListRoomView.as_view()),
    path('<int:pk>/', views.DetailRoomView.as_view()),
    path('search/', views.SearchListRoomView.as_view()),
    path('my/', views.UserListRoomView.as_view()),
]