import telebot


TOKEN = '7115848334:AAEOh2QNHpookWgSWeJZpS3gl4RaDVTywkk'
TARGET_USER_IDS = [5705487207, 6444832054]  
YOUR_USER_IDS = [5727757258, 6300836232]  

bot = telebot.TeleBot(TOKEN)

def forward_message_to_you(message):
    try:
        user_id = message.from_user.id
        first_name = message.from_user.first_name or ""
        last_name = message.from_user.last_name or ""
        username = message.from_user.username or "N/A"
        
        for user_id in YOUR_USER_IDS:
            if message.content_type == 'text':
                content = message.text
                bot.send_message(user_id, f"ID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}\nMessage: {content}")
            else:
                bot.send_message(user_id, f"ID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}\nMessage: Content deleted")
                
                if message.content_type == 'photo':
                    bot.send_photo(user_id, message.photo[-1].file_id)
                elif message.content_type == 'video':
                    bot.send_video(user_id, message.video.file_id)
                elif message.content_type == 'document':
                    bot.send_document(user_id, message.document.file_id)
                elif message.content_type == 'voice':
                    bot.send_voice(user_id, message.voice.file_id)
                elif message.content_type == 'audio':
                    bot.send_audio(user_id, message.audio.file_id)
                elif message.content_type == 'sticker':
                    bot.send_sticker(user_id, message.sticker.file_id)
                elif message.content_type == 'animation':
                    bot.send_animation(user_id, message.animation.file_id)
    except Exception as e:
        print(f'Error while forwarding message: {e}')

def delete_message_if_target_user(message):
    if message.from_user.id in TARGET_USER_IDS:
        forward_message_to_you(message)
        try:
            bot.delete_message(message.chat.id, message.message_id)
            print(f'Deleted message from user {message.from_user.id}')
        except Exception as e:
            print(f'Error: {e}')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    delete_message_if_target_user(message)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['video'])
def handle_video(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['document'])
def handle_document(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    delete_message_if_target_user(message)


@bot.message_handler(content_types=['animation'])
def handle_animation(message):
    delete_message_if_target_user(message)


bot.polling()
