import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Efe Şahin | Türkçe Dijital Asistan", layout="wide")

# --- 🎨 ÖZEL NEON TASARIM ---
st.markdown("""
    <style>
    .main { background-color: #050505; color: #ffffff; }
    .premium-header {
        text-align: center; padding: 25px;
        background: linear-gradient(145deg, #111, #000);
        border: 2px solid #00ff41; border-radius: 20px;
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.3);
        margin-bottom: 20px;
    }
    .neon-footer {
        text-align: center; font-size: 50px; font-weight: bold;
        color: #fff; text-shadow: 0 0 10px #00ff41, 0 0 20px #00ff41, 0 0 40px #00ff41;
        margin-top: 50px; letter-spacing: 5px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #d4af37, #f1c40f) !important;
        color: black !important; font-weight: bold !important;
        border-radius: 12px !important; width: 100% !important; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÜST PANEL ---
st.markdown("""
    <div class="premium-header">
        <p style="color: #00ff41; font-weight: bold; letter-spacing: 3px;">7. SINIF TÜRKÇE PROJESİ</p>
        <h1 style="font-size: 45px; margin: 0; color: white;">DİJİTAL KONU ANLATIM SİSTEMİ</h1>
        <p style="color: #d4af37;">Geliştirici: Yusuf Efe Şahin</p>
    </div>
    """, unsafe_allow_html=True)

# --- 🖊️ CANLI NEON ÇİZİM (ZARFLAR ŞEMASI) ---
st.markdown("### 🖥️ Akıllı Tahta Görünümü")

# Canlı çizim efektli HTML/JS
drawing_html = """
<div style="text-align:center;">
    <canvas id="canvas" width="800" height="450" style="background:#000; border:1px solid #333; border-radius:15px;"></canvas>
</div>
<script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const green = "#00ff41";
    const gold = "#d4af37";

    function drawLine(x1, y1, x2, y2, color, delay) {
        setTimeout(() => {
            ctx.strokeStyle = color;
            ctx.lineWidth = 3;
            ctx.shadowBlur = 15;
            ctx.shadowColor = color;
            ctx.beginPath();
            ctx.moveTo(x1, y1);
            ctx.lineTo(x2, y2);
            ctx.stroke();
        }, delay);
    }

    function drawText(txt, x, y, color, delay) {
        setTimeout(() => {
            ctx.fillStyle = color;
            ctx.font = "bold 24px Arial";
            ctx.shadowBlur = 5;
            ctx.fillText(txt, x, y);
        }, delay);
    }

    // Çizim Başlıyor
    drawText("ZARFLAR", 350, 50, gold, 500);
    drawLine(400, 60, 400, 150, green, 1000); // Ana direk
    
    // Dallar
    drawLine(400, 150, 150, 250, green, 1500); // Durum
    drawLine(400, 150, 400, 250, green, 2000); // Zaman
    drawLine(400, 150, 650, 250, green, 2500); // Miktar

    // Yazılar
    drawText("Durum Zarfı", 80, 280, "#fff", 3000);
    drawText("Zaman Zarfı", 330, 280, "#fff", 3500);
    drawText("Miktar Zarfı", 580, 280, "#fff", 4000);
    
    drawText("(Nasıl?)", 110, 310, gold, 4500);
    drawText("(Ne zaman?)", 340, 310, gold, 5000);
    drawText("(Ne kadar?)", 590, 310, gold, 5500);
</script>
"""
st.components.v1.html(drawing_html, height=480)

# --- İNTERAKTİF BUTONLAR ---
st.write("---")
c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 ÇİZİMİ TEKRARLAT"):
        st.rerun()
with c2:
    if st.button("🎯 ÖRNEK SORU GÖSTER"):
        st.info("**Soru:** 'Öğrenciler sessizce bekliyor.' cümlesinde zarf hangisidir?\n\n**Cevap:** Sessizce (Durum Zarfı)")

# --- 🌟 NEON İMZA ---
st.markdown('<div class="neon-footer">YUSUF EFE ŞAHİN</div>', unsafe_allow_html=True)
