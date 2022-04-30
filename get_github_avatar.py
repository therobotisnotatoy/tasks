
import requests

ENDPOINT = "https://api.github.com/users/"

users_dict = {
    "https://github.com/Misha86/",
    "https://github.com/therobotisnotatoy",
    "https://github.com/Serhii-Voloshyn",
    "https://github.com/OleksiiDatsiuk",
    "https://github.com/shevchenkoira",
    "https://github.com/pazuzu-ua/",
    "https://github.com/morento101",
    "https://github.com/YaroslavBorysko",
    "https://github.com/shv833",
    }


for github_user_url in users_dict:
    user_login = github_user_url.removeprefix("https://github.com/")
    user_url = ENDPOINT + user_login

    try:
        source = dict(requests.get(user_url).json())
        print(f"[![@{source['login']}]({source['avatar_url']}&s=200)]({github_user_url})")
    except:
        print(f"[![@{user_login}](___&s=200)]({github_user_url})")
