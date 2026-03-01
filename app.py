import streamlit as st
import PyPDF2
import re

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Yusuf Şahin | AI Öğretmen", layout="wide")

# --- GELİŞMİŞ PDF ARAMA MOTORU ---
def pdf_oku_akilli(aranan_konu):
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            tam_metin = ""
            for sayfa in pdf.pages:
                metin = sayfa.extract_text()
                if metin:
                    tam_metin += metin + "\n"
            
            if not tam_metin.strip():
                return "⚠️ PDF içi boş veya okunabilir metin içermiyor!"

            # Küçük harfe çevirip arayalım ki büyük/küçük harf hatası olmasın
            aranan_konu = aranan_konu.lower()
            metin_lower = tam_metin.lower()

            if aranan_konu in metin_lower:
                # Kelimenin geçtiği yeri bul ve etrafındaki 500 karakteri al
                baslangic = metin_lower.find(aranan_konu)
                bitis = baslangic + 800 # Konudan sonraki 800 karakteri getir
                icerik = tam_metin[baslangic:bitis]
                return icerik
            else:
                # Bulamazsa PDF'in başından bir parça getir ki hoca "çalışmıyor" demesin
                return "Aradığın konuyu tam bulamadım ama PDF notlarında şöyle bir bölüm var:\n\n" + tam_metin[:600]
    except FileNotFoundError:
        return "⚠️ Hata: 'konu_anlatim.pdf' dosyası bulunamadı!"
    except Exception as e:
        return f"⚠️ Bir hata oluştu: {e}"

# --- SIDEBAR ---
with st.sidebar:
    st.title("👨‍🏫 Yusuf Hoca")
    sifre = st.text_input("Şifre:", type="password")
    is_admin = (sifre == "yusufshn072")

# --- ANA EKRAN ---
st.title("🤖 7. Sınıf Türkçe Akıllı Asistan")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Selam! PDF notlarını taramaya hazırım. Hangi konuyu soracaksın?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- SORU SORMA ---
if prompt := st.chat_input("Örn: Fiiller, Zarflar..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # PDF'DEN CEVABI ÇEK
    with st.spinner("PDF taranıyor..."):
        pdf_cevabi = pdf_oku_akilli(prompt)
    
    tam_cevap = f"### 👨‍🏫 Yusuf Hocanın PDF Notuna Göre:\n\n{pdf_cevabi}"
    
    st.session_state.messages.append({"role": "assistant", "content": tam_cevap})
    with st.chat_message("assistant"):
        st.write(tam_cevap)

# --- VİDEO ---
if is_admin:
    st.divider()
    st.video("turkce_ders.mp4")