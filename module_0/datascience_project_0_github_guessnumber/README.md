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
cd module_0
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

## Package file `guess_number.py`: Guess Number Game Algorithm Implementations (Guessing Strategies) 

Three number guessing strategies are implemented in here:
* `guess_number_game_core_random_snail`, symbolic name - `"random_snail"`;
  **This is the original algoritm implementation which is initially given in the problem statement (`game_core_v2`)**;
* `guess_number_game_core_binary_search`, symbolic name - `"binary-search"`;
  This is a number guessing algoritm implementation based on the binary search algorithm;
* `guess_number_game_core_ternary_search`, symbolic name - `"ternary-search"`;
  This is a number guessing algoritm implementation based on the ternary search algorithm.

The function `score_game` does a test of a given number guessing strategy.
The tested strategy efficiency results are printed in the end of the body of the function `score_game`.
The available strategies are enlisted in the enumeration class `GameCoreType`.

## Usage

### Calling the command `datascience_guessnumber` without arguments

```bash
datascience_guessnumber
```

#### Execution result:
```
- Ваш алгоритм "random-snail" угадывает число в среднем за
	31.9 попыток (31 целых) с 30.9 (30 целых) итерациями основного цикла в среднем.
- Ваш алгоритм "binary-search" угадывает число в среднем за
	5.8 попыток (5 целых) с 4.8 (4 целых) итерациями основного цикла в среднем.
- Ваш алгоритм "ternary-search" угадывает число в среднем за
	7.1 попыток (7 целых) с 2.8 (2 целых) итерациями основного цикла в среднем.
Вывод:
	- наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search;
	- стратегия с минимальным количеством _итераций_ основного цикла: ternary-search.
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber.png)

### Specifying game strategies

```bash
datascience_guessnumber --game-strategies random-snail,binary-search
```

#### Execution result:
```
- Ваш алгоритм "random-snail" угадывает число в среднем за
	31.9 попыток (31 целых) с 30.9 (30 целых) итерациями основного цикла в среднем.
- Ваш алгоритм "binary-search" угадывает число в среднем за
	5.8 попыток (5 целых) с 4.8 (4 целых) итерациями основного цикла в среднем.
Вывод:
	- наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search;
	- стратегия с минимальным количеством _итераций_ основного цикла: binary-search.
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber-strategies.png)

### Specifying attempts number and number segment

```bash
datascience_guessnumber --attempts 1000 --segment "[1, 100]"
```

#### Execution result:
```
- Ваш алгоритм "random-snail" угадывает число в среднем за
	31.9 попыток (31 целых) с 30.9 (30 целых) итерациями основного цикла в среднем.
- Ваш алгоритм "binary-search" угадывает число в среднем за
	5.8 попыток (5 целых) с 4.8 (4 целых) итерациями основного цикла в среднем.
- Ваш алгоритм "ternary-search" угадывает число в среднем за
	7.1 попыток (7 целых) с 2.8 (2 целых) итерациями основного цикла в среднем.
Вывод:
	- наиболее эффективная стратегия по количеству _единичных_ угадываний: binary-search;
	- стратегия с минимальным количеством _итераций_ основного цикла: ternary-search.
```

#### Screenshot:
![](docs/images/usage-datascience_guessnumber-attempts_segment.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)