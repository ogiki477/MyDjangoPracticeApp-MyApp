from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.urls import reverse_lazy
from blogApp.forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blogApp.models import Post,Comment
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name = "blogApp/about.html"



class PostListView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')



class PostDetailView(DetailView):
    model = Post



class PostCreateView(LoginRequiredMixin,CreateView):

    login_url="/login/"
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post

    


class PostUpdateView(LoginRequiredMixin,UpdateView):

    login_url="/login/"
    redirect_field_name = 'blogApp/post_detail.html'
    form_class = PostForm
    model = Post



class PostDeleteView(LoginRequiredMixin,DeleteView):

    model = Post
    success_url = reverse_lazy('blogApp:post_list')


class DraftListView(LoginRequiredMixin,ListView):

    login_url = '/login/'
    redirect_field_name = 'blogApp/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')



#################################################################################
#################################################################################
#################################################################################


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blogApp/post_detail.html',pk=pk)





@login_required
def add_comment_to_post(request,pk):

    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            return redirect('blogApp/post_detail.html',pk=post.pk)

        else:
            form = CommentForm()
        return render(request, 'blogApp/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blogApp/post_detail.html',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return render('blogApp/post_detail.html',pk=post_pk)


