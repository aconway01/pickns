from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
from django.db.models import IntegerField

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from .models import Equibasethoroughbredhorses, Equibasejockeys, Equibaseowners, Equibasethoroughbredhorses, Equibasetrainers

# Create your views here.

def registerPage(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)
            # Customer.objects.create(
            #     user=user,
            #     name=user.username,
            # )

            # messages.success(request,'Account was created for ' + username)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request,'profiles/register.html',context)

# class RegisterPage(FormView):
#     template_name = 'races/register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('races:home')

#     def form_valid(self,form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)

#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('races:home')
#         return super(RegisterPage, self).get(*args, **kwargs)

@login_required
def userPage(request):

    context = {
    }

    return render(request,'profiles/user.html',context)