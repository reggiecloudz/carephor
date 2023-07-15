from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from small_groups.models import SmallGroup
from posts.forms import PostPhotoForm, PostTextForm
from posts.models import Post, Media

@login_required
def post_photo_create(request, pk):
    group = SmallGroup.objects.get(pk=pk)
    
    # check if group member
    
    if request.method == 'POST':
        form = PostPhotoForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            files = request.FILES.getlist('images')
            post = Post.objects.create(
                author=request.user.member,
                text=form.cleaned_data['text'], 
                group=group,
                post_type='Photo'
            )
            for image in files:
                Media.objects.create(
                    description=f"Photo for post {post.id}",
                    file=image,
                    post=post
                )
            return redirect("groups:profile", group.slug)
        return redirect("groups:profile", group.slug)
            
            