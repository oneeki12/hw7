from django.db import models
from django.contrib.auth.models import User

# Здесь идет кастомизация

class CustomUser(User):
    MALE = 1
    FEMALE = 2
    PROGRAMMER = 3
    GENDER_TYPE = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (PROGRAMMER, 'Программист'),
    )

    OCUP_CHOICE = (
        ("STUDENT", "Студент"),
        ("WORKER", "Работающий"),
        ("JOBLESS", "Без работы"),
        ("RETIRED", "Пенсионер"),
        ("MILLIONAIRE", "Миллионер")
    )

    CONTINENT_CHOICE = (
        ("NORTH AMERICA", "Северная Америка"),
        ("SOUTH AMERICA", "Южная Америка"),
        ("EUROPE", "Европа"),
        ("AFRICA", "Африка"),
        ("ANTARCTICA", "Антарктика"),
        ("ASIA", "Азия"),
        ("AUSTRALIA", "Австралия")
    )

    OPERATOR_CHOICE = (
        ("BEELINE", "Билайн"),
        ("OSHKA", "О!"),
        ("MEGACOM", "Мегаком")
    )

    ANIME_SITE = (
        ("YUMMYANIME", "YummyAnime"),
        ("ANIMEKISA", "AnimeKisa"),
        ("ANIMEVOSTORG", "Anime VostOrg"),
        ("JUTSU", "JutSu"),
        ("WAKANIM", "Wakanim"),
        ("CRUNCHYROLL", "Crunchyroll"),
        ("FUNIMATION", "Funimation")
    )
    phone_number = models.CharField("Телефонный номер", max_length=60, unique=True)
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name="Гендер")
    #age = models.IntegerField()
    occupation = models.CharField(choices=OCUP_CHOICE, max_length=80)

    # свои добавленные
    birth_year = models.CharField("Год рождения", max_length=10)
    github_nickname = models.CharField("Никнейм в Гитхабе", max_length=80, unique=True)
    continent = models.CharField(choices=CONTINENT_CHOICE, max_length=80)
    mobile_operator = models.CharField(choices=OPERATOR_CHOICE, max_length=20)
    fav_anime_site = models.CharField(choices=ANIME_SITE, max_length=50)
