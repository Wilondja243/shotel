from django import forms

from shotel.app.chat.models import Message


class ChatForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['message',]

        widgets = {
            "message": forms.TextInput(attrs={
                "class": "input-message",
                "placeholder": "Envoyer un message",
                "required": False
            })
        }