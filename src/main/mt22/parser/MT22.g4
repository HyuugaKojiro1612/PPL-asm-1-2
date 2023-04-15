// 2012528
grammar MT22;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()

    if tk == self.UNCLOSE_STRING:
        y = str(result.text)
        if y[-1] == '\n' or y[-1] == '\r':
            raise UncloseString(y[1:-1])
        else:
            raise UncloseString(y[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options{
	language=Python3;
}
// Declarations
program				: decllist EOF ;
decllist			: decl decllist | decl ;
decl				: vardecl | funcdecl ;

vardecl				: vardecl_short | vardecl_full ;
vardecl_short		: idlist COLON var_type SEMI ;
vardecl_full		: varrec SEMI ;
varbase             : ID COLON var_type EQUAL expr ;
varrec				: ID COMMA varrec COMMA expr 
                    | ID COLON var_type ASSIGN expr ;

paramdecllist		: paramdeclprime |  ;
paramdeclprime		: paramdecl COMMA paramdeclprime | paramdecl ;
paramdecl			: INHERIT? OUT? ID COLON var_type ;

funcdecl			: funcprototype funcbody ;
funcprototype		: ID COLON FUNCTION return_type LP paramdecllist RP INHERIT ID 
                    | ID COLON FUNCTION return_type LP paramdecllist RP ;
funcbody			: block_stmt ; // a block statement



element_type 		: INTEGER | FLOAT | STRING |BOOLEAN ;
var_type			: element_type | AUTO | array_type ;
return_type			: element_type | VOID | AUTO | array_type ;
array   			: ID COLON array_type ;
array_type          : ARRAY LSB dim RSB OF element_type ;
idlist 				: ID COMMA idlist | ID ;
dim 			    : INTLIT COMMA dim | INTLIT ;
// // literal            	: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT ; 
// // literallist 		: literal COMMA literallist | literal ;



exprlist 			: expr COMMA exprlist | expr ;
expr				: exp1 DOUBLE_COLON exp1 | exp1 ;
exp1				: exp2 relationalOp exp2 | exp2 ;
exp2				: exp2 (BOOL_CONJ | BOOL_DISJ) exp3 | exp3 ;
exp3				: exp3 (ADD | SUB) exp4 | exp4 ;
exp4				: exp4 (MUL | DIV | REMAINDER) exp5 | exp5 ;
exp5				: BOOL_NEGA exp5 | exp6 ;
exp6				: SUB exp6 | exp7 ;
exp7				: ID indexOp | operand ;



relationalOp		: EQUAL | NOT_EQUAL | GREATER_THAN | LESS_THAN | GREATER_THAN_EQ | LESS_THAN_EQ ;
// logicalOp	        : BOOL_CONJ | BOOL_DISJ ;
// addingOp	        : ADD | SUB ;
// multiplyingOp		: MUL | DIV | REMAINDER ;
indexOp 			: LSB exprlist RSB ;

// operands may be constants, variables, data returned by another operator, or data returned by a function call

stmtlist			: (stmt | vardecl) stmtlist |  ;
// nullable_stmt       : stmt | SEMI ;
stmt				: /*vardecl |*/ asm_stmt | if_stmt | for_stmt | while_stmt | dowhile_stmt | break_stmt | continue_stmt | return_stmt | call_stmt | block_stmt ;
asm_stmt			: ID ASSIGN expr SEMI
                    | ID indexOp ASSIGN expr SEMI ;
if_stmt				: IF LP expr RP stmt
                    | IF LP expr RP stmt ELSE stmt ;
for_stmt			: FOR LP ID indexOp? ASSIGN expr COMMA expr COMMA expr RP stmt ;
while_stmt			: WHILE LP expr RP stmt ;
dowhile_stmt		: DO block_stmt WHILE LP expr RP SEMI ;
break_stmt			: BREAK SEMI ;
continue_stmt		: CONTINUE SEMI ;
return_stmt			: RETURN expr SEMI | RETURN SEMI ;
call_stmt			: funccall SEMI ;
block_stmt			: LB stmtlist RB ;

constant			: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT  | arraylit ;
funccall			: ID LP argumentlist RP ;
argumentlist		: argumentprime |  ;
argumentprime 		: argument COMMA argumentprime | argument ;
argument			: operand | expr ;
operand			    : ID | constant | funccall | LP expr RP ; 
arraylit 			: LB exprlist RB | LB RB ;

/****** Lexer ******/
// Keywords
AUTO				: 'auto' ;
BREAK				: 'break' ;
BOOLEAN				: 'boolean' ;
DO 					: 'do' ;
ELSE				: 'else' ;
fragment FALSE		: 'false' ;
FLOAT				: 'float' ;
FOR					: 'for' ;
FUNCTION			: 'function' ;
IF					: 'if' ;
INTEGER				: 'integer' ;
RETURN				: 'return' ;
STRING				: 'string' ;
fragment TRUE		: 'true' ;
WHILE				: 'while' ;
VOID				: 'void' ;
OUT 				: 'out' ;
CONTINUE			: 'continue' ;
OF 					: 'of' ;
INHERIT 			: 'inherit' ;
ARRAY 				: 'array' ;
// Operators
ADD                 : '+' ;
SUB                 : '-' ;
MUL                 : '*' ;
DIV    				: '/' ;
REMAINDER           : '%' ;

BOOL_NEGA           : '!' ;
BOOL_CONJ           : '&&' ;
BOOL_DISJ           : '||' ;

EQUAL               : '==' ;
NOT_EQUAL           : '!=' ;
LESS_THAN           : '<' ;
GREATER_THAN        : '>' ;
LESS_THAN_EQ        : '<=' ;
GREATER_THAN_EQ     : '>=' ;
DOUBLE_COLON		: '::' ;
// Separators
COMMA      			: ',' ;
SEMI    			: ';' ;
COLON   			: ':' ;
LB      			: '{' ;
RB      			: '}' ;
LP      			: '(' ;
RP      			: ')' ;
LSB     			: '[' ;
RSB     			: ']' ;
ASSIGN  			: '=' ;
DOT     			: '.' ;

// Identifiers and literals
BOOLEANLIT 			: TRUE | FALSE ;
ID					:[A-Za-z_][A-Za-z0-9_]*;
INTLIT    			: '0' | [1-9] | [1-9][0-9]*([_][0-9]+)*
{
	intlit = str(self.text)
	self.text = intlit.replace("_", "")
} ;

fragment EXP 		: [Ee][+-]?[0-9]+ ;
FLOATLIT 			: INTLIT '.' [0-9]* EXP?
{
	floatlit = str(self.text)
	self.text = floatlit.replace("_", "")
}
					| INTLIT EXP 
{
	floatlit = str(self.text)
	self.text = floatlit.replace("_", "")
}
                    | '.' [0-9]* EXP 
{
	floatlit = str(self.text)
	self.text = floatlit.replace("_", "")
} ;


fragment ESC_CHAR	: '\\'[bfrnt'\\];
fragment STR_CHAR	: (~[\n"'\\] | [\\]["] | ESC_CHAR) ;
fragment ILL_CHAR	: '\\' ~[bfrnt'\\] | '\\' ;
STRINGLIT 			: '"' STR_CHAR* '"' 
{
	stringlit = str(self.text)
	self.text = stringlit[1:-1]
} ;

// Skip tokens
WS 					: [ \t\b\f\r\n]+ -> skip ; // skip spaces, tabs, newlines
SINGLE_LINE_COMMENT : '//' ~[\r\n]* -> skip ;
MULTI_LINE_COMMENT 	: '/*' .*? '*/' ->skip ;

ERROR_CHAR			: .;
UNCLOSE_STRING		: '"' STR_CHAR* ([\n\r] |EOF) ;
ILLEGAL_ESCAPE		: '"' STR_CHAR* ILL_CHAR ;
