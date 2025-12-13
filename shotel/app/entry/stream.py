import time
from django.core.serializers import serialize
from django.http import StreamingHttpResponse

from .models import Notification
from shotel.app.user.models import User


def notification_stream(request):
    def event_stream():
        last_id = None

        while True:
            latest = User.objects.last()

            print("lastest: ", latest)

            if latest and (last_id == None and latest.id != last_id):
                last_id = latest.id

                yield f"data: {serialize('json', [latest])}"
                time.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type='text/event=stream')
