from django.shortcuts import render
from django.views import generic
from .models import Comment


class CommentsView(generic.ListView):
    paginate_by = 25
    model = Comment
    template_name = 'comments.html'


class MainCommentTableView(generic.ListView):
    paginate_by = 25
    model = Comment
    template_name = 'table_comment.html'
    queryset = Comment.objects.filter(parent=None)

