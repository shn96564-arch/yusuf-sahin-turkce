import streamlit as st
import PyPDF2
import re

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Türkçe Öğreticisi", layout="wide", page_icon="📚")

# --- PREMIUM TASARIM (PANEL AKTİF) ---
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
        border-left: 5px solid #d4af37; background-color: #111;
        padding: 25px; border-radius: 10px; margin-top: 15px;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.8);
    }
    .signature {
        text-align: center; color: #ff00ff; font-size: 28px;
        font-weight: bold; text-shadow: 0 0 10px #ff00ff; margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🔍 GELİŞMİŞ PDF OKUYUCU ---
@st.cache_data
def pdf_analiz_et():
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            metin = ""
            for sayfa in pdf.pages:
                sayfa_metni = sayfa.extract_text()
                if sayfa_metni:
                    metin += sayfa_metni + " "
            
            # Yazım hatalarını ve bozuk boşlukları temizle
            metin = re.sub(r'\s+', ' ', metin) # Çoklu boşlukları teke indir
            metin = metin.replace(" .", ".").replace(" ,", ",")
            return metin
    except:
        return "HATA: 'konu_anlatim.pdf' dosyası bulunamadı."

tum_icerik = pdf_analiz_et()

# --- ANA EKRAN ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #d4af37; font-weight: bold; letter-spacing: 2px;">ELITE EDUCATION PROJECT</p>
        <h1 style="font-size: 42px; margin: 0; color: white;">TÜRKÇE ÖĞRETİCİSİ</h1>
        <p style="color: #888;">Proje Geliştiricisi: <b>Yusuf Efe Şahin</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- İNTERAKTİF ARAMA ---
col1, col2, col3 = st.columns([1, 5, 1])

with col2:
    soru = st.text_input("📚 ÖĞRENMEK İSTEDİĞİNİZ KONUYU GİRİN:", placeholder="Örn: Zarflar, Fiiller...")
    
    if soru:
        soru_low = soru.lower().strip()
        icerik_low = tum_icerik.lower()
        
        if soru_low in icerik_low:
            # Kelimenin geçtiği yeri bul
            bulunan_index = icerik_low.find(soru_low)
            
            # 🎯 NOKTA BULUCU: Yarım kelimeyi önlemek için cümlenin başına git
            baslangic = bulunan_index
            while baslangic > 0 and tum_icerik[baslangic-1] not in ".!?":
                baslangic -= 1
            
            # Sonucu al ve temizle
            ham_sonuc = tum_icerik[baslangic:baslangic+1200].strip()
            
            st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#00ff41; margin-top:0;">⚡ Konu Anlatımı:</h3>
                    <p style="font-size:19px; line-height:1.7; color:#eee;">{ham_sonuc}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Aradığınız konu ders notlarında mevcut değil.")

# --- İMZA ---
st.markdown('<div class="signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
