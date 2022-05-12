from dataclasses import field, fields
import imp
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.list import ListView

import bookmark
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6

class BookmarkCrateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
