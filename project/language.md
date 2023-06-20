# Оглавление
- [Оглавление](#оглавление)
  - [Описание абстрактного синтаксиса языка](#описание-абстрактного-синтаксиса-языка)
  - [Описание конкретного синтаксиса языка](#описание-конкретного-синтаксиса-языка)
  - [Пример](#пример)
  - [Генерация парсера](#генерация-парсера)
  - [Система типов](#система-типов)
  - [Используемые алгоритмы](#используемые-алгоритмы)
  - [Запуск](#запуск)


## Описание абстрактного синтаксиса языка

```
prog = List<stmt>

stmt =
    bind of var * expr
  | print of expr

val =
    String of string
  | Int of int
  | Graph of graph
  | Vertex of val
  | Edge of val * string * val
  | Bool of bool

expr =
    Var of var                   // переменные
  | Val of val                   // константы
  | Set_start of Set<val> * expr // задать множество стартовых состояний
  | Set_final of Set<val> * expr // задать множество финальных состояний
  | Add_start of Set<val> * expr // добавить состояния в множество стартовых
  | Add_final of Set<val> * expr // добавить состояния в множество финальных
  | Get_start of expr            // получить множество стартовых состояний
  | Get_final of expr            // получить множество финальных состояний
  | Get_reachable of expr        // получить все пары достижимых вершин
  | Get_vertices of expr         // получить все вершины
  | Get_edges of expr            // получить все рёбра
  | Get_labels of expr           // получить все метки
  | Map of lambda * expr         // классический map
  | Filter of lambda * expr      // классический filter
  | Load of path                 // загрузка графа
  | Intersect of expr * expr     // пересечение языков
  | Concat of expr * expr        // конкатенация языков
  | Union of expr * expr         // объединение языков
  | Star of expr                 // замыкание языков (звезда Клини)
  | Smb of expr                  // единичный переход
  | expr in expr                 // проверка содержится ли первое выражение внутри второго

lambda =
    Lambda of List<val> * expr
```

## Описание конкретного синтаксиса языка

```
grammar language;

program: (stmt SEMICOLON)* EOF;

stmt: PRINT | BIND;

PRINT: print expr;
BIND: VAR ASSIGN expr;

String: STRING
Int: DIGIT+
Vertex: INT
Edge: LP INT COMMA STRING COMMA INT RP
Graph: LP LIST COMMA LIST RP


expr: LP expr RP
    | var
    | val
    | SET_START OF (var | INT | LIST) TO (var | Graph)
    | SET_FINAL OF (var | INT | LIST) TO (var | Graph)
    | ADD_START OF (var | INT | LIST) TO (var | Graph)
    | ADD_FINAL OF (var | INT | LIST) TO (var | Graph)
    | GET_START OF (var | Graph)
    | GET_FINAL OF (var | Graph)
    | GET_REACHABLE OF (var | Graph)
    | GET_VERTICES OF (var | Graph)
    | GET_EDGES OF (var | Graph)
    | GET_LABELS OF (var | Graph)
    | MAP lambda (var | LIST)
    | FILTER lambda (var | LIST)
    | LOAD STRING
    | (var | Graph | STRING) INTERSECT (var | Graph | STRING)
    | (var | Graph | STRING) CONCAT (var | Graph | STRING)
    | (var | Graph | STRING) UNION (var | Graph | STRING)
    | (var | INT | STRING | Edge) IN (var | Graph | STRING)
    | (var | Graph | STRING) KLEENE
    | (var | val) EQUAL (var | val)

lambda: LP LAMBDA LIST ARROW expr RP
val: INT | STRING | LIST | Edge | Graph;

COMMA: ','
ASSIGN: ':='
EQUAL: '='
QUOT: '"'
LP: '('
RP: ')'
LB: '{'
RB: '}'
PRINT: 'print'
BOOL: TRUE | FALSE
OF: 'of'
SET_START: 'set_start'
SET_FINAL: 'set_final'
ADD_START: 'add_start'
ADD_FINAL: 'add_final'
GET_START: 'get_start'
GET_FINAL: 'get_final'
GET_REACHABLE: 'get_reachable'
GET_VERTICES: 'get_vertices'
GET_EDGES: 'get_edges'
GET_LABELS: 'get_labels'
TO: 'to'
LAMBDA: 'lambda'
LOAD: 'load'
MAP: 'map'
FILTER: 'filter'
ARROW: '->'
TRUE: 'true' | 'false'
DIGIT: [0-9]
CHAR: [a-zA-Z]
CHAR_D: CHAR | DIGIT
VAR: CHAR CHAR_D*
STRING: QUOT (CHAR | DIGIT)* QUOT
T: BOOL | DIGIT | CHAR | STRING | vertex | edge
LIST: LB RB
    | LB T ( COMMA T )* RB
INTERSECT: '&'
CONCAT: '.'
UNION: '|'
IN: 'in'
KLEENE: '*'

COMMENT: '//'
```

## Пример

```Go
// Загрузить граф из файла
g := load "./test/graph";

// Создать переменную
start := 1;

// Установаить стартовую вершину start в графе g
ng := set_start of start to g;

// Инициализировать лист
list := {1, 2, 3};

// Установить финальные вершины в графе
nng := set_final of list tp ng;

// Получить достижимые вершины
vs := get_reachable nng;

// Отфильтровать вершины
vsf := filter (lambda { v } -> v = start) vs;

print vsf;
```

## Генерация парсера

Инструкция по генерации парсера.

Изначально необходимо уставить все зависимости. Для этого в корневой директории необходимо выполнить следующую комманду:

```shell
pip install -r requirements.txt
```

Затем необходимо сгенерировать парсер. Для этого в `project/graph_query_language` необходимо выполнить следующую комманду:

```shell
antlr4 -Dlanguage=Python3 -visitor Language.g4 -o language
```

## Система типов

Достыпные типы перечислены в таблице.

| Тип 	   | Краткое описание       |
|----------|------------------------|
| Edge     | Ребро графа            |
| String   | Строка                 |
| Graph    | Граф                   |
| Regex    | Регулярное выражение   |
| Bool     | Логический тип         |
| Lambda   | Lambda функция         |
| int      | Целое число            |

Тип `Regex` явно задать нельзя. `String` автоматически приводится к типу `Regex`, если к нему применить одну из операций `&`  `|`  `.`, при этом сама переменная типа `String` может быть как левым, так правым операндом. Доступны следующие вариации:

> `String op String`

> `Regex op Regex`

> `Graph op Regex`

> `Graph op String`

где `op` - `&`  `|`  `.`

Система типов устроена так, что если инициализировать переменную одним типом, то ей нельзя присвоить значения другого типа.

## Используемые алгоритмы

Для операции `Graph & Regex` используется алгоритм пересечения конечных автоматов, реализованный в домашней работе.

Для остальных операций используются алгоритмы из библиотеки `pyformlang`.

## Запуск

Файл с программой должен иметь расширение `lng`.

Пример программы.

`test.lng`:
```Go
print "Hello world";
```
Чтобы запустить программу в консоли необходимо выполнить:

```Shell
python -m project.graph_query_language test.lng
```
