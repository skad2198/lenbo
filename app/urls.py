from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home, name="home"),
    path('',views.HomePageView.as_view(), name="home"),
    # path('detail/<int:id>/', views.detail,name="detail"),
    path('detail/<int:pk>/', views.ItemDetailView.as_view(),name="detail"),
    path('search/', views.search,name="search"),
    path('items/create',views.ItemCreateView.as_view(),name='create'),
    path('items/update/<int:pk>',views.ItemUpdateView.as_view(),name='update'),
    path('items/delete/<int:pk>',views.ItemDeleteView.as_view(),name='delete'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]
