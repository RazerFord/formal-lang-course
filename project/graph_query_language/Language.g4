grammar Language;

program: (stmt SEMICOLON)* EOF;

stmt: print | bind;

print: PRINT expr;
bind: VAR ASSIGN expr;

String: STRING;
Int: DIGIT+;
Vertex: Int;
Edge: LP Int COMMA STRING COMMA RP;
Graph: LP LIST COMMA LIST RP;
Bool: BOOL;
T: BOOL | DIGIT | CHAR | STRING | Vertex | Edge;
LIST: LB RB | LB T (COMMA T)* RB;

expr:
	LP expr RP
	| VAR
	| VAL
	| LIST
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
	| LOAD STRING
	| expr INTERSECT expr
	| expr CONCAT expr
	| expr UNION expr
	| expr IN expr
	| expr KLEENE
	| expr EQUAL expr;

lambda: LP LAMBDA LIST ARROW expr RP;

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
LAMBDA: 'lambda';
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

VAL: BOOL;

PRINT: 'print';
ASSIGN: ':=';

CHAR: [a-zA-Z];
DIGIT: [0-9];
CHAR_D: CHAR | DIGIT;
VAR: CHAR CHAR_D*;
STRING: QUOT (CHAR_D | [ _])* QUOT;
BOOL: TRUE | FALSE;

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
