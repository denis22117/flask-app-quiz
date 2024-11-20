from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Глобальные переменные
user_data = {}  # Для хранения имени и телефона
current_question_index = 0  # Индекс текущего вопроса
questions = [
    {
        'question': 'Как меня зовут?',
        'options': ['Денис', 'Влад', 'Артюхов'],
        'correct': 'Денис'
    },
    {
        'question': 'Сколько мне лет?',
        'options': ['21', '22', '25'],
        'correct': '25'
    },
    {
        'question': 'Где я живу?',
        'options': ['Тюмень', 'Крым', 'Танк'],
        'correct': 'Тюмень'
    },
    {
        'question': 'Что я люблю?',
        'options': ['Коктейли', 'Себя', 'Деньги'],
        'correct': 'Деньги'
    }
]

@app.route('/', methods=['GET', 'POST'])
def home():
    global current_question_index
    if request.method == 'POST':
        # Сохраняем имя и телефон
        user_data['name'] = request.form['name']
        user_data['phone'] = request.form['phone']

        # Печатаем данные в консоль для проверки
        print(f"User Data: {user_data}")

        current_question_index = 0  # Обнуляем индекс вопросов
        return redirect(url_for('quiz'))
    return render_template('home.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global current_question_index
    if current_question_index < len(questions):
        question = questions[current_question_index]
        if request.method == 'POST':
            selected_option = request.form['option']
            is_correct = selected_option == question['correct']
            print(f"Question: {question['question']}, Answer: {selected_option}, Correct: {is_correct}")

            current_question_index += 1
            return redirect(url_for('quiz'))

        return render_template('quiz.html', question=question, question_number=current_question_index + 1)
    else:
        return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)