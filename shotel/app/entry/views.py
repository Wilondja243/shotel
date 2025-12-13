import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from shotel.app.entry.models import Follower, Profil
from shotel.app.user.models import User
from .forms import AddFriendForm


class HomeView(LoginRequiredMixin, ListView):
    template_name = "entry/index.html"

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        return render(request, self.template_name, {"users": users})
    

class FriendView(LoginRequiredMixin, View):
    template_name = "entry/friend.html"

    def get(self, request):
        friends = User.objects.exclude(id=request.user.id)
        print(request.user)
        return render(request, self.template_name, {"friends": friends})
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            friendId = data.get("friend_id")

            following = get_object_or_404(User, id=friendId)
            following.is_my_follower = True

            if(Follower.objects.filter(
                follower = request.user,
                following = following).exists()):
                print("User already added.")
                return JsonResponse({"message": "User already added.",})

            Follower.objects.create(
                follower = request.user,
                following = following,
            )

            following.save()

            return JsonResponse(
                {
                    'following': serialize('json', [following]),
                    'message':'User added succesfully!',
                }
            )

        except Exception as e:
            print("l'exception est:", str(e))
            return JsonResponse({'erreur':str(e)}, status=500)
        

class FollowerView(LoginRequiredMixin, ListView):
    template_name = "entry/follower.html"

    def get(self, request):
        followers = get_object_or_404(User, id=request.user.id)
        followers = followers.follower.all()

        return render(request, self.template_name, {"followers": followers})