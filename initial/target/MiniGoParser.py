# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'")
        buf.write("\u0118\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\3\2\6\28\n\2\r\2\16\29\3\2\3")
        buf.write("\2\3\3\3\3\3\3\5\3A\n\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4I\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6S\n\6\f\6\16\6V")
        buf.write("\13\6\3\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\3\6\5\6a\n\6\3")
        buf.write("\7\3\7\3\7\3\7\7\7g\n\7\f\7\16\7j\13\7\3\7\3\7\3\7\5\7")
        buf.write("o\n\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\7\tx\n\t\f\t\16\t{\13")
        buf.write("\t\3\n\3\n\6\n\177\n\n\r\n\16\n\u0080\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\5\r\u008b\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\6\16\u0092\n\16\r\16\16\16\u0093\3\16\3\16\3\17")
        buf.write("\3\17\7\17\u009a\n\17\f\17\16\17\u009d\13\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\6\20\u00a7\n\20\r\20\16")
        buf.write("\20\u00a8\3\21\3\21\3\21\3\21\3\21\7\21\u00b0\n\21\f\21")
        buf.write("\16\21\u00b3\13\21\5\21\u00b5\n\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u00bd\n\22\3\23\3\23\3\23\3\23\3\23\6")
        buf.write("\23\u00c4\n\23\r\23\16\23\u00c5\3\23\3\23\3\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u00cf\n\24\f\24\16\24\u00d2\13\24\5")
        buf.write("\24\u00d4\n\24\3\24\3\24\5\24\u00d8\n\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\7\25\u00df\n\25\f\25\16\25\u00e2\13\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u00ec\n\26\f")
        buf.write("\26\16\26\u00ef\13\26\5\26\u00f1\n\26\3\26\3\26\5\26\u00f5")
        buf.write("\n\26\3\26\3\26\7\26\u00f9\n\26\f\26\16\26\u00fc\13\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\32")
        buf.write("\3\32\3\32\5\32\u010b\n\32\3\32\3\32\3\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\5\33\u0116\n\33\3\33\2\2\34\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\4")
        buf.write("\4\3\3\3##\4\2\26\26\"\"\2\u0122\2\67\3\2\2\2\4@\3\2\2")
        buf.write("\2\6H\3\2\2\2\bJ\3\2\2\2\n`\3\2\2\2\fn\3\2\2\2\16p\3\2")
        buf.write("\2\2\20t\3\2\2\2\22|\3\2\2\2\24\u0082\3\2\2\2\26\u0086")
        buf.write("\3\2\2\2\30\u008a\3\2\2\2\32\u008c\3\2\2\2\34\u0097\3")
        buf.write("\2\2\2\36\u00a2\3\2\2\2 \u00aa\3\2\2\2\"\u00b8\3\2\2\2")
        buf.write("$\u00be\3\2\2\2&\u00c9\3\2\2\2(\u00db\3\2\2\2*\u00e5\3")
        buf.write("\2\2\2,\u00ff\3\2\2\2.\u0102\3\2\2\2\60\u0105\3\2\2\2")
        buf.write("\62\u010a\3\2\2\2\64\u0115\3\2\2\2\668\5\4\3\2\67\66\3")
        buf.write("\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7\2")
        buf.write("\2\3<\3\3\2\2\2=A\5\6\4\2>A\5\62\32\2?A\5.\30\2@=\3\2")
        buf.write("\2\2@>\3\2\2\2@?\3\2\2\2AB\3\2\2\2BC\t\2\2\2C\5\3\2\2")
        buf.write("\2DI\5*\26\2EI\5\n\6\2FI\5\b\5\2GI\5\30\r\2HD\3\2\2\2")
        buf.write("HE\3\2\2\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\7\4\2\2KL")
        buf.write("\7\"\2\2LM\7\5\2\2MN\5\60\31\2N\t\3\2\2\2OP\7\6\2\2PT")
        buf.write("\7\"\2\2QS\5\24\13\2RQ\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2UW\3\2\2\2VT\3\2\2\2WZ\5\26\f\2XY\7\5\2\2Y[\5\60")
        buf.write("\31\2ZX\3\2\2\2Z[\3\2\2\2[a\3\2\2\2\\]\7\6\2\2]^\7\"\2")
        buf.write("\2^_\7\5\2\2_a\5\60\31\2`O\3\2\2\2`\\\3\2\2\2a\13\3\2")
        buf.write("\2\2bc\7\7\2\2ch\5\16\b\2de\7\b\2\2eg\5\16\b\2fd\3\2\2")
        buf.write("\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2k")
        buf.write("l\7\t\2\2lo\3\2\2\2mo\5\16\b\2nb\3\2\2\2nm\3\2\2\2o\r")
        buf.write("\3\2\2\2pq\7\7\2\2qr\5\20\t\2rs\7\t\2\2s\17\3\2\2\2ty")
        buf.write("\5\60\31\2uv\7\b\2\2vx\5\60\31\2wu\3\2\2\2x{\3\2\2\2y")
        buf.write("w\3\2\2\2yz\3\2\2\2z\21\3\2\2\2{y\3\2\2\2|~\7\"\2\2}\177")
        buf.write("\5\24\13\2~}\3\2\2\2\177\u0080\3\2\2\2\u0080~\3\2\2\2")
        buf.write("\u0080\u0081\3\2\2\2\u0081\23\3\2\2\2\u0082\u0083\7\n")
        buf.write("\2\2\u0083\u0084\7\25\2\2\u0084\u0085\7\13\2\2\u0085\25")
        buf.write("\3\2\2\2\u0086\u0087\t\3\2\2\u0087\27\3\2\2\2\u0088\u008b")
        buf.write("\5\32\16\2\u0089\u008b\5$\23\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u0089\3\2\2\2\u008b\31\3\2\2\2\u008c\u008d\7\f\2\2\u008d")
        buf.write("\u008e\7\"\2\2\u008e\u008f\7\r\2\2\u008f\u0091\7\7\2\2")
        buf.write("\u0090\u0092\5\34\17\2\u0091\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094")
        buf.write("\u0095\3\2\2\2\u0095\u0096\7\t\2\2\u0096\33\3\2\2\2\u0097")
        buf.write("\u009b\7\"\2\2\u0098\u009a\5\24\13\2\u0099\u0098\3\2\2")
        buf.write("\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009e\3\2\2\2\u009d\u009b\3\2\2\2\u009e")
        buf.write("\u009f\5\26\f\2\u009f\u00a0\3\2\2\2\u00a0\u00a1\7\3\2")
        buf.write("\2\u00a1\35\3\2\2\2\u00a2\u00a6\7\"\2\2\u00a3\u00a7\5")
        buf.write("\24\13\2\u00a4\u00a5\7\16\2\2\u00a5\u00a7\7\"\2\2\u00a6")
        buf.write("\u00a3\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a7\u00a8\3\2\2\2")
        buf.write("\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\37\3\2")
        buf.write("\2\2\u00aa\u00ab\7\"\2\2\u00ab\u00b4\7\7\2\2\u00ac\u00b1")
        buf.write("\5\"\22\2\u00ad\u00ae\7\b\2\2\u00ae\u00b0\5\"\22\2\u00af")
        buf.write("\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b1\u00b2\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3")
        buf.write("\2\2\2\u00b4\u00ac\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\3\2\2\2\u00b6\u00b7\7\t\2\2\u00b7!\3\2\2\2\u00b8\u00b9")
        buf.write("\7\"\2\2\u00b9\u00bc\7\17\2\2\u00ba\u00bd\5\64\33\2\u00bb")
        buf.write("\u00bd\5\"\22\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb\3\2\2")
        buf.write("\2\u00bd#\3\2\2\2\u00be\u00bf\7\f\2\2\u00bf\u00c0\7\"")
        buf.write("\2\2\u00c0\u00c1\7\20\2\2\u00c1\u00c3\7\7\2\2\u00c2\u00c4")
        buf.write("\5&\24\2\u00c3\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7\3\2\2\2")
        buf.write("\u00c7\u00c8\7\t\2\2\u00c8%\3\2\2\2\u00c9\u00ca\7\"\2")
        buf.write("\2\u00ca\u00d3\7\21\2\2\u00cb\u00d0\5(\25\2\u00cc\u00cd")
        buf.write("\7\b\2\2\u00cd\u00cf\5(\25\2\u00ce\u00cc\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00cb\3")
        buf.write("\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7")
        buf.write("\7\22\2\2\u00d6\u00d8\5\26\f\2\u00d7\u00d6\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\7\3\2\2")
        buf.write("\u00da\'\3\2\2\2\u00db\u00e0\7\"\2\2\u00dc\u00dd\7\b\2")
        buf.write("\2\u00dd\u00df\7\"\2\2\u00de\u00dc\3\2\2\2\u00df\u00e2")
        buf.write("\3\2\2\2\u00e0\u00de\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1")
        buf.write("\u00e3\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e4\5\26\f")
        buf.write("\2\u00e4)\3\2\2\2\u00e5\u00e6\7\23\2\2\u00e6\u00e7\7\"")
        buf.write("\2\2\u00e7\u00f0\7\21\2\2\u00e8\u00ed\5,\27\2\u00e9\u00ea")
        buf.write("\7\b\2\2\u00ea\u00ec\5,\27\2\u00eb\u00e9\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00e8\3")
        buf.write("\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4")
        buf.write("\7\22\2\2\u00f3\u00f5\5\26\f\2\u00f4\u00f3\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00fa\7\7\2\2")
        buf.write("\u00f7\u00f9\5\4\3\2\u00f8\u00f7\3\2\2\2\u00f9\u00fc\3")
        buf.write("\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fd")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00fe\7\t\2\2\u00fe")
        buf.write("+\3\2\2\2\u00ff\u0100\7\"\2\2\u0100\u0101\5\26\f\2\u0101")
        buf.write("-\3\2\2\2\u0102\u0103\7\24\2\2\u0103\u0104\5\60\31\2\u0104")
        buf.write("/\3\2\2\2\u0105\u0106\5\64\33\2\u0106\61\3\2\2\2\u0107")
        buf.write("\u010b\7\"\2\2\u0108\u010b\5\22\n\2\u0109\u010b\5\36\20")
        buf.write("\2\u010a\u0107\3\2\2\2\u010a\u0108\3\2\2\2\u010a\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7\34\2\2\u010d")
        buf.write("\u010e\5\60\31\2\u010e\63\3\2\2\2\u010f\u0116\7\25\2\2")
        buf.write("\u0110\u0116\7\35\2\2\u0111\u0116\7!\2\2\u0112\u0116\7")
        buf.write("\33\2\2\u0113\u0116\5\f\7\2\u0114\u0116\5 \21\2\u0115")
        buf.write("\u010f\3\2\2\2\u0115\u0110\3\2\2\2\u0115\u0111\3\2\2\2")
        buf.write("\u0115\u0112\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0114\3")
        buf.write("\2\2\2\u0116\65\3\2\2\2\379@HTZ`hny\u0080\u008a\u0093")
        buf.write("\u009b\u00a6\u00a8\u00b1\u00b4\u00bc\u00c5\u00d0\u00d3")
        buf.write("\u00d7\u00e0\u00ed\u00f0\u00f4\u00fa\u010a\u0115")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'const'", "'='", "'var'", "'{'", 
                     "','", "'}'", "'['", "']'", "'type'", "'struct'", "'.'", 
                     "':'", "'interface'", "'('", "')'", "'func'", "'return'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INTEGER", 
                      "ATOMIC_TYPE", "COMPOSITE_TYPE", "COMMENT1", "COMMENT2", 
                      "KEYWORD", "BOOLEAN", "ASSIGN_OP", "FLOAT", "OPERATOR", 
                      "SEPARATOR", "ESCAPE", "STRING", "ID", "NL", "WS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_decl = 2
    RULE_constdecl = 3
    RULE_vardecl = 4
    RULE_array = 5
    RULE_array_elements = 6
    RULE_array_members = 7
    RULE_array_access = 8
    RULE_array_index = 9
    RULE_typedef = 10
    RULE_typedecl = 11
    RULE_structdecl = 12
    RULE_structfielddecl = 13
    RULE_struct_access = 14
    RULE_structliteral = 15
    RULE_structfieldliteral = 16
    RULE_interfacedecl = 17
    RULE_method_signature = 18
    RULE_argument = 19
    RULE_funcdecl = 20
    RULE_argument_func = 21
    RULE_ret = 22
    RULE_expression = 23
    RULE_assignment = 24
    RULE_literal = 25

    ruleNames =  [ "program", "statement", "decl", "constdecl", "vardecl", 
                   "array", "array_elements", "array_members", "array_access", 
                   "array_index", "typedef", "typedecl", "structdecl", "structfielddecl", 
                   "struct_access", "structliteral", "structfieldliteral", 
                   "interfacedecl", "method_signature", "argument", "funcdecl", 
                   "argument_func", "ret", "expression", "assignment", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    INTEGER=19
    ATOMIC_TYPE=20
    COMPOSITE_TYPE=21
    COMMENT1=22
    COMMENT2=23
    KEYWORD=24
    BOOLEAN=25
    ASSIGN_OP=26
    FLOAT=27
    OPERATOR=28
    SEPARATOR=29
    ESCAPE=30
    STRING=31
    ID=32
    NL=33
    WS=34
    ERROR_CHAR=35
    ILLEGAL_ESCAPE=36
    UNCLOSE_STRING=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 52
                self.statement()
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__9) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 57
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self):
            return self.getTypedRuleContext(MiniGoParser.DeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ret(self):
            return self.getTypedRuleContext(MiniGoParser.RetContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__1, MiniGoParser.T__3, MiniGoParser.T__9, MiniGoParser.T__16]:
                self.state = 59
                self.decl()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 60
                self.assignment()
                pass
            elif token in [MiniGoParser.T__17]:
                self.state = 61
                self.ret()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 64
            _la = self._input.LA(1)
            if not(((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (MiniGoParser.EOF - -1)) | (1 << (MiniGoParser.T__0 - -1)) | (1 << (MiniGoParser.NL - -1)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.funcdecl()
                pass
            elif token in [MiniGoParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.vardecl()
                pass
            elif token in [MiniGoParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.constdecl()
                pass
            elif token in [MiniGoParser.T__9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MiniGoParser.T__1)
            self.state = 73
            self.match(MiniGoParser.ID)
            self.state = 74
            self.match(MiniGoParser.T__2)
            self.state = 75
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 77
                self.match(MiniGoParser.T__3)
                self.state = 78
                self.match(MiniGoParser.ID)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__7:
                    self.state = 79
                    self.array_index()
                    self.state = 84
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 85
                self.typedef()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.T__2:
                    self.state = 86
                    self.match(MiniGoParser.T__2)
                    self.state = 87
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.match(MiniGoParser.T__3)
                self.state = 91
                self.match(MiniGoParser.ID)
                self.state = 92
                self.match(MiniGoParser.T__2)
                self.state = 93
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_elementsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_elementsContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(MiniGoParser.T__4)
                self.state = 97
                self.array_elements()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 98
                    self.match(MiniGoParser.T__5)
                    self.state = 99
                    self.array_elements()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 105
                self.match(MiniGoParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.array_elements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_members(self):
            return self.getTypedRuleContext(MiniGoParser.Array_membersContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = MiniGoParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(MiniGoParser.T__4)
            self.state = 111
            self.array_members()
            self.state = 112
            self.match(MiniGoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_membersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_members" ):
                return visitor.visitArray_members(self)
            else:
                return visitor.visitChildren(self)




    def array_members(self):

        localctx = MiniGoParser.Array_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.expression()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__5:
                self.state = 115
                self.match(MiniGoParser.T__5)
                self.state = 116
                self.expression()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MiniGoParser.ID)
            self.state = 124 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 123
                self.array_index()
                self.state = 126 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.T__7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_indexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_index" ):
                return visitor.visitArray_index(self)
            else:
                return visitor.visitChildren(self)




    def array_index(self):

        localctx = MiniGoParser.Array_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(MiniGoParser.T__7)
            self.state = 129
            self.match(MiniGoParser.INTEGER)
            self.state = 130
            self.match(MiniGoParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATOMIC_TYPE(self):
            return self.getToken(MiniGoParser.ATOMIC_TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typedef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedef" ):
                return visitor.visitTypedef(self)
            else:
                return visitor.visitChildren(self)




    def typedef(self):

        localctx = MiniGoParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typedef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_typedecl)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.structdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.interfacedecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structfielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructfielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructfielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MiniGoParser.T__9)
            self.state = 139
            self.match(MiniGoParser.ID)
            self.state = 140
            self.match(MiniGoParser.T__10)
            self.state = 141
            self.match(MiniGoParser.T__4)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.structfielddecl()
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 147
            self.match(MiniGoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structfielddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfielddecl" ):
                return visitor.visitStructfielddecl(self)
            else:
                return visitor.visitChildren(self)




    def structfielddecl(self):

        localctx = MiniGoParser.StructfielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_structfielddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(MiniGoParser.ID)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 150
                self.array_index()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.typedef()
            self.state = 158
            self.match(MiniGoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_struct_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniGoParser.ID)
            self.state = 164 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 164
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__7]:
                    self.state = 161
                    self.array_index()
                    pass
                elif token in [MiniGoParser.T__11]:
                    self.state = 162
                    self.match(MiniGoParser.T__11)
                    self.state = 163
                    self.match(MiniGoParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.T__7 or _la==MiniGoParser.T__11):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def structfieldliteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructfieldliteralContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructfieldliteralContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteral" ):
                return visitor.visitStructliteral(self)
            else:
                return visitor.visitChildren(self)




    def structliteral(self):

        localctx = MiniGoParser.StructliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_structliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MiniGoParser.ID)
            self.state = 169
            self.match(MiniGoParser.T__4)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 170
                self.structfieldliteral()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 171
                    self.match(MiniGoParser.T__5)
                    self.state = 172
                    self.structfieldliteral()
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 180
            self.match(MiniGoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructfieldliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def structfieldliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructfieldliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structfieldliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructfieldliteral" ):
                return visitor.visitStructfieldliteral(self)
            else:
                return visitor.visitChildren(self)




    def structfieldliteral(self):

        localctx = MiniGoParser.StructfieldliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_structfieldliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(MiniGoParser.ID)
            self.state = 183
            self.match(MiniGoParser.T__12)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 184
                self.literal()
                pass

            elif la_ == 2:
                self.state = 185
                self.structfieldliteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def method_signature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Method_signatureContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Method_signatureContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.T__9)
            self.state = 189
            self.match(MiniGoParser.ID)
            self.state = 190
            self.match(MiniGoParser.T__13)
            self.state = 191
            self.match(MiniGoParser.T__4)
            self.state = 193 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 192
                self.method_signature()
                self.state = 195 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 197
            self.match(MiniGoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_signatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArgumentContext,i)


        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_signature" ):
                return visitor.visitMethod_signature(self)
            else:
                return visitor.visitChildren(self)




    def method_signature(self):

        localctx = MiniGoParser.Method_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_method_signature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(MiniGoParser.ID)
            self.state = 200
            self.match(MiniGoParser.T__14)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 201
                self.argument()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 202
                    self.match(MiniGoParser.T__5)
                    self.state = 203
                    self.argument()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 211
            self.match(MiniGoParser.T__15)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID:
                self.state = 212
                self.typedef()


            self.state = 215
            self.match(MiniGoParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(MiniGoParser.ID)
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__5:
                self.state = 218
                self.match(MiniGoParser.T__5)
                self.state = 219
                self.match(MiniGoParser.ID)
                self.state = 224
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 225
            self.typedef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def argument_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Argument_funcContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Argument_funcContext,i)


        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(MiniGoParser.T__16)
            self.state = 228
            self.match(MiniGoParser.ID)
            self.state = 229
            self.match(MiniGoParser.T__14)
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 230
                self.argument_func()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 231
                    self.match(MiniGoParser.T__5)
                    self.state = 232
                    self.argument_func()
                    self.state = 237
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 240
            self.match(MiniGoParser.T__15)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID:
                self.state = 241
                self.typedef()


            self.state = 244
            self.match(MiniGoParser.T__4)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__9) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.ID))) != 0):
                self.state = 245
                self.statement()
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 251
            self.match(MiniGoParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_func" ):
                return visitor.visitArgument_func(self)
            else:
                return visitor.visitChildren(self)




    def argument_func(self):

        localctx = MiniGoParser.Argument_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argument_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MiniGoParser.ID)
            self.state = 254
            self.typedef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ret

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = MiniGoParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(MiniGoParser.T__17)
            self.state = 257
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 261
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 262
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 263
                self.struct_access()
                pass


            self.state = 266
            self.match(MiniGoParser.ASSIGN_OP)
            self.state = 267
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def array(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayContext,0)


        def structliteral(self):
            return self.getTypedRuleContext(MiniGoParser.StructliteralContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 271
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 272
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 273
                self.array()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 274
                self.structliteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





