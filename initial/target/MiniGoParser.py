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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3&")
        buf.write("\u00f6\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\6\2\62\n\2\r\2\16\2\63\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3=\n\3\3\3\3\3\3\4\3\4\3\4\5\4D\n\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\7\6Q\n\6\f\6\16\6T\13\6\3\6")
        buf.write("\3\6\3\6\5\6Y\n\6\3\6\3\6\3\6\3\6\5\6_\n\6\3\7\3\7\3\7")
        buf.write("\3\7\7\7e\n\7\f\7\16\7h\13\7\3\7\3\7\3\7\5\7m\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\7\tv\n\t\f\t\16\ty\13\t\3\n\3")
        buf.write("\n\6\n}\n\n\r\n\16\n~\3\13\3\13\3\13\3\13\3\f\3\f\3\r")
        buf.write("\3\r\5\r\u0089\n\r\3\16\3\16\3\16\3\16\3\16\6\16\u0090")
        buf.write("\n\16\r\16\16\16\u0091\3\16\3\16\3\17\3\17\7\17\u0098")
        buf.write("\n\17\f\17\16\17\u009b\13\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\6\20\u00a5\n\20\r\20\16\20\u00a6\3\21")
        buf.write("\3\21\3\21\3\21\3\21\7\21\u00ae\n\21\f\21\16\21\u00b1")
        buf.write("\13\21\5\21\u00b3\n\21\3\21\3\21\3\22\3\22\3\22\3\22\5")
        buf.write("\22\u00bb\n\22\3\23\3\23\3\23\3\23\3\23\6\23\u00c2\n\23")
        buf.write("\r\23\16\23\u00c3\3\23\3\23\3\24\3\24\3\24\3\24\3\24\7")
        buf.write("\24\u00cd\n\24\f\24\16\24\u00d0\13\24\5\24\u00d2\n\24")
        buf.write("\3\24\3\24\5\24\u00d6\n\24\3\24\3\24\3\25\3\25\3\25\7")
        buf.write("\25\u00dd\n\25\f\25\16\25\u00e0\13\25\3\25\3\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\5\30\u00f4\n\30\3\30\2\2\31\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\2\5\4\3\3\3")
        buf.write("\"\"\4\2\4\4\33\33\4\2\25\25!!\2\u00fe\2\61\3\2\2\2\4")
        buf.write("<\3\2\2\2\6C\3\2\2\2\bH\3\2\2\2\n^\3\2\2\2\fl\3\2\2\2")
        buf.write("\16n\3\2\2\2\20r\3\2\2\2\22z\3\2\2\2\24\u0080\3\2\2\2")
        buf.write("\26\u0084\3\2\2\2\30\u0088\3\2\2\2\32\u008a\3\2\2\2\34")
        buf.write("\u0095\3\2\2\2\36\u00a0\3\2\2\2 \u00a8\3\2\2\2\"\u00b6")
        buf.write("\3\2\2\2$\u00bc\3\2\2\2&\u00c7\3\2\2\2(\u00d9\3\2\2\2")
        buf.write("*\u00e3\3\2\2\2,\u00eb\3\2\2\2.\u00f3\3\2\2\2\60\62\5")
        buf.write("\4\3\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\66\7\2\2\3\66\3\3\2\2\2\67=")
        buf.write("\5\6\4\28=\5*\26\29=\5\n\6\2:=\5\b\5\2;=\5\30\r\2<\67")
        buf.write("\3\2\2\2<8\3\2\2\2<9\3\2\2\2<:\3\2\2\2<;\3\2\2\2=>\3\2")
        buf.write("\2\2>?\t\2\2\2?\5\3\2\2\2@D\7!\2\2AD\5\22\n\2BD\5\36\20")
        buf.write("\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2DE\3\2\2\2EF\t\3\2\2F")
        buf.write("G\5,\27\2G\7\3\2\2\2HI\7\5\2\2IJ\7!\2\2JK\7\4\2\2KL\5")
        buf.write(",\27\2L\t\3\2\2\2MN\7\6\2\2NR\7!\2\2OQ\5\24\13\2PO\3\2")
        buf.write("\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2")
        buf.write("UX\5\26\f\2VW\7\4\2\2WY\5,\27\2XV\3\2\2\2XY\3\2\2\2Y_")
        buf.write("\3\2\2\2Z[\7\6\2\2[\\\7!\2\2\\]\7\4\2\2]_\5,\27\2^M\3")
        buf.write("\2\2\2^Z\3\2\2\2_\13\3\2\2\2`a\7\7\2\2af\5\16\b\2bc\7")
        buf.write("\b\2\2ce\5\16\b\2db\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2")
        buf.write("\2\2gi\3\2\2\2hf\3\2\2\2ij\7\t\2\2jm\3\2\2\2km\5\16\b")
        buf.write("\2l`\3\2\2\2lk\3\2\2\2m\r\3\2\2\2no\7\7\2\2op\5\20\t\2")
        buf.write("pq\7\t\2\2q\17\3\2\2\2rw\5,\27\2st\7\b\2\2tv\5,\27\2u")
        buf.write("s\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\21\3\2\2\2yw")
        buf.write("\3\2\2\2z|\7!\2\2{}\5\24\13\2|{\3\2\2\2}~\3\2\2\2~|\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\23\3\2\2\2\u0080\u0081\7\n\2\2")
        buf.write("\u0081\u0082\7\24\2\2\u0082\u0083\7\13\2\2\u0083\25\3")
        buf.write("\2\2\2\u0084\u0085\t\4\2\2\u0085\27\3\2\2\2\u0086\u0089")
        buf.write("\5\32\16\2\u0087\u0089\5$\23\2\u0088\u0086\3\2\2\2\u0088")
        buf.write("\u0087\3\2\2\2\u0089\31\3\2\2\2\u008a\u008b\7\f\2\2\u008b")
        buf.write("\u008c\7!\2\2\u008c\u008d\7\r\2\2\u008d\u008f\7\7\2\2")
        buf.write("\u008e\u0090\5\34\17\2\u008f\u008e\3\2\2\2\u0090\u0091")
        buf.write("\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092")
        buf.write("\u0093\3\2\2\2\u0093\u0094\7\t\2\2\u0094\33\3\2\2\2\u0095")
        buf.write("\u0099\7!\2\2\u0096\u0098\5\24\13\2\u0097\u0096\3\2\2")
        buf.write("\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099\u009a")
        buf.write("\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009d\5\26\f\2\u009d\u009e\3\2\2\2\u009e\u009f\7\3\2")
        buf.write("\2\u009f\35\3\2\2\2\u00a0\u00a4\7!\2\2\u00a1\u00a5\5\24")
        buf.write("\13\2\u00a2\u00a3\7\16\2\2\u00a3\u00a5\7!\2\2\u00a4\u00a1")
        buf.write("\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\37\3\2\2\2\u00a8")
        buf.write("\u00a9\7!\2\2\u00a9\u00b2\7\7\2\2\u00aa\u00af\5\"\22\2")
        buf.write("\u00ab\u00ac\7\b\2\2\u00ac\u00ae\5\"\22\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00af")
        buf.write("\u00b0\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af\3\2\2\2")
        buf.write("\u00b2\u00aa\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b5\7\t\2\2\u00b5!\3\2\2\2\u00b6\u00b7")
        buf.write("\7!\2\2\u00b7\u00ba\7\17\2\2\u00b8\u00bb\5.\30\2\u00b9")
        buf.write("\u00bb\5\"\22\2\u00ba\u00b8\3\2\2\2\u00ba\u00b9\3\2\2")
        buf.write("\2\u00bb#\3\2\2\2\u00bc\u00bd\7\f\2\2\u00bd\u00be\7!\2")
        buf.write("\2\u00be\u00bf\7\20\2\2\u00bf\u00c1\7\7\2\2\u00c0\u00c2")
        buf.write("\5&\24\2\u00c1\u00c0\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3")
        buf.write("\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2")
        buf.write("\u00c5\u00c6\7\t\2\2\u00c6%\3\2\2\2\u00c7\u00c8\7!\2\2")
        buf.write("\u00c8\u00d1\7\21\2\2\u00c9\u00ce\5(\25\2\u00ca\u00cb")
        buf.write("\7\b\2\2\u00cb\u00cd\5(\25\2\u00cc\u00ca\3\2\2\2\u00cd")
        buf.write("\u00d0\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00c9\3")
        buf.write("\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5")
        buf.write("\7\22\2\2\u00d4\u00d6\5\26\f\2\u00d5\u00d4\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7\3\2\2")
        buf.write("\u00d8\'\3\2\2\2\u00d9\u00de\7!\2\2\u00da\u00db\7\b\2")
        buf.write("\2\u00db\u00dd\7!\2\2\u00dc\u00da\3\2\2\2\u00dd\u00e0")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e1\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\5\26\f")
        buf.write("\2\u00e2)\3\2\2\2\u00e3\u00e4\7\23\2\2\u00e4\u00e5\7!")
        buf.write("\2\2\u00e5\u00e6\7\21\2\2\u00e6\u00e7\7\22\2\2\u00e7\u00e8")
        buf.write("\7\7\2\2\u00e8\u00e9\7\t\2\2\u00e9\u00ea\7\3\2\2\u00ea")
        buf.write("+\3\2\2\2\u00eb\u00ec\5.\30\2\u00ec-\3\2\2\2\u00ed\u00f4")
        buf.write("\7\24\2\2\u00ee\u00f4\7\34\2\2\u00ef\u00f4\7 \2\2\u00f0")
        buf.write("\u00f4\7\32\2\2\u00f1\u00f4\5\f\7\2\u00f2\u00f4\5 \21")
        buf.write("\2\u00f3\u00ed\3\2\2\2\u00f3\u00ee\3\2\2\2\u00f3\u00ef")
        buf.write("\3\2\2\2\u00f3\u00f0\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3")
        buf.write("\u00f2\3\2\2\2\u00f4/\3\2\2\2\32\63<CRX^flw~\u0088\u0091")
        buf.write("\u0099\u00a4\u00a6\u00af\u00b2\u00ba\u00c3\u00ce\u00d1")
        buf.write("\u00d5\u00de\u00f3")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'const'", "'var'", "'{'", 
                     "','", "'}'", "'['", "']'", "'type'", "'struct'", "'.'", 
                     "':'", "'interface'", "'('", "')'", "'func'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INTEGER", "ATOMIC_TYPE", 
                      "COMPOSITE_TYPE", "COMMENT1", "COMMENT2", "KEYWORD", 
                      "BOOLEAN", "ASSIGN_OP", "FLOAT", "OPERATOR", "SEPARATOR", 
                      "ESCAPE", "STRING", "ID", "NL", "WS", "ERROR_CHAR", 
                      "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_assignment = 2
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
    RULE_expression = 21
    RULE_literal = 22

    ruleNames =  [ "program", "decl", "assignment", "constdecl", "vardecl", 
                   "array", "array_elements", "array_members", "array_access", 
                   "array_index", "typedef", "typedecl", "structdecl", "structfielddecl", 
                   "struct_access", "structliteral", "structfieldliteral", 
                   "interfacedecl", "method_signature", "argument", "funcdecl", 
                   "expression", "literal" ]

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
    INTEGER=18
    ATOMIC_TYPE=19
    COMPOSITE_TYPE=20
    COMMENT1=21
    COMMENT2=22
    KEYWORD=23
    BOOLEAN=24
    ASSIGN_OP=25
    FLOAT=26
    OPERATOR=27
    SEPARATOR=28
    ESCAPE=29
    STRING=30
    ID=31
    NL=32
    WS=33
    ERROR_CHAR=34
    ILLEGAL_ESCAPE=35
    UNCLOSE_STRING=36

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

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


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
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.decl()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__2) | (1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__9) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 51
            self.match(MiniGoParser.EOF)
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


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
        self.enterRule(localctx, 2, self.RULE_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 53
                self.assignment()
                pass
            elif token in [MiniGoParser.T__16]:
                self.state = 54
                self.funcdecl()
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 55
                self.vardecl()
                pass
            elif token in [MiniGoParser.T__2]:
                self.state = 56
                self.constdecl()
                pass
            elif token in [MiniGoParser.T__9]:
                self.state = 57
                self.typedecl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 60
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

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
        self.enterRule(localctx, 4, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 62
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 63
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 64
                self.struct_access()
                pass


            self.state = 67
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__1 or _la==MiniGoParser.ASSIGN_OP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self.expression()
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
            self.state = 70
            self.match(MiniGoParser.T__2)
            self.state = 71
            self.match(MiniGoParser.ID)
            self.state = 72
            self.match(MiniGoParser.T__1)
            self.state = 73
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
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(MiniGoParser.T__3)
                self.state = 76
                self.match(MiniGoParser.ID)
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__7:
                    self.state = 77
                    self.array_index()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                self.typedef()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.T__1:
                    self.state = 84
                    self.match(MiniGoParser.T__1)
                    self.state = 85
                    self.expression()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(MiniGoParser.T__3)
                self.state = 89
                self.match(MiniGoParser.ID)
                self.state = 90
                self.match(MiniGoParser.T__1)
                self.state = 91
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
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(MiniGoParser.T__4)
                self.state = 95
                self.array_elements()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 96
                    self.match(MiniGoParser.T__5)
                    self.state = 97
                    self.array_elements()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.match(MiniGoParser.T__6)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
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
            self.state = 108
            self.match(MiniGoParser.T__4)
            self.state = 109
            self.array_members()
            self.state = 110
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
            self.state = 112
            self.expression()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__5:
                self.state = 113
                self.match(MiniGoParser.T__5)
                self.state = 114
                self.expression()
                self.state = 119
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
            self.state = 120
            self.match(MiniGoParser.ID)
            self.state = 122 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.array_index()
                self.state = 124 
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
            self.state = 126
            self.match(MiniGoParser.T__7)
            self.state = 127
            self.match(MiniGoParser.INTEGER)
            self.state = 128
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
            self.state = 130
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
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.structdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
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
            self.state = 136
            self.match(MiniGoParser.T__9)
            self.state = 137
            self.match(MiniGoParser.ID)
            self.state = 138
            self.match(MiniGoParser.T__10)
            self.state = 139
            self.match(MiniGoParser.T__4)
            self.state = 141 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 140
                self.structfielddecl()
                self.state = 143 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 145
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
            self.state = 147
            self.match(MiniGoParser.ID)

            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 148
                self.array_index()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 154
            self.typedef()
            self.state = 156
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
            self.state = 158
            self.match(MiniGoParser.ID)
            self.state = 162 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 162
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__7]:
                    self.state = 159
                    self.array_index()
                    pass
                elif token in [MiniGoParser.T__11]:
                    self.state = 160
                    self.match(MiniGoParser.T__11)
                    self.state = 161
                    self.match(MiniGoParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 164 
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
            self.state = 166
            self.match(MiniGoParser.ID)
            self.state = 167
            self.match(MiniGoParser.T__4)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 168
                self.structfieldliteral()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 169
                    self.match(MiniGoParser.T__5)
                    self.state = 170
                    self.structfieldliteral()
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 178
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
            self.state = 180
            self.match(MiniGoParser.ID)
            self.state = 181
            self.match(MiniGoParser.T__12)
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 182
                self.literal()
                pass

            elif la_ == 2:
                self.state = 183
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
            self.state = 186
            self.match(MiniGoParser.T__9)
            self.state = 187
            self.match(MiniGoParser.ID)
            self.state = 188
            self.match(MiniGoParser.T__13)
            self.state = 189
            self.match(MiniGoParser.T__4)
            self.state = 191 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 190
                self.method_signature()
                self.state = 193 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 195
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
            self.state = 197
            self.match(MiniGoParser.ID)
            self.state = 198
            self.match(MiniGoParser.T__14)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 199
                self.argument()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__5:
                    self.state = 200
                    self.match(MiniGoParser.T__5)
                    self.state = 201
                    self.argument()
                    self.state = 206
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 209
            self.match(MiniGoParser.T__15)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID:
                self.state = 210
                self.typedef()


            self.state = 213
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
            self.state = 215
            self.match(MiniGoParser.ID)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__5:
                self.state = 216
                self.match(MiniGoParser.T__5)
                self.state = 217
                self.match(MiniGoParser.ID)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 223
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MiniGoParser.T__16)
            self.state = 226
            self.match(MiniGoParser.ID)
            self.state = 227
            self.match(MiniGoParser.T__14)
            self.state = 228
            self.match(MiniGoParser.T__15)
            self.state = 229
            self.match(MiniGoParser.T__4)
            self.state = 230
            self.match(MiniGoParser.T__6)
            self.state = 231
            self.match(MiniGoParser.T__0)
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
        self.enterRule(localctx, 42, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.literal()
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
        self.enterRule(localctx, 44, self.RULE_literal)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.T__4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.array()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
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





