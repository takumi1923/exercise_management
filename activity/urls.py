from django.urls import path
from .import views

app_name = "activity"

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.HomeView.as_view(), name="home"),
    path("home/", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="users_detail"), 
    path("users/<int:pk>/update/", views.UserUpdateView.as_view(), name="users_update"),
    path("lists/", views.ListListView.as_view(), name="lists_list"),
    path("lists/create/", views.ListCreateView.as_view(), name="lists_create"),
    path("lists/<int:pk>/", views.ListDetailView.as_view(), name="lists_detail"),
    path("lists/<int:pk>/update/", views.ListUpdateView.as_view(), name="lists_update"),
    path("lists/<int:pk>/delete/", views.ListDeleteView.as_view(), name="lists_delete"),
    path("cards/create/", views.CardCreateView.as_view(), name="cards_create"),
    path("cards/", views.CardListView.as_view(), name="cards_list"),
    path("cards/done", views.CardDoneView.as_view(), name="cards_done"),
    path("cards/<int:pk>/", views.CardDetailView.as_view(), name="cards_detail"),
    path("cards/<int:pk>/update/", views.CardUpdateView.as_view(), name="cards_update"),
    path("cards/<int:pk>/delete/", views.CardDeleteView.as_view(), name="cards_delete"),
    path("cards/create/<int:list_pk>", views.CardCreateFromHomeView.as_view(), name="cards_create_from_home"),
    path("rank/",views.RankView.as_view(),name="rank_create"),
    path("rank1/",views.Rank1View.as_view(),name="rank1_create"),
    path("rank2/",views.Rank1View.as_view(),name="rank2_create"),
    path("reward/",views.RewardListView.as_view(),name = "rewards_list"),
    path("reward/detail/",views.RewardDetailView.as_view(),name = "rewards_detail"),
    path("reward/<int:pk>/delete",views.RewardDeleteView.as_view(),name = "rewards_delete"),
    path("education/",views.EducationalView.as_view(),name = "education_list"),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path('mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'),

]