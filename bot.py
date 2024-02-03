import json
import telebot
from telebot import types
import os
from datetime import datetime, date
bot = telebot.TeleBot('TOKEN')


current_dir = os.path.dirname(__file__)
#относительные пути для текстовых файлов
file_path_budget = os.path.join(current_dir, 'files', 'budget.png')
file_path_commercial = os.path.join(current_dir, 'files', 'commercial.png')
file_path_ege = os.path.join(current_dir, 'files', 'ege.txt')
file_path_vi1 = os.path.join(current_dir, 'files', 'vi1.txt')
file_path_vi2 = os.path.join(current_dir, 'files', 'vi2.txt')
file_path_to_log = os.path.join (current_dir, "log.log")
file_path_to_log1 = os.path.join (current_dir, "log.json")
file_path_to_log2 = os.path.join (current_dir, "startups.log")


now = datetime.now()
current_time = str(date.today()) + " " + now.strftime("%H:%M:%S")
text =  current_time+" : bot started"
with open(file_path_to_log2, "a",encoding="utf-8") as file:
    file.write("\n"+text)
bot.send_message(575078092, text)


@bot.message_handler(commands=['start']) #стартовая команда
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("ВО")
    btn2 = types.KeyboardButton('СПО')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Вас приветствует бот *Приёмной комиссии ЧИ БГУ*👋 \n\nУ меня вы можете узнать интересующую вас информацию о поступлении в наш институт. \n\n Выберите интересующий вас уровень образования с помощью клавиатуры⌨️\n(_квадратная кнопка на поле для ввода сообщений_)", reply_markup=markup, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    now = datetime.now()
    current_time = str(date.today()) + " " + now.strftime("%H:%M:%S")

    text =  current_time+" @" +message.from_user.username + " ("+str(message.from_user.id) +") : " +message.text
    json_log = {"time" : current_time, "username":message.from_user.username, "userid": message.from_user.id, "text":message.text }
    with open(file_path_to_log, "a",encoding="utf-8") as file:
        file.write("\n"+text)
    # with open(file_path_to_log1, "a",encoding="utf-8") as file:
    #     json.dump(json_log, file, ensure_ascii=False)
    #     file.write(', \n')
    bot.send_message(575078092, text)

    #ВО
    if message.text == 'ВО':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📚Направления подготовки")
        btn2 = types.KeyboardButton('📰Способы подачи документов')
        btn3 = types.KeyboardButton('✍️План приёма')
        btn4 = types.KeyboardButton('📊Мин. баллы ЕГЭ')
        btn5 = types.KeyboardButton('🔎ВИ')
        btn6 = types.KeyboardButton('💳 Стоимость обучения')
        btn7 = types.KeyboardButton('💻 Образцы документов')
        btn8 = types.KeyboardButton('📋 Списки абитуриентов')
        btn9 = types.KeyboardButton('📱 Контакты')
        btn10 = types.KeyboardButton('🔙 Вернуться к выбору уровня образования')
        btn11 = types.KeyboardButton('Связаться с тех.секретарём')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11)
        bot.send_message(message.from_user.id, "👋 ВО - программы Высшего образования", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел \n\nЕсли бот не сможет ответить на интересующие вас вопросы нажмите кнопку `Связаться с тех.секретарём` и мы ответим на все ваши вопросы!',reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🔙 Вернуться к выбору уровня образования':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("ВО")
        btn2 = types.KeyboardButton('СПО')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "✔️Выберите уровень образования", reply_markup=markup)



    elif message.text == '📚Направления подготовки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Юриспруденция')
        btn2 = types.KeyboardButton('ЭПиПД')
        btn3 = types.KeyboardButton('ВЭД')
        btn4 = types.KeyboardButton('ФК')
        btn5 = types.KeyboardButton('УП')
        btn6 = types.KeyboardButton('ГМУ')
        btn7 = types.KeyboardButton('ИСТУ')
        btn8 = types.KeyboardButton('ТоргДело')
        btn9 = types.KeyboardButton('ТаможДело')
        btn10 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        bot.send_message(message.from_user.id, '⬇ Выберите интересующее вас направление подготовки', reply_markup=markup)

    elif message.text == 'Юриспруденция':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Юриспруденция" в ВУЗах предназначено для обучения студентов основам права и юридической деятельности.'
                        'В ходе обучения студенты изучают такие дисциплины, как гражданское право, уголовное право, административное право, конституционное право и другие отрасли права. \n\nПодробнее об направлении подготовки "Юриспруденция" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/134-40-03-01-yurisprudentsiya)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ЭПиПД':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Экономика предприятия и предпринимательская деятельность" в ВУЗах предназначено для обучения студентов основам экономической науки, а также формирования навыков и знаний, необходимых для организации и управления предприятиями и ведения предпринимательской деятельности.'
                        '\n\nПодробнее об направлении подготовки "Экономика предприятия и предпринимательская деятельность" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/106-38-03-01-ekonomika-po-profilyu-ekonomika-predpriyatiya-i-predprinimatelskaya-deyatelnost)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ВЭД':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Внешнеэкономическая деятельность" в ВУЗах предназначено для обучения студентов основам международных экономических отношений и внешней торговли. Оно призвано развить у студентов навыки и знания, необходимые для работы в области международного бизнеса, внешнеэкономических отношений и торговли.'
                        '\n\nПодробнее об направлении подготовки "Внешнеэкономическая деятельность" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/90-38-03-01-ekonomika-po-profilyu-mirovaya-ekonomika)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ФК':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Финансы и кредит" в ВУЗах предназначено для обучения студентов основам финансовой науки, понятиям и принципам, связанным с финансовой системой и кредитной деятельностью. Оно направлено на развитие навыков и знаний, необходимых для работы в банковской сфере, финансовых учреждениях, финансовых отделах предприятий и организациях.'
                        '\n\nПодробнее об направлении подготовки "Финансы и кредит" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/111-38-03-01-ekonomika-po-profilyu-finansy-i-kredit)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'УП':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Управление персоналом" в ВУЗах предназначено для обучения студентов основам управления персоналом, развитию навыков и знаний, необходимых для эффективной работы с сотрудниками в организациях различного типа.'
                        '\n\nПодробнее об направлении подготовки "Управление персоналом" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/116-38-03-03-upravlenie-personalom)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ГМУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Государственное и муниципальное управление" в ВУЗах направлено на обучение студентов основам государственного аппарата и муниципального управления. Цель такого обучения - развитие навыков и знаний, необходимых для работы в государственных и муниципальных органах, а также в организациях, связанных с государственным и муниципальным сектором.'
                        '\n\nПодробнее об направлении подготовки "Государственное и муниципальное управление" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/120-38-03-04-gosudarstvennoe-i-munitsipalnoe-upravlenie)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ИСТУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Информационные системы и технологии в управлении" в ВУЗах предназначено для студентов, которые интересуются применением информационных технологий в сфере управления и бизнеса. Курс обучения включает изучение основных принципов информационных систем, разработку программного обеспечения, анализ данных, управление проектами, электронную коммерцию и другие смежные темы.'
                        '\n\nПодробнее об направлении подготовки "Информационные системы и технологии в управлении" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/104-09-03-03-prikladnaya-informatika-po-profilyu-informatsionnye-sistemy-i-tekhnologii-v-upravlenii)', reply_markup=markup, parse_mode='Markdown')
    
    elif message.text == 'ТоргДело':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Торговое дело" в ВУЗах предназначено для студентов, которые интересуются маркетингом, продажами и логистикой. Курс обучения включает изучение основных принципов работы по продвижению финансовых организаций, контрактной системы закупок и психологии потребителя.'
                        '\n\nПодробнее об направлении подготовки "Информационные системы и технологии в управлении" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/104-09-03-03-prikladnaya-informatika-po-profilyu-informatsionnye-sistemy-i-tekhnologii-v-upravlenii)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ТаможДело':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📚Направления подготовки')
        btn2 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "Таможенное дело" в ВУЗах предназначено для студентов, которые хотят в дальнейшем вести контроль за деятельностью участников внешнеэкономической деятельности. Обучение будет направлено на изучение регулирования внешнеторговой  деятельности, таможенного права, информационных технологий в этой сфере и логистики.'
                        '\n\nПодробнее об направлении подготовки "Информационные системы и технологии в управлении" можно прочитать по [ссылке](https://abit.bgu-chita.ru/abiturient/104-09-03-03-prikladnaya-informatika-po-profilyu-informatsionnye-sistemy-i-tekhnologii-v-upravlenii)', reply_markup=markup, parse_mode='Markdown')


    #общая кнопка для ВО и СПО
    elif message.text == 'Связаться с тех.секретарём':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        bot.send_message(message.from_user.id, 'Напишите свой вопрос техническому секретарю. Для того чтобы связаться с ним нажмите на ссылку - @chita_baikaluniversity\nЧасы работы: пн-пт:9:00-17:00,сб:9:00-13:00 ', reply_markup=markup )

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📚Направления подготовки")
        btn2 = types.KeyboardButton('📰Способы подачи документов')
        btn3 = types.KeyboardButton('✍️План приёма')
        btn4 = types.KeyboardButton('📊Мин. баллы ЕГЭ')
        btn5 = types.KeyboardButton('🔎ВИ')
        btn6 = types.KeyboardButton('💳 Стоимость обучения')
        btn7 = types.KeyboardButton('💻 Образцы документов')
        btn8 = types.KeyboardButton('📋 Списки абитуриентов')
        btn9 = types.KeyboardButton('📱 Контакты')
        btn10 = types.KeyboardButton('🔙 Вернуться к выбору уровня образования')
        btn11 = types.KeyboardButton('Связаться с тех.секретарём')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10,btn11)
        bot.send_message(message.from_user.id, "👋 ВО - программы Высшего образования", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел \n\nЕсли бот не сможет ответить на интересующие вас вопросы нажмите кнопку `Связаться с тех.секретарём` и мы ответим на все ваши вопросы!',reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📰Способы подачи документов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '*Способы подачи документов:*\n\
🚩Лично в приемную комиссию по адресу _г.Чита, ул.Анохина 56_\n\
🚩Через сайт онлайн-приёма ЧИ БГУ https://priem.bgu-chita.ru/\n\
🚩Через единый портал государственных услуг https://www.gosuslugi.ru/vuzonline\ ', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '✍️План приёма':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бюджет')
        btn2 = types.KeyboardButton('Коммерция')
        btn3 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.from_user.id, "Выберите источник финансирования", reply_markup=markup)
    elif message.text =='Бюджет':
        bot.send_photo(message.from_user.id, open(file_path_budget, 'rb'))
    elif message.text=='Коммерция':
        bot.send_photo(message.from_user.id, open(file_path_commercial, 'rb'))

    elif message.text == '📊Мин. баллы ЕГЭ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        with open(file_path_ege, 'r',encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.from_user.id,text=text, reply_markup=markup, parse_mode='Markdown')



    elif message.text == '🔎ВИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📃Перечень ВИ для всех направлений подготовки')
        btn2 = types.KeyboardButton('📧 Форма проведения ВИ')
        btn3 = types.KeyboardButton('📉Мин.баллы по ВИ')
        btn4 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.from_user.id, 'Выберите интересующую вас информацию по вступительным испытаниям ' , reply_markup=markup, parse_mode='Markdown')


    elif message.text == '📃Перечень ВИ для всех направлений подготовки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        with open(file_path_vi1, 'r',encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.from_user.id,text=text, reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📧 Форма проведения ВИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'У вступительных испытаний есть две формы проведения:очно и дистанционно. Заполняя заявление, вы должны отразить в каком формате вам будет удобнее пройти ВИ. Если вы поступаете на бюджет, вы можете сдавать их только очно.\n\
Очно вам нужно будет придти в установленную [расписанием ВИ](https://abit.bgu-chita.ru/priem/wpo/13-priem/43-examtime) очно в институт. При выборе дистанционной формы сдачи ВИ необходимо наличие камеры,т.к потребуется показать своё лицо и фотографию из документа подтвержающего личность и весь экзамен писать под камерой\n\
Допускается сдача нескольких вступительных испытаний в один день.' ,reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📉Мин.баллы по ВИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        with open(file_path_vi2, 'r',encoding='utf-8') as file:
            text = file.read()
        bot.send_message(message.from_user.id,text=text, reply_markup=markup, parse_mode='Markdown')


    elif message.text == '💳 Стоимость обучения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ознакомиться со стоимостью обучения вы можете на нашем [сайте](https://abit.bgu-chita.ru/stoimost)', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '💻 Образцы документов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ознакомиться с образцами документов и бланков вы можете на нашем [сайте](https://abit.bgu-chita.ru/index.php/priem/wpo/18-priem/40) ', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '📋 Списки абитуриентов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ознакомиться со списками абитуриентов вы можете по следующей [ссылке](https://abit.bgu-chita.ru/priem/wpo/13-priem/57-ablist).\nВыставите интересующий вас источник финансирования,организацию(ЧИ БГУ/Колледж),форму обучения и направление подготовки и нажмите кнопку *Показать*.\
                         \nНа сайте в таблице отразится перечень абитуриентов по заданным критериям.Абитуриенты отражаются по номеру *СНИЛС*", reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📱 Контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '*Контакты:*\nтел. (3022) 32-34-21\
        \nтел. 8-914-145-18-88(_Telegram,WhatsApp,Viber_)\n*e-mail*: `priem@bgu-chita.ru`\n*Мы в ВКонтакте*: https://vk.com/4itnarhoz\
        \n*Адрес*: г.Чита, ул. Анохина,56, каб. 70\n*Часы работы*:пн-пт:_9:00-17:00_,сб:_9:00-13:00_', reply_markup=markup, parse_mode='Markdown')



    #Small talk
    elif message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')

    elif message.text == 'как дела?' or message.text == "Как дела?":
        bot.send_message(message.from_user.id, 'Хорошо!')

    elif message.text == 'Что делаешь?' or message.text == 'что делаешь?':
        bot.send_message(message.from_user.id, 'Консультирую абитуриентов!')

    elif message.text == 'Здравствуйте' or message.text == 'здравствуйте':
        bot.send_message(message.from_user.id, 'Здравствуйте,уважаемый абитуриент')




    #СПО
    if message.text == 'СПО':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🗒️Специальности")
        btn2 = types.KeyboardButton('📰Подача документов')
        btn3 = types.KeyboardButton('📮План приёма')
        btn4 = types.KeyboardButton('💳 Стоимость обучения')
        btn5 = types.KeyboardButton('💻 Образцы документов')
        btn6 = types.KeyboardButton('📋 Списки абитуриентов')
        btn7 = types.KeyboardButton('☎️Контакты')
        btn8 = types.KeyboardButton('🔙 Вернуться к выбору уровня образования')
        btn9 = types.KeyboardButton('Связаться с тех.секретарём')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
        bot.send_message(message.from_user.id, "👋 СПО - программы среднего профессионального образования", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел \n\nЕсли бот не сможет ответить на интересующие вас вопросы нажмите кнопку `Связаться с тех.секретарём` и мы ответим на все ваши вопросы!',reply_markup=markup, parse_mode='Markdown')

    elif message.text == '🗒️Специальности':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('ПСО')
        btn2 = types.KeyboardButton('ДОУ')
        btn3 = types.KeyboardButton('БД')
        btn4 = types.KeyboardButton('ЭиБУ')
        btn5 = types.KeyboardButton('Коммерция(по отраслям)')
        btn6 = types.KeyboardButton('Товароведение')
        btn7 = types.KeyboardButton('ИСиП')
        btn8 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.from_user.id, '⬇ Выберите интересующую вас специальность', reply_markup=markup)


    elif message.text == 'ПСО':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "*Право и организация социального обеспечения*" в колледжах предназначено для студентов, которые заинтересованы в изучении правовых аспектов, связанных с организацией и управлением социальным обеспечением.\
                            \n\nПодробнее об направлении подготовки "*Право и организация социального обеспечения*" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-40-02-01-pravo-i-organizaciya-socialnogo-obespecheniya/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ДОУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "*Документационное обеспечение управления и архивоведение*" в колледжах предназначено для студентов, которые интересуются организацией и управлением документацией в организациях, а также изучением архивоведения.\
                            \n\nПодробнее об направлении подготовки "*Документационное обеспечение управления и архивоведение*" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-46-02-01-dokumentacionnoe-obespechenie-upravleniya-i-arkhivovedenie/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'БД':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки "*Банковское дело*" в колледжах предназначено для студентов, желающих приобрести профессиональные навыки и знания, необходимые для работы в сфере банковской деятельности. Курс обучения включает изучение основных принципов и функций банков, правовых аспектов финансовых операций, анализа финансовой деятельности, управления рисками и др.\
                         Студенты также ознакамливаются с практическими аспектами работы в банке, включая клиентское обслуживание, операции с денежными средствами и кредитование. После завершения обучения выпускники могут претендовать на работу в коммерческих банках, кредитных учреждениях, финансовых компаниях и других смежных секторах экономики.\
                            \n\nПодробнее об направлении подготовки "*Банковское дело*" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-38-02-07-bankovskoe-delo/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ЭиБУ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки в колледжах "*Экономика и бухгалтерский учет*" предназначено для студентов, желающих получить знания и навыки в области экономики, финансов, бухгалтерии и аналитики, необходимые для работы в сфере бизнеса и учета. Курс обучения включает изучение основных экономических теорий, методов бухгалтерии, анализа финансовой отчетности, налогообложения, управленческого учета и других финансово-экономических дисциплин.\
                          Студенты также осваивают принципы планирования, оценки и анализа экономической деятельности предприятий, а также нормативно-правовые аспекты бухгалтерии и налогообложения. После окончания обучения выпускники могут работать в финансовых и бухгалтерских службах компаний, аудиторских фирмах, банках, налоговых органах и в других сферах, связанных с финансово-экономической деятельностью.\
                            \n\nПодробнее об направлении подготовки "*Экономика и бухгалтерский учет *" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-38-02-01-ehkonomika-i-bukhgalterskijj-uchet/)', reply_markup=markup, parse_mode='Markdown')



    elif message.text == 'Коммерция(по отраслям)':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки в колледжах "*Коммерция*" предназначено для студентов, желающих получить знания и навыки в области коммерческой деятельности и бизнеса. Курсы обучения включают изучение основных принципов и методов ведения коммерческой деятельности, торговли, маркетинга, логистики, управления персоналом и других коммерческих дисциплин. Студенты также ознакамливаются с принципами организации и управления предприятиями, планированием продаж, международным бизнесом и договорными отношениями.\
                         В процессе обучения студенты получают практические навыки в области продаж, презентаций, управления проектами и командой, а также разрабатывают бизнес-планы и стратегии развития. После окончания обучения выпускники могут работать в коммерческих организациях, торговых сетях, розничной и оптовой торговле, маркетинговых и рекламных агентствах и в других сферах связанных с коммерцией.\
                            \n\nПодробнее об направлении подготовки "*Коммерция*" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-38-02-04-kommerciya-po-otraslyam/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'Товароведение':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки в колледжах "*Товароведение и экспертиза качества потребительских товаров*" предназначено для студентов, желающих приобрести знания и навыки в области исследования и оценки качества товаров, а также различных аспектов товароведения. Курс обучения включает изучение основных принципов товароведения, стандартов качества, методов оценки, контроля и сертификации товаров.\
                         Студенты также осваивают понятия и практики товарной экспертизы, которые включают анализ состава и свойств товаров, их безопасности, соответствия требованиям нормативных документов и стандартов. В процессе обучения студенты ознакамливаются с основами маркетинга, логистики, закупок и снабжения, а также изучают основы управления качеством товаров. После завершения обучения выпускники могут работать в сфере товароведения и экспертизы качества в компаниях, занимающихся производством, реализацией и контролем качества потребительских товаров, а также в органах по сертификации и стандартизации.\
                            \n\nПодробнее об направлении подготовки "*Товароведение и экспертиза качества потребительских товаров*" можно прочитать по [ссылке](https://college.bgu-chita.ru/specialnosti/specialnost-38-02-05-tovarovedenie-i-ehkspertiza-kachestva-potrebitelskikh-tovarov/)', reply_markup=markup, parse_mode='Markdown')

    elif message.text == 'ИСиП':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🗒️Специальности')
        btn2 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2)
        bot.send_message(message.from_user.id, 'Направление подготовки в колледжах "*Информационные системы и программирование*" предназначено для студентов, желающих получить глубокие знания и навыки в области информационных технологий, программирования и разработки программного обеспечения. Курс обучения включает изучение основных языков программирования, структур данных, алгоритмов, баз данных, компьютерных сетей и других компьютерно-технических дисциплин.', reply_markup=markup, parse_mode='Markdown')




    elif message.text == '📰Подача документов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '*Способы подачи документов:*\n\
🚩Лично в приемную комиссию по адресу _г.Чита, ул.Анохина 56_\n\
🚩Через сайт онлайн-приёма ЧИ БГУ https://priem.bgu-chita.ru/', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '📮План приёма':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Бюджетный')
        btn2 = types.KeyboardButton('Коммерческий')
        btn3 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.from_user.id, "Выберите источник финансирования", reply_markup=markup)

    elif message.text =='Бюджетный':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Бюджетный набор в этом году на программы СПО не запланирован ' , reply_markup=markup)
    elif message.text=='Коммерческий':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.from_user.id, 'Ограничений по количеству заявлений на коммерческую основу нет. Вам требуется подать заявление, заключить договор и оплатить 10% суммы в установленный срок для того чтобы быть зачисленными.' , reply_markup=markup)

    elif message.text == '💸 Стоимость обучения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ознакомиться со стоимостью обучения вы можете на нашем [сайте](https://abit.bgu-chita.ru/stoimost)', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '🗃️ Образцы документов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Ознакомиться с образцами документов и бланков вы можете на нашем [сайте](https://abit.bgu-chita.ru/index.php/priem/wpo/18-priem/40) ', reply_markup=markup, parse_mode='Markdown')


    elif message.text == '📝 Списки абитуриентов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Ознакомиться со списками абитуриентов вы можете по следующей [ссылке](https://abit.bgu-chita.ru/priem/wpo/13-priem/57-ablist).\nВыставите интересующий вас источник финансирования,организацию(ЧИ БГУ/Колледж),форму обучения и направление подготовки и нажмите кнопку *Показать*.\
                         \nНа сайте в таблице отразится перечень абитуриентов по заданным критериям.Абитуриенты отражаются по номеру *СНИЛС*", reply_markup=markup, parse_mode='Markdown')

    elif message.text == '☎️Контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('⏪ Главное меню')
        markup.add(btn1)
        bot.send_message(message.from_user.id, '*Контакты:*\nтел. (3022) 32-34-21\
        \nтел. 8-914-145-18-88(_Telegram,WhatsApp,Viber_)\n*e-mail*: `priem@bgu-chita.ru`\n*Мы в ВКонтакте*: https://vk.com/4itnarhoz\
        \n*Адрес*: г.Чита, ул. Анохина,56, каб. 70\n*Часы работы*:пн-пт:_9:00-17:00_,сб:_9:00-13:00_', reply_markup=markup, parse_mode='Markdown')

    elif message.text == '⏪ Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("🗒️Специальности")
        btn2 = types.KeyboardButton('📰Подача документов')
        btn3 = types.KeyboardButton('📮План приёма')
        btn4 = types.KeyboardButton('💸 Стоимость обучения')
        btn5 = types.KeyboardButton('🗃️ Образцы документов')
        btn6 = types.KeyboardButton('📝 Списки абитуриентов')
        btn7 = types.KeyboardButton('☎️Контакты')
        btn8 = types.KeyboardButton('🔙 Вернуться к выбору уровня образования')
        btn9 = types.KeyboardButton('Связаться с тех.секретарём')
        markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
        bot.send_message(message.from_user.id, "👋 СПО - программы среднего профессионального образования", reply_markup=markup)
        bot.send_message(message.from_user.id, '👀 Выберите интересующий вас раздел \n\nЕсли бот не сможет ответить на интересующие вас вопросы нажмите кнопку `Связаться с тех.секретарём` и мы ответим на все ваши вопросы!',reply_markup=markup, parse_mode='Markdown')




bot.polling(none_stop=True, interval=0)
