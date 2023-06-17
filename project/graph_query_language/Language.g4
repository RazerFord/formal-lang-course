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
	| map
	| filter
	| load
	| intersect
	| concat
	| union
	| in
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

map: 'map' (lambda | var) ':' iterable;
filter: 'filter' (lambda | var) ':' iterable;
iterable: list | var;
LAMBDA_DEF: 'lambda';
load: 'load' (string | var);
ARROW: '->';
of: 'of';
to: 'to';
intersect: binary_l '&' binary_r;
concat: binary_l '.' binary_r;
union: binary_l '|' binary_r;
in: binary_in_l 'in' binary_r;
kleene: binary_l '*';
equal: expr '=' expr;
binary_l: graph | var;
binary_r: graph | var;
binary_in_l: var | integer | string | edge;

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