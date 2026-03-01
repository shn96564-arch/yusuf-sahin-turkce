import streamlit as st
import PyPDF2

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Premium AI", layout="wide", page_icon="💎")

# --- ELITE PREMIUM TASARIM (CSS) ---
st.markdown("""
    <style>
    /* Ana Arka Plan: Kömür Siyahı */
    .main { background-color: #0a0a0a; color: #e0e0e0; }
    
    /* Üst Başlık: Altın ve Beyaz Parlaması */
    .premium-header {
        text-align: center;
        padding: 40px;
        background: linear-gradient(145deg, #1a1a1a, #000000);
        border: 1px solid #d4af37; /* Altın Rengi Çerçeve */
        border-radius: 30px;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        margin-bottom: 40px;
    }
    
    .elite-title {
        font-family: 'Inter', sans-serif;
        font-size: 55px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #ffffff;
        text-shadow: 0 0 15px rgba(255,255,255,0.5);
        margin: 0;
    }

    /* Neon Yeşil Arama Kutusu */
    .stTextInput>div>div>input {
        border: 2px solid #00ff41 !important; /* Matrix Yeşili */
        background-color: #111 !important;
        color: #00ff41 !important;
        font-size: 20px;
        border-radius: 15px;
        height: 60px;
    }

    /* Premium Sonuç Kartı */
    .result-card {
        border-left: 5px solid #00ff41;
        background-color: #161616;
        padding: 25px;
        border-radius: 0 20px 20px 0;
        margin-top: 30px;
        box-shadow: 10px 10px 30px rgba(0,0,0,0.5);
    }

    /* Alt İmza: Neon Pembe/Mor */
    .signature {
        text-align: center;
        font-family: 'Courier New', monospace;
        color: #ff00ff;
        font-size: 28px;
        font-weight: bold;
        text-shadow: 0 0 10px #ff00ff;
        margin-top: 60px;
        letter-spacing: 3px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PDF ARAMA MOTORU ---
def premium_search(query):
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            text = "".join([p.extract_text() for p in pdf.pages if p.extract_text()])
            if query.lower() in text.lower():
                start = text.lower().find(query.lower())
                return text[start:start+1000]
            return "❌ Aranan veri 'Premium Notlar' arasında bulunamadı."
    except: return "⚠️ Veri tabanı bağlantısı kurulamadı (PDF Eksik)."

# --- SUNUM ANA EKRANI ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #d4af37; letter-spacing: 3px; margin-bottom: 10px;">PREMIUM EDITION</p>
        <h1 class="elite-title">TÜRKÇE YAPAY ZEKA</h1>
        <p style="color: #666; margin-top: 15px;">Geliştirici: <b>Yusuf Efe Şahin</b></p>
    </div>
    """, unsafe_allow_html=True)

# --- İNTERAKTİF BÖLÜM ---
c1, c2, c3 = st.columns([1, 4, 1])

with c2:
    search_query = st.text_input("💎 ANALİZ ETMEK İSTEDİĞİNİZ KONUYU GİRİNİZ:", placeholder="Örn: Cümlede Anlam")
    
    if search_query:
        with st.spinner("Premium Veriler İşleniyor..."):
            data = premium_search(search_query)
            st.markdown(f"""
                <div class="result-card">
                    <h2 style="color:#00ff41; margin-top:0;">📋 Analiz Sonucu:</h2>
                    <p style="line-height:1.6; font-size:18px; color:#ccc;">{data}</p>
                </div>
            """, unsafe_allow_html=True)

# --- ALT NEON İMZA ---
st.markdown('<div class="signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
