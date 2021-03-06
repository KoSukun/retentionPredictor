"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# import retentionPredict.urls
# import sw.urls
import main.views
# import minjae.urls
# import hyelyeon.urls

urlpatterns = [
    path('', main.views.Index.as_view(), name="index"),
    # path('admin/', admin.site.urls),
    # path('retentionPredict/', include(retentionPredict.urls), name="retentionPredict"),
    # path('sw/', include(sw.urls), name="sw"),
    # path('minjae/', include(minjae.urls), name="minjae"),
    # path('hyelyeon/', include(hyelyeon.urls), name="hyelyeon"),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
