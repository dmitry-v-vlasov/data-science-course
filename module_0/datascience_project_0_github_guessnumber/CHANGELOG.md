# Changelog

## Version 0.1.1

- Пакет [datascience_project_0_github_guessnumber](../datascience_project_0_github_guessnumber)
  перемещён в директорию [module_0](../../module_0) для сдачи задания.

## Version 0.1.0

- Вручную, с помощью IDE PyCharm,
  создан новый проект в соответствии с
  внутренней организацией пакетов Python и
  минимальными требованиями PyPI.
- Добавлена реализация трёх алгоритмов для угадывания
  случайного целого числа из заданного сегмента целых чисел:
  1. Добавлена реализация со **случайным выбором первого угадываемого числа**
     из сегмента. Данная реализация **позаимствована
     из оригинальной формулировки задания** на реализацию более
     оптимального алгоритма пойска загаданного числа. Эта реализациа *добавлена
     для сравнения* с более эффективными алгоритмами на основе бинарного и тернарного поиска.
  2. Добавлена реализация на основе алгоритма **бинарного поиска**,
     когда интервал поиска делится в каждой итерации на две половины,
     а в качестве угадываемого числа берётся середина делимого интервала чисел.
  3. Добавлена реализация на основе алгоритма **тернарного поиска**,
     когда интервал поиска делится в каждой итерации на три части,
     а в качестве угадываемых чисел берутся два числа на границах между этими тремя частями.
- Добавлен интерфейс командной строки, который становится доступен
  через команду `datascience_guessnumber` после
  клонирования GIT репозитория и ручной установки пакета
  посредством пакетного менеджера `pip`. Инструкция по установке
  доступна в файле [README.md](README.md) в секции [Installation](README.md#Installation).
- Добавлен файл `pyprojecct.toml.disabled`,
  который, однако, в настоящий момент не используется.
- Реализованные демонстрационные алгоритмы угадывания целого числа из заданного
  интервала позволяют сделать вывод о том, что
  *наиболее эффективным*, <ins>по количеству предпринимаемых попыток угадывания</ins>,
  *является алгоритм* угадывания на основе алгоритма *бинарного поиска*.