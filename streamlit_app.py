import streamlit as st
import random

# ------------------- ИНИЦИАЛИЗАЦИЯ СОСТОЯНИЯ -------------------
if "name" not in st.session_state:
    st.session_state.name = ""
if "page" not in st.session_state:
    st.session_state.page = "welcome"  # welcome, menu, learn, test
if "table" not in st.session_state:
    st.session_state.table = 2          # текущая выбранная таблица (для обучения/проверки)
if "test_questions" not in st.session_state:
    st.session_state.test_questions = []   # список вопросов для проверки (для выбранной таблицы)
if "test_index" not in st.session_state:
    st.session_state.test_index = 0
if "test_score" not in st.session_state:
    st.session_state.test_score = 0       # правильные ответы за текущую сессию проверки
if "total_correct" not in st.session_state:
    st.session_state.total_correct = 0    # общее количество правильных ответов за всё время (для дипломов)
if "diplomas" not in st.session_state:
    st.session_state.diplomas = 0         # количество полученных дипломов
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "user_answer" not in st.session_state:
    st.session_state.user_answer = ""     # временное хранение ответа

# ------------------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ -------------------
def get_praise(name, correct=True):
    """Возвращает случайную похвалу с именем"""
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
    """Возвращает подсказку для примера a×b"""
    return f"💡 Подсказка: {a} × {b} = {a} + {a} + ... ({b} раз) = {a*b}"

def show_diploma():
    """Показывает диплом и увеличивает счётчик"""
    st.session_state.diplomas += 1
    st.balloons()
    st.success(f"🎓 ДИПЛОМ #{st.session_state.diplomas}! 🎓")
    st.markdown(f"### Поздравляем, {st.session_state.name}! Ты получил диплом за 10 правильных ответов!")
    st.markdown("---")

def reset_test():
    """Сбрасывает состояние теста"""
    st.session_state.test_index = 0
    st.session_state.test_score = 0
    st.session_state.feedback = ""
    # Генерируем новые вопросы для выбранной таблицы
    generate_test_questions()

def generate_test_questions():
    """Генерирует список вопросов для таблицы (1×число до 10×число)"""
    table = st.session_state.table
    questions = []
    # Все примеры от 1 до 10 (можно ограничить, но для маленьких детей можно оставить 1-5, но выбранная таблица уже от 1 до 5)
    for i in range(1, 11):
        questions.append((table, i))
    random.shuffle(questions)
    st.session_state.test_questions = questions

# ------------------- СТРАНИЦЫ -------------------
def welcome_page():
    st.set_page_config(page_title="Учим таблицу умножения", page_icon="🧸")
    st.title("📚 Добро пожаловать в школу умножения!")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/1995/1995571.png", width=150)
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
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📖 Учить таблицу", use_container_width=True):
            st.session_state.page = "learn"
            st.rerun()
    with col2:
        if st.button("✍️ Проверять знания", use_container_width=True):
            # Подготовим вопросы для проверки
            generate_test_questions()
            st.session_state.page = "test"
            st.rerun()
    
    st.markdown("---")
    st.markdown(f"🏆 **Твои достижения:** {st.session_state.diplomas} дипломов")
    st.markdown(f"✅ **Всего правильных ответов:** {st.session_state.total_correct}")

def learn_page():
    st.title(f"📖 Учим таблицу умножения на {st.session_state.table}")
    st.markdown(f"### Выбери, какую таблицу хочешь повторить")
    
    # Выбор таблицы
    table_choice = st.selectbox(
        "Таблица умножения на:",
        [1, 2, 3, 4, 5],
        index=[1,2,3,4,5].index(st.session_state.table) if st.session_state.table in [1,2,3,4,5] else 1
    )
    if table_choice != st.session_state.table:
        st.session_state.table = table_choice
        st.rerun()
    
    # Показываем таблицу
    st.markdown(f"### Таблица умножения на {st.session_state.table}")
    cols = st.columns(5)
    for i in range(1, 11):
        col = cols[(i-1) % 5]
        with col:
            st.info(f"{st.session_state.table} × {i} = {st.session_state.table * i}")
    
    # Кнопка "Назад"
    if st.button("◀️ Вернуться в меню"):
        st.session_state.page = "menu"
        st.rerun()

def test_page():
    st.title(f"✍️ Проверка знаний, {st.session_state.name}!")
    
    # Выбор таблицы для проверки
    table_choice = st.selectbox(
        "Какую таблицу проверяем?",
        [1, 2, 3, 4, 5],
        index=[1,2,3,4,5].index(st.session_state.table) if st.session_state.table in [1,2,3,4,5] else 1,
        key="test_table_select"
    )
    if table_choice != st.session_state.table:
        st.session_state.table = table_choice
        generate_test_questions()
        st.rerun()
    
    # Если вопросы закончились – генерируем новые (но у нас их 10)
    if not st.session_state.test_questions:
        generate_test_questions()
    
    # Если все вопросы пройдены – показываем результаты и возвращаем в меню
    if st.session_state.test_index >= len(st.session_state.test_questions):
        st.success("🎉 Ты ответил на все вопросы! Молодец!")
        # Проверяем, нужно ли дать диплом за 10 правильных
        if st.session_state.test_score >= 10:
            show_diploma()
            st.session_state.total_correct += st.session_state.test_score
        else:
            st.session_state.total_correct += st.session_state.test_score
        st.markdown(f"### Твой результат: {st.session_state.test_score} / {len(st.session_state.test_questions)}")
        if st.button("Вернуться в меню"):
            st.session_state.page = "menu"
            st.rerun()
        return
    
    # Текущий вопрос
    a, b = st.session_state.test_questions[st.session_state.test_index]
    st.markdown(f"### Вопрос {st.session_state.test_index + 1} из {len(st.session_state.test_questions)}")
    st.markdown(f"#### {a} × {b} = ?")
    
    # Поле для ответа
    user_answer = st.text_input("Твой ответ:", key=f"test_input_{st.session_state.test_index}")
    
    if st.button("Проверить", type="primary"):
        if user_answer.strip() == "":
            st.session_state.feedback = "❌ Введи число!"
        else:
            try:
                ans = int(user_answer)
                correct = a * b
                if ans == correct:
                    st.session_state.test_score += 1
                    st.session_state.total_correct += 1
                    praise = get_praise(st.session_state.name)
                    st.session_state.feedback = f"✅ {praise}"
                    # Переход к следующему вопросу
                    st.session_state.test_index += 1
                    # Проверяем, не набрал ли 10 правильных в текущей сессии
                    if st.session_state.test_score % 10 == 0 and st.session_state.test_score > 0:
                        show_diploma()
                else:
                    st.session_state.feedback = f"❌ Неверно! Правильный ответ: {correct}. {get_hint(a, b)}"
            except ValueError:
                st.session_state.feedback = "❌ Введи целое число!"
        
        # После обработки обновляем страницу, чтобы показать следующий вопрос
        st.rerun()
    
    # Отображение обратной связи
    if st.session_state.feedback:
        st.markdown(st.session_state.feedback)
    
    # Кнопка выхода в меню (без потери прогресса, но при возврате тест начнётся заново)
    if st.button("◀️ Выйти в меню"):
        # Сбрасываем тест, чтобы при следующем заходе начать заново
        st.session_state.test_index = 0
        st.session_state.test_score = 0
        st.session_state.feedback = ""
        st.session_state.page = "menu"
        st.rerun()

# ------------------- ГЛАВНЫЙ РОУТИНГ -------------------
def main():
    if st.session_state.page == "welcome":
        welcome_page()
    elif st.session_state.page == "menu":
        menu_page()
    elif st.session_state.page == "learn":
        learn_page()
    elif st.session_state.page == "test":
        test_page()

if __name__ == "__main__":
    main()
