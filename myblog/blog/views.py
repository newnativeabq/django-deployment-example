# Django Utility classes/functions
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Local Classes
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm

# Django View Classes
from django.views.generic import (
    TemplateView, ListView,
    DetailView, CreateView,
    UpdateView, DeleteView
)

## For Function-Based Views specifically
from django.contrib.auth.decorators import login_required


# Create your views here.
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # __lte stands for less than or equal to in Django ORM query
        # ..(-pub...) the minus sign reverses sort order
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:5]

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login'
    model = Post
    redirect_field_name = 'blog/post_detail.html'

    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'blog/post_drafts.html'

    def get_queryset(self):
        # __lte stands for less than or equal to in Django ORM query
        # ..(-pub...) the minus sign reverses sort order
        return Post.objects.filter(published_date__isnull=True).order_by('-published_date')


###############################
###############################
# Function-Based comment views

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # variable object 'comment' could be named anything here.
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    
    return render(request, 'blog/comment_form.html', context={'form':form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
