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
}

options{
	language=Python3;
}


program  : statement+ EOF ;

statement: (decl | assignment | ret) (';' | '\n' | EOF);

decl: funcdecl | vardecl | constdecl | typedecl;

constdecl: 'const' ID '=' expression;

vardecl
        : 'var' ID array_index* typedef ('=' expression)?
        | 'var' ID '=' expression;

array: '{' array_elements (',' array_elements)* '}'
    | array_elements;
array_elements: '{' array_members '}';
array_members: expression (',' expression)*;
array_access: ID array_index+;
array_index: '[' INTEGER ']';

typedef: ATOMIC_TYPE | ID;
typedecl: structdecl | interfacedecl;

structdecl: 'type' ID 'struct' '{' structfielddecl+ '}';
structfielddecl: (ID (array_index* typedef)) ';';
struct_access: ID (array_index | ('.' ID))+;
structliteral: ID '{' (structfieldliteral (',' structfieldliteral)*)? '}';
structfieldliteral: ID ':' (literal | structfieldliteral);

interfacedecl: 'type' ID 'interface' '{' method_signature+ '}';
method_signature: ID '(' (argument (',' argument)*)? ')' typedef? ';';
argument: ID (',' ID)* typedef;

funcdecl: 'func' ID '(' (argument_func (',' argument_func)*)? ')' typedef?  '{' statement* '}' ;
argument_func: ID typedef;
ret: 'return' expression;

expression: literal;

assignment: (ID | array_access | struct_access)  ASSIGN_OP expression;

fragment BINARY: '0' [bB] [0-1]+;
fragment OCTAL: '0' [oO] [0-7]+;
fragment HEXADEC: '0' [xX] [0-9a-fA-F]+;
fragment DECIMAL: '0' | NonZeroDigit Digit*;
INTEGER: DECIMAL | BINARY | OCTAL | HEXADEC;

ATOMIC_TYPE: 'string' | 'int' | 'float' | 'boolean';
COMPOSITE_TYPE: 'struct' | 'interface'; 
literal: INTEGER | FLOAT | STRING | BOOLEAN | array | structliteral;

COMMENT1: '//' .* ('\n' | EOF) -> skip;
COMMENT2: '/*' .* '*/' -> skip;

KEYWORD: 'if' | 'else' | 'for' | 'func' | 'type' |         
        'const' | 'var' | 'continue' | 'break' | 'range' |
        'nil';

BOOLEAN: 'true' | 'false';

ASSIGN_OP: '+=' | '-=' | '*=' | '/=' | '%=' | ':=';

FLOAT: DECIMAL '.' DECIMAL? ([eE] ('+'|'-') DECIMAL)?;

OPERATOR: '+' | '-' | '*' | '/' | '%' | 
        '==' | '!=' | '<' | '<=' | '>' | '>=' | '='
        '&&' | '||' | '!' | '.';

SEPARATOR: '(' | ')' | '{' | '}' | '[' |']' |
            ',' | ';';


ESCAPE: '\\n' | '\\t' | '\\r' | '\\"' | '\\\\';

fragment IN_STRING: (~["\\] | ESCAPE)*;

STRING: '"' IN_STRING '"';

fragment UpperLetter: [A-Z];
fragment LowerLetter: [a-z];
fragment Digit: [0-9];
fragment NonZeroDigit: [1-9];
fragment IdentifierStart: UpperLetter | LowerLetter | '_';
ID: IdentifierStart (IdentifierStart | Digit)*;

NL: '\n' -> skip; //skip newlines

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 


ERROR_CHAR: .;
ILLEGAL_ESCAPE: '"' IN_STRING '\\' {
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING: '"' IN_STRING ('\\n' | EOF) {
    raise UncloseString(self.text[1:])
};


