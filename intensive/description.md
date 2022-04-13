MVCC.
1) Что произойдет со строками, если выполняется ROLLBACK транзакции ?
При ROLLBACK изменения в транзакции откатываются
2) Выполнить sql запросы в двух процессах для таблицы workers:

| Процесс №1                                                                       | Процесс №2                                                                                        |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| begin;                                                                           |                                                                                                   |
| вставить две новых записи (name=Петр)                                            |                                                                                                   |
| для всех только что созданных  записей к значению поля name добавить значение id<br/> |                                                                                                   |
| отобразить все версии строк с которыми работали в текущей транзакции<br/>                                                                             | получить все строки таблицы. почему не видно изменений?                                           |
| commit;                                                                             |                                                                                                   |
|                                                                                     |                                                                                                   |
|begin;                                                                            | begin                                                                                             |
|для всех записей изменить значение поля name чтобы оно было в кавычках.                                                                                | для всех записей изменить значение поля name чтобы оно было в кавычках. <br/>Что произошло и почему? |
|commit;                                                                                | commit;<br/>получить все версии строк таблицы workers                                             |

Ответ на первый вопрос: Когда мы во второй консоли делаем запрос - то мы не видим результат выполнения транзакции, поскольку мы её ещё не закоммитили. Результат увидим после коммита.
ctid state xmin xmax t_ctid
"(0,8)",normal,719',719',"(0,10)"
"(0,9)",normal,719',719',"(0,11)"
"(0,10)",normal,719',0 (a),"(0,10)"
"(0,11)",normal,719',0 (a),"(0,11)"
Ответ на второй вопрос: Если мы уже совершаем транзакцию над этими записями, то во второй консоли при попытке изменить запись, которую мы уже меняем в первой - запрос зависнет.

Блокировки
1) В двух транзакциях добиться блокировки строки при попытке обновления одной и той же записи.
И с помощью представления pg_lock получить информацию о получившейся блокировке.

Результат блокировки:
intensive.public> UPDATE workers SET name = 'Иван' WHERE id=1
[2022-04-12 09:43:38] [25P02] ERROR: current transaction is aborted, commands ignored until end of transaction block
[2022-04-12 09:43:38] [57014] ERROR: canceling statement due to user request
[2022-04-12 09:43:38] Где: while updating tuple (0,2) in relation "workers"
Вывод информации по pg_lock:
relation,pg_locks,AccessShareLock,,6/118,253,true
virtualxid,,ExclusiveLock,,6/118,253,true
relation,workers_name_idx,RowExclusiveLock,,5/747,225,true
relation,workers_pkey,RowExclusiveLock,,5/747,225,true
relation,workers,RowExclusiveLock,,5/747,225,true
virtualxid,,ExclusiveLock,,5/747,225,true
transactionid,,ExclusiveLock,706,5/747,225,true
relation,pg_database_datname_index,AccessShareLock,,6/118,253,true
relation,pg_database,AccessShareLock,,6/118,253,true
relation,pg_database_oid_index,AccessShareLock,,6/118,253,true

