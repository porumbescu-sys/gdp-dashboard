import streamlit as st
import random

praise_phrases = [
    "🎉 Отлично! Ты просто гений умножения!",
    "✨ Вау! Правильно! Молодец!",
    "🌟 Супер! Так держать!",
    "💪 Умница! Таблица умножения тебе покоряется!",
    "🏆 Великолепно! Ты справляешься на отлично!",
    "🎈 Правильно! Продолжай в том же духе!",
    "🍭 Сладкая победа! Верно!",
    "🚀 Космический результат! Правильно!"
]

# Инициализация состояния
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.current_a = random.randint(2, 9)
    st.session_state.current_b = random.randint(2, 9)
    st.session_state.feedback = ""
    st.session_state.answer_value = ""  # для хранения значения поля

st.set_page_config(page_title="Таблица умножения", page_icon="🧸")
st.title("🧸 Изучаем таблицу умножения")
st.markdown("Введи ответ и нажми **Проверить**")

# Отображение примера
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.header(f"{st.session_state.current_a} × {st.session_state.current_b} = ?")

# Форма для ввода и проверки
with st.form(key="quiz_form"):
    # Поле ввода, привязанное к session_state.answer_value
    user_answer = st.text_input("Твой ответ:", key="answer_input", value=st.session_state.answer_value)
    submitted = st.form_submit_button("Проверить")

if submitted:
    if user_answer.strip() == "":
        st.session_state.feedback = "❌ Введи число!"
    else:
        try:
            answer = int(user_answer)
            st.session_state.total += 1
            correct = st.session_state.current_a * st.session_state.current_b

            if answer == correct:
                st.session_state.score += 1
                st.balloons()
                praise = random.choice(praise_phrases)
                st.session_state.feedback = f"✅ {praise}"
                # Генерируем новый пример
                st.session_state.current_a = random.randint(2, 9)
                st.session_state.current_b = random.randint(2, 9)
            else:
                st.session_state.feedback = f"❌ Неверно! Правильный ответ: {correct}"
        except ValueError:
            st.session_state.feedback = "❌ Введи целое число!"

    # Очищаем значение поля
    st.session_state.answer_value = ""
    # Принудительное обновление страницы
    st.rerun()

# Отображение обратной связи
if st.session_state.feedback:
    st.markdown(st.session_state.feedback)

# Статистика
st.markdown("---")
st.metric("Счёт", f"{st.session_state.score} / {st.session_state.total}")

# Кнопка сброса
if st.button("Начать заново"):
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.current_a = random.randint(2, 9)
    st.session_state.current_b = random.randint(2, 9)
    st.session_state.feedback = ""
    st.session_state.answer_value = ""
    st.rerun()
