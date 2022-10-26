from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,resolve_url,get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView,UpdateView,CreateView,ListView,DeleteView
from .forms import UserForm,ListForm,CardCreateFromHomeForm,CardForm,RewardForm,BS4ScheduleForm,IkuseiForm,IkuseiSiyouForm,IkuseiDazeForm
from .mixins import OnlyYouMixin, BaseCalendarMixin,MonthCalendarMixin,WeekCalendarMixin,WeekWithScheduleMixin
from .models import List,Card,Rank,Excercise_Point,Reward,RewardCreate,Excercise_Time,Continue_Point,Reward_Recieve,Calendar,RewardTake,Used_Point,Ikusei_Point,Ikusei_Sum,Point_Limit,Ikusei_Siyou,Ikusei_Daze,Point_Amari
from . import graph
from .import graph1
import datetime


def index(request):
    return render(request, "kanban/index.html")

def home(request):
    return render(request,"kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("activity:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'kanban/signup.html', context)

class UserDetailView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "kanban/users/detail.html"

class UserUpdateView(OnlyYouMixin,UpdateView):
    model = User
    template_name = "kanban/users/update.html"
    form_class = UserForm

    def get_success_url(self):
        return resolve_url('activity:users_detail', pk=self.kwargs['pk'])

class ListCreateView(LoginRequiredMixin, CreateView):
    model = List
    template_name = "kanban/lists/create.html"
    form_class = ListForm
    success_url = reverse_lazy("activity:lists_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListListView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/lists/list.html"

class ListDetailView(LoginRequiredMixin, DetailView):
    model = List
    template_name = "kanban/lists/detail.html"

class ListUpdateView(LoginRequiredMixin, UpdateView):
    model = List
    template_name = "kanban/lists/update.html"
    form_class = ListForm
    success_url = reverse_lazy("activity:home")
    def get_success_url(self):
        return resolve_url('kanban:lists_detail', pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    template_name = "kanban/lists/delete.html"
    success_url = reverse_lazy("activity:home")


#予定作成に関するviews.py
class CardCreateView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html"
    form_class = CardForm
    success_url = reverse_lazy("activity:home")
   
    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.list.title == 'しっかり行えたもの':
            excercise_point = Excercise_Point.objects.create(user=self.request.user)
            excercise_point.excercise_Point += form.instance.excercise_time
            excercise_point.save()
            reward_point,_ = Reward_Recieve.objects.get_or_create(user = self.request.user)
            reward_point.reward_recieve_point += form.instance.excercise_time
            reward_point.save()
            continue_Point,_ = Continue_Point.objects.get_or_create(user = self.request.user)
            continue_Point.continue_point = Card.objects.filter(user = self.request.user, list_id = 3).count() + 1
            continue_Point.save()
            
        return super().form_valid(form)

 
class CardListView(LoginRequiredMixin, ListView):
    model = Card
    template_name = "kanban/cards/list.html"



class CardDetailView(LoginRequiredMixin, DetailView):
    model = Card
    template_name = "kanban/cards/detail.html"

class CardUpdateView(LoginRequiredMixin, UpdateView):
    model = Card
    template_name = "kanban/cards/update.html"
    form_class = CardForm
    success_url = reverse_lazy("activity:home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        if form.instance.list.title == 'しっかり行えたもの':
            excercise_point,_ = Excercise_Point.objects.get_or_create(user=self.request.user)
            excercise_point.excercise_Point += form.instance.excercise_time
            excercise_point.save()
            reward_point,_ = Reward_Recieve.objects.get_or_create(user = self.request.user)
            reward_point.reward_recieve_point += form.instance.excercise_time * 10
            reward_point.save()
            continue_Point,_ = Continue_Point.objects.get_or_create(user = self.request.user)
            continue_Point.continue_point = Card.objects.filter(user = self.request.user, list_id= 3).count() + 1
            continue_Point.save()
            
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('activity:cards_detail', pk=self.kwargs['pk'])

    


class CardDeleteView(LoginRequiredMixin, DeleteView):
    model = Card
    template_name = "kanban/cards/delete.html"
    form_class = CardForm
    success_url = reverse_lazy("activity:home")

class EducationalView(LoginRequiredMixin,CreateView):
    model = Ikusei_Sum
    form_class = IkuseiForm
    template_name = "kanban/education/list.html"
    success_url = reverse_lazy("activity:education_list")


    def form_valid(self,form):
        form.instance.user = self.request.user
        reward_point,_ = Reward_Recieve.objects.get_or_create(user = self.request.user)
        Ikusei_sum,_= Ikusei_Sum.objects.get_or_create(user=self.request.user)
        Point_limit,_ = Point_Limit.objects.get_or_create(user=self.request.user)
        Point_amari,_ = Point_Amari.objects.get_or_create(user = self.request.user)
        Used_point,_= Used_Point.objects.get_or_create(user = self.request.user)
        if  reward_point.reward_recieve_point < form.instance.ikusei_point:
            form.add_error(None,'ポイントが足りません')
            return super().form_invalid(form)
        else:
            Ikusei_sum.ikusei_sum += form.instance.ikusei_point
            Ikusei_sum.save()
            Point_limit.point_limit += form.instance.ikusei_point
            Point_limit.save()
            reward_point.reward_recieve_point -= form.instance.ikusei_point
            reward_point.save()
            return super().form_valid(form)

        
            
        


        
        

        



class HomeView(LoginRequiredMixin, ListView):
    model = List
    template_name = "kanban/home.html"

class CardCreateFromHomeView(LoginRequiredMixin, CreateView):
    model = Card
    template_name = "kanban/cards/create.html" 
    form_class = CardCreateFromHomeForm
    success_url = reverse_lazy("activity:home")
  
    def form_valid(self, form):
        list_pk = self.kwargs['list_pk']
        list_instance = get_object_or_404(List, pk=list_pk)
        form.instance.list = list_instance
        form.instance.user = self.request.user
        
        if list_instance.title == 'しっかり行えたもの':
            excercise_point,_ = Excercise_Point.objects.get_or_create(user=self.request.user)
            excercise_point.excercise_Point += form.instance.excercise_time
            excercise_point.save()
            reward_point,_ = Reward_Recieve.objects.get_or_create(user = self.request.user)
            reward_point.reward_recieve_point += form.instance.excercise_time * 10
            reward_point.save()
            continue_Point,_ = Continue_Point.objects.get_or_create(user = self.request.user)
            continue_Point.continue_point = Card.objects.filter(user = self.request.user, list_id = 3).count() + 1
            continue_Point.save()
            
        return super().form_valid(form)

class RewardListView(LoginRequiredMixin,CreateView):
    model = RewardTake
    form_class = RewardForm
    template_name = "kanban/rewards/list.html"
    success_url = reverse_lazy("activity:rewards_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        Used_point,_= Used_Point.objects.get_or_create(user = self.request.user)
        Point_limit,_= Point_Limit.objects.get_or_create(user=self.request.user)
        reward_point,_ = Reward_Recieve.objects.get_or_create(user = self.request.user)
        Point_amari,_ = Point_Amari.objects.get_or_create(user = self.request.user)
        if  reward_point.reward_recieve_point < form.instance.point:
            form.add_error(None,'ポイントが足りません')
            return super().form_invalid(form)
        else:
            Used_point.used_point += form.instance.point
            Used_point.save()
            Point_limit.point_limit += form.instance.point
            Point_limit.save()
            reward_point.reward_recieve_point -= form.instance.point
            reward_point.save()
            return super().form_valid(form)

        
            

        
            
        
        
            

       
        
        
        

class RewardDetailView(LoginRequiredMixin, ListView):
    model = RewardTake
    template_name = "kanban/rewards/list1.html"
    
class RewardDeleteView(LoginRequiredMixin, DeleteView):
    model = RewardTake
    template_name = "kanban/rewards/delete.html"
    form_class = RewardForm
    success_url = reverse_lazy("activity:rewards_list")

class RewardRecieveView(LoginRequiredMixin,ListView):
    model = Reward_Recieve
    template_name = "kanban/rewards/list.html"

    
class RankView(LoginRequiredMixin,ListView):
    model = Excercise_Point
 
    #テンプレートファイル連携
    template_name = "kanban/rank/rank.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        qs    = Excercise_Point.objects.all()  #モデルクラス(ProductAテーブル)読込
        x     = [x.user.username for x in qs]           #X軸データ
        y     = [y.excercise_Point for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)   
        
        
        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
        
        return context

    def get_context_data1(self, **kwargs):

        #グラフオブジェクト
        ls    = Continue_Point.objects.all()  #モデルクラス(ProductAテーブル)読込
        a     = [a.user.username for a in ls]           #X軸データ
        b     = [b.continue_point for b in ls]  
        chart1 = graph.Plot_Graph1(a,b)   
        
        
        #変数を渡す
        context1 = super().get_context_data1(**kwargs)
        context1['chart1'] = chart1
        
        return context1

    

    

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)



class Rank1View(LoginRequiredMixin,ListView):
    model = Continue_Point

    #テンプレートファイル連携
    template_name = "kanban/rank/rank1.html"

    #変数としてグラフイメージをテンプレートに渡す
    def get_context_data(self, **kwargs):

        #グラフオブジェクト
        ls    = Continue_Point.objects.all()  #モデルクラス(ProductAテーブル)読込
        a     = [a.user.username for a in ls]           #X軸データ
        b     = [b.continue_point for b in ls]  
        chart1 = graph1.Plot_Graph1(a,b)   
        
        
        #変数を渡す
        context1 = super().get_context_data(**kwargs)
        context1['chart1'] = chart1
        
        return context1

    

    #get処理
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
              #Y軸データ
        
    

    


class MyCalendar(MonthCalendarMixin, WeekWithScheduleMixin,CreateView):
    """月間カレンダー、週間カレンダー、スケジュール登録画面のある欲張りビュー"""
    template_name = 'kanban/Calendar/mycalendar.html'
    model = Calendar
    date_field = 'date'
    form_class = BS4ScheduleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week_calendar_context = self.get_week_calendar()
        month_calendar_context = self.get_month_calendar()
        context.update(week_calendar_context)
        context.update(month_calendar_context)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today()
        schedule = form.save(commit=False)
        schedule.date = date
        schedule.save()
        return redirect('activity:mycalendar', year=date.year, month=date.month, day=date.day)


    
    

