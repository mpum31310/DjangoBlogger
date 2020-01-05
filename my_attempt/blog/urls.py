from django.urls import path
from blog.views import (
                        list_posts_view, 
                        detial_post_view,
                        update_post_view,
                        delete_post_view
                        )

urlpatterns = [
    path("", list_posts_view),
    path("<slug:slug>/", detial_post_view),
    path("<slug:slug>/delete/", delete_post_view),
    path("<slug:slug>/edit/", update_post_view),
   
]

