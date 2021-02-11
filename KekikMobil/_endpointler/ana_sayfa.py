# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikMobil import app, log_ver
from flask import render_template, request, jsonify

@app.route('/')
def ana_sayfa():
    log_ver(request)

    return render_template('ana_sayfa.html')

@app.route('/veri_sayfasi', methods=['GET', 'POST'])
def veri_sayfasi():
    log_ver(request)
    return render_template('veri_sayfasi.html')

@app.route('/veri_takip', methods=['GET', 'POST'])
def veri():
    # log_ver(request)
    import random
    return jsonify({'veri': random.randint(50, 50000)})