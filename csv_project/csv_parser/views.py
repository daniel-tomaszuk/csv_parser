from django.shortcuts import render, redirect
from django.views import *
from django.views.generic.edit import *
from .models import *
from .forms import *
from django.http import Http404
from django.contrib.auth.mixins import *
from django.contrib.auth.models import *
from django.contrib.auth import (authenticate, login, logout)
from django.core.urlresolvers import reverse_lazy
# from django.contrib import messages
# from django.contrib.messages import get_messages


class Login(FormView):

    template_name = 'login.html'
    # form_class in FormView !
    form_class = Login

    def get_success_url(self):
        # find your next url here
        # here method should be GET or POST.
        next_url = self.request.GET.get('next')
        if next_url:
            success_url = next_url
            return success_url  # you can include some query strings as well
        else:
            success_url = reverse_lazy('login')
            return success_url  # what url you wish to return'

    def form_valid(self, form):
        user_login = form.cleaned_data["login"]
        password = form.cleaned_data["password"]
        user = authenticate(username=user_login, password=password)
        if user is not None:
            login(self.request, user)
        return super(Login, self).form_valid(form)


class Logout(FormView):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))


class MainPage(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    def get(self, request):
        context = {
            "message": 'Main Page!',
        }
        return render(request, "main-page.html", context)

    def post(self, request):
        pass


class AddFile(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

    def get(self, request):
        form = AddFileForm()
        context = {"form": form}
        return render(request, "add-file.html", context)

    def post(self, request):
        form = AddFileForm(request.POST, request.FILES)

        if form.is_valid():
            server_path = form.cleaned_data['server_path']
            disk_file = form.cleaned_data['disk_file']
            # XOR for input fields
            if not ((server_path and not disk_file) or
                    (not server_path and disk_file)):
                raise forms.ValidationError('Please fill only one '
                                            'of the fields.')

            #
            # if server_path:
            #     # create and save File Model!
            #     new_photo = Photo.objects.create(path=server_path,
            #                                      file="Server_path",
            #                                      my_user=request.user)
            #     new_photo.save()
            # if disk_file:
            #     # save files
            #     new_photo = Photo.objects.create(path="File_path",
            #                                      file=disk_file,
            #                                      my_user=request.user)
            #     new_photo.save()

        # if form not valid
        else:
            context = {
                'message': 'Form not valid!',
                'form': form,
            }
            return render(request, "add-file.html", context)
        return redirect(reverse_lazy('main-page'))
