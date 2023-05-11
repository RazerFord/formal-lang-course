grammar Language;

program: (EOL? WS? stmt SEMICOLON EOL?)* EOF;

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
	LP expr RP;
	// | var
	// | val
	// | SET_START OF (LIST | expr) TO expr
	// | SET_FINAL OF (LIST | expr) TO expr
	// | ADD_START OF (LIST | expr) TO expr
	// | ADD_FINAL OF (LIST | expr) TO expr
	// | GET_START OF expr
	// | GET_FINAL OF expr
	// | GET_REACHABLE OF expr
	// | GET_VERTICES OF expr
	// | GET_EDGES OF expr
	// | GET_LABELS OF expr
	// | MAP lambda expr
	// | FILTER lambda expr
	// | LOAD STRING
	// | expr INTERSECT expr
	// | expr CONCAT expr
	// | expr UNION expr
	// | expr IN expr
	// | expr KLEENE
	// | expr EQUAL expr;

PRINT: WS? 'print' WS?;
ASSIGN: WS? '=' WS?;

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
SPACE: ' ';
WS: [ \t\r]+ -> skip;
SEMICOLON: WS? ';' WS?;
EOL: [\n]+;