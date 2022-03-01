from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from . import models

class RegistrationForm(UserCreationForm):
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

    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    #age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    occupation = forms.ChoiceField(choices=OCUP_CHOICE, required=True)
    birth_year = forms.CharField(required=True)
    github_nickname = forms.CharField(required=True)
    continent = forms.ChoiceField(choices=CONTINENT_CHOICE, required=True)
    mobile_operator = forms.ChoiceField(choices=OPERATOR_CHOICE, required=True)
    fav_anime_site = forms.ChoiceField(choices=ANIME_SITE, required=True)

    class Meta:
        model = models.CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
            "occupation",
            "phone_number",
            "birth_year",
            "github_nickname",
            "continent",
            "mobile_operator",
            "fav_anime_site"
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Номер Телефона",
                "id": "phone_number"
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Почта",
                "id": "email"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Пароль",
                "id": "password"
            }
        )
    )