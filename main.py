from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

# Tasarım: Oyuncu temalı (Koyu mod ve Neon Mavi)
HTML_SAYFASI = '''
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Delta Link Bypasser</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; text-align: center; padding: 30px; background: #0b0b0b; color: #00d4ff; }
        .container { max-width: 500px; margin: auto; background: #151515; padding: 25px; border-radius: 20px; border: 2px solid #00d4ff; box-shadow: 0 0 15px #00d4ff; }
        input { width: 90%; padding: 15px; margin: 15px 0; border-radius: 10px; border: 1px solid #00d4ff; background: #222; color: white; outline: none; }
        button { width: 95%; padding: 15px; background: #00d4ff; border: none; border-radius: 10px; color: #000; font-weight: bold; cursor: pointer; font-size: 16px; }
        button:hover { background: #0088aa; transform: scale(1.02); }
        .sonuc-kutusu { margin-top: 25px; padding: 20px; background: #202020; border-radius: 10px; border-left: 10px solid #00ff00; word-break: break-all; color: #fff; }
        .footer { margin-top: 20px; font-size: 12px; color: #555; }
    </style>
</head>
<body>
    <div class="container">
        <h1>DELTA BYPASS</h1>
        <p>Reklamlı linki aşağıya yapıştırın:</p>
        <form method="POST">
            <input type="text" name="url" placeholder="https://gateway.platoboost.com/..." required>
            <button type="submit">SİSTEMİ GEÇ (BYPASS)</button>
        </form>

        {% if sonuc %}
        <div class="sonuc-kutusu">
            <strong>Anahtar / Link:</strong><br>
            <p style="color: #00ff00; font-size: 18px;">{{ sonuc }}</p>
        </div>
        {% endif %}
    </div>
    <div class="footer">Made with Python & Flask</div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    sonuc = None
    if request.method == 'POST':
        target_url = request.form.get('url')
        
        # Ücretsiz ve popüler bir Bypass API'sini kullanıyoruz
        # Not: API adresleri zaman zaman değişebilir.
        api_url = f"https://api.bypass.city/bypass?url={target_url}"
        
        try:
            # API'ye istek gönderiyoruz
            response = requests.get(api_url, timeout=15)
            data = response.json()
            
            # API'den gelen cevabı kontrol ediyoruz
            if data.get('status') == "success" or "result" in data:
                sonuc = data.get('result') # Gerçek linki veya key'i alıyoruz
            else:
                sonuc = "Bypass başarısız. Link geçersiz olabilir veya API yoğun."
                
        except Exception as e:
            sonuc = "Bağlantı hatası: API şu an yanıt vermiyor."
            
    return render_template_string(HTML_SAYFASI, sonuc=sonuc)

if __name__ == "__main__":
    # Render veya PythonAnywhere gibi yerlerde çalışması için 0.0.0.0 önemli
    app.run(host='0.0.0.0', port=5000)
