from django.urls import include, path

urlpatterns = [

    path('admin/', include('api.admin.urls')),
    # path('site/', include('api.urls')),
]
