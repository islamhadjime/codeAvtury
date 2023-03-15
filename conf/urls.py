from django.urls import path,include
from django.contrib import admin
from posts.views import post_list,detail_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='home'),
    path('detail/<int:pk>/',detail_post,name="detail_post"),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
