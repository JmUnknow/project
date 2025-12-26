import telebot
from telebot import types

TOKEN = '8599434324:AAEAXifSsWzxT2uk1p4gTVKUWCwfhpxL1t8'
bot = telebot.TeleBot(TOKEN)

jobs_db = {
    "IT & Разработка": [
        {"name": "Frontend-разработчик", "desc": "Создает внешнюю часть сайтов, которую мы видим."},
        {"name": "Backend-разработчик", "desc": "Отвечает за серверную логику и базы данных."},
        {"name": "Data Scientist", "desc": "Анализирует огромные массивы данных через нейросети."},
        {"name": "DevOps-инженер", "desc": "Настраивает автоматизацию и серверную инфраструктуру."},
        {"name": "Разработчик игр (Gamedev)", "desc": "Создает миры и механику видеоигр."}
    ],
    "Дизайн": [
        {"name": "UX/UI Дизайнер", "desc": "Делает интерфейсы приложений удобными и красивыми."},
        {"name": "Моушн-дизайнер", "desc": "Создает анимационную графику и видео-эффекты."},
        {"name": "3D-художник", "desc": "Рисует объемные модели для игр и кино."},
        {"name": "Иллюстратор", "desc": "Создает уникальные рисунки для книг и брендов."},
        {"name": "Архитектор интерьеров", "desc": "Планирует пространство жилых и рабочих помещений."}
    ],
    "Маркетинг": [
        {"name": "Интернет-маркетолог", "desc": "Продвигает товары и услуги в сети."},
        {"name": "Таргетолог", "desc": "Настраивает точечную рекламу в соцсетях."},
        {"name": "SEO-специалист", "desc": "Поднимает сайты в топ поисковой выдачи."},
        {"name": "Контент-стратег", "desc": "Планирует, какой контент принесет больше пользы бизнесу."},
        {"name": "PR-менеджер", "desc": "Управляет репутацией бренда в медиа."}
    ],
    "Финансы & Аналитика": [
        {"name": "Финансовый аналитик", "desc": "Прогнозирует доходы и расходы компании."},
        {"name": "Инвестиционный брокер", "desc": "Помогает выгодно вкладывать деньги в акции."},
        {"name": "Риск-менеджер", "desc": "Просчитывает возможные потери в бизнесе."},
        {"name": "Бухгалтер на аутсорсе", "desc": "Ведет учет нескольких компаний удаленно."},
        {"name": "Налоговый консультант", "desc": "Поможет легально оптимизировать налоги."}
    ],
    "Образование": [
        {"name": "Методолог обучения", "desc": "Проектирует структуру образовательных программ."},
        {"name": "EdTech-продюсер", "desc": "Запускает и развивает онлайн-школы."},
        {"name": "Корпоративный тренер", "desc": "Обучает сотрудников внутри больших компаний."},
        {"name": "Тьютор", "desc": "Персональный наставник в обучении."},
        {"name": "Разработчик онлайн-курсов", "desc": "Создает техническую начинку для обучения."}
    ],
    "Медицина & BioTech": [
        {"name": "Генетический консультант", "desc": "Анализирует ДНК на риски заболеваний."},
        {"name": "Телемедицинский врач", "desc": "Консультирует пациентов дистанционно."},
        {"name": "Биофармаколог", "desc": "Создает новые лекарства на основе биологии."},
        {"name": "Психолог-коуч", "desc": "Помогает достигать целей и ментального здоровья."},
        {"name": "Специалист по долголетию", "desc": "Разрабатывает программы продления жизни."}
    ],
    "Техника & Роботы": [
        {"name": "Инженер БПЛА", "desc": "Проектирует и собирает беспилотники."},
        {"name": "Робототехник", "desc": "Создает автоматизированные системы для заводов."},
        {"name": "Инженер умных домов", "desc": "Проектирует системы автоматизации жилья."},
        {"name": "Оператор 3D-печати", "desc": "Занимается аддитивным производством деталей."},
        {"name": "Специалист по кибербезопасности", "desc": "Защищает системы от взломов."}
    ],
    "Медиа & Контент": [
        {"name": "Продюсер подкастов", "desc": "Организует запись и продвижение аудио-шоу."},
        {"name": "Сценарист видео", "desc": "Пишет сюжеты для YouTube и TikTok."},
        {"name": "Стример / Блогер", "desc": "Создает личный бренд через прямые эфиры."},
        {"name": "Звукорежиссер", "desc": "Работает над чистотой и качеством звука."},
        {"name": "Редактор спецпроектов", "desc": "Создает крупные медиа-истории."}
    ],
    "Управление": [
        {"name": "Product Manager", "desc": "Отвечает за успех и развитие конкретного продукта."},
        {"name": "HR-директор", "desc": "Управляет развитием человеческого капитала."},
        {"name": "Team Lead", "desc": "Руководит командой разработчиков или спецов."},
        {"name": "Операционный директор", "desc": "Налаживает внутренние процессы в фирме."},
        {"name": "Менеджер по инновациям", "desc": "Внедряет новые технологии в бизнес."}
    ],
    "Сервис & Туризм": [
        {"name": "Travel-дизайнер", "desc": "Составляет уникальные авторские маршруты."},
        {"name": "Менеджер эко-отеля", "desc": "Управляет отдыхом в стиле эко-френдли."},
        {"name": "Консьерж-сервис", "desc": "Решает любые запросы VIP-клиентов."},
        {"name": "Гид по необычным местам", "desc": "Проводит экскурсии там, где не ходят толпы."},
        {"name": "Организатор бизнес-событий", "desc": "Делает форумы и конференции под ключ."}
    ]
}

cat_list = list(jobs_db.keys())

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Подобрать профессию")
    btn2 = types.KeyboardButton("О проекте")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Привет! Я твой гид по профессиям. Жми кнопку!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "О проекте")
def about(message):
    text = ("Этот бот — твой личный карьерный гид! 🧭 Он умеет фильтровать 50 востребованных профессий "
            "по 10 направлениям, выдавать описания задач и подсказывать путь развития. "
            "Всё просто и без лишней воды")
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Подобрать профессию")
def categories(message):
    markup = types.InlineKeyboardMarkup()
    for i, cat in enumerate(cat_list):
        # Передаем индекс категории i вместо названия
        markup.add(types.InlineKeyboardButton(text=cat, callback_data=f"c_{i}"))
    bot.send_message(message.chat.id, "Выбери сферу:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('c_'))
def show_jobs(call):
    cat_idx = int(call.data.split('_')[1])
    category = cat_list[cat_idx]
    jobs = jobs_db[category]
    
    markup = types.InlineKeyboardMarkup()
    for j_idx, job in enumerate(jobs):
        # Передаем индекс категории и индекс профессии
        markup.add(types.InlineKeyboardButton(text=job['name'], callback_data=f"j_{cat_idx}_{j_idx}"))
    
    markup.add(types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back"))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                          text=f"Профессии в сфере {category}:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('j_'))
def show_details(call):
    _, c_idx, j_idx = call.data.split('_')
    job = jobs_db[cat_list[int(c_idx)]][int(j_idx)]
    
    text = f"✅ *{job['name']}*\n\n{job['desc']}"
    bot.send_message(call.message.chat.id, text, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_btn(call):
    categories(call.message)

if __name__ == "__main__":
    print("123")
    bot.polling(none_stop=True)
