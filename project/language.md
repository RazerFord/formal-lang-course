# Оглавление
- [Оглавление](#оглавление)
  - [Описание абстрактного синтаксиса языка](#описание-абстрактного-синтаксиса-языка)
  - [Описание конкретного синтаксиса языка](#описание-конкретного-синтаксиса-языка)
  - [Примеры](#примеры)


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

print: print expr;
bind: VAR ASSIGN expr;

String: STRING
Int: DIGIT+
Vertex: INT
Edge: LP INT COMMA STRING COMMA RP
Graph: LP LIST COMMA LIST RP
Bool: BOOL


expr: LP expr RP
    | var
    | val
    | SET_START OF LIST TO expr
    | SET_FINAL OF LIST TO expr
    | ADD_START OF LIST TO expr
    | ADD_FINAL OF LIST TO expr
    | GET_START OF expr
    | GET_FINAL OF expr
    | GET_REACHABLE OF expr
    | GET_VERTICES OF expr
    | GET_EDGES OF expr
    | GET_LABELS OF expr
    | MAP lambda expr
    | FILTER lambda expr
    | LOAD STRING
    | expr INTERSECT expr
    | expr CONCAT expr
    | expr UNION expr
    | expr IN expr
    | expr KLEENE

lambda: LAMBDA LP LIST RP ARROW expr

COMMA: ','
ASSIGN: ':='
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
```

## Примеры