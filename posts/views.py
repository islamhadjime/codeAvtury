from django.shortcuts import render, get_object_or_404 
from django.db.models import Count
from .models import Post,Curs,Comment
from .forms import CommentForm
from taggit.models import Tag

def post_list(request):
    context = {
        'posts':Post.published.all(),
        'curs':Curs.objects.all()
    }
    return render(request,'posts/home.html',context)


def detail_post(request,pk):
    post  = get_object_or_404(Post,pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()


    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)

    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                .order_by('-same_tags','-publish')[:4]


    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts':similar_posts}

    return render(request,'posts/detail.html',context)