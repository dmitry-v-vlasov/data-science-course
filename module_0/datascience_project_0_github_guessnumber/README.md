# Data science project 0: A guess number game example with primitive self-testing

A guess number game example with primitive self-testing

## Requrements

* Python 3.7+
* numpy
* setuptools, wheel

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `datascience-project-0-github-guessnumber`.

### Installation of the package `datascience-project-0-github-guessnumber`

```bash
pip install datascience-project-0-github-guessnumber
```

View at:
https://pypi.org/project/datascience-project-0-github-guessnumber/

### Installation from a local copy of the repository
```bash
git clone https://github.com/dmitry-v-vlasov/data-science-course.git
cd data-science-course
cd datascience_project_0_github_guessnumber
pip install .
```

## After the package installation

Type the following command in order to display help text.

```bash
datascience_guessnumber -h
```

Here is a copy of the help text of the `datascience_guessnumber` command.

```
usage: datascience_guessnumber [-h] [-n INTEGER] [-s "[a, b]"] [-g LIST] [-v] [-vv] [--version]

  __ _ _   _  ___  ___ ___   _ __  _   _ _ __ ___ | |__   ___ _ __ 
 / _` | | | |/ _ \/ __/ __| | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
| (_| | |_| |  __/\__ \__ \ | | | | |_| | | | | | | |_) |  __/ |   
 \__, |\__,_|\___||___/___/ |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
 |___/
 Guess Number game strategies demonstration

optional arguments:
  -h, --help                       show this help message and exit
  -n INTEGER, --attempts INTEGER   number of attempts to guess a number
  -s "[a, b]", --segment "[a, b]"  a segment of integer numbers surrounded with double quotes(!!)
  -g LIST, --game-strategies LIST  a comma separated list of strategies (without spaces!!).
                                   The supported strategy names: random-snail,binary-search,ternary-search
  -v, --verbose                    set loglevel to INFO
  -vv, --very-verbose              set loglevel to DEBUG
  --version                        show program's version number and exit

© Copyright 2020, Dmitry Vlasov
Author email: dmitry.v.vlasov@gmail.com
Licence: MIT
--------------------------------------------
```

### Screenshot:
![](docs/images/usage-datascience_guessnumber-help.png)

## Usage

### Calling the command `datascience_guessnumber` without arguments

```bash
datascience_guessnumber
```

#### Execution result:
```
Ваш алгоритм "random-snail" угадывает число в среднем за 30 попыток при 30 итерациях цикла.
Ваш алгоритм "binary-search" угадывает число в среднем за 4 попыток при 4 итерациях цикла.
Ваш алгоритм "ternary-search" угадывает число в среднем за 5 попыток при 2 итерациях цикла.
Вывод: наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber.png)

### Specifying game strategies

```bash
datascience_guessnumber --game-strategies random-snail,binary-search
```

#### Execution result:
```
Ваш алгоритм "random-snail" угадывает число в среднем за 30 попыток при 30 итерациях цикла.
Ваш алгоритм "binary-search" угадывает число в среднем за 4 попыток при 4 итерациях цикла.
Вывод: наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber-strategies.png)

### Specifying attempts number and number segment

```bash
datascience_guessnumber --attempts 1000 --segment "[1, 100]"
```

#### Execution result:
```
Ваш алгоритм "random-snail" угадывает число в среднем за 30 попыток при 30 итерациях цикла.
Ваш алгоритм "binary-search" угадывает число в среднем за 4 попыток при 4 итерациях цикла.
Ваш алгоритм "ternary-search" угадывает число в среднем за 5 попыток при 2 итерациях цикла.
Вывод: наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber-attempts_segment.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)