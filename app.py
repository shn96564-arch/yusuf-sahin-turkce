import streamlit as st
import PyPDF2

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Türkçe Öğreticisi", layout="wide", page_icon="⚡")

# --- PREMIUM TASARIM + PANEL GİZLEME KODU ---
st.markdown("""
    <style>
    /* Sağ alttaki 'Manage app' panelini gizler */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    stDeployButton {display:none;}

    .main { background-color: #050505; color: #ffffff; }
    .premium-header {
        text-align: center; padding: 25px;
        background: linear-gradient(145deg, #111, #000);
        border: 2px solid #d4af37; border-radius: 20px;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.5);
        margin-bottom: 25px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #00ff41 !important;
        background-color: #000 !important; color: #00ff41 !important;
        font-size: 22px; border-radius: 15px; text-align: center;
    }
    .result-card {
        border-left: 5px solid #00ff41; background-color: #111;
        padding: 20px; border-radius: 10px; margin-top: 15px;
        box-shadow: 10px 10px 30px rgba(0,0,0,1);
    }
    .signature {
        text-align: center; color: #ff00ff; font-size: 32px;
        font-weight: bold; text-shadow: 0 0 15px #ff00ff; margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PDF HAFIZAYA ALMA ---
@st.cache_data
def pdf_hafizaya_al():
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            tam_metin = ""
            for sayfa in pdf.pages:
                metin = sayfa.extract_text()
                if metin: tam_metin += metin + "\n "
            return tam_metin
    except: return "HATA: PDF Bulunamadı!"

tum_notlar = pdf_hafizaya_al()

# --- ANA EKRAN ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #d4af37; font-weight: bold; letter-spacing: 3px;">ULTRA SPEED EDITION</p>
        <h1 style="font-size: 45px; margin: 0;">TÜRKÇE ÖĞRETİCİSİ</h1>
        <p style="color: #666;">Geliştirici: <b>Yusuf Efe Şahin</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- ARAMA BÖLÜMÜ ---
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    soru = st.text_input("💎 BİR KONU YAZIN:", placeholder="Örn: Zarflar")
    
    if soru:
        soru_low = soru.lower()
        metin_low = tum_notlar.lower()
        
        if soru_low in metin_low:
            index = metin_low.find(soru_low)
            # Metni tam buradan başlatıyoruz (noktaları sildik)
            end = min(len(tum_notlar), index + 1000)
            sonuc = tum_notlar[index:end]
            
            st.markdown(f"""
                <div class="result-card">
                    <h3 style="color:#00ff41; margin-top:0;">⚡ Analiz Tamamlandı:</h3>
                    <p style="font-size:19px; line-height:1.6; color:#ccc;">{sonuc}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Notlar arasında bu konuya rastlanmadı.")

st.markdown('<div class="signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
