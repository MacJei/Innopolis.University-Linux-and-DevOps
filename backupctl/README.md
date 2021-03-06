## Backupctl
### Задание

Вы участвуете в стартапе, создающем инструмент для удобных бэкапов. Вданный момент стартап начинает делать mvp своего продукта.
Ваша цель - создать cli-инструмент, создающий резервную копию папки сфайлами. backupctl.
Содержание папки и файлов значение не имеет.
Скрипт должен запускаться из терминала, обязательно принимать путь допапки, которую надо заархивировать и путь до папки в которую следуетсложить архив.
В stdout должен возвращаться абсолютный путь до созданного архива.Опционально можно указать при запуске программы алгоритм сжатия, поумолчанию gztar.
Имя архива должно иметь вид:<исходное_название_папки>_<дата_и_время_создания_архива_в_таймзоне_utc>.<расширение>
Программа должна вести журнал своего использования, записывая привызове себя в файл csv или sqlite3 следующую информацию:абсолютный путь архивируемой папки, 
абсолютный путь к созданномуархиву (если он был создан), дату и время вызова программы, статус(success или fail) с которым отработала программа.
Путь до создаваемого журнала вызовов тоже можно задать опционально, поумолчанию файл создаётся в той же директории что и скрипт и имеетназвание journal.
Провальные случаи (например, отсутствие указанной папки или недостатокправ на запись в целевую папку) следует выгружать в stderr
Ошибки при формировании архива (например закончилось место) илиинформация о плохих параметрах запуска - тоже отправляются в stderr
Формат передаваемых параметров можно определить произвольно, нонеобходимо чтобы использование программы с параметром `--help` давало полную исчерпывающую не двусмысленную 
информацию о томкак пользоваться вашей программой.

Ожидаемый пример использования программы:

$>./backupctl.py --directory /tmp/mydir --output /home/user/alex/ -a zip -jjournal.csv/home/user/alex/mydir_2020-09-12_04:06:34.zip

Ожидаемый результат в ФС:

1 - создался архив

2 - пополнились записи в файле journal.csv

Разрешается использовать как стандартные так и сторонние модули(например click, fire, docopt).
в случае использования сторонних решений необходимо наличие файлаrequirements.txt

### Критерии оценки
1 - Программа реализована, работает без нареканий, адекватноотрабатывает как позитивные так и негативные случаи 

0,5 - Часть требований не реализована или работает не так как требуется взадании 

0 - Задание не выполнено, ни одно из требований не реализованоправильно.

---------------------------------------------------------------------------------------------------------------------------------
## Запуск 
```
./backupctl.py -d /home/ako/innopolis/game -o /home/ako/innopolis/backupctl -j journal.csv
```
