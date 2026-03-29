import streamlit as st
import google.generativeai as genai

# --- 🤫 GÜVENLİ MOTOR BAĞLANTISI (Secrets'tan çekiyor) ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-pro')
except:
    st.error("⚠️ API Anahtarı 'Secrets' kısmına eklenmemiş hocam!")

# --- 🎨 SİBER MİNİMALİST TASARIM ---
st.set_page_config(page_title="Yusuf Efe | Zeka Paneli", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    .stTextInput>div>div>input {
        background-color: #050505 !important; 
        color: #00ff41 !important;
        border: 2px solid #d4af37 !important; 
        border-radius: 12px; font-size: 22px; padding: 15px;
    }
    .ai-response {
        background: rgba(15, 15, 15, 0.9);
        border: 2px solid #00ff41; padding: 30px; border-radius: 20px;
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.2); margin-top: 30px;
        font-size: 22px; line-height: 1.6; color: #eee;
    }
    .footer-name {
        text-align: center; color: #ff00ff; font-size: 40px;
        font-weight: bold; text-shadow: 0 0 20px #ff00ff; margin-top: 80px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL BAŞLIĞI ---
st.markdown("""
    <div style='text-align:center; padding:25px; border-bottom:1px solid #333;'>
        <h1 style='color:#d4af37; font-size:50px; margin:0;'>7. SINIF TÜRKÇE ANALİZÖRÜ</h1>
        <p style='color:#888; letter-spacing:4px;'>SİSTEM DURUMU: <span style='color:#00ff41;'>GÜVENLİ & AKTİF</span></p>
    </div>
""", unsafe_allow_html=True)

# --- 🧠 ZEKAYI KULLANMA ALANI ---
st.write("")
soru = st.text_input("💬 Analiz edilecek metni veya konuyu buraya yazın:", placeholder="Örn: 'Hızlıca içeri girdi' cümlesindeki zarfı bul.")

if soru:
    with st.spinner("Yusuf Efe Motoru Analiz Ediyor..."):
        try:
            gizli_talimat = f"Sen bir Türkçe öğretmenisin. 7. sınıf öğrencisine anlatır gibi şu soruyu kısa, maddeler halinde ve net cevapla: {soru}"
            response = model.generate_content(gizli_talimat)
            st.markdown(f"""
                <div class='ai-response'>
                    <h3 style='color:#d4af37; margin-top:0;'>⚡ SİSTEM ANALİZİ:</h3>
                    {response.text.replace("\n", "<br>")}
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error("⚠️ Bir hata oluştu. Lütfen bağlantıyı kontrol edin.")

# --- 🌟 NEON İMZASI ---
st.markdown("<div class='footer-name'>yusufefeşahin7d</div>", unsafe_allow_html=True)
