import telebot

from telebot import types

TOKEN = "5869880785:AAGQIFs9A31kj5Otus8TPbCwbtxsaNUe4e8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("C:/py.projects/venv/static/welcome.webp", "rb")
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кактусы")
    item2 = types.KeyboardButton("Другие суккуленты")
    item3 = types.KeyboardButton("Помощь в определении названия растения")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать! Я - бот, который поможет тебе ухаживать "
                                      "за кактусами и другими скуккулентами. "
                                      "Выбери интересующую тебя категорию:", reply_markup=markup)

@bot.message_handler(commands=['start'])
def one(message):
    send = bot.send_message(message.chat.id, 'Ответы на вопросы нужно вводить с клавиатуры, с большой буквы, '
                                             'без точки, отвечая только Да или Нет '
                                             ' или вводя подходящее под описание слово из предоставленного в вопросах списков.'
                                             '\n\n1. Есть ли у твоего растения колючки?')
    bot.register_next_step_handler(send, two)

def two(message):
    global ans
    ans = []
    one_answer = message.text
    ans.append(one_answer)
    send = bot.send_message(message.chat.id, '2. Есть ли у твоего растения листья?')
    bot.register_next_step_handler(send, three)

def three(message):
    two_answer = message.text
    ans.append(two_answer)
    send = bot.send_message(message.chat.id, '3. Ветвится ли твое растение?')
    bot.register_next_step_handler(send, four)

def four(message):
    three_answer = message.text
    ans.append(three_answer)
    send = bot.send_message(message.chat.id, '4. Какую форму произрастания имеет растение: Шар, Цилиндр, Лиана, Куст, Деревце?')
    bot.register_next_step_handler(send, end)

def end(message):
    four_answer = message.text
    ans.append(four_answer)

    if ans[0] == "Да" and ans[1] == "Да" and ans[2] == "Да" and ans[3] == "Куст":
                    bot.send_message(message.chat.id, "Предполагаю, что это Молочай.")
    elif ans[0] == "Нет" and ans[1] == "Да" and ans[2] == "Да" and ans[3] == "Деревце":
                    bot.send_message(message.chat.id, "Предполагаю, что это Эониум или Крассула.")
    elif ans[0] == "Да" and ans[1] == "Нет" and ans[2] == "Нет" and ans[3] == "Шар":
                    bot.send_message(message.chat.id, "Предполагаю, что это Кактус.")
    elif ans[0] == "Нет" and ans[1] == "Да" and ans[2] == "Нет" and ans[3] == "Куст":
                    bot.send_message(message.chat.id, "Предполагаю, что это Хавортия.")
    elif ans[0] == "Нет" and ans[1] == "Да" and ans[2] == "Да" and ans[3] == "Лиана":
                    bot.send_message(message.chat.id, "Предполагаю, что это Хойя.")
    elif ans[0] == "Нет" and ans[1] == "Нет" and ans[2] == "Да" and ans[3] == "Куст":
                    bot.send_message(message.chat.id, "Предполагаю, что это Стапелия.")
    elif ans[0] == "Нет" and ans[1] == "Нет" and ans[2] == "Нет" and ans[3] == "Цилиндр":
                    bot.send_message(message.chat.id, "Предполагаю, что это Литопс.")
    elif ans[0] == "Нет" and ans[1] == "Да" and ans[2] == "Да" and ans[3] == "Куст":
                    bot.send_message(message.chat.id, "Предполагаю, что это Каланхоэ.")
    elif ans[0] == "Да" and ans[1] == "Да" and ans[2] == "Нет" and ans[3] == "Куст":
                    bot.send_message(message.chat.id, "Предполагаю, что это Алоэ.")
    else:
        bot.send_message(message.chat.id, "Я не знаю, что это за растение :(")

@bot.message_handler(content_types=["text"])
def answers(message):
    if message.chat.type == "private":

        if message.text == "Кактусы":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item0 = types.KeyboardButton("Основы ухода за кактусами")
            item1 = types.KeyboardButton("Астрофитумы")
            item2 = types.KeyboardButton("Акантокалициумы")
            item3 = types.KeyboardButton("Гимнокалициумы")
            item4 = types.KeyboardButton("Лобивии")
            item5 = types.KeyboardButton("Маммиллярии")
            item6 = types.KeyboardButton("Мелокактусы")
            item7 = types.KeyboardButton("Матуканы")
            item8 = types.KeyboardButton("Нотокактусы")
            item9 = types.KeyboardButton("Ребуции")
            item10 = types.KeyboardButton("Эхинопсисы")
            item = types.KeyboardButton("Назад в меню")
            markup.add(item0, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item)

            bot.send_message(message.chat.id, "Семейство Кактусовые включает в себя около 127 родов, "
                                              "с представителем какого рода ты бы хотел ознакомиться?", reply_markup=markup)

        elif message.text == "Основы ухода за кактусами":

            bot.send_message(message.chat.id, ("Десять заповедей кактусиста:\n1. Свои кактусы оставь зимовать в сухих и холодных условиях!"
                                               "\n2. Весной не буди их поливом, а только орошением при повышенной температуре!"
                                               "\n3. Первый полив производи лишь после явного начала вегетации!"
                                               "\n4. Растения, перезимовавшие в темноте, пусть постепенно привыкают к солнцу!"
                                               "\n5. Удобрять можешь лишь в период полной вегетации растений, вне зависимости от того, какое удобрение применяешь!"
                                               "\n6. Растениям в период вегетации предоставь достаток солнца, воды и свежего воздуха! Но мокрую землю никогда не поливай!"
                                               "\n7. Растение, прекратившее свой рост, никогда не поливай! Осторожно вынь его из земли, очисти и прими меры!"
                                               "\n8. Периодически покропи растения или разбрызгивай над ними воду, но не на ярком солнце!"
                                               "\n9. Не переноси бездумно пыльцу с цветка на цветок, следи за видовой чистотой семян и растений!"
                                               "\n10. С сентября, с понижением температуры, уменьши количество и объем поливок и одновременно увеличь проветривание, "
                                               "чтобы растения в совершенстве созрели и перешли в состояние вегетационного покоя!"
                                               "\n\nН.Никонов 'Созвездие кактусов' 1978"))
        elif message.text == "Астрофитумы":
            photo = open("C:/py.projects/venv/static/astro.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Астрофитум или 'Звездчатый кактус' довольно неприхотливый род кактусов, родиной которого являются Южная Америка и Мексика. "
                                              "Самые популярные виды - Astrophytum ornatum, A. myriostigma, A. asterias, и A. capricorne.")
        elif message.text == "Акантокалициумы":
            photo = open("C:/py.projects/venv/static/acant.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Акантокалициум переводится с греческого как 'колючая чашечка', что отражает отличительную особенность данного рода, "
                                              "цветочная чашечка кактуса покрыта колючками. Акантокалициумы - кактусы высокогорья и встречаются на высоте до 1000 м. над уровнем моря.")
        elif message.text == "Гимнокалициумы":
            photo = open("C:/py.projects/venv/static/gymn.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Гимнокалициум, что в переводе с латинского означает 'голая чашечка', один из самых простых в выращивании родов кактусов, "
                                              "довольно легко добиться цветения Гимнокалициума, которое может продолжаться с ранней весны до поздней осени. "
                                              "Его родиной является Южная Америка.")
        elif message.text == "Лобивии":
            photo = open("C:/py.projects/venv/static/lob.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Похожие на эхинопсисы кактусы с красивыми цветами, но довольно прихотливые,"
                                              " некоторые виды требуют прививки.")
        elif message.text == "Маммиллярии":
            photo = open("C:/py.projects/venv/static/mamm.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Род Маммиллярии является одним из самых огромных родов и до сих пор пополняемым новыми видами, "
                                              "количество которых уже превышает 400. Уход за ними не сложен, за исключением некоторых видов. Исключительная "
                                              "особенность Маммиллярий - цветы располагаются венчиком вокруг верхушки.")
        elif message.text == "Мелокактусы":
            photo = open("C:/py.projects/venv/static/melo.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Растут у океанических побережий, в возрасте более 10 лет образуют цефалий, на котором появляются цветы.")
        elif message.text == "Матуканы":
            photo = open("C:/py.projects/venv/static/mat.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Небольшой род шаровидных кактусов, произрастающих в Перу. Особо известна Matucana madisoniorum, "
                                              "обладающая невероятно красивыми карминно-красными цветами и необычным внешним видом.")
        elif message.text == "Нотокактусы":
            photo = open("C:/py.projects/venv/static/noto.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Южноамериканские обильно цветущие весной и летом кактусы с яркими, желтыми цветами.")
        elif message.text == "Ребуции":
            photo = open("C:/py.projects/venv/static/rebut.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Род неприхотливых, а главное богатоцветущих кактусов высокогорья, растущих куртинками.")
        elif message.text == "Эхинопсисы":
            photo = open("C:/py.projects/venv/static/echin.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Эхинопсисы были самыми первыми кактусами, доставленными в Европу. Они славятся своей неприхотливостью, "
                                              "а также красотой цветков, раскрывающихся ближе к ночи и испускающих невероятно приятный сладкий аромат.")
        elif message.text == "Назад в меню":
            welcome(message)

        elif message.text == "Другие суккуленты":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item0 = types.KeyboardButton("Основы ухода за суккулентами")
            item1 = types.KeyboardButton("Алоэ")
            item2 = types.KeyboardButton("Агавы")
            item3 = types.KeyboardButton("Молочаи")
            item4 = types.KeyboardButton("Каланхоэ")
            item5 = types.KeyboardButton("Крассулы")
            item6 = types.KeyboardButton("Литопсы")
            item7 = types.KeyboardButton("Стапелии")
            item8 = types.KeyboardButton("Эониумы")
            item9 = types.KeyboardButton("Хавортии")
            item10 = types.KeyboardButton("Хойи")
            item11 = types.KeyboardButton("Назад в меню")
            markup.add(item0, item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11)

            bot.send_message(message.chat.id, "В группу суккулентов входят много родов. Выбери интересующий тебя род:", reply_markup=markup)

        elif message.text == "Основы ухода за суккулентами":
            bot.send_message(message.chat.id, "Ключевые факторы здорового роста и развития суккулентов это правильный грунт, "
                                              "достаточное количество света, сбалансированный полив и правильная зимовка."
                                              "\nГрунт должен быть бедным и рыхлым, что достигается путем добавления в землю"
                                              "минеральных разрыхлителей (крупнозернистый кварцевый песок, перлит, диатомит, мелкие камни,"
                                              "кирпичная крошка, мелкий керамзит), 50% земли и 50% разрыхлителей. "
                                              "\nРастения долны стоять на хорошо освещаемом месте, восточном, западном или южном окнах,"
                                              " на северном же им потребуется досветка."
                                              "\nПолив нужно проводить по мере просыхания грунта, не поливают только зимующие растения во время периода покоя."
                                              "\nЗимовку необходимо проводить для большинства суккулентов путем снижения температуры до 5 градусов, не ниже,"
                                              "в сухом месте, с октября по март, без полива."
                                              "\nВ зимовке не нуждаются!!! Стапелии, Орбеи, Гуэрнии и другие представители семейства Ластовневых.")
        elif message.text == "Алоэ":
            photo = open("C:/py.projects/venv/static/aloe.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Алоэ, один из самых простых в выращивании и уходе суккулентов, его родина - "
                                              "Африка и Аравийский полуостров")
        elif message.text == "Агавы":
            photo = open("C:/py.projects/venv/static/agave.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Агава - широко используемый в сельском хозяйстве суккулент, в домашней культуре медленно растущий.")
        elif message.text == "Молочаи":
            photo = open("C:/py.projects/venv/static/euph.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Самый большой род семейства Молочайные, включающий более 500 видов. Особенность молочаев или же"
                                              "эуфорбий - млечный сок, содержащийся в их листьях и стебле, он ядовит.")
        elif message.text == "Каланхоэ":
            photo = open("C:/py.projects/venv/static/kalanchoe.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Каланхоэ - простые в уходе растения, произрастающие в Африке и на Мадагаскаре.")
        elif message.text == "Крассулы":
            photo = open("C:/py.projects/venv/static/crass.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Самый популярный представитель рода Крассул - Крассула овата, известная всем как денежное дерево. "
                                              "Крассулы просты в уходе и разнообразны, насчитывается от 300 до 350 видов. ")
        elif message.text == "Литопсы":
            photo = open("C:/py.projects/venv/static/lit.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Литопсы или Живые камни, одни из самых известных представителей семейства Аизовых.")
        elif message.text == "Стапелии":
            photo = open("C:/py.projects/venv/static/stapelia.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Стапелии являются наиболее известными представителями семейства Ластовневые, "
                                              "их необычные цветы со специфическим запахом очень красивы, как и само растение.")
        elif message.text == "Эониумы":
            photo = open("C:/py.projects/venv/static/aeonium.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "К семейству Толстянковые относятся Эониумы, прекрасные растения с Канарских островов, из Мадейры и "
                                              "Восточной Африки. Они не сложны в уходе, но период активной вегетации у них приходится на осень, а период"
                                              "покоя на лето.")
        elif message.text == "Хавортии":
            photo = open("C:/py.projects/venv/static/haw.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Род карликовых суккулентных травянистых растений семейства Асфоделовые, Хавортии произрастают в ЮАР "
                                              "в засушливых местностях, предпочитая тенистые места или почти полностью скрываясь в почве,"
                                              "над поверхностью которой виднеются лишь так называемые 'Окошки', благодаря которым Хавортии"
                                              "и приобрели свою известность, в особенности Haworthia cooperi.")
        elif message.text == "Хойи":
            photo = open("C:/py.projects/venv/static/Hoya.jpg", "rb")
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "Травянистые суккуленты-лианы из Южной и Юго-Восточной Азии, неприхотливые и крайне разнообразные. "
                                              "Хойи хорошо растут в легком, но питательным грунте с добавлением коры и мха, им необходима подпорка, "
                                              "чтобы лиане было куда расти, в дикой природе Хойи в качестве опоры используют кустарники и деревья."
                                              "В домашней культуре Хойи разделяют на кустовые и ампельные, последние можно выращивать в подвесном"
                                              "кашпо (предпочтительно мелколистные) или заплетая на опору.")

        elif message.text == "Назад в меню":
            welcome(message)

        elif message.text == "Помощь в определении названия растения":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item0 = types.KeyboardButton("Загрузить фото")
            item1 = types.KeyboardButton("Определить название по описанию")
            item2 = types.KeyboardButton("Назад в меню")
            markup.add(item0, item1, item2)

            bot.send_message(message.chat.id, "Пожалуйста, загрузите фотографию растения или заполните анкету по его описанию", reply_markup=markup)

        elif message.text == "Загрузить фото":
            bot.send_message(message.chat.id, "...на стадии разработки...")

        elif message.text == "Определить название по описанию":
            one(message)

        elif message.text == "Назад в меню":
            welcome(message)

        else:
            bot.send_message(message.chat.id, "Я не понимаю тебя.")

bot.polling(none_stop=True)