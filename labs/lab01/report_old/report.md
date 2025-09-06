---
## Front matter
title: "Лабораторная работа №1. Установка и конфигурация операционной системы на виртуальную машину"
subtitle: "Отчёт"
author: "Сергеев Даниил Олегович"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Целью данной работы является приобретение практических навыков установки операционной системы на виртуальную машину, настройки минимально необходимых для дальнейшей работы сервисов. [@tuis]

# Задание

- Установить образ Rocky Linux в Virutal Box.
- Настроить параметры в установщике ОС.
- Подключить и установить образ диска дополнений гостевой ОС.

# Ход выполнения лабораторной работы

## Создание виртуальной машины

Откроем менеджер виртуальных машин Oracle VirtualBox и нажмем на кнопку создать в графическом интерфейсе. Выберем тип машины Linux, подтип Red Hat (64-bit). Зададим имя, удовлетворяющее соглашению о наименовании.

![Окно создания ВМ](image/1.PNG){#fig:001 width=70%}

Выделим размер основной памяти виртуальной машины до 8192 МБ и 4 процессора.

![Оборудование ВМ](image/2.PNG){#fig:002 width=70%}

Для жёсткого диска выделим 40 ГБ.

![Жёсткий диск](image/3.PNG){#fig:003 width=70%}

## Установка операционной системы

Запустим ОС. Выберем вариант Install Rocky Linux 9.6.

![Установка ОС](image/4.PNG){#fig:004 width=70%}

Поставим язык English в качестве основного в ОС. В качестве дополнительного поставим русский язык. Также добавим русскую раскладку клавиатуры и возможность её переключения через сочетание клавиш Alt+Shift.

![Выбор основного языка](image/5.PNG){#fig:005 width=70%}

![Выбор языка для раскладки](image/6.PNG){#fig:006 width=70%}

![Выбор второго языка системы](image/7.PNG){#fig:007 width=70%}

В разделе выбора программ укажем в качестве базового окружения Server with GUI, а в качестве дополнительного Development Tools. Отключим KDUMP

![Выбор базового окружения](image/8.PNG){#fig:008 width=70%}

Включим сетевое соединение и в качестве имени узла укажем dosergeev.localdomain.

![Настройка сетевого соединения](image/9.PNG){#fig:009 width=70%}

Установим пароль для root, разрешение на ввод пароля для root при использовании SSH. Затем зададим локального пользователя с правами администратора и пароль.

Начнем установку ОС. После её завершения корректно перезагрузим ОС. Подключим образ гостевой ОС и начнем установку. После неё снова перезагрузим Rocky.

![Ход установки дополнений гостевой ОС](image/10.PNG){#fig:010 width=70%}

# Ход выполнения домашнего задания

1. Дождемся загрузки графического окружения и откроем терминал. Пропишем команду dmesg и узнаем последовательность загрузки системы.

![Вывод команды grep (1)](image/11.PNG){#fig:011 width=70%}

![Вывод команды grep (2)](image/12.PNG){#fig:012 width=70%}

2. Получим имформацию о:
- Версии ядра Linux -> 5.14.0-570.37.1.el9_6.x86_64
- Частоте процессора -> 3400 MHz
- Модели процессора -> AMD Ryzen 5 2600
- Объёме доступной ОЗУ -> ~6 GB
- Типе гипервизора -> KVM
- Типе файловой системы корневого раздела -> XFS
- Последовательности монтирования файловых систем -> Корневая система(dm-0/XFS) -> Дополнительная файловая система (sda1/XFS)

# Ответы на контрольные вопросы

1. Команды терминала для:
- получения справки о команде: man, например: man cd
- перемещения по файловой системе: cd, например: cd ~
- просмотра содержимого каталога: ls, например: ls ~/
- определения объёма каталога: du -sh, например: du -sh ~/
- создания/удаления каталогов/файлов: mkdir, rmdir(rm -r), touch, rm, например: mkdir work/rm -r work
- задания определённых прав на файл/каталог: chmod, например: chmod a=rwx passwords.txt
- просмотра истории команд: history

2. Учётная запись пользователя хранит в себе имя, пароль, уникальный UID пользователя и GID группы, домашний каталог и командную оболочку пользователя. В качестве команд можно использовать id и whoami.

3. Файловая система — это способ организации, хранения и управления данными на носителе информации. XFS - высокопроизводительная ФС, используется на серверах для работы с большими данными. Ext4 - стандартная ФС большинства дистрибутивов Linux, поддерживает журналы, может быть как корневым, так и домшним разделом.

4. Чтобы посмотреть подмонтированные файловые системы, можно использовать команды mount или findmnt (более удобная).

5. Чтобы удалить зависший процесс, нужно найти его UID командой ps и завершить командой kill. Если она не помогает то надо его устранить с помощью kill -9.

# Вывод

В результате выполнения лабораторной работы я приобрел навыки установки операционной системы на виртуальную машину и научился минимально настраивать систему для дальнейшей работы сервисов.

# Список литературы{.unnumbered}

::: {#refs}
:::
