from django.urls import path
from classView import views
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.List.as_view(), name='index'),
    path('detail/<pk>/', views.Detail.as_view(), name='detail'),
    path('add/', views.Add.as_view(), name='add'),
    path('update/<pk>', views.Update.as_view(), name='update'),
    path('delete/<pk>', views.Delete.as_view(), name='delete'),
    path('payment/', views.Payment.as_view(), name='payment'),
]
