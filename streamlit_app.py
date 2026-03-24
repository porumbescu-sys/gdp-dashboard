import streamlit as st
import random

# Список похвальных фраз
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

# Инициализация состояния игры
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.current_a = random.randint(2, 9)
    st.session_state.current_b = random.randint(2, 9)
    st.session_state.answer_submitted = False
    st.session_state.feedback = ""

# Заголовок
st.set_page_config(page_title="Таблица умножения", page_icon="🧸")
st.title("🧸 Изучаем таблицу умножения")
st.markdown("Введи ответ и нажми **Проверить**")

# Показываем пример
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.header(f"{st.session_state.current_a} × {st.session_state.current_b} = ?")

# Поле для ввода
user_answer = st.text_input("Твой ответ:", key="answer_input", value="")

# Кнопка проверки
if st.button("Проверить", type="primary"):
    if user_answer.strip() == "":
        st.session_state.feedback = "❌ Введи число!"
    else:
        try:
            answer = int(user_answer)
            st.session_state.total += 1
            correct = st.session_state.current_a * st.session_state.current_b

            if answer == correct:
                # Правильно
                st.session_state.score += 1
                # Фейерверк
                st.balloons()
                # Похвала
                praise = random.choice(praise_phrases)
                st.session_state.feedback = f"✅ {praise}"
                # Генерируем новый пример
                st.session_state.current_a = random.randint(2, 9)
                st.session_state.current_b = random.randint(2, 9)
            else:
                st.session_state.feedback = f"❌ Неверно! Правильный ответ: {correct}"
        except ValueError:
            st.session_state.feedback = "❌ Введи целое число!"

    # Очищаем поле ввода (хитрость: меняем ключ, чтобы обновить поле)
    st.session_state.answer_input = ""
    st.rerun()

# Показываем обратную связь
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
    st.rerun()
