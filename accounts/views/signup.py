from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import SignUpForm
from . import signin


class SignUpView(View):
    """ User registration view """

    template_name = "accounts/signup.html"
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        context = {"form": forms}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            forms.save()

            #formSignIn = signin.SignInView.form_class(request.POST)

            email = forms.cleaned_data["email"]
            password = forms.cleaned_data["password1"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("accounts:profile-creation")
        context = {"form": forms}
        return render(request, self.template_name, context)
