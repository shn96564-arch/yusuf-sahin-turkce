import streamlit as st
import PyPDF2
import re

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="7. Sınıf Türkçe Asistanı", layout="wide", page_icon="📖")

# --- PDF'DEN BİLGİ ÇEKME FONKSİYONU ---
def ders_notu_oku(konu):
    try:
        with open("konu_anlatim.pdf", "rb") as f:
            pdf = PyPDF2.PdfReader(f)
            tam_metin = ""
            for sayfa in pdf.pages:
                metin = sayfa.extract_text()
                if metin:
                    tam_metin += metin + "\n"
            
            if not tam_metin.strip():
                return "Notlarım şu an boş görünüyor, PDF dosyasını kontrol edelim."

            konu_low = konu.lower()
            metin_low = tam_metin.lower()

            if konu_low in metin_low:
                baslangic = metin_lower.find(konu_low)
                # Konunun geçtiği yerden itibaren 800 karakter al
                bitis = baslangic + 800 
                icerik = tam_metin[baslangic:bitis]
                return icerik
            else:
                return "Aradığın konuyu notlarımda tam bulamadım ama genel bilgilere buradan bakabilirsin:\n\n" + tam_metin[:500]
    except FileNotFoundError:
        return "⚠️ Hata: 'konu_anlatim.pdf' dosyası bulunamadı!"
    except:
        return "Bir şeyler ters gitti, hemen kontrol ediyorum."

# --- YAN MENÜ (ADMİN) ---
with st.sidebar:
    st.title("👨‍🏫 Kontrol Paneli")
    sifre = st.text_input("Şifre:", type="password")
    is_admin = (sifre == "yusufshn072")
    
    if is_admin:
        st.success("Yönetici Girişi Yapıldı!")
        if st.button("Sohbeti Temizle"):
            st.session_state.messages = []
            st.rerun()

# --- ANA EKRAN ---
st.title("🤖 7. Sınıf Türkçe Akıllı Asistanı")
st.write("---")

# Sohbet Geçmişi
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Selam! Ders notlarını senin için tarıyorum. Hangi konuyu sormak istersin?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# --- ÖĞRENCİ SORUSU ---
if prompt := st.chat_input("Bir konu adı yaz (Örn: Fiiller)"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.spinner("Hemen notlarıma bakıyorum..."):
        pdf_bilgisi = ders_notu_oku(prompt)
    
    # Gereksiz tüm isimleri sildik, sadece bilgi geliyor
    cevap = f"### 📖 Ders Notu Bilgisi:\n\n{pdf_bilgisi}\n\n--- \n💡 **Not:** Bu bilgi PDF dosyasından senin için çıkarıldı."
    
    st.session_state.messages.append({"role": "assistant", "content": cevap})
    with st.chat_message("assistant"):
        st.write(cevap)

# --- VİDEO BÖLÜMÜ ---
if is_admin:
    st.divider()
    st.subheader("📺 Özel Anlatım")
    try:
        st.video("turkce_ders.mp4")
    except:
        st.info("Video dosyası yüklendiğinde burada görünecek.")

st.caption("Yusuf Şahin Akademisi | 2026")
