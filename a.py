
# === Імпорт потрібних класів із бібліотеки PyQt5 ===
from PyQt5.QtCore import Qt                             # Модуль із константами, наприклад для вирівнювання (AlignCenter)
from PyQt5.QtWidgets import (QApplication, QWidget,      # Основні класи для GUI
QHBoxLayout, QVBoxLayout,                                # Лейаути (розташування)
QGroupBox, QRadioButton,                                 # Група та радіокнопки
QPushButton, QLabel, QButtonGroup)                       # Кнопка, текст, група кнопок
from random import shuffle,randint                               # Для перемішування варіантів відповідей


# === Клас для зберігання одного питання ===
class Question():
    def __init__(self, ques, right_answer, wrong1, wrong2, wrong3):
        # Питання
        self.ques = ques
        # Правильна відповідь
        self.right_answer = right_answer
        # Три неправильні варіанти
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        


# === Створюємо список усіх питань ===
questions_list = []
questions_list.append( Question("200+5647=", "5847", "877", "200", "5676") )
questions_list.append( Question("переклади англійською автобус", "Bus", "Car", "Tax", "Cow") )
questions_list.append( Question("Скільки континентів?", "7", "8", "6", "5") )
questions_list.append( Question("-100+7647=", "7547", "877", "-200", "-5676") )
questions_list.append( Question("-10000+7986=", "-2014", "-100", "17000", "-17000") )
questions_list.append( Question("654*10=", "6540", "65", "6530", "6544") )
questions_list.append( Question("переклади англійською мох", "Moss", "Grass", "Tree", "Plant") )
questions_list.append( Question("переклади англійською кот", "Cat", "Bear", "Dog", "Human") )
questions_list.append( Question("6*10=", "60", "65", "6530", "644") )
questions_list.append( Question("213+28=", "241", "125", "60", "44") )
questions_list.append( Question("6*1=", "6", "-6", "5", "7") )

# === СТВОРЕННЯ ГОЛОВНОГО ВІКНА ===
app = QApplication([])             # Створення застосунку (обов’язково перед усім)
window = QWidget()                 # Головне вікно
window.resize(800, 500)            # Розміри вікна
window.setWindowTitle("a")  # Назва вікна




# === СТВОРЕННЯ ОСНОВНИХ ВІДЖЕТІВ ===
question = QLabel("переклади англійською")  # Напис із питанням
btn_ok = QPushButton("Answer")               # Кнопка для відповіді / переходу




# === ГРУПА З ВАРІАНТАМИ ВІДПОВІДЕЙ ===
RadioGroupBox = QGroupBox("Варіанти відповідей")  # Рамка для варіантів


# Створюємо 4 радіокнопки (можна вибрати лише одну)
rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")


# Об’єднуємо всі кнопки в одну групу, щоб не можна було вибрати кілька одразу
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)




# === ЛЕЙАУТИ ДЛЯ ВАРІАНТІВ ВІДПОВІДЕЙ ===
ans_h_layout = QHBoxLayout()  # Горизонтальний ряд (основний)
ans_v1_layout = QVBoxLayout() # Перша вертикальна колонка
ans_v2_layout = QVBoxLayout() # Друга вертикальна колонка


# Додаємо кнопки у дві колонки
ans_v1_layout.addWidget(rbtn1)
ans_v1_layout.addWidget(rbtn2)
ans_v2_layout.addWidget(rbtn3)
ans_v2_layout.addWidget(rbtn4)


# Об’єднуємо дві колонки в один ряд
ans_h_layout.addLayout(ans_v1_layout)
ans_h_layout.addLayout(ans_v2_layout)


# Встановлюємо цей лейаут у групу з варіантами
RadioGroupBox.setLayout(ans_h_layout)




# === ГРУПА З РЕЗУЛЬТАТОМ ВІДПОВІДІ ===
AnsGroupBox = QGroupBox("Результат тесту")


lb_Result = QLabel("Відповідь вірна?")         # Текст про правильність
lb_Correct = QLabel("відповідь буде тут!")     # Текст із правильною відповіддю


# Створюємо вертикальний лейаут для блоку результату
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(layout_res)




# === ОСНОВНА СХЕМА РОЗМІЩЕННЯ У ВІКНІ ===
v_line = QVBoxLayout()  # Головне вертикальне розташування
h1_line = QHBoxLayout() # Рядок для питання
h2_line = QHBoxLayout() # Рядок для варіантів / результатів
h3_line = QHBoxLayout() # Рядок для кнопки


# 1. Питання по центру
h1_line.addWidget(question, alignment=Qt.AlignCenter)


# 2. Групи з варіантами та результатом поруч
h2_line.addWidget(RadioGroupBox)
h2_line.addWidget(AnsGroupBox)


# 3. Кнопка по центру з відступами
h3_line.addStretch(1)
h3_line.addWidget(btn_ok, stretch=2)
h3_line.addStretch(1)


# 4. Об’єднуємо всі рядки у вертикальну структуру
v_line.addLayout(h1_line, stretch=2)
v_line.addLayout(h2_line, stretch=8)
v_line.addStretch(1)
v_line.addLayout(h3_line, stretch=1)
v_line.addStretch(1)


# Спочатку ховаємо блок із результатом (він з’явиться пізніше)
AnsGroupBox.hide()




# === ФУНКЦІЇ ДЛЯ ЗМІНИ СТАНУ ПРОГРАМИ ===


def show_result():
    """Показати блок із результатом"""
    RadioGroupBox.hide()                    # Сховати варіанти
    AnsGroupBox.show()                      # Показати результат
    btn_ok.setText("Наступне запитання")    # Змінити текст кнопки




def show_question():
    """Показати нове питання"""
    AnsGroupBox.hide()                      # Сховати результат
    RadioGroupBox.show()                    # Показати варіанти
    btn_ok.setText("Answer")                # Змінити текст кнопки назад


    # Зняти вибір з усіх кнопок
    RadioGroup.setExclusive(False)          # Тимчасово дозволяємо зміну стану
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)           # Повертаємо звичайний режим




# Збираємо всі кнопки в список для зручності
answers = [rbtn1, rbtn2, rbtn3, rbtn4]




# --- ФУНКЦІЯ, ЩО ВСТАНОВЛЮЄ НОВЕ ПИТАННЯ ---
def ask(q: Question):
    """Встановлює нове запитання та перемішує варіанти"""
    shuffle(answers)                         # Перемішуємо кнопки випадковим чином


    # Призначаємо тексти для кнопок
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)


    # Встановлюємо текст питання та правильної відповіді
    question.setText(q.ques)
    lb_Correct.setText(q.right_answer)


    # Показуємо питання (ховаємо попередній результат)
    show_question()




# --- ФУНКЦІЯ, ЩО ПОКАЗУЄ РЕЗУЛЬТАТ ---
def show_correct(res):
    """Показує результат ('правильно' або 'неправильно')"""
    lb_Result.setText(res)   # Встановлюємо текст результату
    show_result()            # Показуємо блок із результатом




# --- ФУНКЦІЯ ПЕРЕВІРКИ ВІДПОВІДІ ---
def check_answer():
    """Перевіряє, яку відповідь вибрав користувач"""
    if answers[0].isChecked():                # Перша кнопка — правильна (після shuffle)
        show_correct("Correct!") 
        window.score +=1
        print("resultat",window.score/window.total*100)
    else:
        # Якщо вибрана будь-яка інша — відповідь невірна
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct("INCORRECT!!")
            print("resultat",window.score/window.total*100)



# --- ПЕРЕХІД ДО НАСТУПНОГО ПИТАННЯ ---
def next_question():
    window.cur_question=randint(0,len(questions_list)-1)                  # Збільшуємо індекс питання
    window.total +=1

    # Якщо дійшли до кінця списку — починаємо спочатку
    if window.cur_question >= len(questions_list):
        window.cur_question = 0


    q = questions_list[window.cur_question]   # Беремо поточне питання
    ask(q)                                   # Показуємо його




# --- ГОЛОВНА КНОПКА (Answer / Наступне питання) ---
def click_OK():
    if btn_ok.text() == "Answer":             # Якщо текст на кнопці"Answer"
        check_answer()                        # Перевіряємо відповідь
    else:
        next_question()                       # Інакше — показуємо наступне питання




# Починаємо з першого питання
window.cur_question = -1


# Підключаємо кнопку до функції
btn_ok.clicked.connect(click_OK)
window.score = 0
window.total = 0
# Показуємо перше питання
next_question()




# === ВСТАНОВЛЕННЯ ГОЛОВНОГО ЛЕЙАУТУ ===
window.setLayout(v_line)  # Додаємо все у вікно


# Показуємо вікно на екрані
window.show()


# Запускаємо основний цикл програми
app.exec()