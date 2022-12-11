Название каждого файла говорит само за себя.
Запуск игры осуществляется в модуле Gamerun. Tower и Enemy содержат базовые классы которые наследуют другие классы башен и противников соответственно.
Игра начала создаваться еще в июне, но наиболее активная фаза создания пришлась на последние 10 дней, где было написано половины кода.
Из за чего не успел спроектировать уровни( в игре только один) и сбалансировать башни и характеристики противников.
Вся логика игры прописана в модуле game.

Всё реализованные механики и идеи можно легко увидеть в ходе игры: (изменение разрешения, громкости музыки, переход между окнами меню, обьекты на карте которые можно уничтожить за деньги, разнообразие волн,разбиение волн на мини волны( в мини волне один вид врагов, в параметрах загрузки мини волны указывается - вид противника, его уровень, наличие щита, количество противников, задержка между выходом противников, задержка до перехода к следующей мини волне), виды мини волны(1 вид- противники в этой мини волне идут сразу по два в два ряда, 2 вид - противники идут по одному из случайного положения начала дороги), возможность выйти из игры в меню, начать сначала, выбор алгоритма по которому башня может выбирать цель и так далее.

Модуль button содержит все классы кнопок которые используются в игре.

Модуль wave_stats содержит класс имеющий только статистические методы, первый из которых называется level1, который принимает параметры в виде ширины и высоты картинки дороги( которую нужно будет отобразить в окне выбора уровней ) и возращает картинку дороги, на которой рисуются ТОЛЬКО сама картинка с дорогой, водой(элементами которые никак нельзя уничтожить в ходе игры). При отсутствии данных параметров, метод level1 возращает все характеристики уровня(здоровье, начальное кол-во денег,закрытые клетки, список разрушаемых обьектов - кустов и камней.

Изменение разрешения игры осуществляется путем изменения атрибутов класса, имеющих значение или параметры напрямую зависящих от значения ширины и высоты окна игры.
Для этого у каждого класса имеется статистический метод scaling_attributes который меняет все это добро. В модуле game, где содержится класс Game, импортируются множество других классов. Класс Game содержит статистический метод scaling_attributes который вызывает этот же метод у других классов импортированных в этот модуль. Аналогично с классом Levels модуля wave_stats и с классом LevelSelection модуля level_selection

P.S: readme в большей части писал 11 числа, также сегодня убрал ненужные импорты, которые забыл убрать. Мусора и лишних строк по прежнему много, ведь код писался до самих 12 часов 10 декабря.
