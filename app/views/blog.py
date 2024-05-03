from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from app.forms import CommentForm
from app.models import BlogPost, Comment


class PostDetailView(View):

    @staticmethod
    def get_context(post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        latest_posts = BlogPost.objects.exclude(id=post_id)[:4]
        comments = Comment.objects.filter(post=post).order_by('-date').all()
        context = {
            'post': post,
            'comments': comments,
            'latest_posts': latest_posts
        }
        return context

    def get(self, request, post_id):
        context = self.get_context(post_id)
        return render(request, 'blog/blog-detail.html', context=context)

    def post(self, request, post_id):
        post = get_object_or_404(BlogPost, id=post_id)
        context = self.get_context(post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            comment = form.cleaned_data.get('comment')
            subject = form.cleaned_data.get('subject')

            comment = Comment(fullname=fullname, email=email, comment=comment, subject=subject, post=post)
            comment.save()

            messages.success(request, 'Your comment has been successfully left.')
            return redirect('post_detail', post_id=post_id)

        return render(request, 'blog/blog-detail.html', context=context)
