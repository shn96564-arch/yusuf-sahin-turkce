import streamlit as st
import PyPDF2
import re

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Türkçe Öğreticisi", layout="wide", page_icon="📚")

# --- ELITE TASARIM (PANEL AKTİF) ---
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    .premium-header {
        text-align: center; padding: 30px;
        background: linear-gradient(145deg, #111, #000);
        border: 2px solid #d4af37; border-radius: 20px;
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.4);
        margin-bottom: 25px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #00ff41 !important;
        background-color: #000 !important; color: #00ff41 !important;
        font-size: 20px !important; border-radius: 12px;
    }
    .result-card {
        border-left: 5px solid #00ff41; background-color: #111;
        padding: 25px; border-radius: 15px; margin-top: 15px;
        box-shadow: 10px 10px 30px rgba(0,0,0,1);
    }
    .signature {
        text-align: center; color: #ff00ff; font-size: 30px;
        font-weight: bold; text-shadow: 0 0 15px #ff00ff; margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🔍 HATASIZ METİN TEMİZLEME MOTORU ---
@st.cache_data
def pdf_temiz_oku():
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            metin = ""
            for sayfa in pdf.pages:
                sayfa_metni = sayfa.extract_text()
                if sayfa_metni:
                    # PDF hatalarını (kelime arasına giren tek tük harfleri) temizler
                    sayfa_metni = re.sub(r'(?<=[a-z])\s?d\s?(?=[a-z])', '', sayfa_metni) 
                    metin += sayfa_metni + " "
            
            # Gereksiz boşlukları ve satır sonu bozukluklarını düzelt
            metin = re.sub(r'\s+', ' ', metin)
            return metin
    except:
        return "HATA: PDF dosyası bulunamadı."

tum_icerik = pdf_temiz_oku()

# --- ANA EKRAN ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #d4af37; font-weight: bold; letter-spacing: 2px;">ELITE PREMIUM EDITION</p>
        <h1 style="font-size: 45px; margin: 0; color: white;">TÜRKÇE ÖĞRETİCİSİ</h1>
        <p style="color: #888;">Geliştirici: <b>Yusuf Efe Şahin</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- ARAMA ALANI ---
c1, c2, c3 = st.columns([1, 4, 1])

with c2:
    soru = st.text_input("📚 KONU ARA (Örn: Zarflar):", placeholder="Buraya yazın...")
    
    if soru:
        soru_low = soru.lower().strip()
        icerik_low = tum_icerik.lower()
        
        if soru_low in icerik_low:
            idx = icerik_low.find(soru_low)
            
            # 🎯 CÜMLE BAŞI BULUCU: "ÖN" gibi yarım başlangıçları engeller
            bas = idx
            while bas > 0 and tum_icerik[bas-1] not in ".!?":
                bas -= 1
            
            sonuc = tum_icerik[bas:bas+1200].strip()
            
            # Başlangıçtaki anlamsız karakterleri (varsa) temizle
            sonuc = re.sub(r'^[^A-ZÇĞİÖŞÜa-zçğıöşü]+', '', sonuc)
            
            st.markdown(f"""
                <div class="result-card">
                    <h2 style="color:#00ff41; margin-top:0;">⚡ Analiz Sonucu:</h2>
                    <p style="font-size:20px; line-height:1.8; color:#eee;">{sonuc}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Aradığınız konu notlar arasında bulunamadı.")

st.markdown('<div class="signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
