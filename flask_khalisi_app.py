from flask import Flask, request
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "d37fbbcd-9cd8-4de2-888f-99ed4e7c0a94"
bot = telepot.Bot('1689833840:AAEVj4mCltLZFZ7BE3opnyJ2Ww_OcFy1JPY')
bot.setWebhook("https://khalisibot.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            if text == '/start':
                bot.sendMessage(chat_id,
                                "Привет! Говорит Кхалиси-бот! Скажи мне что нибудь и услышь в ответ издевательство!")
            else:
                result = ''
                vovel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
                vovel_up = ['А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
                consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц',
                              'ч', 'ш',
                              'щ']
                consonants_up = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'К', 'Л', 'М', 'Н',
                                 'П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
                if set(vovel).isdisjoint(text) and set(vovel_up).isdisjoint(text):
                    bot.sendMessage(chat_id, "Не могу Кхалисифицировать!")
                else:
                    for i in range(len(text)):

                        if text[i] == 'а':
                            result += 'я'
                        elif text[i] == 'ж':
                            result += 'з'
                        elif text[i] == 'з':
                            result += 'ж'
                        elif text[i] == 'о':
                            result += 'ё'
                        elif text[i] == 'с':
                            result += 'щ'
                        elif text[i] == 'у':
                            result += 'ю'
                        elif text[i] == 'ц' or text[i] == 'щ':
                            result += 'с'
                        elif text[i] == 'ч':
                            result += 'щ'
                        elif text[i] == 'э':
                            result += 'е'
                        elif text[i] == 'ы':
                            result += 'и'
                        elif text[i] == 'А':
                            result += 'Я'
                        elif text[i] == 'Ж':
                            result += 'З'
                        elif text[i] == 'З':
                            result += 'Ж'
                        elif text[i] == 'О':
                            result += 'Ё'
                        elif text[i] == 'С':
                            result += 'Щ'
                        elif text[i] == 'У':
                            result += 'Ю'
                        elif text[i] == 'Ц' or text[i] == 'Щ':
                            result += 'С'
                        elif text[i] == 'Ч':
                            result += 'Щ'
                        elif text[i] == 'Э':
                            result += 'Е'
                        elif text[i] == 'Ы':
                            result += 'И'
                        elif text[i] == ' ' and text[i - 1] in consonants:
                            result += 'ь'
                            result += ' '
                        elif text[i] == ' ' and text[i - 1] in consonants_up:
                            result += 'Ь'
                            result += ' '
                        else:
                            result += text[i]
                    if result[len(result) - 1] in consonants:
                        result += 'ь'
                    elif result[len(result) - 1] in consonants_up:
                        result += 'Ь'
                    bot.sendMessage(chat_id, result)
        else:
            bot.sendMessage(chat_id, "Не могу Кхалисифицировать!")
    return "OK"
