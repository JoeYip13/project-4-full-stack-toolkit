from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Post
from .forms import CommentForm, PostForm


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_count": comment_count,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        liked = False

        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Comment awaiting approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented_count": comment_count,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def comment_delete(request, slug, comment_id, *args, **kwargs):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = post.comments.filter(id=comment_id).first()

    if comment.name == request.user.username:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_edit(request, slug, comment_id, *args, **kwargs):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = post.comments.filter(id=comment_id).first()

        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.name == request.user.username:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(SuccessMessageMixin, CreateView):
    """
    Adding a new post view
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_message = '%(title)s was created successfully - awaiting approval'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(SuccessMessageMixin, UpdateView):
    """
    Update post view
    """
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_message = '%(title)s was updated successfully'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView):
    """
    Delete a post view
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = 'Blog post was deleted successfully'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePostView, self).delete(request, *args, **kwargs)


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)
