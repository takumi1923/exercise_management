import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# models.py
class Card(models.Model):
    title = models.CharField('予定タイトル',max_length=200)
    description = models.TextField('予定概要')
    date = models.DateField('運動活動日')
    start_time = models.TimeField('運動開始時間',default=datetime.time(7,0,0))
    excercise_time = models.DecimalField('予定活動時間',max_digits=2,decimal_places=1,default=0.0,validators=[MinValueValidator(0.5), MaxValueValidator(9.9)])
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    list = models.ForeignKey(List,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Excercise_Point(models.Model):
    excercise_Point = models.DecimalField(max_digits=5,decimal_places=1,default=0.0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)




class Rank(models.Model):
    excercise_time_sum = models.DecimalField(max_digits=5,decimal_places=1,default=0.0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



    

class Reward(models.Model):
    title = models.CharField(max_length=200)
    comsumption_point = models.IntegerField('消費ポイント',default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comsumption_Point(models.Model):
    comsumption_point= models.IntegerField('消費ポイント',validators=[MinValueValidator(1), MaxValueValidator(5)],default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.comsumption_point)
    


    
class RewardCreate(models.Model):
    date = models.DateField('受け取る日付')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    list = models.ForeignKey(Reward,on_delete=models.CASCADE)
    
class RewardTake(models.Model):
    date = models.DateField('ご褒美を受けとる日付')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reward = models.ForeignKey(Reward,on_delete=models.CASCADE)
    point = models.IntegerField('ご褒美に使用するポイント',validators=[MinValueValidator(1), MaxValueValidator(5)],default = 0)






class Excercise_Time(models.Model):
    excercise_sum = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

class Continue_Point(models.Model):
    continue_point = models.IntegerField('運動ポイント',default =0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Reward_Recieve(models.Model):
    reward_recieve_point = models.IntegerField('運動ポイント',default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Used_Point(models.Model):
    used_point = models.IntegerField('使用済ポイント', default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Calendar(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField('日付')
    start_time = models.TimeField('開始時間',default=datetime.time(7,0,0))
    excercise_time = models.DecimalField(max_digits=2,decimal_places=1,default=0.0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    list = models.ForeignKey(List,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Ikusei_Point(models.Model):
    ikusei_point = models.IntegerField('育成に運動ポイントを使用する',validators=[MinValueValidator(1), MaxValueValidator(3)],default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Ikusei_Siyou(models.Model):
    ikusei_siyou = models.IntegerField('育成に運動ポイントを使用する',validators=[MinValueValidator(1), MaxValueValidator(5)],default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Ikusei_Sum(models.Model):
    ikusei_sum = models.IntegerField('育成合計ポイント',default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Point_Limit(models.Model):
    point_limit = models.IntegerField('残りポイント',default = 0)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

class Ikusei_Suruze(models.Model):
    ikusei_suruze = models.IntegerField('育成するぜ',default = 0)
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    def __str__(self):
        return str(self.ikusei_suruze)

class Ikusei_Daze(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    ikusei_daze = models.ForeignKey(Ikusei_Suruze,on_delete=models.CASCADE)
   
class Point_Amari(models.Model):
    point_amari = models.IntegerField('余っているポイント',default= 0)
    user = models.ForeignKey(User,on_delete= models.CASCADE)


    
# Create your models here.
