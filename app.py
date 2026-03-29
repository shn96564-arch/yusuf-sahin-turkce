import streamlit as st
import google.generativeai as genai

# --- 🤫 GÜVENLİ BAĞLANTI ---
def sitemi_baslat():
    try:
        # Secrets'tan çekiyoruz
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            return genai.GenerativeModel('gemini-1.5-flash')
        else:
            st.error("Secrets bulunamadı!")
            return None
    except Exception as e:
        st.error(f"Bağlantı Hatası: {e}")
        return None

model = sitemi_baslat()

# --- 🎨 SİBER TASARIM (SİYAH & NEON) ---
st.set_page_config(page_title="Yusuf Efe | Analizör", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stTextInput>div>div>input {
        background-color: #0a0a0a !important; color: #00ff41 !important;
        border: 2px solid #d4af37 !important; border-radius: 10px; font-size: 20px;
    }
    .result-box {
        background: #111; border-left: 5px solid #00ff41;
        padding: 20px; border-radius: 10px; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#d4af37;'>7. SINIF TÜRKÇE ANALİZÖRÜ</h1>", unsafe_allow_html=True)

# --- 🧠 SORGU ---
soru = st.text_input("💬 Cümleyi veya konuyu buraya yazın:", placeholder="Örn: 'Sessizce gitti' cümlesinde zarf nedir?")

if soru and model:
    with st.spinner("Yusuf Efe Motoru Analiz Ediyor..."):
        try:
            prompt = f"Sen bir Türkçe öğretmenisin. 7. sınıf seviyesinde şu soruyu çok kısa ve maddelerle açıkla: {soru}"
            response = model.generate_content(prompt)
            st.markdown(f"<div class='result-box'><b>⚡ SONUÇ:</b><br><br>{response.text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.warning("Motor şu an meşgul veya anahtar hatası var. Lütfen 10 saniye sonra tekrar dene.")

st.markdown("<div style='text-align:center; color:#ff00ff; font-weight:bold; margin-top:100px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
