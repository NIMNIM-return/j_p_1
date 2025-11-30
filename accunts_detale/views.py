from django.shortcuts import render,redirect
from django.views import generic ,View
from django.urls import reverse_lazy
from .form import *
from django.contrib.auth import login
from django.contrib.auth.models import User

class RegesterView(generic.CreateView):
    form_class = RegesterForm
    template_name = 'registration/Regester.html'
    success_url = reverse_lazy('login')

class log_in_view(View):
    def get (self, request):
        loginform =LoginForm()
        return render(request,template_name='registration/login.html',context={'form':loginform})
    
    def post (self,request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data.get('username')
            password = loginform.cleaned_data.get('password')
            email = loginform.cleaned_data.get('email')
            user= User.objects.filter(username=username).first()
            

            if user is not None : 
                active_user= user.is_active
                if  active_user==True:
                    password_corect= user.check_password(password)
                    if password_corect :
                        login(request,user)
                        return redirect('p_list')
                
                    else:
                        loginform.add_error('password','password is wrong!!!')
                elif active_user==False:
                    loginform.add_error('password','It seems like your account is deactivated!!! (call managers)')
            else:
                loginform.add_error('username','username not found.')
            return render(request,template_name='registration/login.html',context={'form':loginform})

    

