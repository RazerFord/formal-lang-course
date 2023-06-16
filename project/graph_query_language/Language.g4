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
	| set_start of expr to expr
	| set_final of expr to expr
	| add_start of expr to expr
	| add_final of expr to expr
	| get_start of expr
	| get_final of expr
	| get_reachable of expr
	| get_vertices of expr
	| get_edges of expr
	| get_labels of expr
	| map lambda expr
	| filter lambda expr
	| load (string | var)
	| expr intersect expr
	| expr concat expr
	| expr union expr
	| expr in expr
	| expr kleene
	| expr equal expr;

lambda: LP LAMBDA_DEF list ARROW expr RP;

var: id;
val: integer | string | edge | list | bool | graph;

bool: TRUE | FALSE;
string: QUOT (CHAR | DIGIT)* QUOT;
integer: DIGIT+;
edge: LP integer COMMA string COMMA integer RP;
item: string | integer | edge | bool | var;
list: LB RB | LB item (COMMA item)* RB;
graph: LP list COMMA list RP;

id: (CHAR (CHAR | DIGIT)*);
CHAR: [a-zA-Z_];
DIGIT: [0-9];

set_start: 'set_start';
set_final: 'set_final';
add_start: 'add_start';
add_final: 'add_final';
get_start: 'get_start';
get_final: 'get_final';
get_reachable: 'get_reachable';
get_vertices: 'get_vertices';
get_edges: 'get_edges';
get_labels: 'get_labels';
map: 'map';
LAMBDA_DEF: 'lambda';
load: 'load';
filter: 'filter';
ARROW: '->';
of: 'of';
to: 'to';
intersect: '&';
concat: '.';
union: '|';
in: 'in';
kleene: '*';
equal: '=';
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
