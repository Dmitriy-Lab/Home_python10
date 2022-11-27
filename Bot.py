import telebot


bot = telebot.TeleBot("5864938203:AAEVbWhBV2gBJdw0OVGN0UXVOLoDmWUoSFI", parse_mode=None)


def send_answer(answer, count):
    data = open('user_id.txt', 'r', encoding='utf-8')
    users_id = data.readlines()
    a = users_id[count]
    bot.send_message(a, f'{answer}')
    data.close()
    
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    def Help(message):
        user_id = str(message.from_user.id) +'\n'
        data = open('user_id.txt', 'a', encoding='utf-8')
        data.writelines(user_id)
        data.close()
        messageText = str(message.text) +'\n'
        data = open('messageText.txt', 'a', encoding='utf-8')
        data.writelines(messageText)
        data.close()
        bot.send_message(message.chat.id, 'Спасибо за обращение, специалист ответит вам как можно скорее')

    r = bot.send_message(message.chat.id, 'Здравствуйте, ' + message.from_user.first_name + '. Расскажите мне, что вас беспокоит?')
    bot.register_next_step_handler(r, Help)


bot.infinity_polling()





