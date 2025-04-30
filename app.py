import streamlit as st
from textblob import TextBlob
from googletrans import Translator


def analyze_sentiment(text):
    translator = Translator()
    eng = translator.translate(text, dest='en').text
    blob = TextBlob(eng)
    return blob.sentiment.polarity

def generate_response(polarity):
    if polarity >= 0.6:
        return " Harika! Gerçekten mutlu görünüyorsun. Enerjini çevrendekilerle paylaşabilirsin."
    elif polarity >= 0.2:
        return " İyi hissetmene sevindim. Sevdiğin bir şeyle gününü daha da güzelleştirebilirsin."
    elif -0.2 < polarity < 0.2:
        return " Karışık duygular hissediyor gibisin. Belki bir müzik, yürüyüş ya da biriyle konuşmak iyi gelir."
    elif polarity <= -0.2 and polarity > -0.5:
        return " Zor bir gün olabilir. Kendine zaman tanı ve gerekirse bir nefes egzersizi dene."
    else:
        return " Üzgün hissediyorsan, lütfen bu duygularla yalnız kalma. Konuşabileceğin biri mutlaka vardır."

# Streamlit Arayüzü
st.set_page_config(page_title="Duygu Analizli Sohbet Botu", layout="centered")
st.title("🧠 Duygu Analizli Sohbet Botu")
st.markdown("Nasıl hissettiğini bana yaz, ben de duyguna uygun bir şeyler söyleyeyim. ")

user_input = st.text_area("Bugün nasılsın?", height=150)

if st.button("Gönder"):
    if user_input.strip() == "":
        st.warning("Lütfen bir şeyler yaz.")
    else:
        polarity = analyze_sentiment(user_input)
        response = generate_response(polarity)

        if polarity > 0.2:
            st.success(response)
        elif polarity < -0.2:
            st.error(response)
        else:
            st.info(response)
