from django.views import generic
from django.shortcuts import render, redirect

from .forms import CommentModelForm
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


class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = 'comment_detail.html'

    def get_queryset(self):
        tree_id = Comment.objects.get(pk=self.kwargs.get('pk')).tree_id
        return Comment.objects.filter(tree_id=tree_id)
    
    def get_object(self, queryset=None):
        return self.get_queryset()


def add_comment(request):
    if request.POST:
        form = CommentModelForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            request_body = request.body.decode("utf").split("&")
            request_dict = {}
            for i in request_body:
                request_dict[i.split("=")[0]] = i.split("=")[1]
            Comment.objects.create(
                user_name=request_dict.get("user_name"),
                email=request_dict.get("email").replace("%", "@"),
                home_page=request_dict.get("home_page"),
                text=request_dict.get("text")
            )
            return redirect("/main")
    else:
        form = CommentModelForm()

    return render(request, 'add_comment.html', {'form': form})
    # return redirect("/main")