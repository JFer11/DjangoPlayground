from django.urls import path
from . import views

pages_patterns = ([
    path('', views.PageListView.as_view(), name='pages'),
    path('create/', views.PageCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PageDeleteView.as_view(), name='delete'),
    path('<int:pk>/<slug:page_slug>/', views.PageDetailView.as_view(), name='page'),
], 'pages')
