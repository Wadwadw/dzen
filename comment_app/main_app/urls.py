from django.urls import path
from .views import CommentsView, MainCommentTableView, CommentDetailView, \
    add_comment

app_name = "main_app"

urlpatterns = [
    path('main', MainCommentTableView.as_view(), name='main'),
    path('comments/', CommentsView.as_view(), name='comments'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('add_comment/', add_comment, name='add_comment')
]