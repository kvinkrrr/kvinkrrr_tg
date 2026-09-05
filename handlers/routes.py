from aiogram import Router, F
from aiogram.types import (Message, MessageEntity, InlineKeyboardButton,
                           InlineKeyboardMarkup, CallbackQuery)
from aiogram.types import FSInputFile
from aiogram import Bot, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()
GROUP_ID = -1004480965680


def get_main_inline_keyboard():
    keyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='инфо', callback_data="information"),
            InlineKeyboardButton(text='напиши мне', callback_data="write")],
            [InlineKeyboardButton(text='тгк: 𝓀𝓋𝒾𝓃𝓀𝓇𝓇𝓇.𝓋𝓇𝓃✨', callback_data="tgc")]
        ]
    )
    return keyboard


def get_main_information():
    keyboard=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Telegram', url="https://t.me/kvinkrrr"), InlineKeyboardButton(text='Discord', url="https://discordapp.com/users/801829624354701373"),
            InlineKeyboardButton(text='Steam', url="https://steamcommunity.com/id/kvinkrrr/")]
        ]
    )
    return keyboard



@router.message(Command("start"))
@router.message(F.text.lower()=="вернутся к началу")
async def start (message: Message):
    caption=("👇🔜😳👅😭💀🔫❌😇\n\n"
             "Это простой бот-инфо 💎.\nВыбери то, что тебя интересует с помощью кнопок 🚀!")
    emojis = [
        ("💎", "5442990914391791134"),
        ("🚀", "5256258204651785650"),
        ("👇", "5366394914311544061"),
        ("🔜", "5366191826782951761"),
        ("😳", "5364168240056540758"),
        ("👅", "5366337305915202344"),
        ("😭", "5366040948876810901"),
        ("💀", "5366103436356000593"),
        ("🔫", "5364168240056540758"),
        ("❌", "5364031685866331763"),
        ("😇", "5366272666657398526")
    ]

    entities = []

    # Добавляем Premium Emoji
    for emoji, emoji_id in emojis:
        pos = caption.find(emoji)

        entities.append(
            MessageEntity(
                type="custom_emoji",
                offset=len(
                    caption[:pos].encode("utf-16-le")
                ) // 2,
                length=len(
                    emoji.encode("utf-16-le")
                ) // 2,
                custom_emoji_id=emoji_id
            )
        )
    await message.answer_photo(
    photo = FSInputFile("welcome.jpg"),
    caption = caption,
    caption_entities = entities,
    reply_markup=get_main_inline_keyboard()
    )


@router.callback_query(lambda c: c.data=="tgc")
async def process_more_info(callback:CallbackQuery):
    caption = "\t👇🔜😳       👅️😭💀 \n\nВот ссылка на мой тгк!\nПодай заявку, чтобы вступить в канал\nhttps://t.me/+GLuF0ukWBL9kYTky\n\n"\
              "Нажми / start, чтобы вернутся обратно в меню\n"

    # Реальные ID Premium Emoji
    emojis = [
        ("👇", "5363794492002440391"),
        ("🔜", "5363914742496793834"),
        ("😳", "5366479817225049534"),
        ("👅", "5366103436356000593"),
        ("😭", "5366227891623335842"),
        ("💀", "5364031685866331763")

    ]

    entities = []

    # Добавляем Premium Emoji
    for emoji, emoji_id in emojis:
        pos = caption.find(emoji)

        entities.append(
            MessageEntity(
                type="custom_emoji",
                offset=len(
                    caption[:pos].encode("utf-16-le")
                ) // 2,
                length=len(
                    emoji.encode("utf-16-le")
                ) // 2,
                custom_emoji_id=emoji_id
            )
        )
    await callback.message.answer_photo(
        photo=FSInputFile("tgc.jpg"),
        caption=caption,
        caption_entities=entities)
    await callback.answer()





@router.callback_query(lambda c: c.data=="information")
async def process_more_info(callback:CallbackQuery):

    caption = "\t      🔥 💎 🚀 ⭐️\n\n\tинфо kvinkrrr \n\nНажми /start, чтобы вернутся обратно в меню"

    # Реальные ID Premium Emoji
    emojis = [
        ("🔥", "5364168240056540758"),
        ("💎", "5366264218456727517"),
        ("🚀", "5364105658088069862"),
        ("⭐️", "5363914742496793834"),

    ]

    entities = []

    # Добавляем Premium Emoji
    for emoji, emoji_id in emojis:
        pos = caption.find(emoji)

        entities.append(
            MessageEntity(
                type="custom_emoji",
                offset=len(
                    caption[:pos].encode("utf-16-le")
                ) // 2,
                length=len(
                    emoji.encode("utf-16-le")
                ) // 2,
                custom_emoji_id=emoji_id
            )
        )

    # Добавляем кликабельный текст
    link_text = "инфо kvinkrrr"
    pos = caption.find(link_text)

    entities.append(
        MessageEntity(
            type="text_link",
            offset=len(
                caption[:pos].encode("utf-16-le")
            ) // 2,
            length=len(
                link_text.encode("utf-16-le")
            ) // 2,
            url="https://telegra.ph/info-09-05-41"
        )
    )

    await callback.message.answer_photo(
        photo=FSInputFile("information.jpg"),
        caption=caption,
        caption_entities=entities,
        reply_markup=get_main_information()
    )
    await callback.answer()





#ФУНКЦИЯ ОТПРАВКИ СООБЩЕНИЯ

group_to_user = {}

# ID сообщения пользователя -> ID сообщения в группе
user_to_group = {}

class SendMessage(StatesGroup):
    waiting_for_message = State()

@router.callback_query(lambda c: c.data=="write")
@router.message(Command("send"))
async def send_command(
    message: types.Message,
    state: FSMContext
):

    await message.answer(
        "✉️ Отправь сообщение, которое хочешь мне отправить (текст, фото, видео, стикер).\n"
        "Если хочешь ответить на сообщение от меня, то свайпни влево для ответа\n"
        "Нажми /start, чтобы вернутся обратно в меню\n"

    )

    await state.set_state(
        SendMessage.waiting_for_message
    )

# =========================
# ОТПРАВКА СООБЩЕНИЯ В ГРУППУ
# =========================

@router.message(SendMessage.waiting_for_message)
async def process_message(
    message: types.Message,
    state: FSMContext,
    bot: Bot
):

    try:

        # Копируем сообщение пользователя в группу
        sent = await bot.copy_message(
            chat_id=GROUP_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id
        )

        # Связываем сообщение в группе с пользователем
        group_to_user[sent.message_id] = message.from_user.id

        # Связываем сообщение пользователя с сообщением группы
        user_to_group[message.message_id] = sent.message_id

        await message.answer(
            "✅ Сообщение отправлено!\n"
            "Если хочешь ответить на сообщение от меня, то свайпни влево для ответа\n\n"
            "Нажми /start, чтобы вернутся обратно в меню\n"
        )

    except Exception as e:

        await message.answer(
            f"❌ Ошибка:\n{e}"
        )

    finally:

        await state.clear()

# ==================================================
# ОТВЕТ УЧАСТНИКА ГРУППЫ
# ==================================================

@router.message(
    lambda message:
    message.chat.id == GROUP_ID
    and message.reply_to_message is not None
)
async def group_reply(message: types.Message, bot: Bot):

    replied_message_id = (
        message.reply_to_message.message_id
    )

    # Ищем пользователя, которому принадлежит
    # сообщение, на которое ответили
    user_id = group_to_user.get(
        replied_message_id
    )

    if not user_id:
        return

    try:

        # Отправляем ответ пользователю
        sent = await bot.copy_message(
            chat_id=user_id,
            from_chat_id=GROUP_ID,
            message_id=message.message_id
        )

        # Теперь сообщение пользователя в личке
        # связано с сообщением в группе
        user_to_group[sent.message_id] = (
            message.message_id
        )

    except Exception as e:

        print(
            f"Ошибка отправки ответа пользователю: {e}\n\n"
            "Нажми /start, чтобы вернутся обратно в меню\n"
        )

# ==================================================
# ОТВЕТ ПОЛЬЗОВАТЕЛЯ НА СООБЩЕНИЕ ИЗ ГРУППЫ
# ==================================================

@router.message(
    lambda message:
    message.chat.id != GROUP_ID
    and message.reply_to_message is not None
)
async def user_reply(message: types.Message, bot: Bot):

    replied_message_id = (
        message.reply_to_message.message_id
    )

    # Находим сообщение в группе,
    # которому соответствует сообщение в личке
    group_message_id = user_to_group.get(
        replied_message_id
    )

    if not group_message_id:
        return

    try:

        # Копируем ответ пользователя в группу
        sent = await bot.copy_message(
            chat_id=GROUP_ID,
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            reply_parameters=types.ReplyParameters(
                message_id=group_message_id
            )
        )

        # Связываем новое сообщение в группе
        # с пользователем
        group_to_user[sent.message_id] = (
            message.from_user.id
        )

    except Exception as e:

        print(
            f"Ошибка отправки ответа в группу: {e}\n\n"
            "Нажми /start, чтобы вернутся обратно в меню\n"
        )




