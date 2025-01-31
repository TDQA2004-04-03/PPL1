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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01e8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3")
        buf.write("\5\3\5\6\5\u0087\n\5\r\5\16\5\u0088\3\6\3\6\3\6\6\6\u008e")
        buf.write("\n\6\r\6\16\6\u008f\3\7\3\7\3\7\6\7\u0095\n\7\r\7\16\7")
        buf.write("\u0096\3\b\3\b\3\b\7\b\u009c\n\b\f\b\16\b\u009f\13\b\5")
        buf.write("\b\u00a1\n\b\3\t\3\t\3\t\3\t\5\t\u00a7\n\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\n\u00be\n\n\3\13\3\13\3\13\3\13\7")
        buf.write("\13\u00c4\n\13\f\13\16\13\u00c7\13\13\3\13\5\13\u00ca")
        buf.write("\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u00d2\n\f\f\f\16\f")
        buf.write("\u00d5\13\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0144\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\5\34\u0150\n\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\7\36\u015a\n\36\f\36\16\36\u015d\13\36")
        buf.write("\3\36\3\36\7\36\u0161\n\36\f\36\16\36\u0164\13\36\3\36")
        buf.write("\3\36\3\36\7\36\u0169\n\36\f\36\16\36\u016c\13\36\5\36")
        buf.write("\u016e\n\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 ")
        buf.write("\3 \5 \u017d\n \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\5\61\u01ad\n\61\3\62\3\62\7\62")
        buf.write("\u01b1\n\62\f\62\16\62\u01b4\13\62\3\63\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\58\u01c5")
        buf.write("\n8\39\39\39\79\u01ca\n9\f9\169\u01cd\139\3:\6:\u01d0")
        buf.write("\n:\r:\16:\u01d1\3:\3:\3;\3;\3;\3<\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\5=\u01e3\n=\3=\3=\3>\3>\2\2?\3\3\5\4\7\5\t\2\13")
        buf.write("\2\r\2\17\2\21\6\23\7\25\b\27\t\31\n\33\13\35\f\37\r!")
        buf.write("\16#\17%\20\'\21)\22+\23-\24/\25\61\26\63\27\65\30\67")
        buf.write("\319\32;\33=\34?\35A\36C\37E G!I\"K#M$O%Q&S\'U(W)Y*[+")
        buf.write("],_-a.c\2e/g\2i\2k\2m\2o\2q\60s\61u\62w\63y\64{\65\3\2")
        buf.write("\21\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2\62;")
        buf.write("CHch\3\3\f\f\4\2GGgg\4\2--//\4\2$$^^\3\2C\\\3\2c|\3\2")
        buf.write("\62;\3\2\63;\5\2\13\13\17\17\"\"\2\u0204\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2e\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\3}\3\2\2\2\5")
        buf.write("\177\3\2\2\2\7\u0081\3\2\2\2\t\u0083\3\2\2\2\13\u008a")
        buf.write("\3\2\2\2\r\u0091\3\2\2\2\17\u00a0\3\2\2\2\21\u00a6\3\2")
        buf.write("\2\2\23\u00bd\3\2\2\2\25\u00bf\3\2\2\2\27\u00cd\3\2\2")
        buf.write("\2\31\u00db\3\2\2\2\33\u00df\3\2\2\2\35\u00e5\3\2\2\2")
        buf.write("\37\u00ed\3\2\2\2!\u00f2\3\2\2\2#\u00f9\3\2\2\2%\u0103")
        buf.write("\3\2\2\2\'\u0108\3\2\2\2)\u0111\3\2\2\2+\u0116\3\2\2\2")
        buf.write("-\u011b\3\2\2\2/\u0121\3\2\2\2\61\u0127\3\2\2\2\63\u012f")
        buf.write("\3\2\2\2\65\u0143\3\2\2\2\67\u014f\3\2\2\29\u0153\3\2")
        buf.write("\2\2;\u015b\3\2\2\2=\u016f\3\2\2\2?\u017c\3\2\2\2A\u017e")
        buf.write("\3\2\2\2C\u0181\3\2\2\2E\u0184\3\2\2\2G\u0186\3\2\2\2")
        buf.write("I\u0188\3\2\2\2K\u018a\3\2\2\2M\u018c\3\2\2\2O\u018e\3")
        buf.write("\2\2\2Q\u0190\3\2\2\2S\u0192\3\2\2\2U\u0194\3\2\2\2W\u0197")
        buf.write("\3\2\2\2Y\u019a\3\2\2\2[\u019c\3\2\2\2]\u019e\3\2\2\2")
        buf.write("_\u01a0\3\2\2\2a\u01ac\3\2\2\2c\u01b2\3\2\2\2e\u01b5\3")
        buf.write("\2\2\2g\u01b9\3\2\2\2i\u01bb\3\2\2\2k\u01bd\3\2\2\2m\u01bf")
        buf.write("\3\2\2\2o\u01c4\3\2\2\2q\u01c6\3\2\2\2s\u01cf\3\2\2\2")
        buf.write("u\u01d5\3\2\2\2w\u01d8\3\2\2\2y\u01dd\3\2\2\2{\u01e6\3")
        buf.write("\2\2\2}~\7<\2\2~\4\3\2\2\2\177\u0080\7\60\2\2\u0080\6")
        buf.write("\3\2\2\2\u0081\u0082\7a\2\2\u0082\b\3\2\2\2\u0083\u0084")
        buf.write("\7\62\2\2\u0084\u0086\t\2\2\2\u0085\u0087\t\3\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0086\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\n\3\2\2\2\u008a\u008b\7\62")
        buf.write("\2\2\u008b\u008d\t\4\2\2\u008c\u008e\t\5\2\2\u008d\u008c")
        buf.write("\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\f\3\2\2\2\u0091\u0092\7\62\2\2\u0092")
        buf.write("\u0094\t\6\2\2\u0093\u0095\t\7\2\2\u0094\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0094\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\16\3\2\2\2\u0098\u00a1\7\62\2\2\u0099\u009d")
        buf.write("\5m\67\2\u009a\u009c\5k\66\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u0098\3")
        buf.write("\2\2\2\u00a0\u0099\3\2\2\2\u00a1\20\3\2\2\2\u00a2\u00a7")
        buf.write("\5\17\b\2\u00a3\u00a7\5\t\5\2\u00a4\u00a7\5\13\6\2\u00a5")
        buf.write("\u00a7\5\r\7\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3\2\2\2")
        buf.write("\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\22\3\2")
        buf.write("\2\2\u00a8\u00a9\7u\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00be")
        buf.write("\7i\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2\u00b0\u00be")
        buf.write("\7v\2\2\u00b1\u00b2\7h\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7q\2\2\u00b4\u00b5\7c\2\2\u00b5\u00be\7v\2\2\u00b6\u00b7")
        buf.write("\7d\2\2\u00b7\u00b8\7q\2\2\u00b8\u00b9\7q\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00be")
        buf.write("\7p\2\2\u00bd\u00a8\3\2\2\2\u00bd\u00ae\3\2\2\2\u00bd")
        buf.write("\u00b1\3\2\2\2\u00bd\u00b6\3\2\2\2\u00be\24\3\2\2\2\u00bf")
        buf.write("\u00c0\7\61\2\2\u00c0\u00c1\7\61\2\2\u00c1\u00c5\3\2\2")
        buf.write("\2\u00c2\u00c4\13\2\2\2\u00c3\u00c2\3\2\2\2\u00c4\u00c7")
        buf.write("\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00ca\t\b\2\2")
        buf.write("\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\b")
        buf.write("\13\2\2\u00cc\26\3\2\2\2\u00cd\u00ce\7\61\2\2\u00ce\u00cf")
        buf.write("\7,\2\2\u00cf\u00d3\3\2\2\2\u00d0\u00d2\13\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d4\3\2\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00d3\3")
        buf.write("\2\2\2\u00d6\u00d7\7,\2\2\u00d7\u00d8\7\61\2\2\u00d8\u00d9")
        buf.write("\3\2\2\2\u00d9\u00da\b\f\2\2\u00da\30\3\2\2\2\u00db\u00dc")
        buf.write("\7p\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7n\2\2\u00de\32")
        buf.write("\3\2\2\2\u00df\u00e0\7x\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2")
        buf.write("\7t\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\b\16\3\2\u00e4")
        buf.write("\34\3\2\2\2\u00e5\u00e6\7e\2\2\u00e6\u00e7\7q\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\u00ec\b\17\4\2\u00ec\36\3\2\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee\u00ef\7{\2\2\u00ef\u00f0\7r\2\2\u00f0")
        buf.write("\u00f1\7g\2\2\u00f1 \3\2\2\2\u00f2\u00f3\7u\2\2\u00f3")
        buf.write("\u00f4\7v\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7w\2\2\u00f6")
        buf.write("\u00f7\7e\2\2\u00f7\u00f8\7v\2\2\u00f8\"\3\2\2\2\u00f9")
        buf.write("\u00fa\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7v\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe\u00ff\7h\2\2\u00ff")
        buf.write("\u0100\7c\2\2\u0100\u0101\7e\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("$\3\2\2\2\u0103\u0104\7h\2\2\u0104\u0105\7w\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106\u0107\7e\2\2\u0107&\3\2\2\2\u0108")
        buf.write("\u0109\7t\2\2\u0109\u010a\7g\2\2\u010a\u010b\7v\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7t\2\2\u010d\u010e\7p\2\2\u010e")
        buf.write("\u010f\3\2\2\2\u010f\u0110\b\24\5\2\u0110(\3\2\2\2\u0111")
        buf.write("\u0112\7k\2\2\u0112\u0113\7h\2\2\u0113\u0114\3\2\2\2\u0114")
        buf.write("\u0115\b\25\6\2\u0115*\3\2\2\2\u0116\u0117\7g\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118\u0119\7u\2\2\u0119\u011a\7g\2\2\u011a")
        buf.write(",\3\2\2\2\u011b\u011c\7h\2\2\u011c\u011d\7q\2\2\u011d")
        buf.write("\u011e\7t\2\2\u011e\u011f\3\2\2\2\u011f\u0120\b\27\7\2")
        buf.write("\u0120.\3\2\2\2\u0121\u0122\7t\2\2\u0122\u0123\7c\2\2")
        buf.write("\u0123\u0124\7p\2\2\u0124\u0125\7i\2\2\u0125\u0126\7g")
        buf.write("\2\2\u0126\60\3\2\2\2\u0127\u0128\7d\2\2\u0128\u0129\7")
        buf.write("t\2\2\u0129\u012a\7g\2\2\u012a\u012b\7c\2\2\u012b\u012c")
        buf.write("\7m\2\2\u012c\u012d\3\2\2\2\u012d\u012e\b\31\b\2\u012e")
        buf.write("\62\3\2\2\2\u012f\u0130\7e\2\2\u0130\u0131\7q\2\2\u0131")
        buf.write("\u0132\7p\2\2\u0132\u0133\7v\2\2\u0133\u0134\7k\2\2\u0134")
        buf.write("\u0135\7p\2\2\u0135\u0136\7w\2\2\u0136\u0137\7g\2\2\u0137")
        buf.write("\u0138\3\2\2\2\u0138\u0139\b\32\t\2\u0139\64\3\2\2\2\u013a")
        buf.write("\u013b\7v\2\2\u013b\u013c\7t\2\2\u013c\u013d\7w\2\2\u013d")
        buf.write("\u0144\7g\2\2\u013e\u013f\7h\2\2\u013f\u0140\7c\2\2\u0140")
        buf.write("\u0141\7n\2\2\u0141\u0142\7u\2\2\u0142\u0144\7g\2\2\u0143")
        buf.write("\u013a\3\2\2\2\u0143\u013e\3\2\2\2\u0144\66\3\2\2\2\u0145")
        buf.write("\u0146\7-\2\2\u0146\u0150\7?\2\2\u0147\u0148\7/\2\2\u0148")
        buf.write("\u0150\7?\2\2\u0149\u014a\7,\2\2\u014a\u0150\7?\2\2\u014b")
        buf.write("\u014c\7\61\2\2\u014c\u0150\7?\2\2\u014d\u014e\7\'\2\2")
        buf.write("\u014e\u0150\7?\2\2\u014f\u0145\3\2\2\2\u014f\u0147\3")
        buf.write("\2\2\2\u014f\u0149\3\2\2\2\u014f\u014b\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0152\b\34\n\2\u0152")
        buf.write("8\3\2\2\2\u0153\u0154\7<\2\2\u0154\u0155\7?\2\2\u0155")
        buf.write("\u0156\3\2\2\2\u0156\u0157\b\35\13\2\u0157:\3\2\2\2\u0158")
        buf.write("\u015a\5k\66\2\u0159\u0158\3\2\2\2\u015a\u015d\3\2\2\2")
        buf.write("\u015b\u0159\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015e\3")
        buf.write("\2\2\2\u015d\u015b\3\2\2\2\u015e\u0162\7\60\2\2\u015f")
        buf.write("\u0161\5k\66\2\u0160\u015f\3\2\2\2\u0161\u0164\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u016d\3")
        buf.write("\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\t\t\2\2\u0166\u016a")
        buf.write("\t\n\2\2\u0167\u0169\5k\66\2\u0168\u0167\3\2\2\2\u0169")
        buf.write("\u016c\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u016b\3\2\2\2")
        buf.write("\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016d\u0165\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016e<\3\2\2\2\u016f\u0170")
        buf.write("\7=\2\2\u0170\u0171\b\37\f\2\u0171>\3\2\2\2\u0172\u0173")
        buf.write("\7?\2\2\u0173\u017d\7?\2\2\u0174\u0175\7#\2\2\u0175\u017d")
        buf.write("\7?\2\2\u0176\u017d\7>\2\2\u0177\u0178\7>\2\2\u0178\u017d")
        buf.write("\7?\2\2\u0179\u017d\7@\2\2\u017a\u017b\7@\2\2\u017b\u017d")
        buf.write("\7?\2\2\u017c\u0172\3\2\2\2\u017c\u0174\3\2\2\2\u017c")
        buf.write("\u0176\3\2\2\2\u017c\u0177\3\2\2\2\u017c\u0179\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017d@\3\2\2\2\u017e\u017f\7(\2\2")
        buf.write("\u017f\u0180\7(\2\2\u0180B\3\2\2\2\u0181\u0182\7~\2\2")
        buf.write("\u0182\u0183\7~\2\2\u0183D\3\2\2\2\u0184\u0185\7#\2\2")
        buf.write("\u0185F\3\2\2\2\u0186\u0187\7-\2\2\u0187H\3\2\2\2\u0188")
        buf.write("\u0189\7/\2\2\u0189J\3\2\2\2\u018a\u018b\7,\2\2\u018b")
        buf.write("L\3\2\2\2\u018c\u018d\7\61\2\2\u018dN\3\2\2\2\u018e\u018f")
        buf.write("\7\'\2\2\u018fP\3\2\2\2\u0190\u0191\7?\2\2\u0191R\3\2")
        buf.write("\2\2\u0192\u0193\7*\2\2\u0193T\3\2\2\2\u0194\u0195\7+")
        buf.write("\2\2\u0195\u0196\b+\r\2\u0196V\3\2\2\2\u0197\u0198\7}")
        buf.write("\2\2\u0198\u0199\b,\16\2\u0199X\3\2\2\2\u019a\u019b\7")
        buf.write("\177\2\2\u019bZ\3\2\2\2\u019c\u019d\7]\2\2\u019d\\\3\2")
        buf.write("\2\2\u019e\u019f\7_\2\2\u019f^\3\2\2\2\u01a0\u01a1\7.")
        buf.write("\2\2\u01a1`\3\2\2\2\u01a2\u01a3\7^\2\2\u01a3\u01ad\7p")
        buf.write("\2\2\u01a4\u01a5\7^\2\2\u01a5\u01ad\7v\2\2\u01a6\u01a7")
        buf.write("\7^\2\2\u01a7\u01ad\7t\2\2\u01a8\u01a9\7^\2\2\u01a9\u01ad")
        buf.write("\7$\2\2\u01aa\u01ab\7^\2\2\u01ab\u01ad\7^\2\2\u01ac\u01a2")
        buf.write("\3\2\2\2\u01ac\u01a4\3\2\2\2\u01ac\u01a6\3\2\2\2\u01ac")
        buf.write("\u01a8\3\2\2\2\u01ac\u01aa\3\2\2\2\u01adb\3\2\2\2\u01ae")
        buf.write("\u01b1\n\13\2\2\u01af\u01b1\5a\61\2\u01b0\u01ae\3\2\2")
        buf.write("\2\u01b0\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3d\3\2\2\2\u01b4\u01b2")
        buf.write("\3\2\2\2\u01b5\u01b6\7$\2\2\u01b6\u01b7\5c\62\2\u01b7")
        buf.write("\u01b8\7$\2\2\u01b8f\3\2\2\2\u01b9\u01ba\t\f\2\2\u01ba")
        buf.write("h\3\2\2\2\u01bb\u01bc\t\r\2\2\u01bcj\3\2\2\2\u01bd\u01be")
        buf.write("\t\16\2\2\u01bel\3\2\2\2\u01bf\u01c0\t\17\2\2\u01c0n\3")
        buf.write("\2\2\2\u01c1\u01c5\5g\64\2\u01c2\u01c5\5i\65\2\u01c3\u01c5")
        buf.write("\7a\2\2\u01c4\u01c1\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c3\3\2\2\2\u01c5p\3\2\2\2\u01c6\u01cb\5o8\2\u01c7")
        buf.write("\u01ca\5o8\2\u01c8\u01ca\5k\66\2\u01c9\u01c7\3\2\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01ca\u01cd\3\2\2\2\u01cb\u01c9\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01ccr\3\2\2\2\u01cd\u01cb\3\2\2")
        buf.write("\2\u01ce\u01d0\t\20\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d4\b:\2\2\u01d4t\3\2\2\2\u01d5")
        buf.write("\u01d6\7\f\2\2\u01d6\u01d7\b;\17\2\u01d7v\3\2\2\2\u01d8")
        buf.write("\u01d9\7$\2\2\u01d9\u01da\5c\62\2\u01da\u01db\7^\2\2\u01db")
        buf.write("\u01dc\b<\20\2\u01dcx\3\2\2\2\u01dd\u01de\7$\2\2\u01de")
        buf.write("\u01e2\5c\62\2\u01df\u01e0\7^\2\2\u01e0\u01e3\7p\2\2\u01e1")
        buf.write("\u01e3\7\2\2\3\u01e2\u01df\3\2\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01e5\b=\21\2\u01e5z\3\2\2")
        buf.write("\2\u01e6\u01e7\13\2\2\2\u01e7|\3\2\2\2\34\2\u0088\u008f")
        buf.write("\u0096\u009d\u00a0\u00a6\u00bd\u00c5\u00c9\u00d3\u0143")
        buf.write("\u014f\u015b\u0162\u016a\u016d\u017c\u01ac\u01b0\u01b2")
        buf.write("\u01c4\u01c9\u01cb\u01d1\u01e2\22\b\2\2\3\16\2\3\17\3")
        buf.write("\3\24\4\3\25\5\3\27\6\3\31\7\3\32\b\3\34\t\3\35\n\3\37")
        buf.write("\13\3+\f\3,\r\3;\16\3<\17\3=\20")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    INTEGER = 4
    ATOMIC_TYPE = 5
    COMMENT1 = 6
    COMMENT2 = 7
    KEYWORD = 8
    VAR = 9
    CONST = 10
    TYPE = 11
    STRUCT = 12
    INTERFACE = 13
    FUNC = 14
    RETURN = 15
    IF = 16
    ELSE = 17
    FOR = 18
    RANGE = 19
    BREAK = 20
    CONTINUE = 21
    BOOLEAN = 22
    ASSIGN_OP = 23
    ASSIGN_STMT_OP = 24
    FLOAT = 25
    SEMI = 26
    COMPARE_OP = 27
    AND_OP = 28
    OR_OP = 29
    NOT_OP = 30
    ADD_OP = 31
    MINUS_OP = 32
    MUL_OP = 33
    DIV_OP = 34
    MOD_OP = 35
    ASSIGN_INIT = 36
    LPARENTHESIS = 37
    RPARENTHESIS = 38
    LBRACE = 39
    RBRACE = 40
    LBRACKET = 41
    RBRACKET = 42
    SEPARATOR = 43
    ESCAPE = 44
    STRING = 45
    ID = 46
    WS = 47
    NL = 48
    ILLEGAL_ESCAPE = 49
    UNCLOSE_STRING = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'.'", "'_'", "'nil'", "'var'", "'const'", "'type'", 
            "'struct'", "'interface'", "'func'", "'return'", "'if'", "'else'", 
            "'for'", "'range'", "'break'", "'continue'", "':='", "';'", 
            "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", "KEYWORD", 
            "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", "FUNC", "RETURN", 
            "IF", "ELSE", "FOR", "RANGE", "BREAK", "CONTINUE", "BOOLEAN", 
            "ASSIGN_OP", "ASSIGN_STMT_OP", "FLOAT", "SEMI", "COMPARE_OP", 
            "AND_OP", "OR_OP", "NOT_OP", "ADD_OP", "MINUS_OP", "MUL_OP", 
            "DIV_OP", "MOD_OP", "ASSIGN_INIT", "LPARENTHESIS", "RPARENTHESIS", 
            "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEPARATOR", "ESCAPE", 
            "STRING", "ID", "WS", "NL", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "BINARY", "OCTAL", "HEXADEC", 
                  "DECIMAL", "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", 
                  "KEYWORD", "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", 
                  "FUNC", "RETURN", "IF", "ELSE", "FOR", "RANGE", "BREAK", 
                  "CONTINUE", "BOOLEAN", "ASSIGN_OP", "ASSIGN_STMT_OP", 
                  "FLOAT", "SEMI", "COMPARE_OP", "AND_OP", "OR_OP", "NOT_OP", 
                  "ADD_OP", "MINUS_OP", "MUL_OP", "DIV_OP", "MOD_OP", "ASSIGN_INIT", 
                  "LPARENTHESIS", "RPARENTHESIS", "LBRACE", "RBRACE", "LBRACKET", 
                  "RBRACKET", "SEPARATOR", "ESCAPE", "IN_STRING", "STRING", 
                  "UpperLetter", "LowerLetter", "Digit", "NonZeroDigit", 
                  "IdentifierStart", "ID", "WS", "NL", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

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

    afterStatement = False
    afterIf = False
    afterFor = False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.VAR_action 
            actions[13] = self.CONST_action 
            actions[18] = self.RETURN_action 
            actions[19] = self.IF_action 
            actions[21] = self.FOR_action 
            actions[23] = self.BREAK_action 
            actions[24] = self.CONTINUE_action 
            actions[26] = self.ASSIGN_OP_action 
            actions[27] = self.ASSIGN_STMT_OP_action 
            actions[29] = self.SEMI_action 
            actions[41] = self.RPARENTHESIS_action 
            actions[42] = self.LBRACE_action 
            actions[57] = self.NL_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def VAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.afterStatement = True

     

    def CONST_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.afterStatement = True

     

    def RETURN_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.afterStatement = True

     

    def IF_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                self.afterIf = True

     

    def FOR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                self.afterFor = True

     

    def BREAK_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                self.afterStatement = True

     

    def CONTINUE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

                self.afterStatement = True

     

    def ASSIGN_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

                self.afterStatement = True

     

    def ASSIGN_STMT_OP_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

                if not self.afterFor:
                    self.afterStatement = True
                else:
                    self.afterFor = False

     

    def SEMI_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

                self.afterStatement = False

     

    def RPARENTHESIS_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:

                if not self.afterIf:
                    self.afterStatement = True
                else:
                    self.afterIf = False

     

    def LBRACE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 11:

                self.afterStatement = False

     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 12:

                if self.afterStatement:
                    self.afterStatement = False
                    self.type = self.SEMI
                    self.text = ";"
                    return self.emit()
                self.skip()

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 13:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 14:

                raise UncloseString(self.text[1:])

     


