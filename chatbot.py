from googletrans import Translator
from textblob import TextBlob

def analyze_sentiment(text):
    translator = Translator()
    eng = translator.translate(text, dest='en').text
    blob = TextBlob(eng)
    return blob.sentiment.polarity

def generate_response(polarity):
    if polarity >= 0.3:
        return "Bot: Harika böyle hissetmene sevindim!"
    elif polarity <= -0.3:
        return "Bot: Üzgünüm, umarım yakında kendini daha iyi hissedersin."
    else:
        return "Bot: Hmm karmaşık duygular hissediyor gibisin."


def chat():
    print("Çıkmak için 'çık' yazın.")
    while True:
        user_input = input("Sen: ")
        if user_input.lower() in ("çık", "exit"):
            print("Bot: Görüşürüz!")
            break
        polarity = analyze_sentiment(user_input)
        response = generate_response(polarity)
        print(response)

if __name__ == "__main__":
    chat()
