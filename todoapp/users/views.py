from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DetailView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.http import JsonResponse,HttpResponse


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    
def check_email(request):
    email = request.POST.get('email', '')
    if CustomUser.objects.filter(email=email).exists():
         return HttpResponse("This email already exists")
    else:
         return HttpResponse("This email is available")
    
class CustomLoginView(LoginView):
        template_name = 'login.html'
        success_url = reverse_lazy('home')

class UserProfileView(LoginRequiredMixin ,DetailView):
    model = CustomUser
    template_name = 'profile.html'
    # context_object_name = 'user_profile'
    
    def get_object(self, queryset=None):
        return self.request.user


