import streamlit as st
import google.generativeai as genai

# --- 🎨 SİBER TASARIM ---
st.set_page_config(page_title="Yusuf Efe | Analizör", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #000; color: #fff; }
    .stTextInput>div>div>input {
        background-color: #050505 !important; color: #00ff41 !important;
        border: 2px solid #d4af37 !important; border-radius: 12px;
    }
    .result-box {
        background: #111; border: 1px solid #00ff41;
        padding: 20px; border-radius: 10px; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🤫 BAĞLANTIYI KUR ---
try:
    # Secrets'tan anahtarı alıyoruz
    key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=key)
    
    # DİKKAT: En stabil model ismini 'gemini-1.5-flash-latest' olarak güncelledik
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"Sistem anahtarı okuyamadı! Hata: {e}")
    st.stop()

st.markdown("<h1 style='text-align:center; color:#d4af37;'>7. SINIF TÜRKÇE ANALİZÖRÜ</h1>", unsafe_allow_html=True)

# --- 🧠 SORGU ---
soru = st.text_input("💬 Cümle veya konu yazın:", placeholder="Örn: 'Hızlıca geldi' cümlesini incele.")

if soru:
    with st.spinner("Yusuf Efe Motoru Cevaplıyor..."):
        try:
            # Gemini'ye soruyu gönderiyoruz
            response = model.generate_content(f"Sen 7. sınıf Türkçe öğretmenisin. Şu soruyu kısa ve maddelerle cevapla: {soru}")
            
            st.markdown(f"""
                <div class='result-box'>
                    <h3 style='color:#00ff41; margin-top:0;'>⚡ ANALİZ:</h3>
                    {response.text.replace("\n", "<br>")}
                </div>
            """, unsafe_allow_html=True)
            
        except Exception as e:
            # Eğer yine model hatası verirse, 'gemini-pro' modeline otomatik döner
            try:
                model_yedek = genai.GenerativeModel('gemini-pro')
                response = model_yedek.generate_content(f"7. sınıf Türkçe: {soru}")
                st.write(response.text)
            except:
                st.warning(f"Google Motoru Hatası: {e}")

st.markdown("<div style='text-align:center; color:#ff00ff; margin-top:50px; font-weight:bold;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
