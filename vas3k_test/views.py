from unicodedata import category

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Post, Category, Travel, Notes, Challenge


class Travels:
    def get_travel(self):
        return Travel.objects.all()


class Challenges:
    def get_challenge(self):
        return Challenge.objects.all()


class Note:
    def get_notes(self):
        return Notes.objects.all()


class PostsView(Challenges, Note, Travels, ListView):
    """Список постов"""
    model = Post
    queryset = Post.objects.filter(draft=False)
    template_name = "vas3k/iindex.html"


class TravelDetailView(DetailView):
    """Подробное описание поста"""
    model = Travel
    slug_field = "url"
    template_name = "vas3k/travel_detail.html"


class NotesDetailView(DetailView):
    """Подробное описание поста"""
    model = Notes
    slug_field = "url"
    template_name = "vas3k/notes_detail.html"


class ChallengeDetailView(DetailView):
    """Подробное описание поста"""
    model = Challenge
    slug_field = "url"
    template_name = "vas3k/challenges_detail.html"


class PostDetailView(DetailView):
    """Подробное описание поста"""
    model = Post
    slug_field = "url"
    template_name = "vas3k/blog_detail.html"