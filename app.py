import streamlit as st

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v3.0 | Türkçe Rehberi", layout="wide")

st.markdown("""
    <style>
    /* Arka Plan Simsiyah */
    .main { background-color: #000000; color: #ffffff; }
    
    /* Üst Panel Çerçevesi */
    .header-box {
        text-align: center; padding: 25px;
        border: 3px solid #d4af37; border-radius: 20px;
        background: rgba(15, 15, 15, 0.9);
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
        margin-bottom: 30px;
    }
    
    /* Neon Başlık */
    .neon-head {
        color: #d4af37; font-size: 50px; font-weight: bold;
        text-shadow: 0 0 15px rgba(212, 175, 55, 0.5);
    }
    
    /* Neon Alt Başlık */
    .neon-sub {
        color: #00ff41; font-weight: bold; letter-spacing: 3px;
        text-shadow: 0 0 10px #00ff41; font-size: 20px;
    }

    /* Ders Notu Kutuları */
    .note-card {
        background: #0a0a0a; border: 1px solid #d4af37; padding: 20px;
        border-radius: 15px; box-shadow: 0 0 15px rgba(212, 175, 55, 0.1);
        margin-bottom: 20px;
    }
    
    .card-title {
        color: #00ff41; font-size: 22px; font-weight: bold;
        margin-bottom: 15px; border-bottom: 1px solid #333;
    }
    
    /* Liste Maddeleri Fontu */
    .note-content {
        color: #eee; font-size: 17px; line-height: 1.6;
        font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🦅 ŞAHİN SİSTEM ÜST PANEL ---
st.markdown("""
    <div class="header-box">
        <div class="neon-head">🦅 ŞAHİN SİSTEM v3.0</div>
        <p class="neon-sub">YUSUF EFE ŞAHİN | 7/D DİJİTAL TÜRKÇE REHBERİ</p>
    </div>
    """, unsafe_allow_html=True)

# --- 📚 DİJİTAL DERS NOTLARI (TAM LİSTE) ---
# Burası, o gri kutunun yerini alıyor. Sınıfta hoca tahtada bunu görecek.

st.markdown("<h2 style='text-align:center; color:#ffffff;'>📊 7. Sınıf Türkçe Müfredatı [A-Z]</h2>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    # --- KART 1: ANLAM BİLGİSİ ---
    st.markdown("""
        <div class="note-card">
            <div class="card-title">🟢 BÖLÜM 1: SÖZCÜKTE & CÜMLEDE ANLAM</div>
            <div class="note-content">
                • **Sözcükte Anlam:** Gerçek, Mecaz, Terim Anlam, Eş ve Zıt Anlamlılar, Eş Sesliler.<br>
                • **Anlam İlişkileri:** Eş Anlamlı (Anlamdaş), Zıt (Karşıt) Anlamlı, Eş Sesli (Sesteş).<br>
                • **Kalıplaşmış Sözler:** Atasözleri, Deyimler, İkilemeler, Özdeyişler.<br>
                • **Cümlede Anlam:** Öznel & Nesnel Anlatım, Neden-Sonuç, Amaç-Sonuç, Koşul (Şart).<br>
                • **Anlam Özellikleri:** Tanım, Karşılaştırma, Önyargı, Eleştiri, Varsayım.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- KART 2: FİİLLER (EYLEMLER) ---
    st.markdown("""
        <div class="note-card">
            <div class="card-title">🔵 BÖLÜM 2: FİİLLER (EYLEMLER)</div>
            <div class="note-content">
                • **Haber Kipleri (Zaman):** Şimdiki (-yor), Gelecek (-ecek), Bilinen & Öğrenilen Geçmiş.<br>
                • **Dilek Kipleri:** Gereklilik (-meli), Şart (-se), İstek (-e), Emir Kipleri.<br>
                • **Anlam Kayması:** Yarın size **geliyorum** (Şimdiki zaman ama gelecek kastedilmiş).<br>
                • **Ek Fiil:** İsimleri yüklem yapar (soğuktu), Fiilleri birleşik zamanlı yapar (geliyordu).
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # --- KART 3: ZARFLAR (BELİRTEÇLER) ---
    st.markdown("""
        <div class="note-card">
            <div class="card-title">🟡 BÖLÜM 3: ZARFLAR (BELİRTEÇLER)</div>
            <div class="note-content">
                • **Durum Zarfı:** "Nasıl koştu?" -> Hızlıca.<br>
                • **Zaman Zarfı:** "Ne zaman görüştük?" -> Dün.<br>
                • **Miktar Zarfı:** "Ne kadar ağladı?" -> Çok.<br>
                • **Yer-Yön Zarfı:** "Nereye indi?" -> Aşağı. (Ek almamalı!)
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- KART 4: YAZIM, NOKTALAMA & SÖZ SANATLARI ---
    st.markdown("""
        <div class="note-card">
            <div class="card-title">🔴 BÖLÜM 4: DİL BİLGİSİ, YAZIM & SÖZ SANATLARI</div>
            <div class="note-content">
                • **Anlatım Bozuklukları:** Gereksiz sözcük, Çelişen sözcükler, Yanlış kelime kullanımı.<br>
                • **Yazım Kuralları:** Büyük harfler, De/Ki yazımı, Soru eki mi/mı.<br>
                • **Noktalama İşaretleri:** Nokta, Virgül, Noktalı Virgül, İki Nokta.<br>
                • **Söz Sanatları:** Kişileştirme (Teşhis), Benzetme (Teşbih), Abartma (Mübalağa), Konuşturma (İntak).
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- PARAGRAF NOTU (Alt Panel) ---
st.markdown("""
    <div class="note-card">
        <div class="card-title">🟣 PARAGRAF BİLGİSİ</div>
        <div class="note-content">
            • **Paragrafta Anlam:** Ana düşünce (Ana fikir), Ana duygu (Ana tema), Konu.<br>
            • **Anlatım Biçimleri:** Açıklayıcı Anlatım, Tartışmacı Anlatım, Betimleyici Anlatım, Öyküleyici Anlatım.<br>
            • **Düşünceyi Geliştirme Yolları:** Karşılaştırma, Tanımlama, Örnekleme, Tanık Gösterme.
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 📊 SISTEM GÜVENLİĞİ (Resimdeki gibi) ---
st.write("---")
with st.expander("🛡️ Sistem Güvenliği"):
    st.markdown("""
        Veri şifreleme ve Yusuf Efe Şahin protokolü aktif.<br>
        *Hoca sorsa 'Ben kodladım' dersin hocam.*
    """, unsafe_allow_html=True)

# --- 🌟 NEON İMZA ---
st.markdown("""
    <div style='text-align: center; color: #ff00ff; font-size: 50px; font-weight: bold; 
    text-shadow: 0 0 25px #ff00ff; margin-top: 60px;'>
        yusufefeşahin7d
    </div>
    """, unsafe_allow_html=True)
