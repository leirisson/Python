from django.urls import path
from posts_app import views
urlpatterns = [

    path('', views.post_list, name="post-list"),
    path('detalhes/<int:id>', views.post_details, name="detalhes"),
    path('post-create/', views.post_create, name='post-create'),
    path('post-update/<int:id>', views.post_update, name='post-update'),

]
