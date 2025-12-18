from django.db.models import Count
from shotel.app.chat.models import Conversation


def get_or_create_conversation(user1, user2):

    conversations = Conversation.objects.annotate(
        num_participants=Count('participants')) \
        .filter(num_participants=2) \
        .filter(participants=user1) \
        .filter(participants=user2)
    
    if conversations.exists():
        return conversations.first()
    else:
        new_conv = Conversation.objects.create()
        new_conv.participants.add(user1, user2)

        return new_conv