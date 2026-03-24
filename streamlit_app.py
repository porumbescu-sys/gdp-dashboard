import streamlit as st
import random

# ------------------- БАЗА ЗАДАЧ -------------------
problems = [
    {"text": "В одной коробке 6 карандашей. Сколько карандашей в 4 таких коробках?", "answer": 24},
    {"text": "На одной ветке 5 яблок. Сколько яблок на 3 таких ветках?", "answer": 15},
    {"text": "В каждой вазе 7 конфет. Сколько конфет в 5 вазах?", "answer": 35},
    {"text": "У кошки 4 лапы. Сколько лап у 6 кошек?", "answer": 24},
    {"text": "В одном пакете 2 килограмма муки. Сколько килограммов в 8 таких пакетах?", "answer": 16},
    {"text": "Каждая девочка посадила 3 цветка. Сколько цветов посадили 9 девочек?", "answer": 27},
    {"text": "В одной книге 8 страниц. Сколько страниц в 5 таких книгах?", "answer": 40},
    {"text": "У каждого мальчика 10 наклеек. Сколько наклеек у 7 мальчиков?", "answer": 70},
    {"text": "В одном ряду 9 стульев. Сколько стульев в 4 рядах?", "answer": 36},
    {"text": "Один стул стоит 3 рубля. Сколько стоят 6 таких стульев?", "answer": 18}
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
