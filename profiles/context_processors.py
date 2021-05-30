
from followers.models import Follower
from feed.models import Post

def message_processor(request):
    if request.user.is_authenticated:
        user = request.user
        following = Follower.objects.filter(followed_by=user).count()
        followers = Follower.objects.filter(following=user).count()
        totalposts = Post.objects.filter(author=request.user).count()
    else:
        following = 0
        followers = 0
        totalposts = 0
    return {
        'total_following' : following,
        'total_followers' : followers,
        'total_posts' : totalposts,
    }