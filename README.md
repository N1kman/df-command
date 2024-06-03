Данная программа реализует утилиту командной строки, которая поддерживает несколько дополнительных взаимоисключающих параметров и
должен обеспечивать следующую функциональность:
- --human — выполняет и анализирует системную команду Linux «df -h»;
- --inode — выполняет и анализирует системную команду Linux «df -i»;
- если опций нет, выполняет «df».

Результат выполнения JSON dict на стандартный вывод со следующими ключами:
- «status»: «success» | «failure»
- «error»: «error message» | «None»
- «result»: «None» или dict со следующими ключами:
  - В случае «df -h»: [Filesystem, Size, Used, Avail, Use%, Mounted on];
  - В случае «df -i»: [Filesystem, Inodes, IUsed, IFree, IUse%, Mounted on];
  - В случае «df»: [Filesystem, 1K-blocks, Used, Available, Use%, Mounted on].

Утилита использует Python 3.6.8, json, subprocess.Popen, argrapse.

Весь код покрыт <a href="tests">юнит-тестами</a>, используя модуль Unittest Python.

Код программы:
- <a href="df_utility/parsers">Классы утилиты для парсинга</a>
  - <a href="df_utility/parsers/parser_base.py">базовый класс(интерфейс)</a>
  - <a href="df_utility/parsers/df_parser.py">стандартная реализация(«df»)</a>
  - <a href="df_utility/parsers/df_human_parser.py">реализация для команды «df --human»</a>
  - <a href="df_utility/parsers/df_human_parser.py">реализация для команды «df --inode»</a>
- <a href="df_utility/parsers">Классы утилиты выполнения команд</a>
  - <a href="df_utility/executors/executer_base.py">базовый класс(интерфейс)</a>
  - <a href="df_utility/executors/df_executer.py">стандартная реализация(«df»)</a>
  - <a href="df_utility/executors/df_human_executer.py">реализация для команды «df --human»</a>
  - <a href="df_utility/executors/df_inode_executer.py">реализация «df --inode»</a>
- <a href="df_utility/parsers">Итоговый код с использованием своей утилиты</a>
