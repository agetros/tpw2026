from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/crear/", views.create_post, name="create_post"),
    path("post/<int:post_id>/editar/", views.edit_post, name="edit_post"),
    path("post/<int:post_id>/eliminar/", views.delete_post, name="delete_post"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
