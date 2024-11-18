from collections import defaultdict

class Table:
    def __init__(self, table_id, name, row_count, database_id):
        self.table_id = table_id
        self.name = name
        self.row_count = row_count
        self.database_id = database_id

class Database:
    def __init__(self, database_id, name):
        self.database_id = database_id
        self.name = name

class DatabaseTableAssociation:
    def __init__(self, table_id, database_id):
        self.table_id = table_id
        self.database_id = database_id


databases = [
    Database(database_id=1, name="Legal pluralism of the North Caucasus"),
    Database(database_id=2, name="Tradition"),
    Database(database_id=3, name="Language"),
    Database(database_id=4, name="Database Auls")
]

tables = [
    Table(table_id=1, name="AdatLaw", row_count=636, database_id=1),
    Table(table_id=2, name="Darkquante languages", row_count=6543, database_id=3),
    Table(table_id=3, name="Interclass relations", row_count=2345, database_id=2),
    Table(table_id=4, name="Leki language family", row_count=765, database_id=3),
    Table(table_id=5, name="Feud", row_count=200, database_id=2),
    Table(table_id=6, name="Kurah", row_count=642, database_id=4),
    Table(table_id=7, name="Qala-Qouraish", row_count=200, database_id=4),
]

associations = [
    DatabaseTableAssociation(table_id=1, database_id=1),
    DatabaseTableAssociation(table_id=2, database_id=3),
    DatabaseTableAssociation(table_id=3, database_id=2),
    DatabaseTableAssociation(table_id=4, database_id=3),
    DatabaseTableAssociation(table_id=5, database_id=2)
]

# «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список всех связанных сотрудников и отделов, отсортированный по отделам, сортировка по сотрудникам произвольная.
# "База данных" и "Таблица данных" связаны соотношением один-ко-многим. Выведен список всех связанных таблиц и баз данных, отсортированный по Таблицам, сортировка по Базам произвольная
sorted_data = sorted(tables, key=lambda x: x.database_id)
result_1 = [
    (database.name, table.name) for database in databases for table in sorted_data if table.database_id == database.database_id
]

# «Отдел» и «Сотрудник» связаны соотношением один-ко-многим. Выведите список отделов с суммарной зарплатой сотрудников в каждом отделе, отсортированный по суммарной зарплате.
# Сортировка по числу записей в таблице данных
database_row_count = defaultdict(int)
for table in tables:
    database_row_count[table.database_id] += table.row_count

result_2 = sorted(
    [(database.name, database_row_count[database.database_id]) for database in databases],
    key=lambda x: x[1],
    reverse=True
)

# «Отдел» и «Сотрудник» связаны соотношением многие-ко-многим. Выведите список всех отделов, у которых в названии присутствует слово «отдел», и список работающих в них сотрудников.
# Вывод всех баз данных, в названии которых есть слово Database, и список таблиц в них
result_3 = [
    (database.name, [table.name for table in tables if table.database_id == database.database_id])
    for database in databases if "Database" in database.name
]


print(result_1)
print(result_2)
print(result_3)
