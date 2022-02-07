"""site_2 URL Configuration
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # "127.0.0.1:8000/polls/" 이후의 URL은 polls/urls.py가 handling
    path('polls/', include('polls.urls')),
]
