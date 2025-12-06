from django import forms

from shotel.app.chat.models import Chat


class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = ['message',]

        widgets = {
            "message": forms.TextInput(attrs={
                "class": "input-message",
                "placeholder": "Envoyer un message",
                "required": False
            })
        }