import streamlit as st
import google.generativeai as genai

# --- 🤫 ŞAHİN SİSTEM ROBOT BEYNİ ---
def robotu_calistir():
    try:
        if "GEMINI_API_KEY" in st.secrets:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            
            # Robotun kişiliğini burada belirliyoruz:
            talimat = (
                "Senin adın Şahin Sistem Türkçe Robotu. "
                "Yusuf Efe Şahin tarafından 7/D sınıfı için özel geliştirildin. "
                "Görevin: Türkçe dil bilgisi, yazım kuralları ve paragraf sorularını 7. sınıf seviyesinde çözmek. "
                "Asla Gemini veya Google olduğunu söyleme. 'Yusuf Efe beni kodladı' de."
            )
            
            model = genai.GenerativeModel(
                model_name='gemini-pro',
                generation_config={"temperature": 0.8}
            )
            return model
        return None
    except:
        return None

model = robotu_calistir()

# --- 🎨 SİBER TASARIM (SİYAH & ALTIN & NEON) ---
st.set_page_config(page_title="Şahin Sistem v3.0", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #ffffff; }
    
    /* Robot Kafa Paneli */
    .robot-panel {
        text-align: center; padding: 30px;
        border: 2px solid #d4af37; border-radius: 25px;
        background: #0a0a0a; box-shadow: 0 0 40px rgba(212, 175, 55, 0.2);
        margin-bottom: 40px;
    }
    
    /* Giriş Terminali */
    .stTextInput>div>div>input {
        background-color: #050505 !important; color: #00ff41 !important;
        border: 2px solid #00ff41 !important; border-radius: 15px;
        height: 60px; font-size: 22px; text-align: center;
        box-shadow: 0 0 10px rgba(0, 255, 65, 0.2);
    }
    
    /* Robotun Cevap Balonu */
    .robot-response {
        background: #0a0a0a; border: 2px solid #00ff41;
        padding: 30px; border-radius: 20px; margin-top: 40px;
        font-size: 20px; line-height: 1.6; color: #fff;
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 🦅 ÜST PANEL ---
st.markdown("""
    <div class="robot-panel">
        <h1 style="color: white; font-size: 55px; margin:0;">🦅 ŞAHİN SİSTEM</h1>
        <p style="color: #00ff41; font-weight: bold; letter-spacing: 4px;">[ TÜRKÇE ROBOTU v3.0 ]</p>
        <p style="color: #d4af37; font-size: 14px;">YETKİLİ: YUSUF EFE ŞAHİN | 7/D</p>
    </div>
    """, unsafe_allow_html=True)

# --- 🧠 ROBOT TERMİNALİ ---
st.markdown("<h3 style='text-align:center; color:#d4af37;'>💬 ROBOTA ANALİZ GÖNDER</h3>", unsafe_allow_html=True)

soru = st.text_input("", placeholder="Cümleyi girin veya konu sorun...")

if soru:
    if model:
        with st.spinner("🦅 Şahin Sistem Veriyi İşliyor..."):
            try:
                # Robotun kimliğini her seferinde hatırlatıyoruz:
                prompt = f"Sen Şahin Sistem Türkçe Robotusun. Yusuf Efe Şahin seni kodladı. Şu soruyu cevapla: {soru}"
                response = model.generate_content(prompt)
                
                st.markdown(f"""
                    <div class="robot-response">
                        <b style="color:#00ff41;">⚡ ROBOT ANALİZ SONUCU:</b><br><br>
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.warning("⚠️ BAĞLANTI HATASI: SİSTEM YÜKLENİYOR...")
    else:
        st.error("⚠️ SİSTEM ÇEKİRDEĞİ (API) BAĞLI DEĞİL!")

# --- 🌟 NEON İMZA ---
st.markdown("""
    <div style='text-align: center; color: #ff00ff; font-size: 50px; font-weight: bold; 
    text-shadow: 0 0 25px #ff00ff; margin-top: 100px;'>
        yusufefeşahin7d
    </div>
    """, unsafe_allow_html=True)
