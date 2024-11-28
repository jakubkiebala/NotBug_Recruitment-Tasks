from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.views import View
from .models import Like, Post
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(View):
    def get(self, request):
        return render(request, 'blog/home.html')


class Register(View):
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        return render(request, 'blog/register.html', {'form': form})

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'blog/register.html', {'form': form})


class UserLogin(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
        return render(request, 'blog/login.html')

    def get(self, request):
        return render(request, 'blog/login.html')


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class PostList(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-updated_at')
        return render(request, 'blog/post_list.html', {'posts': posts})


class CreatePost(LoginRequiredMixin, View):
    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        return redirect('post_list')

    def get(self, request):
        return render(request, 'blog/create_post.html')


class EditPost(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if post.author != request.user:
            return redirect('post_list')
        return render(request, 'blog/edit_post.html', {'post': post})

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if post.author != request.user:
            return redirect('post_list')
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_list')


class PostDetail(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user_liked = Like.objects.filter(user=request.user, post=post).exists()

        return render(request, 'blog/post_detail.html', {'post': post, 'user_liked': user_liked})


class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
        else:
            Like.objects.create(user=request.user, post=post)

        return redirect('post_detail', post_id=post.id)