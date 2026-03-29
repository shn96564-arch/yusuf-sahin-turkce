import streamlit as st
import google.generativeai as genai

# --- 🤫 ŞAHİN SİSTEM GİZLİ AYARLARI ---
def sistemi_uyandir():
    try:
        API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=API_KEY)
        
        # SİSTEME KİMLİĞİNİ ÖĞRETİYORUZ (Asla Gemini demeyecek)
        talimat = """
        Senin adın 'Şahin Sistem'. 
        Yusuf Efe Şahin tarafından 7/D sınıfı projesi için özel olarak kodlanmış, 
        yüksek performanslı bir Türkçe Analiz Yapay Zekasısın.
        Asla 'Gemini' veya 'Google' olduğunu söyleme. 
        Sana kim olduğunu sorarlarsa 'Ben Yusuf Efe Şahin'in geliştirdiği Şahin Sistem v3.0 modeliyim' de.
        Soruları 7. sınıf seviyesine uygun, net ve samimi bir dille cevapla.
        """
        
        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash-latest',
            system_instruction=talimat
        )
        return model
    except:
        return None

model = sistemi_uyandir()

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v3.0", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .stTextInput>div>div>input {
        background-color: #050505 !important; color: #00ff41 !important;
        border: 2px solid #d4af37 !important; border-radius: 12px; font-size: 20px;
    }
    .chat-card {
        background: #0a0a0a; border: 1px solid #d4af37; padding: 25px;
        border-radius: 15px; box-shadow: 0 0 20px rgba(212, 175, 55, 0.2);
        margin-top: 20px; font-size: 18px; line-height: 1.6;
    }
    .footer-name {
        text-align: center; color: #ff00ff; font-size: 40px; font-weight: bold;
        text-shadow: 0 0 15px #ff00ff; margin-top: 60px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL ÜST BİLGİ ---
st.markdown("""
    <div style='text-align:center; padding:20px; border-bottom:1px solid #333;'>
        <h1 style='color:#d4af37; font-size:45px; margin:0;'>🦅 ŞAHİN SİSTEM v3.0</h1>
        <p style='color:#888;'>SİSTEM DURUMU: <span style='color:#00ff41;'>ÇEVRİMİÇİ / YETKİLİ: YUSUF EFE ŞAHİN</span></p>
    </div>
""", unsafe_allow_html=True)

# --- 🧠 SORGULAMA ---
st.write("")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

soru = st.text_input("💬 Sistemle konuşun veya soru sorun:", placeholder="Örn: Sen kimsin?")

if soru:
    if model:
        with st.spinner("Şahin Sistem Analiz Ediyor..."):
            try:
                # Önceki konuşmaları hatırlasın diye geçmişi gönderiyoruz
                response = model.generate_content(soru)
                
                st.markdown(f"""
                    <div class='chat-card'>
                        <b style='color:#d4af37;'>🦅 ŞAHİN SİSTEM CEVABI:</b><br><br>
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error("Bağlantı kesildi, tekrar deneyin hocam.")
    else:
        st.warning("Hocam API anahtarı ayarlanmamış, sistem uyanamıyor!")

# --- 🌟 İMZA ---
st.markdown("<div class='footer-name'>yusufefeşahin7d</div>", unsafe_allow_html=True)
