# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
import re


class Worker:
    def __init__(self, input_list):
        self.input_list = input_list

    @property
    def first_name(self):
        return self.input_list[0]

    @property
    def last_name(self):
        return self.input_list[1]

    @property
    def salary(self):
        return int(self.input_list[2])

    @property
    def position(self):
        return self.input_list[3]

    @property
    def hours_normal(self):
        return int(self.input_list[4])

    @property
    def hours_worked(self):
        return int(self.input_list[5])

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_salary(self):
        if self.hours_worked <= self.hours_normal:
            actual_salary = self.salary * self.hours_worked / self.hours_normal
        else:
            actual_salary = self.salary + 2 * (self.hours_worked - self.hours_normal) * self.salary / self.hours_normal
        return '{} {} в этом месяце получит {}'.format(self.position, self.full_name, actual_salary)


def data_handler(workers_file, hours_of_file):
    """
    Cleans input data files and returns a file to use for actual salary accounting
    :param workers_file:
    :param hours_of_file:
    :return:
    """
    # матрица очищенных исходных данных
    with open(workers_file, 'r', encoding='utf-8') as workers_file:
        lst_1 = workers_file.readlines()
        lst_2 = []
        for line in lst_1:
            a = line.replace('\n', '')
            workers = []
            for x in re.split(r'\s+', a):
                workers.append(x)
            lst_2.append(workers)
        lst_2[0].append('Отработано часов')

    # матрица очищенных данных по отработке
    with open(hours_of_file, 'r', encoding='utf-8') as hours_file:
        lst_raw = hours_file.readlines()
        lst_employee = []
        for l in lst_raw:
            b = l.replace('\n', '')
            done = []
            for y in re.split(r'\s+', b):
                done.append(y)
            lst_employee.append(done)

    # список работников компании
    employee_list = []
    for idx, line in enumerate(lst_2):
        if idx != 0:
            employee = lst_2[idx][0] + ' ' + lst_2[idx][1]
            employee_list.append(employee)

    # список [Ф.И. работника, кол-во отработанных часов]
    worked_hours = []
    for line in lst_employee:
        employee_1 = line[0] + ' ' + line[1]
        if employee_1 in employee_list:
            worked_hours.append([employee_1, line[2]])

    # формиование сводного списка по всем работникам компании и отработанному времени для дальнейшей обработки
    w_hours_sorted = sorted(worked_hours)
    lst_2_sorted = sorted(list(lst_2[1:]))
    final_list = lst_2_sorted.copy()
    for idx, line in enumerate(w_hours_sorted):
        if w_hours_sorted[idx][0] == (lst_2_sorted[idx][0] + ' ' + lst_2_sorted[idx][1]) and idx < len(final_list):
            final_list[idx].append(w_hours_sorted[idx][1])

    return final_list


# сама программа
final_list = data_handler('data\workers', 'data\hours_of')

for i, line in enumerate(final_list):
    worker = Worker(line)
    print(worker.get_salary())
