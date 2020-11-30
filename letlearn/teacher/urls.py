
from django.contrib import admin
from django.urls import path
from teacher import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', views.login_page, name="login_page"),
    path('portal', views.portal, name="portal"),
    path('', views.home, name="home"),
    path('logout', views.logout_page, name="logout_page"),
    path('Assignment', views.Assignment, name="Assignmnet_page"),
    path('add_ass', views.addAssignment, name="addAssignmnet"),
    path('uploaded_ass', views.uploadedAssignment, name="uploadedAssignmnet"),
    path('delete_ass', views.deleteAssignment, name="deleteAssignmnet"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
