import streamlit as st
import random

# ------------------- БАЗА ЗАДАЧ -------------------
problems = [
    # Первые 10 (оставляем)
    {"text": "В одной коробке 6 карандашей. Сколько карандашей в 4 таких коробках?", "answer": 24},
    {"text": "На одной ветке 5 яблок. Сколько яблок на 3 таких ветках?", "answer": 15},
    {"text": "В каждой вазе 7 конфет. Сколько конфет в 5 вазах?", "answer": 35},
    {"text": "У кошки 4 лапы. Сколько лап у 6 кошек?", "answer": 24},
    {"text": "В одном пакете 2 килограмма муки. Сколько килограммов в 8 таких пакетах?", "answer": 16},
    {"text": "Каждая девочка посадила 3 цветка. Сколько цветов посадили 9 девочек?", "answer": 27},
    {"text": "В одной книге 8 страниц. Сколько страниц в 5 таких книгах?", "answer": 40},
    {"text": "У каждого мальчика 10 наклеек. Сколько наклеек у 7 мальчиков?", "answer": 70},
    {"text": "В одном ряду 9 стульев. Сколько стульев в 4 рядах?", "answer": 36},
    {"text": "Один стул стоит 3 рубля. Сколько стоят 6 таких стульев?", "answer": 18},
    {"text": "В одной пачке 8 мелков. Сколько мелков в 3 таких пачках?", "answer": 24},
    {"text": "На одной тарелке 4 пирожка. Сколько пирожков на 5 таких тарелках?", "answer": 20},
    {"text": "У каждого щенка 5 мячей. Сколько мячей у 4 щенков?", "answer": 20},
    {"text": "В одном наборе 6 фломастеров. Сколько фломастеров в 3 наборах?", "answer": 18},
    {"text": "В каждой упаковке 9 йогуртов. Сколько йогуртов в 2 упаковках?", "answer": 18},
    {"text": "На одной клумбе 7 тюльпанов. Сколько тюльпанов на 3 клумбах?", "answer": 21},
    {"text": "В одном гараже 5 машин. Сколько машин в 4 таких гаражах?", "answer": 20},
    {"text": "У каждого кролика 4 морковки. Сколько морковок у 8 кроликов?", "answer": 32},
    {"text": "В одной корзине 8 грибов. Сколько грибов в 6 корзинах?", "answer": 48},
    {"text": "На одной полке 10 книг. Сколько книг на 3 полках?", "answer": 30},
    {"text": "В одном классе 7 парт. Сколько парт в 4 классах?", "answer": 28},
    {"text": "У каждого медведя 5 банок мёда. Сколько банок у 3 медведей?", "answer": 15},
    {"text": "В одном ящике 6 апельсинов. Сколько апельсинов в 5 ящиках?", "answer": 30},
    {"text": "Каждый день турист проходит 9 километров. Сколько километров он пройдёт за 3 дня?", "answer": 27},
    {"text": "В одном аквариуме 4 рыбки. Сколько рыбок в 7 аквариумах?", "answer": 28},
    {"text": "На одной странице 8 марок. Сколько марок на 5 страницах?", "answer": 40},
    {"text": "У одной курицы 2 ноги. Сколько ног у 9 кур?", "answer": 18},
    {"text": "В одной коробке 3 конфеты. Сколько конфет в 10 коробках?", "answer": 30},
    {"text": "Одна тарелка стоит 7 рублей. Сколько стоят 4 такие тарелки?", "answer": 28},
    {"text": "В одной вазе 5 роз. Сколько роз в 6 вазах?", "answer": 30},
    {"text": "На одном дереве 8 ворон. Сколько ворон на 4 деревьях?", "answer": 32},
    {"text": "В одном пенале 3 ручки. Сколько ручек в 7 пеналах?", "answer": 21},
    {"text": "У каждого паука 8 ног. Сколько ног у 3 пауков?", "answer": 24},
    {"text": "В одной упаковке 10 тетрадей. Сколько тетрадей в 5 упаковках?", "answer": 50},
    {"text": "На одной грядке 6 кустов клубники. Сколько кустов на 4 грядках?", "answer": 24},
    {"text": "В одном автобусе 9 пассажиров. Сколько пассажиров в 2 таких автобусах?", "answer": 18},
    {"text": "У одной бабушки 7 котят. Сколько котят у 3 бабушек?", "answer": 21},
    {"text": "В одном наборе 5 карандашей. Сколько карандашей в 8 наборах?", "answer": 40},
    {"text": "На одной тарелке 2 бутерброда. Сколько бутербродов на 6 тарелках?", "answer": 12},
    {"text": "У каждого мальчика 3 шарика. Сколько шариков у 5 мальчиков?", "answer": 15},
    {"text": "В одной коробке 4 катушки ниток. Сколько катушек в 6 коробках?", "answer": 24},
    {"text": "В одном пакете 8 яблок. Сколько яблок в 3 пакетах?", "answer": 24},
    {"text": "Каждый день ученик решает 7 примеров. Сколько примеров он решит за 4 дня?", "answer": 28},
    {"text": "В одном часе 60 минут. Сколько минут в 3 часах?", "answer": 180},
    {"text": "Один килограмм конфет стоит 9 рублей. Сколько стоят 4 килограмма?", "answer": 36},
    {"text": "На одной парте 2 учебника. Сколько учебников на 9 партах?", "answer": 18},
    {"text": "В одном дворе 5 качелей. Сколько качелей в 4 дворах?", "answer": 20},
    {"text": "У одного осьминога 8 щупалец. Сколько щупалец у 6 осьминогов?", "answer": 48},
    {"text": "В одном ведре 6 литров воды. Сколько литров в 3 вёдрах?", "answer": 18},
    {"text": "На одной ветке 4 синицы. Сколько синиц на 5 ветках?", "answer": 20},
    {"text": "В одной упаковке 10 шоколадок. Сколько шоколадок в 7 упаковках?", "answer": 70},
    {"text": "У каждого робота 2 колеса. Сколько колёс у 8 роботов?", "answer": 16},
    {"text": "В одной сумке 3 альбома. Сколько альбомов в 6 сумках?", "answer": 18},
    {"text": "На одной улице 9 домов. Сколько домов на 3 улицах?", "answer": 27},
    {"text": "В одной клетке 5 кроликов. Сколько кроликов в 4 клетках?", "answer": 20},
    {"text": "Один билет в кино стоит 8 рублей. Сколько стоят 5 билетов?", "answer": 40},
    {"text": "В одном аквариуме 7 улиток. Сколько улиток в 3 аквариумах?", "answer": 21},
    {"text": "На одной полке 6 машинок. Сколько машинок на 4 полках?", "answer": 24},
    {"text": "У каждого человека 2 руки. Сколько рук у 10 человек?", "answer": 20},
    {"text": "В одном пакете 4 груши. Сколько груш в 7 пакетах?", "answer": 28},
    {"text": "В одной упаковке 9 батареек. Сколько батареек в 2 упаковках?", "answer": 18},
    {"text": "На одной тарелке 5 пирожных. Сколько пирожных на 8 тарелках?", "answer": 40},
    {"text": "В одной связке 6 воздушных шаров. Сколько шаров в 4 связках?", "answer": 24},
    {"text": "У каждой лошади 4 ноги. Сколько ног у 7 лошадей?", "answer": 28},
    {"text": "В одном наборе 10 наклеек. Сколько наклеек в 6 наборах?", "answer": 60},
    {"text": "На одной скамейке 3 человека. Сколько человек на 5 скамейках?", "answer": 15},
    {"text": "В одной банке 2 литра сока. Сколько литров в 9 банках?", "answer": 18},
    {"text": "У каждого велосипеда 2 колеса. Сколько колёс у 7 велосипедов?", "answer": 14},
    {"text": "В одном ряду 8 столов. Сколько столов в 4 рядах?", "answer": 32},
    {"text": "На одной полке 5 кукол. Сколько кукол на 9 полках?", "answer": 45},
]
def get_praise(name):
    praises = [
        f"🎉 Отлично, {name}! Ты просто гений умножения!",
        f"✨ Вау, {name}! Правильно! Молодец!",
        f"🌟 Супер, {name}! Так держать!",
        f"💪 Умница, {name}! Таблица умножения тебе покоряется!",
        f"🏆 Великолепно, {name}! Ты справляешься на отлично!",
        f"🎈 Правильно, {name}! Продолжай в том же духе!",
        f"🍭 Сладкая победа, {name}! Верно!",
        f"🚀 Космический результат, {name}!"
    ]
    return random.choice(praises)

def get_hint(a, b):
    return f"💡 Подсказка: {a} × {b} = {a} + {a} + ... ({b} раз) = {a * b}"

def check_diploma():
    if "last_diploma_count" not in st.session_state:
        st.session_state.last_diploma_count = 0
    expected = st.session_state.total_correct // 10
    if expected > st.session_state.last_diploma_count:
        for _ in range(expected - st.session_state.last_diploma_count):
            st.session_state.diplomas += 1
            st.balloons()
            st.success(f"🎓 ДИПЛОМ #{st.session_state.diplomas}! 🎓")
            st.markdown(f"### Поздравляем, {st.session_state.name}! Ты получил диплом за 10 правильных ответов!")
            st.markdown("---")
        st.session_state.last_diploma_count = expected

# Инициализация состояния
if "name" not in st.session_state:
    st.session_state.name = ""
if "page" not in st.session_state:
    st.session_state.page = "welcome"
if "table" not in st.session_state:
    st.session_state.table = 2
if "test_questions" not in st.session_state:
    st.session_state.test_questions = []
if "test_index" not in st.session_state:
    st.session_state.test_index = 0
if "test_score" not in st.session_state:
    st.session_state.test_score = 0
if "total_correct" not in st.session_state:
    st.session_state.total_correct = 0
if "diplomas" not in st.session_state:
    st.session_state.diplomas = 0
if "last_diploma_count" not in st.session_state:
    st.session_state.last_diploma_count = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "problems_remaining" not in st.session_state:
    st.session_state.problems_remaining = []
if "current_problem" not in st.session_state:
    st.session_state.current_problem = None

def reset_test():
    st.session_state.test_index = 0
    st.session_state.test_score = 0
    st.session_state.feedback = ""
    generate_test_questions()

def generate_test_questions():
    table = st.session_state.table
    questions = []
    for i in range(1, 11):
        questions.append((table, i))
    random.shuffle(questions)
    st.session_state.test_questions = questions

def generate_problem():
    if not st.session_state.problems_remaining:
        st.session_state.problems_remaining = problems.copy()
        random.shuffle(st.session_state.problems_remaining)
    problem = st.session_state.problems_remaining.pop()
    st.session_state.current_problem = problem

# ------------------- СТРАНИЦЫ -------------------
def welcome_page():
    st.set_page_config(page_title="Учим таблицу умножения", page_icon="🧸", layout="centered", initial_sidebar_state="collapsed")
    st.title("📚 Добро пожаловать в школу умножения!")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # ЗДЕСЬ КАРТИНКА — заменена на нужную
        st.image("https://avatars.mds.yandex.net/i?id=2648a0f1b0c2a75695ec3c114bedea26_l-6959671-images-thumbs&n=13", width=150)
        st.markdown("### 👩‍🏫 Здравствуй, маленький ученик!")
        st.markdown("Я твоя учительница, София. Я помогу тебе выучить таблицу умножения.")
        st.markdown("Для начала давай познакомимся. Как тебя зовут?")
        name_input = st.text_input("Твоё имя:", key="name_input")
        if st.button("Начать учиться", type="primary"):
            if name_input.strip():
                st.session_state.name = name_input.strip()
                st.session_state.page = "menu"
                st.rerun()
            else:
                st.warning("Пожалуйста, напиши своё имя!")

def menu_page():
    st.title(f"🎒 Привет, {st.session_state.name}!")
    st.markdown("### Чем хочешь заняться?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("📖 Учить таблицу", use_container_width=True):
            st.session_state.page = "learn"
            st.rerun()
    with col2:
        if st.button("✍️ Проверять знания", use_container_width=True):
            generate_test_questions()
            st.session_state.page = "test"
            st.rerun()
    with col3:
        if st.button("📖 Решаем задачи", use_container_width=True):
            generate_problem()
            st.session_state.page = "problems"
            st.rerun()

    st.markdown("---")
    st.markdown(f"🏆 **Твои достижения:** {st.session_state.diplomas} дипломов")
    st.markdown(f"✅ **Всего правильных ответов:** {st.session_state.total_correct}")

def learn_page():
    st.title(f"📖 Учим таблицу умножения")
    st.markdown("### Выбери, какую таблицу хочешь повторить")
    table_choice = st.selectbox(
        "Таблица умножения на:",
        list(range(1, 11)),
        index=st.session_state.table - 1
    )
    if table_choice != st.session_state.table:
        st.session_state.table = table_choice
        st.rerun()

    st.markdown(f"### Таблица умножения на {st.session_state.table}")
    cols = st.columns(5)
    for i in range(1, 11):
        col = cols[(i-1) % 5]
        with col:
            st.info(f"{st.session_state.table} × {i} = {st.session_state.table * i}")

    if st.button("◀️ Вернуться в меню"):
        st.session_state.page = "menu"
        st.rerun()

def test_page():
    st.title(f"✍️ Проверка знаний, {st.session_state.name}!")
    table_choice = st.selectbox(
        "Какую таблицу проверяем?",
        list(range(1, 11)),
        index=st.session_state.table - 1,
        key="test_table_select"
    )
    if table_choice != st.session_state.table:
        st.session_state.table = table_choice
        generate_test_questions()
        st.rerun()

    if not st.session_state.test_questions:
        generate_test_questions()

    if st.session_state.test_index >= len(st.session_state.test_questions):
        st.success("🎉 Ты ответил на все вопросы! Молодец!")
        if st.button("Вернуться в меню"):
            st.session_state.page = "menu"
            st.rerun()
        return

    a, b = st.session_state.test_questions[st.session_state.test_index]
    st.markdown(f"### Вопрос {st.session_state.test_index + 1} из {len(st.session_state.test_questions)}")
    st.markdown(f"#### {a} × {b} = ?")

    user_answer = st.text_input("Твой ответ:", key=f"test_input_{st.session_state.test_index}")
    if st.button("Проверить", type="primary"):
        if user_answer.strip() == "":
            st.session_state.feedback = "❌ Введи число!"
        else:
            try:
                ans = int(user_answer)
                correct = a * b
                if ans == correct:
                    st.session_state.total_correct += 1
                    check_diploma()
                    praise = get_praise(st.session_state.name)
                    st.session_state.feedback = f"✅ {praise}"
                    st.session_state.test_index += 1
                else:
                    st.session_state.feedback = f"❌ Неверно! Правильный ответ: {correct}. {get_hint(a, b)}"
            except ValueError:
                st.session_state.feedback = "❌ Введи целое число!"
        st.rerun()

    if st.session_state.feedback:
        st.markdown(st.session_state.feedback)

    if st.button("◀️ Выйти в меню"):
        st.session_state.test_index = 0
        st.session_state.test_score = 0
        st.session_state.feedback = ""
        st.session_state.page = "menu"
        st.rerun()

def problems_page():
    st.title(f"📖 Решаем задачи, {st.session_state.name}!")
    if st.session_state.current_problem is None:
        generate_problem()

    problem = st.session_state.current_problem
    if problem is None:
        st.success("🎉 Ты решил все задачи! Молодец!")
        if st.button("Вернуться в меню"):
            st.session_state.page = "menu"
            st.rerun()
        return

    st.markdown(f"**{problem['text']}**")
    user_answer = st.text_input("Твой ответ:", key="problem_input")
    if st.button("Проверить", type="primary"):
        if user_answer.strip() == "":
            st.session_state.feedback = "❌ Введи число!"
        else:
            try:
                ans = int(user_answer)
                if ans == problem["answer"]:
                    st.session_state.total_correct += 1
                    check_diploma()
                    praise = get_praise(st.session_state.name)
                    st.session_state.feedback = f"✅ {praise}"
                    generate_problem()
                else:
                    st.session_state.feedback = f"❌ Неверно! Правильный ответ: {problem['answer']}."
            except ValueError:
                st.session_state.feedback = "❌ Введи целое число!"
        st.rerun()

    if st.session_state.feedback:
        st.markdown(st.session_state.feedback)

    if st.button("◀️ Выйти в меню"):
        st.session_state.page = "menu"
        st.rerun()

def main():
    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "menu":
        menu_page()
    elif st.session_state.page == "learn":
        learn_page()
    elif st.session_state.page == "test":
        test_page()
    elif st.session_state.page == "problems":
        problems_page()

if __name__ == "__main__":
    main()
