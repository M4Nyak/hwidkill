import subprocess

sahte = input('Sahte HWID\'inizi giriniz: ')
sahte2= input('Sahte mac adresini giriniz: ')
def hwid_degistir():
    # HWID değiştirmek için kullanicam komut ( 'wmic'  kullanacam)
    hwid_degistirme_komutu = f'wmic csproduct set uuid="{sahte}"'
    mac_degistirme_komutu= f'wmic nicconfig where Description="Ethernet Bağlantısı" call setMACAddress="{sahte2}"


    try:
        subprocess.run(hwid_degistirme_komutu, shell=True, check=True)
        subprocess.run(mac_degistirme_komutu, shell=True, check=True)
        print("HWID başarıyla değiştirildi.hiçbir engel beni zaptedemez")
    except subprocess.CalledProcessError:
        print("HWID değiştirilemedi. sen benim gibi gizli değilsin.")

hwid_degistir()
