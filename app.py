import streamlit as st
import google.generativeai as genai

# --- 🎨 TASARIM ---
st.set_page_config(page_title="Yusuf Efe | Analizör", layout="wide")
st.markdown("<style>.main { background-color: #000; color: #fff; }</style>", unsafe_allow_html=True)

# --- 🤫 BAĞLANTIYI ZORLA ---
try:
    # Secrets'tan anahtarı alıyoruz
    key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=key)
    # En hızlı ve güncel model: gemini-1.5-flash
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Sistem anahtarı okuyamadı! Hata: {e}")
    st.stop()

st.markdown("<h1 style='text-align:center; color:#d4af37;'>7. SINIF TÜRKÇE SİSTEMİ</h1>", unsafe_allow_html=True)

# --- 🧠 SORGU ---
soru = st.text_input("💬 Cümle yazın:", placeholder="Örn: 'Hızlıca geldi' cümlesini incele.")

if soru:
    try:
        # Gemini'ye soruyu gönderiyoruz
        response = model.generate_content(f"7. sınıf Türkçe öğretmeni gibi kısa cevapla: {soru}")
        st.success("✅ Analiz Tamamlandı!")
        st.write(response.text)
    except Exception as e:
        # BURASI ÖNEMLİ: Hatanın gerçek sebebini burası söyleyecek
        st.warning(f"Google Motorundan Gelen Mesaj: {e}")

st.markdown("<div style='text-align:center; color:#ff00ff; margin-top:50px;'>yusufefeşahin7d</div>", unsafe_allow_html=True)
