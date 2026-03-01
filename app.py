import streamlit as st
import PyPDF2

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Türkçe Öğreticisi", layout="wide", page_icon="⚡")

# --- 🛠️ SİSTEMİ KÖKTEN TEMİZLEME (PANEL GİZLEME) ---
st.markdown("""
    <style>
    /* Sağ alttaki siyah paneli ve tüm menüleri zorla gizler */
    #MainMenu, footer, header, .stDeployButton, [data-testid="stStatusWidget"], [data-testid="stToolbar"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Gelişmiş Gizleme: Yönetim araçlarını hedef alır */
    button[title="View menu"], .st-emotion-cache-1wbqy5l, .st-emotion-cache-1ky6f6x {
        display: none !important;
    }

    /* Arka Plan ve Tasarım */
    .main { background-color: #050505 !important; color: #ffffff !important; }
    
    .premium-header {
        text-align: center; padding: 30px;
        background: linear-gradient(145deg, #111, #000);
        border: 2px solid #d4af37; border-radius: 20px;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.5);
        margin-bottom: 25px;
    }
    
    .stTextInput>div>div>input {
        border: 2px solid #00ff41 !important;
        background-color: #000 !important;
        color: #00ff41 !important;
        font-size: 22px !important;
        border-radius: 15px !important;
    }

    .result-card {
        border-left: 5px solid #00ff41;
        background-color: #111;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 10px 10px 30px rgba(0,0,0,1);
    }
    
    .signature {
        text-align: center; color: #ff00ff; font-size: 32px;
        font-weight: bold; text-shadow: 0 0 15px #ff00ff; margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🚀 HIZLI PDF OKUMA ---
@st.cache_data
def pdf_yukle():
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            tam_metin = ""
            for sayfa in pdf.pages:
                metin = sayfa.extract_text()
                if metin: tam_metin += metin + "\n "
            return tam_metin
    except: return "HATA: PDF Bulunamadı!"

notlar = pdf_yukle()

# --- ANA EKRAN ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #d4af37; font-weight: bold; letter-spacing: 3px;">ELITE EDITION</p>
        <h1 style="font-size: 45px; margin: 0; color: white;">TÜRKÇE ÖĞRETİCİSİ</h1>
        <p style="color: #888;">Geliştirici: <b>Yusuf Efe Şahin</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- ARAMA ---
c1, c2, c3 = st.columns([1, 4, 1])

with c2:
    soru = st.text_input("💎 ÖĞRENMEK İSTEDİĞİNİZ KONUYU GİRİN:", key="arama_kutusu")
    
    if soru:
        s_low = soru.lower()
        m_low = notlar.lower()
        
        if s_low in m_low:
            # Yarım kelime sorununu çözmek için kelimenin başlangıcını tam bul
            idx = m_low.find(s_low)
            # Metni direkt kelimenin başından başlat (Başta anlamsız harf kalmaz)
            gosterilecek = notlar[idx:idx+1200]
            
            st.markdown(f"""
                <div class="result-card">
                    <h2 style="color:#00ff41; margin-top:0;">⚡ Analiz Sonucu:</h2>
                    <p style="font-size:21px; line-height:1.8; color:#eee;">{gosterilecek}</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.error("❌ Notlar arasında bu konuya rastlanmadı.")

st.markdown('<div class="signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
