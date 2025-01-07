from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'blog'


urlpatterns = [
    path("", views.blogs, name='blogs'),
    # path('video/', views.display_video, name='display_video')
    path('<int:blog_id>/', views.detail, name="detail")
]
