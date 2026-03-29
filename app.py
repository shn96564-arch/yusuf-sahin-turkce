import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Akıllı Tahta", layout="wide")

# --- 🎨 ARKA TEMA VE NEON CSS (Burada temayı hallediyoruz) ---
st.markdown("""
    <style>
    /* Arka Planı Simsiyah ve Matrix Havasında Yapıyoruz */
    .main { 
        background-color: #000000; 
        background-image: radial-gradient(#111 1px, transparent 1px);
        background-size: 20px 20px;
    }
    
    /* Üst Panel: Altın Sarısı Neon */
    .smart-header {
        text-align: center; padding: 30px;
        background: rgba(20, 20, 20, 0.9);
        border: 3px solid #d4af37; border-radius: 25px;
        box-shadow: 0 0 40px rgba(212, 175, 55, 0.4);
        margin-bottom: 40px;
    }

    /* Ders Notu Kartları: Neon Yeşil */
    .note-card {
        background: rgba(0, 0, 0, 0.8);
        border-left: 10px solid #00ff41;
        padding: 25px; border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 5px 5px 20px rgba(0, 255, 65, 0.1);
        transition: 0.3s;
    }
    .note-card:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.3);
    }

    /* İmza Alanı */
    .neon-signature {
        text-align: center; color: #ff00ff; 
        font-size: 45px; font-weight: bold;
        text-shadow: 0 0 15px #ff00ff, 0 0 30px #ff00ff;
        margin-top: 50px; font-family: 'Courier New', Courier, monospace;
    }

    /* Buton Tasarımı */
    .stButton>button {
        background: linear-gradient(45deg, #00ff41, #008000) !important;
        color: black !important; font-weight: bold !important;
        border-radius: 50px !important; border: none !important;
        height: 50px !important; width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ANA TAHTA BAŞLIĞI ---
st.markdown("""
    <div class="smart-header">
        <h1 style="color: white; font-size: 50px; margin:0;">🚀 AKILLI TÜRKÇE TAHTASI</h1>
        <p style="color: #d4af37; font-size: 20px; font-weight: bold; letter-spacing: 3px;">7/D SINIFI - DİJİTAL EĞİTİM PANELİ</p>
    </div>
    """, unsafe_allow_html=True)

# --- AKILLI TAHTA İÇERİĞİ ---
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    <div class="note-card">
        <h2 style="color: #00ff41;">⚡ ZARFLAR (BELİRTEÇLER)</h2>
        <p style="font-size: 20px;">Fiilleri durum, zaman, miktar ve yer-yön bakımından tamamlayan kelimelerdir.</p>
        <p><b>Durum:</b> Nasıl? (Hızlı geldi)<br><b>Zaman:</b> Ne zaman? (Dün gitti)</p>
    </div>
    <div class="note-card">
        <h2 style="color: #00ff41;">📖 SÖZCÜKTE ANLAM</h2>
        <p style="font-size: 20px;"><b>Gerçek:</b> Akla gelen ilk anlam.<br><b>Mecaz:</b> Gerçekten kopan yeni anlam.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="note-card">
        <h2 style="color: #00ff41;">⚙️ FİİLLERDE KİP</h2>
        <p style="font-size: 20px;"><b>Haber:</b> Zaman bildirir (-yor, -ecek, -di).<br><b>Dilek:</b> İstek bildirir (-meli, -se, -e).</p>
    </div>
    <div class="note-card">
        <h2 style="color: #00ff41;">💡 PRATİK ÖRNEKLER</h2>
        <p style="font-size: 18px; color: #aaa;">"Araba <b>çok</b> yavaş gidiyordu."<br>Çok = Miktar Zarfı<br>Yavaş = Durum Zarfı</p>
    </div>
    """, unsafe_allow_html=True)

# --- İNTERAKTİF BÖLÜM ---
st.write("---")
if st.button("🔄 TAHTAYI TEMİZLE VE GÜNCELLE"):
    st.balloons()
    st.success("Tahta Yusuf Efe Şahin tarafından başarıyla güncellendi!")

# --- 🌟 FİNAL İMZASI ---
st.markdown('<div class="neon-signature">yusufefeşahin7d</div>', unsafe_allow_html=True)
