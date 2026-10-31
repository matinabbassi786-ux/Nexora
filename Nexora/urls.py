from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.mail import get_connection, send_mail
from django.db import connection
from django.urls import path,include



from django.http import HttpResponse
from django.views.decorators.http import require_GET

from django.core import mail
from .tasks import send_notification

@require_GET
def views(request):
    backend = mail.mailers["default"]
    email = mail.EmailMessage(
        subject="Report Attached",
        body="Please find your monthly report attached.",
        from_email=None,
        to=["matinabbassi786@gmail.com"],
        connection=backend,
    )

    task = send_notification.delay(
        101,
        "Hello0000000000000000 from Nexora!"
    )



    

    return HttpResponse(f"Pass  {task.id}")



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views)
]
#  MEDIA files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  debug_toolbar 
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns