from django.db import models

import urllib.request as ul
import xmltodict
import json
import sys
import io


class Food:  # 음식
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
    # 아톰에디터 한글사용을 위한 구문

    def searchFood(input):
        service_key = ""  # 공공데이터 인증키
        url = "http://apis.data.go.kr/1470000/FoodNtrIrdntInfoService/getFoodNtrItdntList?ServiceKey=" + service_key + "&desc_kor=" + input + "&numOfRows=10"
        # 데이터를 받을 url

        request = ul.Request(url)
        # url의 데이터를 요청함

        response = ul.urlopen(request)
        # 요청받은 데이터를 열어줌

        rescode = response.getcode()
        # 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
        if (rescode == 200):
            responseData = response.read()
            # 요청받은 데이터를 읽음
            rD = xmltodict.parse(responseData)
            # XML형식의 데이터를 dict형식으로 변환시켜줌

            rDJ = json.dumps(rD)
            # dict 형식의 데이터를 json형식으로 변환

            rDD = json.loads(rDJ)
            # json형식의 데이터를 dict 형식으로 변환

        return rDD

# class Food(models.Model):  # 음식
#     name = models.CharField(max_length=50)  # 음식 이름
#     manufacturer = models.CharField(max_length=50, null=True)  # 제조사명
#     pic = models.CharField(max_length=300, null=True)  # 음식사진 링크
#     food_categorize = (
#         ('c1', '자연 식품'),
#         ('c2', '건강기능 식품'),
#         ('c3', '가공 식품')
#     )
#     food_unit = models.CharField(max_length=50)  # 음식 단위 (ml, g 등)품
#     food_ex = models.CharField(max_length=500, null=True)  # 추가 설명
#     created_date = models.DateTimeField(auto_now_add=True)  # 작성일
#     update_date = models.DateTimeField(auto_now=True)  # 수정일
#
#     def __str__(self):
#         return self.name + " (" + self.manufacturer + ")" if self.manufacturer is None else self.name  # 음식 이름 (제조사명)
#
#
# class NutritionFacts(models.Model):  # 영양정보
#     food = models.ForeignKey(Food, on_delete=models.CASCADE)  # 음식이 삭제될 때 영양정보도 삭제된다
#     standard_per = models.FloatField  # 기준 무게
#     calories = models.FloatField(default=0)  # 칼로리
#     total_fat = models.FloatField(default=0)  # 총 지방
#     saturated_fat = models.FloatField(default=0)  # 포화 지방
#     trans_fat = models.FloatField(default=0)  # 트랜스 지방
#     cholesterol = models.FloatField(default=0)  # 콜레스테롤
#     sodium = models.FloatField(default=0)  # 나트륨
#     potassium = models.FloatField(default=0)  # 칼륨
#     total_carbohydrate = models.FloatField(default=0)  # 총 탄수화물
#     dietary_fiber = models.FloatField(default=0)  # 식이섬유
#     sugars = models.FloatField(default=0)  # 당류
#     protein = models.FloatField(default=0)  # 단백질
#     vitamin_A = models.FloatField(default=0)  # 비타민 A
#     vitamin_C = models.FloatField(default=0)  # 비타민 C
#     calcium = models.FloatField(default=0)  # 칼슘
#     iron = models.FloatField(default=0)  # 철분
#     nutritionFacts_ex = models.CharField(max_length=500, null=True)  # 추가 설명
#
#     def __float__(self):
#         return self.calories
