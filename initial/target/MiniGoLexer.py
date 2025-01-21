# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2&")
        buf.write("\u01b7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\6\23\u009e\n\23\r\23\16\23\u009f")
        buf.write("\3\24\3\24\3\24\6\24\u00a5\n\24\r\24\16\24\u00a6\3\25")
        buf.write("\3\25\3\25\6\25\u00ac\n\25\r\25\16\25\u00ad\3\26\3\26")
        buf.write("\3\26\7\26\u00b3\n\26\f\26\16\26\u00b6\13\26\5\26\u00b8")
        buf.write("\n\26\3\27\3\27\3\27\3\27\5\27\u00be\n\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u00d5\n")
        buf.write("\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u00e6\n\31\3\32\3\32\3")
        buf.write("\32\3\32\7\32\u00ec\n\32\f\32\16\32\u00ef\13\32\3\32\5")
        buf.write("\32\u00f2\n\32\3\32\3\32\3\33\3\33\3\33\3\33\7\33\u00fa")
        buf.write("\n\33\f\33\16\33\u00fd\13\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u0138\n")
        buf.write("\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0143\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u0151\n\36\3\37\3\37\3\37\5\37")
        buf.write("\u0156\n\37\3\37\3\37\3\37\5\37\u015b\n\37\3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u016d\n \3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u017b\n")
        buf.write("\"\3#\3#\7#\u017f\n#\f#\16#\u0182\13#\3$\3$\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\5)\u0193\n)\3*\3*\3*\7")
        buf.write("*\u0198\n*\f*\16*\u019b\13*\3+\3+\3+\3+\3,\6,\u01a2\n")
        buf.write(",\r,\16,\u01a3\3,\3,\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/")
        buf.write("\3/\5/\u01b4\n/\3/\3/\2\2\60\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\2\'\2)\2+\2-\24/\25\61\26\63\27\65\30\67\319\32")
        buf.write(";\33=\34?\35A\36C\37E\2G I\2K\2M\2O\2Q\2S!U\"W#Y$[%]&")
        buf.write("\3\2\24\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2")
        buf.write("\62;CHch\3\3\f\f\4\2GGgg\4\2--//\6\2\'\',-//\61\61\4\2")
        buf.write("##\60\60\t\2*+..==]]__}}\177\177\4\2$$^^\3\2C\\\3\2c|")
        buf.write("\3\2\62;\3\2\63;\5\2\13\13\17\17\"\"\2\u01e2\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2G\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2")
        buf.write("\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2")
        buf.write("\2\5a\3\2\2\2\7c\3\2\2\2\ti\3\2\2\2\13m\3\2\2\2\ro\3\2")
        buf.write("\2\2\17q\3\2\2\2\21s\3\2\2\2\23u\3\2\2\2\25w\3\2\2\2\27")
        buf.write("|\3\2\2\2\31\u0083\3\2\2\2\33\u0085\3\2\2\2\35\u0087\3")
        buf.write("\2\2\2\37\u0091\3\2\2\2!\u0093\3\2\2\2#\u0095\3\2\2\2")
        buf.write("%\u009a\3\2\2\2\'\u00a1\3\2\2\2)\u00a8\3\2\2\2+\u00b7")
        buf.write("\3\2\2\2-\u00bd\3\2\2\2/\u00d4\3\2\2\2\61\u00e5\3\2\2")
        buf.write("\2\63\u00e7\3\2\2\2\65\u00f5\3\2\2\2\67\u0137\3\2\2\2")
        buf.write("9\u0142\3\2\2\2;\u0150\3\2\2\2=\u0152\3\2\2\2?\u016c\3")
        buf.write("\2\2\2A\u016e\3\2\2\2C\u017a\3\2\2\2E\u0180\3\2\2\2G\u0183")
        buf.write("\3\2\2\2I\u0187\3\2\2\2K\u0189\3\2\2\2M\u018b\3\2\2\2")
        buf.write("O\u018d\3\2\2\2Q\u0192\3\2\2\2S\u0194\3\2\2\2U\u019c\3")
        buf.write("\2\2\2W\u01a1\3\2\2\2Y\u01a7\3\2\2\2[\u01a9\3\2\2\2]\u01ae")
        buf.write("\3\2\2\2_`\7=\2\2`\4\3\2\2\2ab\7?\2\2b\6\3\2\2\2cd\7e")
        buf.write("\2\2de\7q\2\2ef\7p\2\2fg\7u\2\2gh\7v\2\2h\b\3\2\2\2ij")
        buf.write("\7x\2\2jk\7c\2\2kl\7t\2\2l\n\3\2\2\2mn\7}\2\2n\f\3\2\2")
        buf.write("\2op\7.\2\2p\16\3\2\2\2qr\7\177\2\2r\20\3\2\2\2st\7]\2")
        buf.write("\2t\22\3\2\2\2uv\7_\2\2v\24\3\2\2\2wx\7v\2\2xy\7{\2\2")
        buf.write("yz\7r\2\2z{\7g\2\2{\26\3\2\2\2|}\7u\2\2}~\7v\2\2~\177")
        buf.write("\7t\2\2\177\u0080\7w\2\2\u0080\u0081\7e\2\2\u0081\u0082")
        buf.write("\7v\2\2\u0082\30\3\2\2\2\u0083\u0084\7\60\2\2\u0084\32")
        buf.write("\3\2\2\2\u0085\u0086\7<\2\2\u0086\34\3\2\2\2\u0087\u0088")
        buf.write("\7k\2\2\u0088\u0089\7p\2\2\u0089\u008a\7v\2\2\u008a\u008b")
        buf.write("\7g\2\2\u008b\u008c\7t\2\2\u008c\u008d\7h\2\2\u008d\u008e")
        buf.write("\7c\2\2\u008e\u008f\7e\2\2\u008f\u0090\7g\2\2\u0090\36")
        buf.write("\3\2\2\2\u0091\u0092\7*\2\2\u0092 \3\2\2\2\u0093\u0094")
        buf.write("\7+\2\2\u0094\"\3\2\2\2\u0095\u0096\7h\2\2\u0096\u0097")
        buf.write("\7w\2\2\u0097\u0098\7p\2\2\u0098\u0099\7e\2\2\u0099$\3")
        buf.write("\2\2\2\u009a\u009b\7\62\2\2\u009b\u009d\t\2\2\2\u009c")
        buf.write("\u009e\t\3\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0&\3\2\2")
        buf.write("\2\u00a1\u00a2\7\62\2\2\u00a2\u00a4\t\4\2\2\u00a3\u00a5")
        buf.write("\t\5\2\2\u00a4\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7(\3\2\2\2\u00a8")
        buf.write("\u00a9\7\62\2\2\u00a9\u00ab\t\6\2\2\u00aa\u00ac\t\7\2")
        buf.write("\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00ab")
        buf.write("\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae*\3\2\2\2\u00af\u00b8")
        buf.write("\7\62\2\2\u00b0\u00b4\5O(\2\u00b1\u00b3\5M\'\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4")
        buf.write("\u00b5\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2")
        buf.write("\u00b7\u00af\3\2\2\2\u00b7\u00b0\3\2\2\2\u00b8,\3\2\2")
        buf.write("\2\u00b9\u00be\5+\26\2\u00ba\u00be\5%\23\2\u00bb\u00be")
        buf.write("\5\'\24\2\u00bc\u00be\5)\25\2\u00bd\u00b9\3\2\2\2\u00bd")
        buf.write("\u00ba\3\2\2\2\u00bd\u00bb\3\2\2\2\u00bd\u00bc\3\2\2\2")
        buf.write("\u00be.\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2")
        buf.write("\u00c1\u00c2\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p")
        buf.write("\2\2\u00c4\u00d5\7i\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00d5\7v\2\2\u00c8\u00c9\7h\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00d5")
        buf.write("\7v\2\2\u00cd\u00ce\7d\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0")
        buf.write("\7q\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3")
        buf.write("\7c\2\2\u00d3\u00d5\7p\2\2\u00d4\u00bf\3\2\2\2\u00d4\u00c5")
        buf.write("\3\2\2\2\u00d4\u00c8\3\2\2\2\u00d4\u00cd\3\2\2\2\u00d5")
        buf.write("\60\3\2\2\2\u00d6\u00d7\7u\2\2\u00d7\u00d8\7v\2\2\u00d8")
        buf.write("\u00d9\7t\2\2\u00d9\u00da\7w\2\2\u00da\u00db\7e\2\2\u00db")
        buf.write("\u00e6\7v\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de")
        buf.write("\u00df\7v\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7t\2\2\u00e1")
        buf.write("\u00e2\7h\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7e\2\2\u00e4")
        buf.write("\u00e6\7g\2\2\u00e5\u00d6\3\2\2\2\u00e5\u00dc\3\2\2\2")
        buf.write("\u00e6\62\3\2\2\2\u00e7\u00e8\7\61\2\2\u00e8\u00e9\7\61")
        buf.write("\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00ec\13\2\2\2\u00eb\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00f0\u00f2\t\b\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3")
        buf.write("\2\2\2\u00f3\u00f4\b\32\2\2\u00f4\64\3\2\2\2\u00f5\u00f6")
        buf.write("\7\61\2\2\u00f6\u00f7\7,\2\2\u00f7\u00fb\3\2\2\2\u00f8")
        buf.write("\u00fa\13\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fd\3\2\2")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fe\u00ff\7,\2\2\u00ff")
        buf.write("\u0100\7\61\2\2\u0100\u0101\3\2\2\2\u0101\u0102\b\33\2")
        buf.write("\2\u0102\66\3\2\2\2\u0103\u0104\7k\2\2\u0104\u0138\7h")
        buf.write("\2\2\u0105\u0106\7g\2\2\u0106\u0107\7n\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0138\7g\2\2\u0109\u010a\7h\2\2\u010a\u010b")
        buf.write("\7q\2\2\u010b\u0138\7t\2\2\u010c\u010d\7t\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\u010f\7v\2\2\u010f\u0110\7w\2\2\u0110\u0111")
        buf.write("\7t\2\2\u0111\u0138\7p\2\2\u0112\u0113\7h\2\2\u0113\u0114")
        buf.write("\7w\2\2\u0114\u0115\7p\2\2\u0115\u0138\7e\2\2\u0116\u0117")
        buf.write("\7v\2\2\u0117\u0118\7{\2\2\u0118\u0119\7r\2\2\u0119\u0138")
        buf.write("\7g\2\2\u011a\u011b\7e\2\2\u011b\u011c\7q\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7u\2\2\u011e\u0138\7v\2\2\u011f\u0120")
        buf.write("\7x\2\2\u0120\u0121\7c\2\2\u0121\u0138\7t\2\2\u0122\u0123")
        buf.write("\7e\2\2\u0123\u0124\7q\2\2\u0124\u0125\7p\2\2\u0125\u0126")
        buf.write("\7v\2\2\u0126\u0127\7k\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7w\2\2\u0129\u0138\7g\2\2\u012a\u012b\7d\2\2\u012b\u012c")
        buf.write("\7t\2\2\u012c\u012d\7g\2\2\u012d\u012e\7c\2\2\u012e\u0138")
        buf.write("\7m\2\2\u012f\u0130\7t\2\2\u0130\u0131\7c\2\2\u0131\u0132")
        buf.write("\7p\2\2\u0132\u0133\7i\2\2\u0133\u0138\7g\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7k\2\2\u0136\u0138\7n\2\2\u0137\u0103")
        buf.write("\3\2\2\2\u0137\u0105\3\2\2\2\u0137\u0109\3\2\2\2\u0137")
        buf.write("\u010c\3\2\2\2\u0137\u0112\3\2\2\2\u0137\u0116\3\2\2\2")
        buf.write("\u0137\u011a\3\2\2\2\u0137\u011f\3\2\2\2\u0137\u0122\3")
        buf.write("\2\2\2\u0137\u012a\3\2\2\2\u0137\u012f\3\2\2\2\u0137\u0134")
        buf.write("\3\2\2\2\u01388\3\2\2\2\u0139\u013a\7v\2\2\u013a\u013b")
        buf.write("\7t\2\2\u013b\u013c\7w\2\2\u013c\u0143\7g\2\2\u013d\u013e")
        buf.write("\7h\2\2\u013e\u013f\7c\2\2\u013f\u0140\7n\2\2\u0140\u0141")
        buf.write("\7u\2\2\u0141\u0143\7g\2\2\u0142\u0139\3\2\2\2\u0142\u013d")
        buf.write("\3\2\2\2\u0143:\3\2\2\2\u0144\u0145\7-\2\2\u0145\u0151")
        buf.write("\7?\2\2\u0146\u0147\7/\2\2\u0147\u0151\7?\2\2\u0148\u0149")
        buf.write("\7,\2\2\u0149\u0151\7?\2\2\u014a\u014b\7\61\2\2\u014b")
        buf.write("\u0151\7?\2\2\u014c\u014d\7\'\2\2\u014d\u0151\7?\2\2\u014e")
        buf.write("\u014f\7<\2\2\u014f\u0151\7?\2\2\u0150\u0144\3\2\2\2\u0150")
        buf.write("\u0146\3\2\2\2\u0150\u0148\3\2\2\2\u0150\u014a\3\2\2\2")
        buf.write("\u0150\u014c\3\2\2\2\u0150\u014e\3\2\2\2\u0151<\3\2\2")
        buf.write("\2\u0152\u0153\5+\26\2\u0153\u0155\7\60\2\2\u0154\u0156")
        buf.write("\5+\26\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u015a\3\2\2\2\u0157\u0158\t\t\2\2\u0158\u0159\t\n\2\2")
        buf.write("\u0159\u015b\5+\26\2\u015a\u0157\3\2\2\2\u015a\u015b\3")
        buf.write("\2\2\2\u015b>\3\2\2\2\u015c\u016d\t\13\2\2\u015d\u015e")
        buf.write("\7?\2\2\u015e\u016d\7?\2\2\u015f\u0160\7#\2\2\u0160\u016d")
        buf.write("\7?\2\2\u0161\u016d\7>\2\2\u0162\u0163\7>\2\2\u0163\u016d")
        buf.write("\7?\2\2\u0164\u016d\7@\2\2\u0165\u0166\7@\2\2\u0166\u016d")
        buf.write("\7?\2\2\u0167\u0168\7(\2\2\u0168\u016d\7(\2\2\u0169\u016a")
        buf.write("\7~\2\2\u016a\u016d\7~\2\2\u016b\u016d\t\f\2\2\u016c\u015c")
        buf.write("\3\2\2\2\u016c\u015d\3\2\2\2\u016c\u015f\3\2\2\2\u016c")
        buf.write("\u0161\3\2\2\2\u016c\u0162\3\2\2\2\u016c\u0164\3\2\2\2")
        buf.write("\u016c\u0165\3\2\2\2\u016c\u0167\3\2\2\2\u016c\u0169\3")
        buf.write("\2\2\2\u016c\u016b\3\2\2\2\u016d@\3\2\2\2\u016e\u016f")
        buf.write("\t\r\2\2\u016fB\3\2\2\2\u0170\u0171\7^\2\2\u0171\u017b")
        buf.write("\7p\2\2\u0172\u0173\7^\2\2\u0173\u017b\7v\2\2\u0174\u0175")
        buf.write("\7^\2\2\u0175\u017b\7t\2\2\u0176\u0177\7^\2\2\u0177\u017b")
        buf.write("\7$\2\2\u0178\u0179\7^\2\2\u0179\u017b\7^\2\2\u017a\u0170")
        buf.write("\3\2\2\2\u017a\u0172\3\2\2\2\u017a\u0174\3\2\2\2\u017a")
        buf.write("\u0176\3\2\2\2\u017a\u0178\3\2\2\2\u017bD\3\2\2\2\u017c")
        buf.write("\u017f\n\16\2\2\u017d\u017f\5C\"\2\u017e\u017c\3\2\2\2")
        buf.write("\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180\u017e\3")
        buf.write("\2\2\2\u0180\u0181\3\2\2\2\u0181F\3\2\2\2\u0182\u0180")
        buf.write("\3\2\2\2\u0183\u0184\7$\2\2\u0184\u0185\5E#\2\u0185\u0186")
        buf.write("\7$\2\2\u0186H\3\2\2\2\u0187\u0188\t\17\2\2\u0188J\3\2")
        buf.write("\2\2\u0189\u018a\t\20\2\2\u018aL\3\2\2\2\u018b\u018c\t")
        buf.write("\21\2\2\u018cN\3\2\2\2\u018d\u018e\t\22\2\2\u018eP\3\2")
        buf.write("\2\2\u018f\u0193\5I%\2\u0190\u0193\5K&\2\u0191\u0193\7")
        buf.write("a\2\2\u0192\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191")
        buf.write("\3\2\2\2\u0193R\3\2\2\2\u0194\u0199\5Q)\2\u0195\u0198")
        buf.write("\5Q)\2\u0196\u0198\5M\'\2\u0197\u0195\3\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019aT\3\2\2\2\u019b\u0199\3\2\2\2\u019c")
        buf.write("\u019d\7\f\2\2\u019d\u019e\3\2\2\2\u019e\u019f\b+\2\2")
        buf.write("\u019fV\3\2\2\2\u01a0\u01a2\t\23\2\2\u01a1\u01a0\3\2\2")
        buf.write("\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\b,\2\2\u01a6")
        buf.write("X\3\2\2\2\u01a7\u01a8\13\2\2\2\u01a8Z\3\2\2\2\u01a9\u01aa")
        buf.write("\7$\2\2\u01aa\u01ab\5E#\2\u01ab\u01ac\7^\2\2\u01ac\u01ad")
        buf.write("\b.\3\2\u01ad\\\3\2\2\2\u01ae\u01af\7$\2\2\u01af\u01b3")
        buf.write("\5E#\2\u01b0\u01b1\7^\2\2\u01b1\u01b4\7p\2\2\u01b2\u01b4")
        buf.write("\7\2\2\3\u01b3\u01b0\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5\u01b6\b/\4\2\u01b6^\3\2\2\2\34\2")
        buf.write("\u009f\u00a6\u00ad\u00b4\u00b7\u00bd\u00d4\u00e5\u00ed")
        buf.write("\u00f1\u00fb\u0137\u0142\u0150\u0155\u015a\u016c\u017a")
        buf.write("\u017e\u0180\u0192\u0197\u0199\u01a3\u01b3\5\b\2\2\3.")
        buf.write("\2\3/\3")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    INTEGER = 18
    ATOMIC_TYPE = 19
    COMPOSITE_TYPE = 20
    COMMENT1 = 21
    COMMENT2 = 22
    KEYWORD = 23
    BOOLEAN = 24
    ASSIGN_OP = 25
    FLOAT = 26
    OPERATOR = 27
    SEPARATOR = 28
    ESCAPE = 29
    STRING = 30
    ID = 31
    NL = 32
    WS = 33
    ERROR_CHAR = 34
    ILLEGAL_ESCAPE = 35
    UNCLOSE_STRING = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'const'", "'var'", "'{'", "','", "'}'", "'['", 
            "']'", "'type'", "'struct'", "'.'", "':'", "'interface'", "'('", 
            "')'", "'func'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "ATOMIC_TYPE", "COMPOSITE_TYPE", "COMMENT1", "COMMENT2", 
            "KEYWORD", "BOOLEAN", "ASSIGN_OP", "FLOAT", "OPERATOR", "SEPARATOR", 
            "ESCAPE", "STRING", "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "BINARY", "OCTAL", "HEXADEC", 
                  "DECIMAL", "INTEGER", "ATOMIC_TYPE", "COMPOSITE_TYPE", 
                  "COMMENT1", "COMMENT2", "KEYWORD", "BOOLEAN", "ASSIGN_OP", 
                  "FLOAT", "OPERATOR", "SEPARATOR", "ESCAPE", "IN_STRING", 
                  "STRING", "UpperLetter", "LowerLetter", "Digit", "NonZeroDigit", 
                  "IdentifierStart", "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.ILLEGAL_ESCAPE_action 
            actions[45] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise UncloseString(self.text[1:])

     


