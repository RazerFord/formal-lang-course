grammar Language;

program: (EOL? WS? stmt SEMICOLON EOL? WS?)* EOF;

stmt: PRINT expr | VAR ASSIGN expr;

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

SET_START: WS? 'set_start' WS?;
SET_FINAL: WS? 'set_final' WS?;
ADD_START: WS? 'add_start' WS?;
ADD_FINAL: WS? 'add_final' WS?;
GET_START: WS? 'get_start' WS?;
GET_FINAL: WS? 'get_final' WS?;
GET_REACHABLE: WS? 'get_reachable' WS?;
GET_VERTICES: WS? 'get_vertices' WS?;
GET_EDGES: WS? 'get_edges' WS?;
GET_LABELS: WS? 'get_labels' WS?;
MAP: WS? 'map' WS?;
LAMBDA: WS? 'lambda' WS?;
LOAD: 'load';
FILTER: 'filter';
ARROW: '->';
OF: WS? 'of' WS?;
TO: WS? 'to' WS?;
INTERSECT: WS? '&' WS?;
CONCAT: WS? '.' WS?;
UNION: WS? '|' WS?;
IN: WS? 'in' WS?;
KLEENE: WS? '*' WS?;
EQUAL: WS? '=' WS?;

VAL: BOOL;

PRINT: WS? 'print' WS?;
ASSIGN: WS? ':=' WS?;

CHAR: [a-zA-Z];
DIGIT: [0-9];
CHAR_D: CHAR | DIGIT;
VAR: CHAR CHAR_D*;
STRING: QUOT (CHAR_D | [ _])* QUOT;
BOOL: TRUE | FALSE;

TRUE: 'true';
FALSE: 'false';
COMMA: WS? ',' WS?;
QUOT: WS? '"' WS?;
LP: WS? '(' WS?;
RP: WS? ')' WS?;
LB: WS? '{' WS?;
RB: WS? '}' WS?;
SPACE: ' ';
WS: [ \t\r]+ -> skip;
SEMICOLON: WS? ';' WS?;
EOL: [\n]+;