from django.urls import path
from comments import views

urlpatterns = [
    path("comments/", views.CommentList.as_view(), name="get_comments"),
    path("comment/<int:pk>/", views.CommentDetail.as_view(), name="get_comment"),
]
