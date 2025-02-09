grammar Language;

program: (stmt SEMICOLON)* EOF;

stmt: print | bind;

print: PRINT expr;
bind: id ASSIGN expr;

PRINT: 'print';
ASSIGN: ':=';

expr:
	LP expr RP
	| var
	| val
	| lambda
	| SET_START OF expr TO expr
	| SET_FINAL OF expr TO expr
	| ADD_START OF expr TO expr
	| ADD_FINAL OF expr TO expr
	| GET_START OF expr
	| GET_FINAL OF expr
	| GET_REACHABLE OF expr
	| GET_VERTICES OF expr
	| GET_EDGES OF expr
	| GET_LABELS OF expr
	| MAP lambda expr
	| FILTER lambda expr
	| LOAD (string | var)
	| expr INTERSECT expr
	| expr CONCAT expr
	| expr UNION expr
	| expr IN expr
	| expr KLEENE
	| expr EQUAL expr;

lambda: LP LAMBDA_DEF list ARROW expr RP;

var: id;
val: integer | string | vertex | edge | list | bool | graph;

bool: TRUE | FALSE;
string: QUOT (CHAR | DIGIT)* QUOT;
integer: DIGIT+;
vertex: integer;
edge: LP integer COMMA string COMMA integer RP;
item: string | integer | vertex | edge | bool | var;
list: LB RB | LB item (COMMA item)* RB;
graph: LP list COMMA list RP;

id: (CHAR (CHAR | DIGIT)*);
CHAR: [a-zA-Z_];
DIGIT: [0-9];

SET_START: 'set_start';
SET_FINAL: 'set_final';
ADD_START: 'add_start';
ADD_FINAL: 'add_final';
GET_START: 'get_start';
GET_FINAL: 'get_final';
GET_REACHABLE: 'get_reachable';
GET_VERTICES: 'get_vertices';
GET_EDGES: 'get_edges';
GET_LABELS: 'get_labels';
MAP: 'map';
LAMBDA_DEF: 'lambda';
LOAD: 'load';
FILTER: 'filter';
ARROW: '->';
OF: 'of';
TO: 'to';
INTERSECT: '&';
CONCAT: '.';
UNION: '|';
IN: 'in';
KLEENE: '*';
EQUAL: '=';
TRUE: 'true';
FALSE: 'false';
COMMA: ',';
QUOT: '"';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
WS: [ \n\t\r]+ -> channel(HIDDEN);
COMMENT: '//' ~[\n]* -> skip;
SEMICOLON: ';';
