from django.shortcuts import render, get_object_or_404 
from django.db.models import Count
from .models import Post,Curs,Comment,PostCountViews
from .forms import CommentForm
from taggit.models import Tag

def post_list(request):
    context = {
        'posts':Post.published.all(),
        'curs':Curs.objects.all()
    }
    return render(request,'posts/home.html',context)





def count_post(req,post):
    if not req.session.session_key:
        req.session.save()
    session_key = req.session.session_key


    is_views = PostCountViews.objects.filter(postId=post.id, sesId=session_key)
    if is_views.count() == 0 and str(session_key) != 'None':


        views = PostCountViews()
        views.sesId = session_key
        views.postId = post
        views.save

        post.count_views +=1
        post.save()

def detail_post(request,pk):
    post  = get_object_or_404(Post,pk=pk)
    count_post(request,post)

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
        'similar_posts':similar_posts
    }

    return render(request,'posts/detail.html',context)