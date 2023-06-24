import telebot
import speech_recognition as sr
import soundfile as sf

token="6034380785:AAG4BkPrnhKWlPw-e8BbBgaM9wy0zUvJ1EU"
bot = telebot.TeleBot(token)
r=sr.Recognizer()
language='ru_RU'
@bot.message_handler(content_types=['voice'])
def convert(message):
    bot.reply_to(message,message)
    voice_file=bot.get_file(message.voice.file_id)
    voice_m=bot.download_file(voice_file.file_path)
    with open('audio.ogg','wb') as f:
        f.write(voice_m)
    
    data,samplerate = sf.read('audio.ogg')
    sf.write('audio.wav',data,samplerate)
    with sr.AudioFile('audio.wav') as sourse:
        audio_data = r.record(sourse)
    try:
        text =r.recognize_google(audio_data,language=language)
        bot.reply_to(message,text)
    except :
        bot.reply_to(message,"не могу расшифровать")
@bot.message_handler(content_types=['text'])
def send(message):
    #bot.reply_to(message,message)
    try:
        if message.from_user.id==1161725719 and '@DELMi090' in message.text :
        #bot.send_message(message.chat.id,'1')
            bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIFU2Q2zthaa6hRySy6hi73IqpbZoToAAJdEgAC5SfRSJRZXiTYMQOQLwQ')
        if message.entities[0].user.id==1396462798:
            bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAIFWGQ20Qlt9XhfNvDx0ElHQzKse_SoAAIuHQACySWASpVguKRI2K_ALwQ')
    except:
        pass
# @bot.message_handler(content_types=['video_note'])
# def send1(message):
#     bot.reply_to(message,message)
    
#@bot.message_handler(content_types=['sticker'])
#def send(message):
#    bot.send_message(message.chat.id,message)
bot.polling(none_stop=True)
