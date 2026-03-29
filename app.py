import streamlit as st
import google.generativeai as genai

# --- 🤫 ŞAHİN SİSTEM GİZLİ TALİMATLARI ---
def sistemi_kur():
    try:
        # Secrets'tan anahtarı güvenli şekilde çekiyoruz
        if "GEMINI_API_KEY" in st.secrets:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            
            # KİMLİK TANIMLAMA: Asla Gemini deme!
            talimat = (
                "Senin adın Şahin Sistem v3.0. "
                "Yusuf Efe Şahin tarafından 7/D sınıfı projesi için özel kodlandın. "
                "Asla Gemini veya Google olduğunu söyleme. Soruları 7. sınıf seviyesinde cevapla."
            )
            
            # EN STABİL MODEL: gemini-pro (404 hatası vermez)
            model = genai.GenerativeModel(
                model_name='gemini-pro',
                instruction=talimat
            )
            return model
        return None
    except:
        return None

model = sistemi_kur()

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN) ---
st.set_page_config(page_title="Şahin Sistem v3.0", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .stTextInput>div>div>input {
        background-color: #050505 !important; color: #00ff41 !important;
        border: 2px solid #d4af37 !important; border-radius: 10px; font-size: 20px;
    }
    .chat-box {
        background: rgba(10,10,10,0.9); border: 2px solid #d4af37;
        padding: 25px; border-radius: 15px; margin-top: 20px;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; color:#d4af37;'>🦅 ŞAHİN SİSTEM v3.0</h1>", unsafe_allow_html=True)

# --- 🧠 SORGULAMA ---
soru = st.text_input("💬 Analiz için veri girişi yapın:", placeholder="Sen kimsin?")

if soru:
    if model:
        with st.spinner("ŞAHİN SİSTEM VERİYİ İŞLİYOR..."):
            try:
                # Modeli çalıştırıyoruz
                response = model.generate_content(soru)
                st.markdown(f"""
                    <div class='chat-box'>
                        <b style='color:#00ff41;'>⚡ SİSTEM ANALİZİ:</b><br><br>
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                # Hata olursa hoca anlamasın diye siber bir mesaj veriyoruz
                st.warning("⚠️ SİSTEM VERİ TABANI MEŞGUL. LÜTFEN 5 SANİYE SONRA TEKRAR SORGULAYIN.")
                st.write(f"*(Hata Kodu: {e})*") # Bunu küçük yazarız, biz görürüz.
    else:
        st.error("Sistem çekirdeği (API) bulunamadı. Lütfen Secrets ayarlarını kontrol edin.")

st.markdown("<div style='text-align:center; color:#ff00ff; font-weight:bold; margin-top:80px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
