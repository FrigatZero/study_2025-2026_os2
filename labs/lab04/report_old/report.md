---
## Front matter
title: "Лабораторная работа №4. Работа с программными пакетами"
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

Получить навыки работы с репозиториями и менеджерами пакетов. [@tuis]

# Задание

- Изучить, как и в каких файлах подключаются репозитории для установки программного обеспечения; изучить основные возможности (поиск, установка, обновление, удаление пакета, работа с историей действий) команды dnf.
- Изучить и повторить процесс установки/удаления определённого пакета с использованием возможностей dnf.
- Изучить и повторите процесс установки/удаления определённого пакета с использованием возможностей rpm.

# Ход выполнения лабораторной работы

## Работа с репозиториями

Откроем терминал под учётной записью root. Перейдем в каталог /etc/yum.repos.d и узнаем какие репозитории в нем расположены.

![Репозитории в каталоге /etc/yum.repos.d](image/1.PNG){#fig:001 width=90%}

Откроем один из них, например epel-cisco-openh264.repo, и изучим его содержимое. В нем находится информация репозитория:

- название пакета;
- ссылка на скачивание;
- тип пакета;
- состояния (включен/выключен);
- срок истечения мета-данных;
- прочая информация о ключе gpg.

![Информация о пакетах в репозитории epel-cisco-openh264](image/2.PNG){#fig:002 width=90%}

Список репозиториев можно вывести более удобным способом, прописав команду dnf repolist. Она выводит два столбца: идентификатор и имя репозитория. Первый соответствует названию файла, а второй значению в поле name. На рисунке ниже можем убедиться, что репозитории из списка команды соответствуют тем, что находятся в каталоге.

![Список репозиториев команды dnf repolist](image/3.PNG){#fig:003 width=90%}

Выведем на экран список пакетов, в названии или описании которых есть слово user. Сделаем это командой dnf search "шаблон". Она выведет 3 вида совпадений: по названию и описанию, по названию, по описанию.

![Совпадения по имени и описанию](image/4.PNG){#fig:004 width=90%}

![Совпадения по имени](image/5.PNG){#fig:005 width=90%}

![Совпадения по описанию](image/6.PNG){#fig:006 width=90%}

Установим nmap, предварительно проверив наличие пакета в менеджере. В задании дополнительно необходимо применить команду dnf install nmap\*. В отличие от dnf install nmap, она установит все пакеты, которые начинаются с nmap. Например, в этот список попадет пакет nmap-ncat. Удалим установленные пакеты.

![Поиск пакетов nmap](image/7.PNG){#fig:007 width=90%}

![Установка nmap](image/8.PNG){#fig:008 width=90%}

![Установка nmap*, удаление nmap](image/9.PNG){#fig:009 width=90%}

![Удаление nmap*](image/10.PNG){#fig:010 width=90%}

Получим список групп пакетов и установим RPM Development Tools.

![Список групп пакетов](image/11.PNG){#fig:011 width=90%}

![Установка RPM Development Tools](image/12.PNG){#fig:012 width=90%}

Также удалим его.

![Удаление RPM Development Tools](image/13.PNG){#fig:013 width=90%}

Просмотрим историю использования команд dnf и отменим последнее действие, чтобы использовать пакет rpm в следующем задании.

![Манипуляции с историей команд dnf](image/14.PNG){#fig:014 width=90%}

## Использование rpm

Скачаем rpm-пакет lynx.

![Установка пакета lynx](image/15.PNG){#fig:015 width=90%}

Найдем каталог, в который был помещен пакет, перейдем в него и установим его. Определим расположение исполняемого файла: /usr/bin/lynx.

![Ручная установка пакета через команду rpm](image/16.PNG){#fig:016 width=90%}

Определим по имени файла к какому пакету принадлежит lynx. Получим дополнительную информацию о содержимом пакета, список всех файлов в пакете, перечень файлов с документацией пакета и перечень и месторасположение конфигурационных файлов пакета.

![Поиск пакета rpm, информация о содержимом пакета](image/17.PNG){#fig:017 width=90%}

![Файлы документации и файлы конфигов lynx](image/17_2.PNG){#fig:018 width=90%}

Попробуем вывести рпсположение и содержание скриптов, выполнямых при установке пакета. В моем случае их нет, поэтому продолжим.

В отдельном терминале под своей учётной записью откроем lynx. Браузер успешно запустился.

![Окно браузера lynx](image/18.PNG){#fig:019 width=90%}

Вернемся в root и удалим lynx.

![Удаление программы lynx](image/19.PNG){#fig:020 width=90%}

Совершим похожие действия для пакета dnsmasq.

![Список пакетов dnsmasq](image/20.PNG){#fig:021 width=90%}

Определим расположение dnsmasq и к какому пакету он относится. Получим список всех файлов в пакете, дополнительную информацию о содержимом пакета, перечень файлов с документацией пакета и перечень и месторасположение конфигурационных фалов пакета.

![Пакет файла dnsmasq и дополнительная информация](image/21.PNG){#fig:022 width=90%}

![Файлы документации и файлы конфигов dnsmasq](image/21_2.PNG){#fig:023 width=90%}

Выведем на экран расположение и содержание скриптов, выполняемых при установке пакета. Удалим пакет dnsmasq.

![Скрипты пакета dnsmasq](image/22.PNG){#fig:024 width=90%}

Всего для пакета dnsmasq существует 4 скрипта:

- preinstall: предварительно создает пользователей чтобы RPM мог установить файлы от лица этого пользователя;
- postinstall: осуществляет первоначальную установку;
- preuninstall: удаляет пакет rpm;
- postuninstall: обновление пакета, вместо удаления.

# Ответы на контрольные вопросы

1. Какая команда позволяетвам искать пакет rpm, содержащий файл useradd?

- Можно использовать rpm -qf $(which useradd).

2. Какие команды вам нужно использовать, чтобы показать имя группы dnf, которая содержит инструменты безопасности и показывает, что находится в этой группе?

- Можно использовать последовательность dnf group list | grep -i security , dnf group info "группа, которую нашли"
- Или же одной командой dnf group info "*security*"

3. Какая команда позволяет вам установить rpm, который вы загрузили из Интернета и который не находится в репозиториях?

- sudo rpm -i пакет.rpm или sudo dnf install (путь к пакету)/пакет.rpm

4. Вы хотите убедиться, что пакет rpm, который вы загрузили, не содержит никакого опасного кода сценария. Какая команда позволяет это сделать?

- Можно использовать rpm -qp --scripts пакет.rpm

5. Какая команда показывает всю документацию в rpm?

- rpm -qd имя_пакета

6. Какая команда показывает, какому пакету rpm принадлежит файл?

- rpm -qf $(which путь_до_исполняемого_файла) или же rpm -qf $(which имя_исполняемого_файла)

# Вывод

В результате выполнения лабораторной работы я получил навыки работы с репозиториями, менеджером пакетов dnf и пакетами rpm.

# Список литературы{.unnumbered}

::: {#refs}
:::
