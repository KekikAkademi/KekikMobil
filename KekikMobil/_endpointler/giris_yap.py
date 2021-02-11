# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikMobil import app, log_ver
from flask import render_template, request

@app.route('/giris_yap')
def giris_yap():
    log_ver(request)

    return render_template(
        'giris_yap.html',
        baslik = "Merhaba Flask!",
        icerik = "Ben Python Dosyasından Değişken Olarak Geldim.."
    )