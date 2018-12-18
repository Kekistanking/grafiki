import sys
import math
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog
from MyWindow import Ui_MainWindow
from MyGraph import Ui_Graphs


def sin_result(x, list):
    return list[0] * math.sin(list[1] * x) + list[2]


def cos_result(x, list):
    return list[0] * math.cos(list[1] * x) + list[2]


def tg_result(x, list):
    return list[0] * math.tan(list[1] * x) + list[2]


def p_result(x, list):
    a = list[0] * x ** 5 + list[1] * x ** 4 + list[2] * x ** 3 + list[3] * x ** 2 + list[4] * x ** 1
    return a + list[5]


def check_funk(x, list):
    if list[0] == 'sin':
        return sin_result(x, list[1])
    elif list[0] == 'cos':
        return cos_result(x, list[1])
    elif list[0] == 'tg':
        return tg_result(x, list[1])
    else:
        return p_result(x, list[1])


def run_znak(znak, func1, func2):
    if znak == '+':
        return func1 + func2
    if znak == '-':
        return func1 - func2
    if znak == '*':
        return func1 * func2
    if znak == '/':
        return func1 / func2


def mytan(number):
    if math.tan(number) > 10:
        return math.tan(1.5)
    if math.tan(number) < -10:
        return math.tan(-1.5)
    return math.tan(number)


class SecondWindow(QMainWindow, Ui_Graphs):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.build()
        self.window = None
        self.cal_znak = '+'
        self.dop_funk = 0
        self.history_funk = ['']
        self.is_znak_chenged = True
        self.is_func_chenged = False
        self.coefisients_list = []
        self.znak_list = []
        self.funk_list = []

    def build(self):
        self.goback.clicked.connect(self.back)
        self.sin.clicked.connect(self.run_sin)
        self.cos.clicked.connect(self.run_cos)
        self.tg.clicked.connect(self.run_tg)
        self.P.clicked.connect(self.run_p)
        self.clear.clicked.connect(self.clear_graph)
        self.plus.clicked.connect(self.run_plus)
        self.minus.clicked.connect(self.run_minus)
        self.multiplication.clicked.connect(self.run_multiplication)
        self.devision.clicked.connect(self.run_devision)
        self.cal_back.clicked.connect(self.run_cal_back)
        self.cal_clear.clicked.connect(self.run_cal_clear)
        self.cal_sin.clicked.connect(self.run_cal_sin)
        self.cal_cos.clicked.connect(self.run_cal_cos)
        self.cal_tg.clicked.connect(self.run_cal_tg)
        self.cal_result.clicked.connect(self.run_mainfunc)
        self.cal_p.clicked.connect(self.run_cal_p)

    def back(self):
        self.window = MyWidget()
        self.window.show()
        self.close()

    def get_bounds(self):
        lines, okBtnPressed = QInputDialog.getText(self, "Ввод границ",
                                                   "Введите нижнюю и верхнюю границу \nобласти "
                                                   "определения x через запятую (2 целых числа)")
        if okBtnPressed:
            try:
                lower_bound = int(lines.split(",")[0])
                upper_bound = int(lines.split(",")[1])
                if lower_bound > upper_bound:
                    raise ValueError
            except Exception:
                lower_bound, upper_bound = self.get_bounds_error()
            if len(lines.split(",")) != 2:
                lower_bound, upper_bound = self.get_bounds_error()
            return lower_bound, upper_bound
        else:
            return None, None

    def get_bounds_error(self):
        lines, okBtnPressed = QInputDialog.getText(self, "Ввод границ",
                                                   "Вы ввели границы неккоректно. Введите нижнюю и "
                                                   "\nверхнюю границу области определения x через "
                                                   "запятую (2 целых числа)")
        lower_bound = 0
        upper_bound = 0
        if okBtnPressed:
            try:
                lower_bound = int(lines.split(",")[0])
                upper_bound = int(lines.split(",")[1])
                if lower_bound > upper_bound:
                    raise ValueError
            except Exception:
                self.get_bounds_error()
            if len(lines.split(",")) != 2:
                lower_bound, upper_bound = self.get_bounds_error()
            return lower_bound, upper_bound
        else:
            return None, None

    def get_coefficients(self, number):
        coefficients, okBtnPressed = QInputDialog.getText(self, "Ввод коэффициентов",
                                                          "Введите все коэффициенты слева "
                                                          "направо через запятую")
        coefficients_list = []
        if okBtnPressed:
            if len(coefficients.split(",")) != number:
                coefficients_list = self.get_coefficients_error(number)
            else:
                try:
                    for i in range(number):
                        coefficients_list.append(float(coefficients.split(",")[i]))
                except Exception:
                    coefficients_list = self.get_coefficients_error(number)
            return coefficients_list
        else:
            return None

    def get_coefficients_error(self, number):
        coefficients, okBtnPressed = QInputDialog.getText(self, "Ввод коэффициентов",
                                                          "Вы ввели коэффициенты некорректно. "
                                                          "\nВведите коэффициенты слева направо "
                                                          "через запятую")
        coefficients_list = []
        if okBtnPressed:
            if len(coefficients.split(",")) != number:
                coefficients_list = self.get_coefficients_error(number)
            else:
                try:
                    for i in range(number):
                        coefficients_list.append(float(coefficients.split(",")[i]))
                except Exception:
                    coefficients_list = self.get_coefficients_error(number)
            return coefficients_list
        else:
            return None

    def run_sin(self):
        coefficients = self.get_coefficients(3)
        if coefficients is None:
            return None
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        lower_bound, upper_bound = self.get_bounds()
        if lower_bound is None:
            return None
        self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                               [a * math.sin(c * (i / 10)) + b
                                for i in range(10 * lower_bound, 10 * upper_bound)],
                               pen="w")
        self.graphicsView.setAspectLocked(lock=True, ratio=1)

    def run_tg(self):
        coefficients = self.get_coefficients(3)
        if coefficients is None:
            return None
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        lower_bound, upper_bound = self.get_bounds()
        if lower_bound is None:
            return None
        self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                               [a * self.mytan(c * (i / 10)) + b
                                for i in range(10 * lower_bound, 10 * upper_bound)],
                               pen="y")
        self.graphicsView.setAspectLocked(lock=True, ratio=1)

    def run_cos(self):
        coefficients = self.get_coefficients(3)
        if coefficients is None:
            return None
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        lower_bound, upper_bound = self.get_bounds()
        if lower_bound is None:
            return None
        self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                               [a * math.cos(c * (i / 10)) + b
                                for i in range(10 * lower_bound, 10 * upper_bound)],
                               pen="m")
        self.graphicsView.setAspectLocked(lock=True, ratio=1)

    def run_p(self):
        number, okBtnPressed = QInputDialog.getInt(self, "Ввод степени многочлчена", "Введите "
                                                         "степень многочлена", 0, 0, 5, 1)
        coefficients = self.get_coefficients(number + 1)
        if coefficients is None:
            return None
        lower_bound, upper_bound = self.get_bounds()
        if lower_bound is None:
            return None
        if number == 5:
            a = coefficients[0]
            b = coefficients[1]
            c = coefficients[2]
            d = coefficients[3]
            e = coefficients[4]
            f = coefficients[5]
            self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                                   [a * (i / 10) ** 5 + b * (i / 10) ** 4 + c * (
                                       i / 10) ** 3 + d * (i / 10) ** 2 + e * (i / 10) + f
                                    for i in range(10 * lower_bound, 10 * upper_bound)],
                                   pen="r")
        elif number == 4:
            a = coefficients[0]
            b = coefficients[1]
            c = coefficients[2]
            d = coefficients[3]
            e = coefficients[4]
            self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                                   [a * (i / 10) ** 4 + b * (i / 10) ** 3 + c * (
                                       i / 10) ** 2 + d * (i / 10) ** 1 + e
                                    for i in range(10 * lower_bound, 10 * upper_bound)],
                                   pen="c")
        elif number == 3:
            a = coefficients[0]
            b = coefficients[1]
            c = coefficients[2]
            d = coefficients[3]
            self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                                   [a * (i / 10) ** 3 + b * (i / 10) ** 2 + c * (
                                       i / 10) ** 1 + d
                                    for i in range(10 * lower_bound, 10 * upper_bound)],
                                   pen="g")
        elif number == 2:
            a = coefficients[0]
            b = coefficients[1]
            c = coefficients[2]
            self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                                   [a * (i / 10) ** 2 + b * (i / 10) ** 1 + c
                                    for i in range(10 * lower_bound, 10 * upper_bound)],
                                   pen="b")
        elif number == 1:
            a = coefficients[0]
            b = coefficients[1]
            self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                                   [a * (i / 10) ** 1 + b
                                    for i in range(10 * lower_bound, 10 * upper_bound)],
                                   pen="r")

    def clear_graph(self):
        self.graphicsView.clear()

    def run_plus(self):
        self.cal_znak = '+'
        self.is_znak_chenged = True
        if self.cal_dop_funk.text() == '+' or self.cal_dop_funk.text() == '' or (
                len(self.cal_dop_funk.text()) > 0 and self.cal_dop_funk.text()[-1] in ['+', '-',
                                                                                       '*', '/']):
            pass
        else:
            self.cal_dop_funk.setText(self.cal_dop_funk.text() + '+')

    def run_minus(self):
        self.cal_znak = '-'
        self.is_znak_chenged = True
        if len(self.cal_dop_funk.text()) > 0 and self.cal_dop_funk.text()[-1] in ['+', '-',
                                                                                  '*', '/']:
            pass
        elif self.cal_dop_funk.text() == '+':
            self.cal_dop_funk.setText('-')
        else:
            self.cal_dop_funk.setText(self.cal_dop_funk.text() + '-')

    def run_devision(self):
        if self.cal_dop_funk.text() == '' or (
                len(self.cal_dop_funk.text()) > 0 and self.cal_dop_funk.text()[-1] in ['+', '-',
                                                                                       '*', '/']):
            pass
        elif self.cal_dop_funk.text() == '-' or self.cal_dop_funk.text() == '+':
            self.cal_znak = '+'
            self.cal_dop_funk.setText('')
        else:
            self.cal_dop_funk.setText(self.cal_dop_funk.text() + '/')
            self.cal_znak = '/'
            self.is_znak_chenged = True

    def run_multiplication(self):
        if self.cal_dop_funk.text() == '' or (
                len(self.cal_dop_funk.text()) > 0 and self.cal_dop_funk.text()[-1] in ['+', '-',
                                                                                       '*', '/']):
            pass
        elif self.cal_dop_funk.text() == '-' or self.cal_dop_funk.text() == '+':
            self.cal_znak = '+'
            self.cal_dop_funk.setText('')
        else:
            self.cal_dop_funk.setText(self.cal_dop_funk.text() + '*')
            self.cal_znak = '*'
            self.is_znak_chenged = True

    def run_cal_back(self):
        if len(self.znak_list) > 0:
            if (len(self.znak_list) > len(self.funk_list) or (
                            len(self.znak_list) == len(self.funk_list) and self.is_znak_chenged)):
                self.is_znak_chenged = False
                self.cal_znak = '+'
                self.cal_dop_funk.setText(
                    self.cal_dop_funk.text()[:len(self.cal_dop_funk.text()) - 1])
                if self.znak_list == []:
                    self.cal_znak = '+'
                    self.is_znak_chenged = True
            else:
                try:
                    del self.funk_list[-1]
                    del self.znak_list[-1]
                    del self.history_funk[-1]
                except Exception:
                    pass
                if self.history_funk == []:
                    self.history_funk = ['']
                if self.znak_list == []:
                    self.cal_znak = '+'
                    self.is_znak_chenged = True
                self.cal_dop_funk.setText(self.history_funk[-1])
        else:
            pass

    def run_cal_clear(self):
        self.funk_list.clear()
        self.znak_list.clear()
        self.cal_znak = '+'
        self.is_znak_chenged = True
        self.cal_dop_funk.setText('')

    def run_cal_sin(self):
        if self.is_znak_chenged:
            coefisients_list = self.get_coefficients(3)
            if coefisients_list is None:
                return None
            self.funk_list.append(
                ('sin', [coefisients_list[0], coefisients_list[1], coefisients_list[2]]))
            self.znak_list.append(self.cal_znak)
            self.cal_dop_funk.setText(
                self.cal_dop_funk.text() + str(coefisients_list[0]) + '*sin(' + str(
                    coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            self.is_znak_chenged = False
            if len(self.history_funk) > 2:
                self.history_funk.append(
                    self.history_funk[-1] + self.cal_znak + str(coefisients_list[0]) + '*tg(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            else:
                self.history_funk.append(
                    self.history_funk[-1] + str(coefisients_list[0]) + '*sin(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))

        else:
            pass

    def run_mainfunc(self):
        lower_bound, upper_bound = self.get_bounds()
        if lower_bound is None:
            return None
        results = []
        for i in range(10 * lower_bound, 10 * upper_bound):
            res = 0
            result_funk_list = [0 for i in range(len(self.funk_list))]

            result_znak_list = [i for i in self.znak_list]

            for k in range(len(self.funk_list)):
                result_funk_list[k] = check_funk(i / 10, self.funk_list[k])

            r = 0
            result_funk_list = [0] + result_funk_list
            while r < (len(result_znak_list)):
                if result_znak_list[r] == '*' or result_znak_list[r] == '/':
                    result_funk_list[r + 1] = run_znak(self.znak_list[r], result_funk_list[r],
                                                       result_funk_list[r + 1])
                    del result_funk_list[r]
                    del result_znak_list[r]
                else:
                    r += 1
            for u in range(len(result_znak_list)):
                res += run_znak(result_znak_list[u], result_funk_list[u - 1], result_funk_list[u])
            results.append(res)

        self.graphicsView.plot([i / 10 for i in range(10 * lower_bound, 10 * upper_bound)],
                               results,
                               pen="w")
        self.graphicsView.setAspectLocked(lock=True, ratio=1)

    def run_cal_cos(self):
        if self.is_znak_chenged:
            coefisients_list = self.get_coefficients(3)
            if coefisients_list is None:
                return None
            self.funk_list.append(
                ('cos', [coefisients_list[0], coefisients_list[1], coefisients_list[2]]))
            self.znak_list.append(self.cal_znak)
            self.cal_dop_funk.setText(
                self.cal_dop_funk.text() + str(coefisients_list[0]) + '*cos(' + str(
                    coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            self.is_znak_chenged = False
            if len(self.history_funk) > 2:
                self.history_funk.append(
                    self.history_funk[-1] + self.cal_znak + str(coefisients_list[0]) + '*tg(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            else:
                self.history_funk.append(
                    self.history_funk[-1] + str(coefisients_list[0]) + '*cos(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))

        else:
            pass

    def run_cal_tg(self):
        if self.is_znak_chenged:
            coefisients_list = self.get_coefficients(3)
            if coefisients_list is None:
                return None
            self.funk_list.append(
                ('tg', [coefisients_list[0], coefisients_list[1], coefisients_list[2]]))
            self.znak_list.append(self.cal_znak)
            self.cal_dop_funk.setText(
                self.cal_dop_funk.text() + str(coefisients_list[0]) + '*tg(' + str(
                    coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            self.is_znak_chenged = False
            if len(self.history_funk) > 2:
                self.history_funk.append(
                    self.history_funk[-1] + self.cal_znak + str(coefisients_list[0]) + '*tg(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))
            else:
                self.history_funk.append(
                    self.history_funk[-1] + str(coefisients_list[0]) + '*tg(' + str(
                        coefisients_list[1]) + 'x)' + '+' + str(coefisients_list[2]))

        else:
            pass

    def run_cal_p(self):
        if self.is_znak_chenged:
            number, okBtnPressed = QInputDialog.getInt(self, "Ввод степени многочлчена",
                                                       "Введите степень многочлена", 0, 0, 5, 1)
            coefficients = self.get_coefficients(number + 1)
            if coefficients is None:
                return None
            list = [0 for i in range(5 - number)] + coefficients
            self.funk_list.append(('p', list))
            self.znak_list.append(self.cal_znak)
            self.cal_dop_funk.setText(' + '.join(
                [str(coefficients[i]) + '*x^' + str(number - i) for i in range(number + 1)]))
            if len(self.history_funk) > 2:
                self.history_funk.append(self.history_funk[-1] + self.cal_znak + ' + '.join(
                 [str(coefficients[i]) + '*x^' + str(number - i) for i in range(number + 1)]))
            else:
                self.history_funk.append(self.history_funk[-1] + ' + '.join(
                 [str(coefficients[i]) + '*x^' + str(number - i) for i in range(number + 1)]))
            self.is_znak_chenged = False

        else:
            pass


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.secondWin = None
        self.setupUi(self)
        self.buildgraph.clicked.connect(self.run)
        self.bexit.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def run(self):
        self.secondWin = SecondWindow()
        self.secondWin.show()
        self.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
