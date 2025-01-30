//ID: 2210134

grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();

afterStatement = False
}


options{
	language=Python3;
}


program  : statement+ EOF;

statement: block_statement | semi_statement;

block_statement: func_and_method_decl | typedecl | if_stmt;
semi_statement: (vardecl | constdecl | assignment | ret | funccall) (SEMI | EOF);


constdecl: CONST ID ASSIGN_INIT expression;

vardecl
        : VAR ID array_index* typedef (ASSIGN_INIT expression)?
        | VAR ID ASSIGN_INIT expression;

array: LBRACE array_elements (SEPARATOR array_elements)* RBRACE
    | array_elements;
array_elements: LBRACE array_members RBRACE;
array_members: expression (SEPARATOR expression)*;
array_index: LBRACKET (INTEGER | ID) RBRACKET;

typedef: ATOMIC_TYPE | ID;
typedecl: structdecl | interfacedecl;

structdecl: TYPE ID STRUCT LBRACE structfielddecl+ RBRACE;
structfielddecl: (ID (array_index* typedef)) SEMI;
structliteral: ID LBRACE (structfieldliteral (SEPARATOR structfieldliteral)*)? RBRACE;
structfieldliteral: ID ':' (literal | structfieldliteral);

interfacedecl: TYPE ID INTERFACE LBRACE method_signature+ RBRACE;
method_signature: ID LPARENTHESIS (argument (SEPARATOR argument)*)? RPARENTHESIS typedef? SEMI;
argument: ID (SEPARATOR ID)* typedef;

var_access: ID (array_index | '.' ID)*; // use for accessing atomic variable, properties in struct, values in array as well as mixed case 

func_and_method_decl: FUNC (LPARENTHESIS ID ID RPARENTHESIS)? ID LPARENTHESIS (argument_func (SEPARATOR argument_func)*)? RPARENTHESIS 
typedef?  LBRACE statement* RBRACE ;
argument_func: ID typedef;
ret: RETURN expression;
funccall: ID ('.' ID)? '(' (expression (SEPARATOR expression)*)? ')';
methodcall: var_access '.' ID '(' (expression (',' expression)*)? ')';

assignment: var_access  ASSIGN_OP expression;

expression: LPARENTHESIS expression RPARENTHESIS
    | (MINUS_OP | NOT_OP) expression
    | expression (MUL_OP | DIV_OP | MOD_OP) expression
    | expression (ADD_OP | MINUS_OP) expression  
    | expression COMPARE_OP expression
    | expression AND_OP expression
    | expression OR_OP expression
    | funccall| methodcall | var_access | literal;

if_stmt: if_condition block (ELSE (if_stmt | block))?;
if_condition: IF LPARENTHESIS expression RPARENTHESIS;
block: LBRACE statement+ RBRACE;

fragment BINARY: '0' [bB] [0-1]+;
fragment OCTAL: '0' [oO] [0-7]+;
fragment HEXADEC: '0' [xX] [0-9a-fA-F]+;
fragment DECIMAL: '0' | NonZeroDigit Digit*;
INTEGER: DECIMAL | BINARY | OCTAL | HEXADEC;

ATOMIC_TYPE: 'string' | 'int' | 'float' | 'boolean';
literal: INTEGER | FLOAT | STRING | BOOLEAN | array | structliteral;


COMMENT1: '//' .* ('\n' | EOF) -> skip;
COMMENT2: '/*' .* '*/' -> skip;


KEYWORD: 'for' | 'continue' | 'break' | 'range' | 'nil';

VAR: 'var' {
    self.afterStatement = True
};
CONST: 'const' {
    self.afterStatement = True
};
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
FUNC: 'func';
RETURN: 'return' {
    self.afterStatement = True
};
IF: 'if';
ELSE: 'else';

BOOLEAN: 'true' | 'false';

ASSIGN_OP: ('+=' | '-=' | '*=' | '/=' | '%=' | ':=') {
    self.afterStatement = True
};

FLOAT: Digit* '.' Digit* ([eE] ('+'|'-') Digit*)?;

SEMI: ';' {
    self.afterStatement = False
};

COMPARE_OP: '==' | '!=' | '<' | '<=' | '>' | '>=';
AND_OP: '&&';
OR_OP: '||';
NOT_OP: '!';
ADD_OP: '+';
MINUS_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
ASSIGN_INIT: '=';

LPARENTHESIS: '(';
RPARENTHESIS: ')' {
    self.afterStatement = True
};
LBRACE: '{' {
    self.afterStatement = False
};
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';

SEPARATOR: ',';

ESCAPE: '\\n' | '\\t' | '\\r' | '\\"' | '\\\\';

fragment IN_STRING: (~["\\] | ESCAPE)*;

STRING: '"' IN_STRING '"';

fragment UpperLetter: [A-Z];
fragment LowerLetter: [a-z];
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment IdentifierStart: UpperLetter | LowerLetter | '_';
ID: IdentifierStart (IdentifierStart | Digit)*;

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

NL: '\n' {
    if self.afterStatement:
        self.afterStatement = False
        self.type = self.SEMI
        self.text = ";"
        return self.emit()
    self.skip()
}; // skip newlines

ILLEGAL_ESCAPE: '"' IN_STRING '\\' {
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"' IN_STRING ('\\n' | EOF) {
    raise UncloseString(self.text[1:])
};
ERROR_CHAR: .;