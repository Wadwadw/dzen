from django.views import generic
from django.shortcuts import render, redirect

from .forms import CommentModelForm
from .models import Comment


class CommentsView(generic.ListView):
    """Returns all comments with tree"""
    paginate_by = 25
    model = Comment
    template_name = 'comments.html'


class MainCommentTableView(generic.ListView):
    """Returns comments without parents"""
    paginate_by = 25
    model = Comment
    template_name = 'table_comment.html'

    def get_queryset(self):
        # ordering comments
        order_by = self.request.GET.get('order_by', 'name')
        if order_by not in ['user_name', '-user_name', 'add_date', '-add_date', 'email', '-email']:
            order_by = 'user_name'
        return Comment.objects.filter(parent=None).order_by(order_by)


class CommentDetailView(generic.DetailView):
    """Returns selected comment with all children"""
    model = Comment
    template_name = 'comment_detail.html'

    def get_queryset(self):
        tree_id = Comment.objects.get(pk=self.kwargs.get('pk')).tree_id
        return Comment.objects.filter(tree_id=tree_id)
    
    def get_object(self, queryset=None):
        return self.get_queryset()


def add_comment(request):
    """View create comment"""
    if request.POST:
        form = CommentModelForm(request.POST)
        if form.is_valid():
            if request.GET.get("parent_id"):
                parent = Comment.objects.get(id=request.GET.get("parent_id"))
            else:
                parent = None
            Comment.objects.create(
                user_name=request.POST.get("user_name"),
                email=request.POST.get("email").replace("%", "@"),
                home_page=request.POST.get("home_page"),
                text=request.POST.get("text"),
                parent=parent
            )
            return redirect("/main")
    else:
        form = CommentModelForm()

    return render(request, 'add_comment.html', {'form': form})
