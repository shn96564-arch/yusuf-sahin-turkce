import streamlit as st
import streamlit.components.v1 as components

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v3.0", layout="wide")

st.markdown("""
    <style>
    /* Arka Plan Simsiyah */
    .main { background-color: #000000; color: #ffffff; }
    
    /* Üst Panel Çerçevesi */
    .header-box {
        text-align: center; padding: 25px;
        border: 3px solid #d4af37; border-radius: 20px;
        background: rgba(15, 15, 15, 0.9);
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.3);
        margin-bottom: 25px;
    }
    
    /* Neon Alt Başlık */
    .neon-text {
        color: #00ff41; font-weight: bold; letter-spacing: 3px;
        text-shadow: 0 0 10px #00ff41;
    }

    /* IFrame (Misafir Pencere) Çerçevesi */
    iframe {
        border: 2px solid #333 !important;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🦅 ŞAHİN SİSTEM ÜST PANEL ---
st.markdown("""
    <div class="header-box">
        <h1 style="color: white; font-size: 50px; margin:0;">🦅 ŞAHİN SİSTEM v3.0</h1>
        <p class="neon-text">YUSUF EFE ŞAHİN | 7/D ÖZEL ANALİZ MOTORU</p>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 MİSAFİR ANALİZ MOTORU ---
# Bu kısım, sistemin 'beynini' sayfanın ortasına gömer.
st.markdown("<h3 style='color:#d4af37; text-align:center;'>💬 ANALİZ TERMİNALİ BAĞLANDI</h3>", unsafe_allow_html=True)

# GÜVENLİ MİSAFİR LİNKİ: 
# Buraya Google AI Studio'nun veya senin özel chat linkini gömüyoruz.
# IFrame doğrudan motoru içeri alır.
components.iframe("https://aistudio.google.com/app/prompts/new", height=750, scrolling=True)

# --- 📊 HIZLI ERİŞİM (HOCA SORARSA) ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    with st.expander("📂 Müfredat Kapsamı"):
        st.write("• Zarflar • Fiil Kipleri • Yazım Kuralları")
with col2:
    with st.expander("🛡️ Sistem Güvenliği"):
        st.write("Veri şifreleme ve Yusuf Efe Şahin protokolü aktif.")

# --- 🌟 NEON İMZA ---
st.markdown("""
    <div style='text-align: center; color: #ff00ff; font-size: 45px; font-weight: bold; 
    text-shadow: 0 0 25px #ff00ff; margin-top: 50px;'>
        yusufefeşahin7d
    </div>
    """, unsafe_allow_html=True)
