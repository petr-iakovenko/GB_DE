"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше
хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный
проект; можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах
(добавлять детали)?
"""

# скрипт les_7_ex_1.py - обращается к файлу "name_dir.csv"


"""
2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом 
редакторе «руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки 
использовать нельзя.
"""



"""
3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» 
в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:

|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены 
в родительских папках (они играют роль пространств имён); предусмотреть возможные исключительные 
ситуации; это реальная задача, которая решена, например, во фреймворке django.
"""



"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи
— верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов 
(в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей 
(начинаем с 0), например:

    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""


"""
5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, 
в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:

  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
"""