from django.contrib import admin
from django.urls import path

import portfolio.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.index, name='index'),

    path('jobs/', portfolio.views.jobs, name='jobs'),
    # path('jobs/<int:job_id>', portfolio.views.job_detail, name='job_detail'),

    path('certificates/', portfolio.views.certificates, name='certificates'),
    # path('certificates/<int:cert_id>', portfolio.views.certificate_detail, name='certificate_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
