from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic import UpdateView, DetailView, View
from django.urls import reverse_lazy



from followers.models import  Follower
from .models import Profile

class ProfileDetailView(DetailView):
    http_method_names = ['get']
    template_name = "profiles/detail.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"
    
class FollowView(LoginRequiredMixin, View):
    http_method_names=['post']
    def post(self, request, *args, **kwargs):
        data = request.POST.dict()

        if "action" not in data or "username" not in data:
            return HttpResponseBadRequest("Missing data")

        try:
            other_user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return HttpResponseBadRequest("Missing user")

        if data['action'] == 'follow':
            #follow
            follower, created = Follower.objects.get_or_create(
                followed_by=request.user,
                following=other_user,
            )
        else:
            #unfollow
            try:
                follower = Follower.objects.get(
                    followed_by=request.user,
                    following=other_user,
                )
            except Follower.DoesNotExist:
                follower = None
            
            if follower:
                follower.delete()

 
        return JsonResponse({
            'success':True,
            'wording': "Unfollow" if data['action'] == "follow" else "Follow"
        })

class UserProfileView(DetailView):
    http_method_names = ['get']
    template_name = "profiles/userprofile.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"

class ManageUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    http_method_names = ['get', 'post']
    template_name = "profiles/manageprofile.html"
    model = User
    context_object_name = "user"
    slug_field = "username"
    slug_url_kwarg = "username"
    success_url ="../../{username}/profile"
    success_message = "Your Profile has been updated!"
    fields = ['username', 'last_name', 'first_name', 'email']

    if http_method_names == 'POST':

        def dispatch(self, request, *args, **kwargs):
            self.request = request
            return super().dispatch(request, *args, **kwargs)
        
        def form_valid(self, form):
            obj = form.save(commit=False)
            obj.save()
            return super().form_valid(form)

        def get_success_message(self, cleaned_data):
            return self.success_message % dict(
                cleaned_data,
                calculated_field=self.object.calculated_field,
            )

        def get_success_url(self):
            return reverse_lazy('detail', kwargs={"username": self.request.user.username})

class ManageProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    http_method_names = ['get', 'post']
    template_name = "profiles/manageprofiledetails.html"
    model = Profile
    slug_field = "user_id"
    slug_url_kwarg = "user_id"
    success_url ="."
    fields = ['image']
    success_message = "Your Avatar has been updated!"

    if http_method_names == 'POST':
        def dispatch(self, request, *args, **kwargs):
            self.request = request
            return super().dispatch(request, *args, **kwargs)
        
        def form_valid(self, form):
            obj = form.save(commit=False)
            obj.save()
            return super().form_valid(form)

        def get_success_message(self, cleaned_data):
            return self.success_message % dict(
                cleaned_data,
                calculated_field=self.object.calculated_field,
            )