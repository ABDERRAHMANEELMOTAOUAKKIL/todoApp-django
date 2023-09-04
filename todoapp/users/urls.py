from django.urls import path
from .views import RegisterView,CustomLoginView,UserProfileView
from django.contrib.auth.views import LogoutView
from .import views


urlpatterns = [
    # Other URL patterns
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# htmx_urlpatterns = [
#     path('check_email/', views.check_email, name='check_email'),
# ]

# urlpatterns += htmx_urlpatterns