from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView

from shotel.app.user.models import User
from shotel.app.chat.models import Chat
from shotel.app.chat.forms import ChatForm


class ChatView(LoginRequiredMixin, View):
    template_name = "entry/chat.html"
    form_class = ChatForm

    def get(self, request, receive_id):
        form = self.form_class()
        other_user = get_object_or_404(User, id=receive_id)

        messages = Chat.objects.filter(
            Q(sender=request.user, receiver=other_user) |
            Q(sender=other_user, receiver=request.user)
        ).order_by("created_at")

        return render(
            request, self.template_name,
            {"form": form, 'messages': messages, 'other_user': other_user}
        )
    
    def post(self, request, receive_id):
        other_user = get_object_or_404(User, id=receive_id)

        messages = Chat.objects.filter(
            Q(sender=request.user, receiver=other_user) |
            Q(sender=other_user, receiver=request.user)
        ).order_by("created_at")

        form = self.form_class(request.POST)

        if form.is_valid():

            Chat.objects.create(
                sender=request.user,
                receiver=other_user,
                message=form.cleaned_data['message'],
            )
        else:
            form = self.form_class()
        
        return render(
            request, self.template_name,
            {'form': form, 'other_user': other_user, 'messages': messages}
        )
