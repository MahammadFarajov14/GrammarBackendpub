from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse_lazy
from django.views.generic import FormView
from core.forms import CheckUpForm

# Create your views here.

class Home(FormView):
    form_class = CheckUpForm
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid() and form.accept_policy:
            checkup = form.save(False)
            checkup.phone_number = '+994' + checkup.phone_number
            form.save()
            return redirect(reverse_lazy('home'))