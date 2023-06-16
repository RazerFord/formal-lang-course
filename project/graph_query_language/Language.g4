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
	| set_start
	| set_final
	| add_start
	| add_final
	| get_start
	| get_final
	| get_reachable
	| get_vertices
	| get_edges
	| get_labels
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
val: integer | string | edge | list | graph;

string: STRING_LITERAL;
integer: DIGIT+;
edge: LP integer COMMA string COMMA integer RP;
item: string | integer | edge | var | list;
list: LB RB | LB item (COMMA item)* RB;
graph: LP list COMMA list RP;

id: (CHAR (CHAR | DIGIT)*);
CHAR: [a-zA-Z_];
DIGIT: [0-9];

set_start: 'set_start' of source to target;
set_final: 'set_final' of source to target;
add_start: 'add_start' of source to target;
add_final: 'add_final' of source to target;
target: var | graph;
source: var | integer | list;

get_start: 'get_start' of target;
get_final: 'get_final' of target;

get_reachable: 'get_reachable' of target;
get_vertices: 'get_vertices' of target;
get_edges: 'get_edges' of target;
get_labels: 'get_labels' of target;

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
COMMA: ',';
QUOT: '"';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
WS: [ \n\t\r]+ -> channel(HIDDEN);
COMMENT: '//' ~[\n]* -> skip;
SEMICOLON: ';';
STRING_LITERAL: QUOT (~["\\] | '\\' .)* QUOT;