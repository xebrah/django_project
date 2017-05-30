
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^tables/', include('tables.urls')),
    url(r'^', include('tables.urls'))
]
