"""cv_project URL Configuration
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 아래의 URL Pattern을 opencv_webapp/urls.py가 handling
    path('', include('opencv_webapp.urls')),
]
