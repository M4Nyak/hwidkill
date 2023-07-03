import subprocess

sahte = input('Sahte HWID\'inizi giriniz: ')

def hwid_degistir():
    # HWID değiştirmek için kullanicam komut ( 'wmic'  kullanacam)
    hwid_degistirme_komutu = f'wmic csproduct set uuid="{sahte}"'

    try:
        subprocess.run(hwid_degistirme_komutu, shell=True, check=True)
        print("HWID başarıyla değiştirildi.hiçbir engel beni zaptedemez")
    except subprocess.CalledProcessError:
        print("HWID değiştirilemedi. sen benim gibi gizli değilsin.")

hwid_degistir()
