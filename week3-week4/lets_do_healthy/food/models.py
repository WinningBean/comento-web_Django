from django.db import models


class Food(models.Model):  # 음식
    name = models.CharField(max_length=50)  # 음식 이름
    manufacturer = models.CharField(max_length=50, null=True)  # 제조사명
    pic = models.CharField(max_length=300, null=True)  # 음식사진 링크
    food_categorize = (
        ('c1', '자연 식품'),
        ('c2', '건강기능 식품'),
        ('c3', '가공 식품')
    )
    food_unit = models.CharField(max_length=50)  # 음식 단위 (ml, g 등)품
    food_ex = models.CharField(max_length=500, null=True)  # 추가 설명
    created_date = models.DateTimeField(auto_now_add=True)  # 작성일
    update_date = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.name + " (" + self.manufacturer + ")" if self.manufacturer is None else self.name  # 음식 이름 (제조사명)


class NutritionFacts(models.Model):  # 영양정보
    food = models.ForeignKey(Food, on_delete=models.CASCADE)  # 음식이 삭제될 때 영양정보도 삭제된다
    standard_per = models.FloatField  # 기준 무게
    calories = models.FloatField(default=0)  # 칼로리
    total_fat = models.FloatField(default=0)  # 총 지방
    saturated_fat = models.FloatField(default=0)  # 포화 지방
    trans_fat = models.FloatField(default=0)  # 트랜스 지방
    cholesterol = models.FloatField(default=0)  # 콜레스테롤
    sodium = models.FloatField(default=0)  # 나트륨
    potassium = models.FloatField(default=0)  # 칼륨
    total_carbohydrate = models.FloatField(default=0)  # 총 탄수화물
    dietary_fiber = models.FloatField(default=0)  # 식이섬유
    sugars = models.FloatField(default=0)  # 당류
    protein = models.FloatField(default=0)  # 단백질
    vitamin_A = models.FloatField(default=0)  # 비타민 A
    vitamin_C = models.FloatField(default=0)  # 비타민 C
    calcium = models.FloatField(default=0)  # 칼슘
    iron = models.FloatField(default=0)  # 철분
    nutritionFacts_ex = models.CharField(max_length=500, null=True)  # 추가 설명

    def __float__(self):
        return self.calories
