from django.urls import path
from .views import CommentsView, MainCommentTableView

app_name = "main_app"

urlpatterns = [
    path('', MainCommentTableView.as_view(), name='home_page'),
    path('comments/', CommentsView.as_view()),
]