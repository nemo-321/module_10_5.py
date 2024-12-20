#
#   Здесь импортируются необходимые модули. datetime используется для измерения времени выполнения,
#   а Pool из модуля multiprocessing позволяет создавать пул процессов для многопроцессного выполнения.
from datetime import datetime
from multiprocessing import Pool


# Функция read_info принимает имя файла name в качестве аргумента.
# Создается пустой список all_data, в который будут добавляться строки из файла.
# Файл открывается с помощью контекстного менеджера with, что гарантирует его закрытие после завершения работы.
# В цикле for считываются строки из файла, и каждая строка добавляется в список all_data.
def read_info(name):
    all_data = []
    with open(name) as file:
        for line in file:
            all_data.append(line)


# Основной блок программы:он выполняется только если скрипт запускается напрямую, а не импортируется как модуль.
if __name__ == '__main__':
    # создается список filenames, который содержит имена файлов от file 1.txt до file 4.txt.
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    #  Линейное считывание:
    # Сначала фиксируется текущее время с помощью datetime.now().
    # Затем для каждого файла из списка filenames вызывается функция read_info.
    # После завершения считывания выводится время, затраченное на линейное считывание.
    start_time = datetime.now()
    for name in filenames:
        read_info(name)
    print(datetime.now() - start_time, ('Линейный'))
    # Многопроцессное считывание:
    # Снова фиксируется текущее время.
    # Создается пул из 4 процессов с помощью Pool(processes=4).
    # Метод map используется для параллельного вызова функции read_info для каждого файла из списка filenames.
    # После завершения многопроцессного считывания выводится время, затраченное на этот процесс.
    start_time = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    print(datetime.now() - start_time, ('Многопроцессный'))
