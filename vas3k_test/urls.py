from django.urls import path

from . import views


urlpatterns = [
    path("", views.PostsView.as_view()),
    path("post/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("travels/<slug:slug>/", views.TravelDetailView.as_view(), name="travel_detail"),
    path("notes/<slug:slug>/", views.NotesDetailView.as_view(), name="notes_detail"),
    path("challenges/<slug:slug>/", views.ChallengeDetailView.as_view(), name="challenge_detail"),

]
