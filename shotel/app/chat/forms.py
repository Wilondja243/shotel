from django import forms

from shotel.app.chat.models import Chat


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['message',]

        widget = {
            "message": forms.TextInput(attrs={"placeholder": "message", "required": False})
        }