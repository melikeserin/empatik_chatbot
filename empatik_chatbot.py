from googletrans import Translator
from textblob import TextBlob
from colorama import Fore, Style, init

init(autoreset=True)  

def analyze_sentiment(text):
    translator = Translator()
    eng = translator.translate(text, dest='en').text
    blob = TextBlob(eng)
    return blob.sentiment.polarity

def generate_response(polarity):
    if polarity >= 0.6:
        print(Fore.GREEN + "Bot: Gerçekten çok mutlu olman harika!Enerjini çevrendekilerle paylaşabilirsin.")
    elif polarity >= 0.2:
        print(Fore.GREEN + "Bot: İyi hissetmene sevindim! Bu duyguyu sürdürmek için bugün sevdiğin bir şeyi yapmayı unutma.")
    elif -0.2 < polarity < 0.2:
        print(Fore.YELLOW + "Bot: Karışık duygular hissediyor gibisin. Böyle günler normaldir. Belki sevdiğin biriyle konuşmak iyi gelebilir.")
    elif polarity <= -0.2 and polarity > -0.5:
        print(Fore.RED + "Bot: Zor bir gün geçiriyor olabilirsin. Yürüyüş yapmak, nefes egzersizi denemek iyi gelebilir. Yalnız değilsin.")
    else:
        print(Fore.RED + "Bot: Gerçekten kötü hissediyor gibisin. Lütfen bu duygularla tek başına baş etmeye çalışmak zorunda değilsin. Bir uzmana ya da güvendiğin birine ulaşmak iyi olabilir.")

def chat():
    print(Style.BRIGHT + Fore.CYAN + "Bot: Merhaba, nasıl hissettiğini bana anlatabilirsin. (Çıkmak için 'çık' yaz)")
    while True:
        user_input = input(Fore.WHITE + "Sen: ")
        if user_input.lower() in ("çık", "exit"):
            print(Fore.MAGENTA + "Bot: Görüşmek üzere! Kendine iyi bak!")
            break
        polarity = analyze_sentiment(user_input)
        generate_response(polarity)

if __name__ == "__main__":
    chat()
