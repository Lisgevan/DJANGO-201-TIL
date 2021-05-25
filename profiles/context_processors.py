
from followers.models import Follower
from feed.models import Post

def message_processor(request):
    if request.user.is_authenticated:
        user = request.user
        following = Follower.objects.filter(followed_by=user).count()
        totalposts = Post.objects.filter(author=request.user).count()
    else:
        following = 0
        totalposts = 0
    return {
        'total_following' : following,
        'total_posts' : totalposts
    }