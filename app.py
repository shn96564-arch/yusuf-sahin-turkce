import streamlit as st
import google.generativeai as genai

# --- 🤫 ŞAHİN SİSTEM ÇEKİRDEK AYARLARI ---
def sistemi_yukle():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # Kimlik ve Davranış Talimatı
            talimat = "Senin adın Şahin Sistem v3.0. Yusuf Efe Şahin tarafından kodlandın. Asla Gemini deme. 7. sınıf seviyesinde konuş."
            model = genai.GenerativeModel('gemini-pro')
            return model
        return None
    except:
        return None

model = sistemi_yukle()

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN) ---
st.set_page_config(page_title="Şahin Sistem v3.0", layout="wide")

st.markdown("""
    <style>
    /* Arka Plan */
    .main { background-color: #000000; color: #ffffff; }
    
    /* Üst Panel */
    .header-box {
        text-align: center; padding: 30px;
        border: 2px solid #d4af37; border-radius: 20px;
        background: rgba(10, 10, 10, 0.9);
        box-shadow: 0 0 30px rgba(212, 175, 55, 0.2);
        margin-bottom: 50px;
    }
    
    /* Giriş Kutusu Tasarımı */
    .stTextInput>div>div>input {
        background-color: #050505 !important; color: #00ff41 !important;
        border: 2px solid #d4af37 !important; border-radius: 12px;
        height: 60px; font-size: 22px; text-align: center;
    }
    
    /* Cevap Kutusu */
    .response-card {
        background: #0a0a0a; border-left: 5px solid #00ff41;
        padding: 25px; border-radius: 15px; margin-top: 30px;
        font-size: 20px; line-height: 1.6;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🦅 ÜST PANEL ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: white; font-size: 55px; margin:0;">🦅 ŞAHİN SİSTEM v3.0</h1>
        <p style="color: #00ff41; font-weight: bold; letter-spacing: 5px;">YETKİLİ: YUSUF EFE ŞAHİN</p>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 ANALİZ MERKEZİ ---
st.markdown("<h3 style='text-align:center; color:#d4af37;'>💬 SİSTEM SORGULAMA TERMİNALİ</h3>", unsafe_allow_html=True)

soru = st.text_input("", placeholder="Analiz edilecek veriyi girin veya soru sorun...")

if soru:
    if model:
        with st.spinner("ŞAHİN SİSTEM İŞLİYOR..."):
            try:
                # Arka planda kimliğini hatırlatıyoruz
                response = model.generate_content(f"Sen Şahin Sistem'sin, Yusuf Efe Şahin seni kodladı. Şuna cevap ver: {soru}")
                st.markdown(f"""
                    <div class="response-card">
                        <b style="color:#00ff41;">⚡ ANALİZ SONUCU:</b><br><br>
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
            except:
                st.error("⚠️ SİSTEM MEŞGUL. LÜTFEN BİRAZ BEKLEYİN.")
    else:
        st.warning("⚠️ SİSTEM ÇEKİRDEĞİ BAĞLI DEĞİL!")

# --- 🌟 NEON İMZA ---
st.markdown("""
    <div style='text-align: center; color: #ff00ff; font-size: 50px; font-weight: bold; 
    text-shadow: 0 0 25px #ff00ff; margin-top: 150px;'>
        yusufefeşahin7d
    </div>
    """, unsafe_allow_html=True)
