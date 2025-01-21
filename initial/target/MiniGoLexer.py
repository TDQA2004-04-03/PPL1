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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'")
        buf.write("\u01bb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\6\24\u00a7\n\24\r\24\16\24\u00a8\3\25\3\25")
        buf.write("\3\25\6\25\u00ae\n\25\r\25\16\25\u00af\3\26\3\26\3\26")
        buf.write("\6\26\u00b5\n\26\r\26\16\26\u00b6\3\27\3\27\3\27\7\27")
        buf.write("\u00bc\n\27\f\27\16\27\u00bf\13\27\5\27\u00c1\n\27\3\30")
        buf.write("\3\30\3\30\3\30\5\30\u00c7\n\30\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00de\n\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\5\32\u00ef\n\32\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u00f5\n\33\f\33\16\33\u00f8\13\33\3\33\5\33\u00fb")
        buf.write("\n\33\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u0103\n\34\f")
        buf.write("\34\16\34\u0106\13\34\3\34\3\34\3\34\3\34\3\34\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u013b\n\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\5\36\u0146\n\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0154\n\37\3")
        buf.write(" \3 \3 \5 \u0159\n \3 \3 \3 \5 \u015e\n \3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u0171\n!\3\"")
        buf.write("\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#\u017f\n#\3$\3$\7")
        buf.write("$\u0183\n$\f$\16$\u0186\13$\3%\3%\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3*\5*\u0197\n*\3+\3+\3+\7+\u019c\n")
        buf.write("+\f+\16+\u019f\13+\3,\3,\3,\3,\3-\6-\u01a6\n-\r-\16-\u01a7")
        buf.write("\3-\3-\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\5")
        buf.write("\60\u01b8\n\60\3\60\3\60\2\2\61\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\2)\2+\2-\2/\25\61\26\63\27\65\30\67\319")
        buf.write("\32;\33=\34?\35A\36C\37E G\2I!K\2M\2O\2Q\2S\2U\"W#Y$[")
        buf.write("%]&_\'\3\2\24\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZ")
        buf.write("zz\5\2\62;CHch\3\3\f\f\4\2GGgg\4\2--//\6\2\'\',-//\61")
        buf.write("\61\4\2##\60\60\t\2*+..==]]__}}\177\177\4\2$$^^\3\2C\\")
        buf.write("\3\2c|\3\2\62;\3\2\63;\5\2\13\13\17\17\"\"\2\u01e5\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2")
        buf.write("\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3")
        buf.write("\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2I\3\2\2\2\2U")
        buf.write("\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2")
        buf.write("_\3\2\2\2\3a\3\2\2\2\5c\3\2\2\2\7i\3\2\2\2\tk\3\2\2\2")
        buf.write("\13o\3\2\2\2\rq\3\2\2\2\17s\3\2\2\2\21u\3\2\2\2\23w\3")
        buf.write("\2\2\2\25y\3\2\2\2\27~\3\2\2\2\31\u0085\3\2\2\2\33\u0087")
        buf.write("\3\2\2\2\35\u0089\3\2\2\2\37\u0093\3\2\2\2!\u0095\3\2")
        buf.write("\2\2#\u0097\3\2\2\2%\u009c\3\2\2\2\'\u00a3\3\2\2\2)\u00aa")
        buf.write("\3\2\2\2+\u00b1\3\2\2\2-\u00c0\3\2\2\2/\u00c6\3\2\2\2")
        buf.write("\61\u00dd\3\2\2\2\63\u00ee\3\2\2\2\65\u00f0\3\2\2\2\67")
        buf.write("\u00fe\3\2\2\29\u013a\3\2\2\2;\u0145\3\2\2\2=\u0153\3")
        buf.write("\2\2\2?\u0155\3\2\2\2A\u0170\3\2\2\2C\u0172\3\2\2\2E\u017e")
        buf.write("\3\2\2\2G\u0184\3\2\2\2I\u0187\3\2\2\2K\u018b\3\2\2\2")
        buf.write("M\u018d\3\2\2\2O\u018f\3\2\2\2Q\u0191\3\2\2\2S\u0196\3")
        buf.write("\2\2\2U\u0198\3\2\2\2W\u01a0\3\2\2\2Y\u01a5\3\2\2\2[\u01ab")
        buf.write("\3\2\2\2]\u01ad\3\2\2\2_\u01b2\3\2\2\2ab\7=\2\2b\4\3\2")
        buf.write("\2\2cd\7e\2\2de\7q\2\2ef\7p\2\2fg\7u\2\2gh\7v\2\2h\6\3")
        buf.write("\2\2\2ij\7?\2\2j\b\3\2\2\2kl\7x\2\2lm\7c\2\2mn\7t\2\2")
        buf.write("n\n\3\2\2\2op\7}\2\2p\f\3\2\2\2qr\7.\2\2r\16\3\2\2\2s")
        buf.write("t\7\177\2\2t\20\3\2\2\2uv\7]\2\2v\22\3\2\2\2wx\7_\2\2")
        buf.write("x\24\3\2\2\2yz\7v\2\2z{\7{\2\2{|\7r\2\2|}\7g\2\2}\26\3")
        buf.write("\2\2\2~\177\7u\2\2\177\u0080\7v\2\2\u0080\u0081\7t\2\2")
        buf.write("\u0081\u0082\7w\2\2\u0082\u0083\7e\2\2\u0083\u0084\7v")
        buf.write("\2\2\u0084\30\3\2\2\2\u0085\u0086\7\60\2\2\u0086\32\3")
        buf.write("\2\2\2\u0087\u0088\7<\2\2\u0088\34\3\2\2\2\u0089\u008a")
        buf.write("\7k\2\2\u008a\u008b\7p\2\2\u008b\u008c\7v\2\2\u008c\u008d")
        buf.write("\7g\2\2\u008d\u008e\7t\2\2\u008e\u008f\7h\2\2\u008f\u0090")
        buf.write("\7c\2\2\u0090\u0091\7e\2\2\u0091\u0092\7g\2\2\u0092\36")
        buf.write("\3\2\2\2\u0093\u0094\7*\2\2\u0094 \3\2\2\2\u0095\u0096")
        buf.write("\7+\2\2\u0096\"\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b\7e\2\2\u009b$\3")
        buf.write("\2\2\2\u009c\u009d\7t\2\2\u009d\u009e\7g\2\2\u009e\u009f")
        buf.write("\7v\2\2\u009f\u00a0\7w\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2&\3\2\2\2\u00a3\u00a4\7\62\2\2\u00a4\u00a6")
        buf.write("\t\2\2\2\u00a5\u00a7\t\3\2\2\u00a6\u00a5\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2")
        buf.write("\u00a9(\3\2\2\2\u00aa\u00ab\7\62\2\2\u00ab\u00ad\t\4\2")
        buf.write("\2\u00ac\u00ae\t\5\2\2\u00ad\u00ac\3\2\2\2\u00ae\u00af")
        buf.write("\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("*\3\2\2\2\u00b1\u00b2\7\62\2\2\u00b2\u00b4\t\6\2\2\u00b3")
        buf.write("\u00b5\t\7\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7,\3\2\2")
        buf.write("\2\u00b8\u00c1\7\62\2\2\u00b9\u00bd\5Q)\2\u00ba\u00bc")
        buf.write("\5O(\2\u00bb\u00ba\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf")
        buf.write("\u00bd\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00b9\3\2\2\2")
        buf.write("\u00c1.\3\2\2\2\u00c2\u00c7\5-\27\2\u00c3\u00c7\5\'\24")
        buf.write("\2\u00c4\u00c7\5)\25\2\u00c5\u00c7\5+\26\2\u00c6\u00c2")
        buf.write("\3\2\2\2\u00c6\u00c3\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\60\3\2\2\2\u00c8\u00c9\7u\2\2\u00c9")
        buf.write("\u00ca\7v\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7k\2\2\u00cc")
        buf.write("\u00cd\7p\2\2\u00cd\u00de\7i\2\2\u00ce\u00cf\7k\2\2\u00cf")
        buf.write("\u00d0\7p\2\2\u00d0\u00de\7v\2\2\u00d1\u00d2\7h\2\2\u00d2")
        buf.write("\u00d3\7n\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d5\7c\2\2\u00d5")
        buf.write("\u00de\7v\2\2\u00d6\u00d7\7d\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7q\2\2\u00d9\u00da\7n\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\u00dc\7c\2\2\u00dc\u00de\7p\2\2\u00dd\u00c8\3\2\2\2\u00dd")
        buf.write("\u00ce\3\2\2\2\u00dd\u00d1\3\2\2\2\u00dd\u00d6\3\2\2\2")
        buf.write("\u00de\62\3\2\2\2\u00df\u00e0\7u\2\2\u00e0\u00e1\7v\2")
        buf.write("\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7")
        buf.write("e\2\2\u00e4\u00ef\7v\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7")
        buf.write("\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\u00e9\7g\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7h\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ef\7g\2\2\u00ee\u00df\3\2\2\2\u00ee\u00e5")
        buf.write("\3\2\2\2\u00ef\64\3\2\2\2\u00f0\u00f1\7\61\2\2\u00f1\u00f2")
        buf.write("\7\61\2\2\u00f2\u00f6\3\2\2\2\u00f3\u00f5\13\2\2\2\u00f4")
        buf.write("\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3\2\2\2")
        buf.write("\u00f6\u00f7\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8\u00f6\3")
        buf.write("\2\2\2\u00f9\u00fb\t\b\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc")
        buf.write("\3\2\2\2\u00fc\u00fd\b\33\2\2\u00fd\66\3\2\2\2\u00fe\u00ff")
        buf.write("\7\61\2\2\u00ff\u0100\7,\2\2\u0100\u0104\3\2\2\2\u0101")
        buf.write("\u0103\13\2\2\2\u0102\u0101\3\2\2\2\u0103\u0106\3\2\2")
        buf.write("\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0107")
        buf.write("\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7,\2\2\u0108")
        buf.write("\u0109\7\61\2\2\u0109\u010a\3\2\2\2\u010a\u010b\b\34\2")
        buf.write("\2\u010b8\3\2\2\2\u010c\u010d\7k\2\2\u010d\u013b\7h\2")
        buf.write("\2\u010e\u010f\7g\2\2\u010f\u0110\7n\2\2\u0110\u0111\7")
        buf.write("u\2\2\u0111\u013b\7g\2\2\u0112\u0113\7h\2\2\u0113\u0114")
        buf.write("\7q\2\2\u0114\u013b\7t\2\2\u0115\u0116\7h\2\2\u0116\u0117")
        buf.write("\7w\2\2\u0117\u0118\7p\2\2\u0118\u013b\7e\2\2\u0119\u011a")
        buf.write("\7v\2\2\u011a\u011b\7{\2\2\u011b\u011c\7r\2\2\u011c\u013b")
        buf.write("\7g\2\2\u011d\u011e\7e\2\2\u011e\u011f\7q\2\2\u011f\u0120")
        buf.write("\7p\2\2\u0120\u0121\7u\2\2\u0121\u013b\7v\2\2\u0122\u0123")
        buf.write("\7x\2\2\u0123\u0124\7c\2\2\u0124\u013b\7t\2\2\u0125\u0126")
        buf.write("\7e\2\2\u0126\u0127\7q\2\2\u0127\u0128\7p\2\2\u0128\u0129")
        buf.write("\7v\2\2\u0129\u012a\7k\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7w\2\2\u012c\u013b\7g\2\2\u012d\u012e\7d\2\2\u012e\u012f")
        buf.write("\7t\2\2\u012f\u0130\7g\2\2\u0130\u0131\7c\2\2\u0131\u013b")
        buf.write("\7m\2\2\u0132\u0133\7t\2\2\u0133\u0134\7c\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7i\2\2\u0136\u013b\7g\2\2\u0137\u0138")
        buf.write("\7p\2\2\u0138\u0139\7k\2\2\u0139\u013b\7n\2\2\u013a\u010c")
        buf.write("\3\2\2\2\u013a\u010e\3\2\2\2\u013a\u0112\3\2\2\2\u013a")
        buf.write("\u0115\3\2\2\2\u013a\u0119\3\2\2\2\u013a\u011d\3\2\2\2")
        buf.write("\u013a\u0122\3\2\2\2\u013a\u0125\3\2\2\2\u013a\u012d\3")
        buf.write("\2\2\2\u013a\u0132\3\2\2\2\u013a\u0137\3\2\2\2\u013b:")
        buf.write("\3\2\2\2\u013c\u013d\7v\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7w\2\2\u013f\u0146\7g\2\2\u0140\u0141\7h\2\2\u0141\u0142")
        buf.write("\7c\2\2\u0142\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0146")
        buf.write("\7g\2\2\u0145\u013c\3\2\2\2\u0145\u0140\3\2\2\2\u0146")
        buf.write("<\3\2\2\2\u0147\u0148\7-\2\2\u0148\u0154\7?\2\2\u0149")
        buf.write("\u014a\7/\2\2\u014a\u0154\7?\2\2\u014b\u014c\7,\2\2\u014c")
        buf.write("\u0154\7?\2\2\u014d\u014e\7\61\2\2\u014e\u0154\7?\2\2")
        buf.write("\u014f\u0150\7\'\2\2\u0150\u0154\7?\2\2\u0151\u0152\7")
        buf.write("<\2\2\u0152\u0154\7?\2\2\u0153\u0147\3\2\2\2\u0153\u0149")
        buf.write("\3\2\2\2\u0153\u014b\3\2\2\2\u0153\u014d\3\2\2\2\u0153")
        buf.write("\u014f\3\2\2\2\u0153\u0151\3\2\2\2\u0154>\3\2\2\2\u0155")
        buf.write("\u0156\5-\27\2\u0156\u0158\7\60\2\2\u0157\u0159\5-\27")
        buf.write("\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015d")
        buf.write("\3\2\2\2\u015a\u015b\t\t\2\2\u015b\u015c\t\n\2\2\u015c")
        buf.write("\u015e\5-\27\2\u015d\u015a\3\2\2\2\u015d\u015e\3\2\2\2")
        buf.write("\u015e@\3\2\2\2\u015f\u0171\t\13\2\2\u0160\u0161\7?\2")
        buf.write("\2\u0161\u0171\7?\2\2\u0162\u0163\7#\2\2\u0163\u0171\7")
        buf.write("?\2\2\u0164\u0171\7>\2\2\u0165\u0166\7>\2\2\u0166\u0171")
        buf.write("\7?\2\2\u0167\u0171\7@\2\2\u0168\u0169\7@\2\2\u0169\u0171")
        buf.write("\7?\2\2\u016a\u016b\7?\2\2\u016b\u016c\7(\2\2\u016c\u0171")
        buf.write("\7(\2\2\u016d\u016e\7~\2\2\u016e\u0171\7~\2\2\u016f\u0171")
        buf.write("\t\f\2\2\u0170\u015f\3\2\2\2\u0170\u0160\3\2\2\2\u0170")
        buf.write("\u0162\3\2\2\2\u0170\u0164\3\2\2\2\u0170\u0165\3\2\2\2")
        buf.write("\u0170\u0167\3\2\2\2\u0170\u0168\3\2\2\2\u0170\u016a\3")
        buf.write("\2\2\2\u0170\u016d\3\2\2\2\u0170\u016f\3\2\2\2\u0171B")
        buf.write("\3\2\2\2\u0172\u0173\t\r\2\2\u0173D\3\2\2\2\u0174\u0175")
        buf.write("\7^\2\2\u0175\u017f\7p\2\2\u0176\u0177\7^\2\2\u0177\u017f")
        buf.write("\7v\2\2\u0178\u0179\7^\2\2\u0179\u017f\7t\2\2\u017a\u017b")
        buf.write("\7^\2\2\u017b\u017f\7$\2\2\u017c\u017d\7^\2\2\u017d\u017f")
        buf.write("\7^\2\2\u017e\u0174\3\2\2\2\u017e\u0176\3\2\2\2\u017e")
        buf.write("\u0178\3\2\2\2\u017e\u017a\3\2\2\2\u017e\u017c\3\2\2\2")
        buf.write("\u017fF\3\2\2\2\u0180\u0183\n\16\2\2\u0181\u0183\5E#\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185H")
        buf.write("\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\7$\2\2\u0188")
        buf.write("\u0189\5G$\2\u0189\u018a\7$\2\2\u018aJ\3\2\2\2\u018b\u018c")
        buf.write("\t\17\2\2\u018cL\3\2\2\2\u018d\u018e\t\20\2\2\u018eN\3")
        buf.write("\2\2\2\u018f\u0190\t\21\2\2\u0190P\3\2\2\2\u0191\u0192")
        buf.write("\t\22\2\2\u0192R\3\2\2\2\u0193\u0197\5K&\2\u0194\u0197")
        buf.write("\5M\'\2\u0195\u0197\7a\2\2\u0196\u0193\3\2\2\2\u0196\u0194")
        buf.write("\3\2\2\2\u0196\u0195\3\2\2\2\u0197T\3\2\2\2\u0198\u019d")
        buf.write("\5S*\2\u0199\u019c\5S*\2\u019a\u019c\5O(\2\u019b\u0199")
        buf.write("\3\2\2\2\u019b\u019a\3\2\2\2\u019c\u019f\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019eV\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u01a0\u01a1\7\f\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u01a3\b,\2\2\u01a3X\3\2\2\2\u01a4\u01a6\t\23\2")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9")
        buf.write("\u01aa\b-\2\2\u01aaZ\3\2\2\2\u01ab\u01ac\13\2\2\2\u01ac")
        buf.write("\\\3\2\2\2\u01ad\u01ae\7$\2\2\u01ae\u01af\5G$\2\u01af")
        buf.write("\u01b0\7^\2\2\u01b0\u01b1\b/\3\2\u01b1^\3\2\2\2\u01b2")
        buf.write("\u01b3\7$\2\2\u01b3\u01b7\5G$\2\u01b4\u01b5\7^\2\2\u01b5")
        buf.write("\u01b8\7p\2\2\u01b6\u01b8\7\2\2\3\u01b7\u01b4\3\2\2\2")
        buf.write("\u01b7\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\b")
        buf.write("\60\4\2\u01ba`\3\2\2\2\34\2\u00a8\u00af\u00b6\u00bd\u00c0")
        buf.write("\u00c6\u00dd\u00ee\u00f6\u00fa\u0104\u013a\u0145\u0153")
        buf.write("\u0158\u015d\u0170\u017e\u0182\u0184\u0196\u019b\u019d")
        buf.write("\u01a7\u01b7\5\b\2\2\3/\2\3\60\3")
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
    T__17 = 18
    INTEGER = 19
    ATOMIC_TYPE = 20
    COMPOSITE_TYPE = 21
    COMMENT1 = 22
    COMMENT2 = 23
    KEYWORD = 24
    BOOLEAN = 25
    ASSIGN_OP = 26
    FLOAT = 27
    OPERATOR = 28
    SEPARATOR = 29
    ESCAPE = 30
    STRING = 31
    ID = 32
    NL = 33
    WS = 34
    ERROR_CHAR = 35
    ILLEGAL_ESCAPE = 36
    UNCLOSE_STRING = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'const'", "'='", "'var'", "'{'", "','", "'}'", "'['", 
            "']'", "'type'", "'struct'", "'.'", "':'", "'interface'", "'('", 
            "')'", "'func'", "'return'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "ATOMIC_TYPE", "COMPOSITE_TYPE", "COMMENT1", "COMMENT2", 
            "KEYWORD", "BOOLEAN", "ASSIGN_OP", "FLOAT", "OPERATOR", "SEPARATOR", 
            "ESCAPE", "STRING", "ID", "NL", "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "BINARY", "OCTAL", 
                  "HEXADEC", "DECIMAL", "INTEGER", "ATOMIC_TYPE", "COMPOSITE_TYPE", 
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
            actions[45] = self.ILLEGAL_ESCAPE_action 
            actions[46] = self.UNCLOSE_STRING_action 
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

     


