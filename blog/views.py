from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from blog.forms import BlogForm, CommentForm
from blog.models import Blog, Comment
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# Create your views here.
class BlogView(CreateView):
    template_name = 'blogs.html'
    form_class = BlogForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        formcom = CommentForm

        context['blogs'] = Blog.objects.all()
        context['comments'] = Comment.objects.all()
        context['formcomments'] = formcom

        if self.request.method == 'POST':
            formcom = CommentForm(data=self.request.POST)
            if formcom.is_valid():
                formcom.save()

        return context

    def form_invalid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _("Succesfully Sent!"))
        return super().form_invalid(form)
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            blog = form.save(False)
            blog.user = self.request.user
            form.save()
            return redirect(reverse_lazy('blog'))