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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0196\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\3\2\6\2D\n\2\r\2\16\2E\3\2\3\2")
        buf.write("\3\3\3\3\5\3L\n\3\3\4\3\4\3\4\3\4\5\4R\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\5\5[\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\7\7g\n\7\f\7\16\7j\13\7\3\7\3\7\3\7\5\7o")
        buf.write("\n\7\3\7\3\7\3\7\3\7\5\7u\n\7\3\b\3\b\3\b\3\b\7\b{\n\b")
        buf.write("\f\b\16\b~\13\b\3\b\3\b\3\b\5\b\u0083\n\b\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\7\n\u008c\n\n\f\n\16\n\u008f\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\r\3\r\5\r\u0099\n\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\6\16\u00a0\n\16\r\16\16\16\u00a1\3\16")
        buf.write("\3\16\3\17\3\17\7\17\u00a8\n\17\f\17\16\17\u00ab\13\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\7\20\u00b6")
        buf.write("\n\20\f\20\16\20\u00b9\13\20\5\20\u00bb\n\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00c3\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\6\22\u00ca\n\22\r\22\16\22\u00cb\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\7\23\u00d5\n\23\f\23\16\23\u00d8")
        buf.write("\13\23\5\23\u00da\n\23\3\23\3\23\5\23\u00de\n\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\7\24\u00e5\n\24\f\24\16\24\u00e8")
        buf.write("\13\24\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u00f0\n\25\f")
        buf.write("\25\16\25\u00f3\13\25\3\26\3\26\3\26\3\26\3\26\5\26\u00fa")
        buf.write("\n\26\3\26\3\26\3\26\3\26\3\26\7\26\u0101\n\26\f\26\16")
        buf.write("\26\u0104\13\26\5\26\u0106\n\26\3\26\3\26\5\26\u010a\n")
        buf.write("\26\3\26\3\26\7\26\u010e\n\26\f\26\16\26\u0111\13\26\3")
        buf.write("\26\3\26\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\5\31\u011e\n\31\3\31\3\31\3\31\3\31\7\31\u0124\n\31\f")
        buf.write("\31\16\31\u0127\13\31\5\31\u0129\n\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u0134\n\32\f\32\16\32")
        buf.write("\u0137\13\32\5\32\u0139\n\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u014c\n\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u015d")
        buf.write("\n\34\f\34\16\34\u0160\13\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u0167\n\35\5\35\u0169\n\35\3\36\3\36\3\36\3\36\3")
        buf.write("\36\3\37\3\37\6\37\u0172\n\37\r\37\16\37\u0173\3\37\3")
        buf.write("\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \5 \u018c\n \3!\3!\3!\3!\3!\3!\5!\u0194\n!\3")
        buf.write("!\2\3\66\"\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\668:<>@\2\n\3\3\34\34\4\2\6\6\60\60\4\2")
        buf.write("\7\7\60\60\3\2\31\32\4\2  \"\"\3\2#%\3\2!\"\4\2\5\5\60")
        buf.write("\60\2\u01b1\2C\3\2\2\2\4K\3\2\2\2\6Q\3\2\2\2\bZ\3\2\2")
        buf.write("\2\n^\3\2\2\2\ft\3\2\2\2\16\u0082\3\2\2\2\20\u0084\3\2")
        buf.write("\2\2\22\u0088\3\2\2\2\24\u0090\3\2\2\2\26\u0094\3\2\2")
        buf.write("\2\30\u0098\3\2\2\2\32\u009a\3\2\2\2\34\u00a5\3\2\2\2")
        buf.write("\36\u00b0\3\2\2\2 \u00be\3\2\2\2\"\u00c4\3\2\2\2$\u00cf")
        buf.write("\3\2\2\2&\u00e1\3\2\2\2(\u00eb\3\2\2\2*\u00f4\3\2\2\2")
        buf.write(",\u0114\3\2\2\2.\u0117\3\2\2\2\60\u011a\3\2\2\2\62\u012c")
        buf.write("\3\2\2\2\64\u013c\3\2\2\2\66\u014b\3\2\2\28\u0161\3\2")
        buf.write("\2\2:\u016a\3\2\2\2<\u016f\3\2\2\2>\u018b\3\2\2\2@\u0193")
        buf.write("\3\2\2\2BD\5\4\3\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2")
        buf.write("\2\2FG\3\2\2\2GH\7\2\2\3H\3\3\2\2\2IL\5\6\4\2JL\5\b\5")
        buf.write("\2KI\3\2\2\2KJ\3\2\2\2L\5\3\2\2\2MR\5*\26\2NR\5\30\r\2")
        buf.write("OR\58\35\2PR\5> \2QM\3\2\2\2QN\3\2\2\2QO\3\2\2\2QP\3\2")
        buf.write("\2\2R\7\3\2\2\2S[\5\f\7\2T[\5\n\6\2U[\5\64\33\2V[\5.\30")
        buf.write("\2W[\5\60\31\2X[\7\26\2\2Y[\7\27\2\2ZS\3\2\2\2ZT\3\2\2")
        buf.write("\2ZU\3\2\2\2ZV\3\2\2\2ZW\3\2\2\2ZX\3\2\2\2ZY\3\2\2\2[")
        buf.write("\\\3\2\2\2\\]\t\2\2\2]\t\3\2\2\2^_\7\f\2\2_`\7\60\2\2")
        buf.write("`a\7&\2\2ab\5\66\34\2b\13\3\2\2\2cd\7\13\2\2dh\7\60\2")
        buf.write("\2eg\5\24\13\2fe\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2")
        buf.write("ik\3\2\2\2jh\3\2\2\2kn\5\26\f\2lm\7&\2\2mo\5\66\34\2n")
        buf.write("l\3\2\2\2no\3\2\2\2ou\3\2\2\2pq\7\13\2\2qr\7\60\2\2rs")
        buf.write("\7&\2\2su\5\66\34\2tc\3\2\2\2tp\3\2\2\2u\r\3\2\2\2vw\7")
        buf.write(")\2\2w|\5\20\t\2xy\7-\2\2y{\5\20\t\2zx\3\2\2\2{~\3\2\2")
        buf.write("\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u0080")
        buf.write("\7*\2\2\u0080\u0083\3\2\2\2\u0081\u0083\5\20\t\2\u0082")
        buf.write("v\3\2\2\2\u0082\u0081\3\2\2\2\u0083\17\3\2\2\2\u0084\u0085")
        buf.write("\7)\2\2\u0085\u0086\5\22\n\2\u0086\u0087\7*\2\2\u0087")
        buf.write("\21\3\2\2\2\u0088\u008d\5\66\34\2\u0089\u008a\7-\2\2\u008a")
        buf.write("\u008c\5\66\34\2\u008b\u0089\3\2\2\2\u008c\u008f\3\2\2")
        buf.write("\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2\u008e\23\3")
        buf.write("\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\7+\2\2\u0091\u0092")
        buf.write("\t\3\2\2\u0092\u0093\7,\2\2\u0093\25\3\2\2\2\u0094\u0095")
        buf.write("\t\4\2\2\u0095\27\3\2\2\2\u0096\u0099\5\32\16\2\u0097")
        buf.write("\u0099\5\"\22\2\u0098\u0096\3\2\2\2\u0098\u0097\3\2\2")
        buf.write("\2\u0099\31\3\2\2\2\u009a\u009b\7\r\2\2\u009b\u009c\7")
        buf.write("\60\2\2\u009c\u009d\7\16\2\2\u009d\u009f\7)\2\2\u009e")
        buf.write("\u00a0\5\34\17\2\u009f\u009e\3\2\2\2\u00a0\u00a1\3\2\2")
        buf.write("\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\3\2\2\2\u00a3\u00a4\7*\2\2\u00a4\33\3\2\2\2\u00a5\u00a9")
        buf.write("\7\60\2\2\u00a6\u00a8\5\24\13\2\u00a7\u00a6\3\2\2\2\u00a8")
        buf.write("\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ac\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ad\5")
        buf.write("\26\f\2\u00ad\u00ae\3\2\2\2\u00ae\u00af\7\34\2\2\u00af")
        buf.write("\35\3\2\2\2\u00b0\u00b1\7\60\2\2\u00b1\u00ba\7)\2\2\u00b2")
        buf.write("\u00b7\5 \21\2\u00b3\u00b4\7-\2\2\u00b4\u00b6\5 \21\2")
        buf.write("\u00b5\u00b3\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3")
        buf.write("\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00bb\3\2\2\2\u00b9\u00b7")
        buf.write("\3\2\2\2\u00ba\u00b2\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb")
        buf.write("\u00bc\3\2\2\2\u00bc\u00bd\7*\2\2\u00bd\37\3\2\2\2\u00be")
        buf.write("\u00bf\7\60\2\2\u00bf\u00c2\7\3\2\2\u00c0\u00c3\5@!\2")
        buf.write("\u00c1\u00c3\5 \21\2\u00c2\u00c0\3\2\2\2\u00c2\u00c1\3")
        buf.write("\2\2\2\u00c3!\3\2\2\2\u00c4\u00c5\7\r\2\2\u00c5\u00c6")
        buf.write("\7\60\2\2\u00c6\u00c7\7\17\2\2\u00c7\u00c9\7)\2\2\u00c8")
        buf.write("\u00ca\5$\23\2\u00c9\u00c8\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\u00ce\7*\2\2\u00ce#\3\2\2\2\u00cf\u00d0\7")
        buf.write("\60\2\2\u00d0\u00d9\7\'\2\2\u00d1\u00d6\5&\24\2\u00d2")
        buf.write("\u00d3\7-\2\2\u00d3\u00d5\5&\24\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00d1")
        buf.write("\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dd\7(\2\2\u00dc\u00de\5\26\f\2\u00dd\u00dc\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\7")
        buf.write("\34\2\2\u00e0%\3\2\2\2\u00e1\u00e6\7\60\2\2\u00e2\u00e3")
        buf.write("\7-\2\2\u00e3\u00e5\7\60\2\2\u00e4\u00e2\3\2\2\2\u00e5")
        buf.write("\u00e8\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e9\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e9\u00ea\5")
        buf.write("\26\f\2\u00ea\'\3\2\2\2\u00eb\u00f1\7\60\2\2\u00ec\u00f0")
        buf.write("\5\24\13\2\u00ed\u00ee\7\4\2\2\u00ee\u00f0\7\60\2\2\u00ef")
        buf.write("\u00ec\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f3\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2)\3\2\2")
        buf.write("\2\u00f3\u00f1\3\2\2\2\u00f4\u00f9\7\20\2\2\u00f5\u00f6")
        buf.write("\7\'\2\2\u00f6\u00f7\7\60\2\2\u00f7\u00f8\7\60\2\2\u00f8")
        buf.write("\u00fa\7(\2\2\u00f9\u00f5\3\2\2\2\u00f9\u00fa\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00fc\7\60\2\2\u00fc\u0105")
        buf.write("\7\'\2\2\u00fd\u0102\5,\27\2\u00fe\u00ff\7-\2\2\u00ff")
        buf.write("\u0101\5,\27\2\u0100\u00fe\3\2\2\2\u0101\u0104\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0106\3")
        buf.write("\2\2\2\u0104\u0102\3\2\2\2\u0105\u00fd\3\2\2\2\u0105\u0106")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\7(\2\2\u0108")
        buf.write("\u010a\5\26\f\2\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2")
        buf.write("\2\u010a\u010b\3\2\2\2\u010b\u010f\7)\2\2\u010c\u010e")
        buf.write("\5\4\3\2\u010d\u010c\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0112\3\2\2\2")
        buf.write("\u0111\u010f\3\2\2\2\u0112\u0113\7*\2\2\u0113+\3\2\2\2")
        buf.write("\u0114\u0115\7\60\2\2\u0115\u0116\5\26\f\2\u0116-\3\2")
        buf.write("\2\2\u0117\u0118\7\21\2\2\u0118\u0119\5\66\34\2\u0119")
        buf.write("/\3\2\2\2\u011a\u011d\7\60\2\2\u011b\u011c\7\4\2\2\u011c")
        buf.write("\u011e\7\60\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2")
        buf.write("\2\u011e\u011f\3\2\2\2\u011f\u0128\7\'\2\2\u0120\u0125")
        buf.write("\5\66\34\2\u0121\u0122\7-\2\2\u0122\u0124\5\66\34\2\u0123")
        buf.write("\u0121\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2")
        buf.write("\u0125\u0126\3\2\2\2\u0126\u0129\3\2\2\2\u0127\u0125\3")
        buf.write("\2\2\2\u0128\u0120\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a")
        buf.write("\3\2\2\2\u012a\u012b\7(\2\2\u012b\61\3\2\2\2\u012c\u012d")
        buf.write("\5(\25\2\u012d\u012e\7\4\2\2\u012e\u012f\7\60\2\2\u012f")
        buf.write("\u0138\7\'\2\2\u0130\u0135\5\66\34\2\u0131\u0132\7-\2")
        buf.write("\2\u0132\u0134\5\66\34\2\u0133\u0131\3\2\2\2\u0134\u0137")
        buf.write("\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0139\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0130\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\7")
        buf.write("(\2\2\u013b\63\3\2\2\2\u013c\u013d\5(\25\2\u013d\u013e")
        buf.write("\t\5\2\2\u013e\u013f\5\66\34\2\u013f\65\3\2\2\2\u0140")
        buf.write("\u0141\b\34\1\2\u0141\u0142\7\'\2\2\u0142\u0143\5\66\34")
        buf.write("\2\u0143\u0144\7(\2\2\u0144\u014c\3\2\2\2\u0145\u0146")
        buf.write("\t\6\2\2\u0146\u014c\5\66\34\f\u0147\u014c\5\60\31\2\u0148")
        buf.write("\u014c\5\62\32\2\u0149\u014c\5(\25\2\u014a\u014c\5@!\2")
        buf.write("\u014b\u0140\3\2\2\2\u014b\u0145\3\2\2\2\u014b\u0147\3")
        buf.write("\2\2\2\u014b\u0148\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014a")
        buf.write("\3\2\2\2\u014c\u015e\3\2\2\2\u014d\u014e\f\13\2\2\u014e")
        buf.write("\u014f\t\7\2\2\u014f\u015d\5\66\34\f\u0150\u0151\f\n\2")
        buf.write("\2\u0151\u0152\t\b\2\2\u0152\u015d\5\66\34\13\u0153\u0154")
        buf.write("\f\t\2\2\u0154\u0155\7\35\2\2\u0155\u015d\5\66\34\n\u0156")
        buf.write("\u0157\f\b\2\2\u0157\u0158\7\36\2\2\u0158\u015d\5\66\34")
        buf.write("\t\u0159\u015a\f\7\2\2\u015a\u015b\7\37\2\2\u015b\u015d")
        buf.write("\5\66\34\b\u015c\u014d\3\2\2\2\u015c\u0150\3\2\2\2\u015c")
        buf.write("\u0153\3\2\2\2\u015c\u0156\3\2\2\2\u015c\u0159\3\2\2\2")
        buf.write("\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3")
        buf.write("\2\2\2\u015f\67\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162")
        buf.write("\5:\36\2\u0162\u0168\5<\37\2\u0163\u0166\7\23\2\2\u0164")
        buf.write("\u0167\58\35\2\u0165\u0167\5<\37\2\u0166\u0164\3\2\2\2")
        buf.write("\u0166\u0165\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u0163\3")
        buf.write("\2\2\2\u0168\u0169\3\2\2\2\u01699\3\2\2\2\u016a\u016b")
        buf.write("\7\22\2\2\u016b\u016c\7\'\2\2\u016c\u016d\5\66\34\2\u016d")
        buf.write("\u016e\7(\2\2\u016e;\3\2\2\2\u016f\u0171\7)\2\2\u0170")
        buf.write("\u0172\5\4\3\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175\3")
        buf.write("\2\2\2\u0175\u0176\7*\2\2\u0176=\3\2\2\2\u0177\u0178\7")
        buf.write("\24\2\2\u0178\u0179\5\66\34\2\u0179\u017a\5<\37\2\u017a")
        buf.write("\u018c\3\2\2\2\u017b\u017c\7\24\2\2\u017c\u017d\5\64\33")
        buf.write("\2\u017d\u017e\7\34\2\2\u017e\u017f\5\66\34\2\u017f\u0180")
        buf.write("\7\34\2\2\u0180\u0181\5\64\33\2\u0181\u0182\5<\37\2\u0182")
        buf.write("\u018c\3\2\2\2\u0183\u0184\7\24\2\2\u0184\u0185\t\t\2")
        buf.write("\2\u0185\u0186\7-\2\2\u0186\u0187\7\60\2\2\u0187\u0188")
        buf.write("\7\32\2\2\u0188\u0189\7\25\2\2\u0189\u018a\7\60\2\2\u018a")
        buf.write("\u018c\5<\37\2\u018b\u0177\3\2\2\2\u018b\u017b\3\2\2\2")
        buf.write("\u018b\u0183\3\2\2\2\u018c?\3\2\2\2\u018d\u0194\7\6\2")
        buf.write("\2\u018e\u0194\7\33\2\2\u018f\u0194\7/\2\2\u0190\u0194")
        buf.write("\7\30\2\2\u0191\u0194\5\16\b\2\u0192\u0194\5\36\20\2\u0193")
        buf.write("\u018d\3\2\2\2\u0193\u018e\3\2\2\2\u0193\u018f\3\2\2\2")
        buf.write("\u0193\u0190\3\2\2\2\u0193\u0191\3\2\2\2\u0193\u0192\3")
        buf.write("\2\2\2\u0194A\3\2\2\2+EKQZhnt|\u0082\u008d\u0098\u00a1")
        buf.write("\u00a9\u00b7\u00ba\u00c2\u00cb\u00d6\u00d9\u00dd\u00e6")
        buf.write("\u00ef\u00f1\u00f9\u0102\u0105\u0109\u010f\u011d\u0125")
        buf.write("\u0128\u0135\u0138\u014b\u015c\u015e\u0166\u0168\u0173")
        buf.write("\u018b\u0193")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'.'", "'_'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'nil'", "'var'", "'const'", 
                     "'type'", "'struct'", "'interface'", "'func'", "'return'", 
                     "'if'", "'else'", "'for'", "'range'", "'break'", "'continue'", 
                     "<INVALID>", "<INVALID>", "':='", "<INVALID>", "';'", 
                     "<INVALID>", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'='", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INTEGER", "ATOMIC_TYPE", "COMMENT1", "COMMENT2", 
                      "KEYWORD", "VAR", "CONST", "TYPE", "STRUCT", "INTERFACE", 
                      "FUNC", "RETURN", "IF", "ELSE", "FOR", "RANGE", "BREAK", 
                      "CONTINUE", "BOOLEAN", "ASSIGN_OP", "ASSIGN_STMT_OP", 
                      "FLOAT", "SEMI", "COMPARE_OP", "AND_OP", "OR_OP", 
                      "NOT_OP", "ADD_OP", "MINUS_OP", "MUL_OP", "DIV_OP", 
                      "MOD_OP", "ASSIGN_INIT", "LPARENTHESIS", "RPARENTHESIS", 
                      "LBRACE", "RBRACE", "LBRACKET", "RBRACKET", "SEPARATOR", 
                      "ESCAPE", "STRING", "ID", "WS", "NL", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_block_statement = 2
    RULE_semi_statement = 3
    RULE_constdecl = 4
    RULE_vardecl = 5
    RULE_array = 6
    RULE_array_elements = 7
    RULE_array_members = 8
    RULE_array_index = 9
    RULE_typedef = 10
    RULE_typedecl = 11
    RULE_structdecl = 12
    RULE_structfielddecl = 13
    RULE_structliteral = 14
    RULE_structfieldliteral = 15
    RULE_interfacedecl = 16
    RULE_method_signature = 17
    RULE_argument = 18
    RULE_var_access = 19
    RULE_func_and_method_decl = 20
    RULE_argument_func = 21
    RULE_ret = 22
    RULE_funccall = 23
    RULE_methodcall = 24
    RULE_assignment = 25
    RULE_expression = 26
    RULE_if_stmt = 27
    RULE_if_condition = 28
    RULE_block = 29
    RULE_for_loop = 30
    RULE_literal = 31

    ruleNames =  [ "program", "statement", "block_statement", "semi_statement", 
                   "constdecl", "vardecl", "array", "array_elements", "array_members", 
                   "array_index", "typedef", "typedecl", "structdecl", "structfielddecl", 
                   "structliteral", "structfieldliteral", "interfacedecl", 
                   "method_signature", "argument", "var_access", "func_and_method_decl", 
                   "argument_func", "ret", "funccall", "methodcall", "assignment", 
                   "expression", "if_stmt", "if_condition", "block", "for_loop", 
                   "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    INTEGER=4
    ATOMIC_TYPE=5
    COMMENT1=6
    COMMENT2=7
    KEYWORD=8
    VAR=9
    CONST=10
    TYPE=11
    STRUCT=12
    INTERFACE=13
    FUNC=14
    RETURN=15
    IF=16
    ELSE=17
    FOR=18
    RANGE=19
    BREAK=20
    CONTINUE=21
    BOOLEAN=22
    ASSIGN_OP=23
    ASSIGN_STMT_OP=24
    FLOAT=25
    SEMI=26
    COMPARE_OP=27
    AND_OP=28
    OR_OP=29
    NOT_OP=30
    ADD_OP=31
    MINUS_OP=32
    MUL_OP=33
    DIV_OP=34
    MOD_OP=35
    ASSIGN_INIT=36
    LPARENTHESIS=37
    RPARENTHESIS=38
    LBRACE=39
    RBRACE=40
    LBRACKET=41
    RBRACKET=42
    SEPARATOR=43
    ESCAPE=44
    STRING=45
    ID=46
    WS=47
    NL=48
    ILLEGAL_ESCAPE=49
    UNCLOSE_STRING=50
    ERROR_CHAR=51

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
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.statement()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 69
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

        def block_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Block_statementContext,0)


        def semi_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Semi_statementContext,0)


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
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.TYPE, MiniGoParser.FUNC, MiniGoParser.IF, MiniGoParser.FOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.block_statement()
                pass
            elif token in [MiniGoParser.VAR, MiniGoParser.CONST, MiniGoParser.RETURN, MiniGoParser.BREAK, MiniGoParser.CONTINUE, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.semi_statement()
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


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_and_method_decl(self):
            return self.getTypedRuleContext(MiniGoParser.Func_and_method_declContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.For_loopContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = MiniGoParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block_statement)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.func_and_method_decl()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.typedecl()
                pass
            elif token in [MiniGoParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                self.if_stmt()
                pass
            elif token in [MiniGoParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.for_loop()
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


    class Semi_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ret(self):
            return self.getTypedRuleContext(MiniGoParser.RetContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_semi_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSemi_statement" ):
                return visitor.visitSemi_statement(self)
            else:
                return visitor.visitChildren(self)




    def semi_statement(self):

        localctx = MiniGoParser.Semi_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_semi_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 81
                self.vardecl()
                pass

            elif la_ == 2:
                self.state = 82
                self.constdecl()
                pass

            elif la_ == 3:
                self.state = 83
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 84
                self.ret()
                pass

            elif la_ == 5:
                self.state = 85
                self.funccall()
                pass

            elif la_ == 6:
                self.state = 86
                self.match(MiniGoParser.BREAK)
                pass

            elif la_ == 7:
                self.state = 87
                self.match(MiniGoParser.CONTINUE)
                pass


            self.state = 90
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.EOF or _la==MiniGoParser.SEMI):
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


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)

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
        self.enterRule(localctx, 8, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MiniGoParser.CONST)
            self.state = 93
            self.match(MiniGoParser.ID)
            self.state = 94
            self.match(MiniGoParser.ASSIGN_INIT)
            self.state = 95
            self.expression(0)
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

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def array_index(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_indexContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_indexContext,i)


        def ASSIGN_INIT(self):
            return self.getToken(MiniGoParser.ASSIGN_INIT, 0)

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
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(MiniGoParser.VAR)
                self.state = 98
                self.match(MiniGoParser.ID)
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.LBRACKET:
                    self.state = 99
                    self.array_index()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 105
                self.typedef()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==MiniGoParser.ASSIGN_INIT:
                    self.state = 106
                    self.match(MiniGoParser.ASSIGN_INIT)
                    self.state = 107
                    self.expression(0)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(MiniGoParser.VAR)
                self.state = 111
                self.match(MiniGoParser.ID)
                self.state = 112
                self.match(MiniGoParser.ASSIGN_INIT)
                self.state = 113
                self.expression(0)
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_elements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_elementsContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_elementsContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = MiniGoParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(MiniGoParser.LBRACE)
                self.state = 117
                self.array_elements()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 118
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 119
                    self.array_elements()
                    self.state = 124
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 125
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_members(self):
            return self.getTypedRuleContext(MiniGoParser.Array_membersContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_elements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_elements" ):
                return visitor.visitArray_elements(self)
            else:
                return visitor.visitChildren(self)




    def array_elements(self):

        localctx = MiniGoParser.Array_elementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_elements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(MiniGoParser.LBRACE)
            self.state = 131
            self.array_members()
            self.state = 132
            self.match(MiniGoParser.RBRACE)
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


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_members

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_members" ):
                return visitor.visitArray_members(self)
            else:
                return visitor.visitChildren(self)




    def array_members(self):

        localctx = MiniGoParser.Array_membersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_members)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.expression(0)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR:
                self.state = 135
                self.match(MiniGoParser.SEPARATOR)
                self.state = 136
                self.expression(0)
                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def LBRACKET(self):
            return self.getToken(MiniGoParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(MiniGoParser.RBRACKET, 0)

        def INTEGER(self):
            return self.getToken(MiniGoParser.INTEGER, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MiniGoParser.LBRACKET)
            self.state = 143
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.INTEGER or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 144
            self.match(MiniGoParser.RBRACKET)
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
            self.state = 146
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
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
                self.structdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
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

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
            self.state = 152
            self.match(MiniGoParser.TYPE)
            self.state = 153
            self.match(MiniGoParser.ID)
            self.state = 154
            self.match(MiniGoParser.STRUCT)
            self.state = 155
            self.match(MiniGoParser.LBRACE)
            self.state = 157 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self.structfielddecl()
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 161
            self.match(MiniGoParser.RBRACE)
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

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

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
            self.state = 163
            self.match(MiniGoParser.ID)

            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.LBRACKET:
                self.state = 164
                self.array_index()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
            self.typedef()
            self.state = 172
            self.match(MiniGoParser.SEMI)
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

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def structfieldliteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StructfieldliteralContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StructfieldliteralContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structliteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructliteral" ):
                return visitor.visitStructliteral(self)
            else:
                return visitor.visitChildren(self)




    def structliteral(self):

        localctx = MiniGoParser.StructliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_structliteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.LBRACE)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 176
                self.structfieldliteral()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 177
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 178
                    self.structfieldliteral()
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 186
            self.match(MiniGoParser.RBRACE)
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
        self.enterRule(localctx, 30, self.RULE_structfieldliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.match(MiniGoParser.ID)
            self.state = 189
            self.match(MiniGoParser.T__0)
            self.state = 192
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 190
                self.literal()
                pass

            elif la_ == 2:
                self.state = 191
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

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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
        self.enterRule(localctx, 32, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(MiniGoParser.TYPE)
            self.state = 195
            self.match(MiniGoParser.ID)
            self.state = 196
            self.match(MiniGoParser.INTERFACE)
            self.state = 197
            self.match(MiniGoParser.LBRACE)
            self.state = 199 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 198
                self.method_signature()
                self.state = 201 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.ID):
                    break

            self.state = 203
            self.match(MiniGoParser.RBRACE)
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

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ArgumentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ArgumentContext,i)


        def typedef(self):
            return self.getTypedRuleContext(MiniGoParser.TypedefContext,0)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_method_signature

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_signature" ):
                return visitor.visitMethod_signature(self)
            else:
                return visitor.visitChildren(self)




    def method_signature(self):

        localctx = MiniGoParser.Method_signatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_method_signature)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.ID)
            self.state = 206
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 207
                self.argument()
                self.state = 212
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 208
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 209
                    self.argument()
                    self.state = 214
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 217
            self.match(MiniGoParser.RPARENTHESIS)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID:
                self.state = 218
                self.typedef()


            self.state = 221
            self.match(MiniGoParser.SEMI)
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


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_argument)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(MiniGoParser.ID)
            self.state = 228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR:
                self.state = 224
                self.match(MiniGoParser.SEPARATOR)
                self.state = 225
                self.match(MiniGoParser.ID)
                self.state = 230
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 231
            self.typedef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_accessContext(ParserRuleContext):
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
            return MiniGoParser.RULE_var_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_access" ):
                return visitor.visitVar_access(self)
            else:
                return visitor.visitChildren(self)




    def var_access(self):

        localctx = MiniGoParser.Var_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(MiniGoParser.ID)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [MiniGoParser.LBRACKET]:
                        self.state = 234
                        self.array_index()
                        pass
                    elif token in [MiniGoParser.T__1]:
                        self.state = 235
                        self.match(MiniGoParser.T__1)
                        self.state = 236
                        self.match(MiniGoParser.ID)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_and_method_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LPARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPARENTHESIS)
            else:
                return self.getToken(MiniGoParser.LPARENTHESIS, i)

        def RPARENTHESIS(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPARENTHESIS)
            else:
                return self.getToken(MiniGoParser.RPARENTHESIS, i)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

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


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_and_method_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_and_method_decl" ):
                return visitor.visitFunc_and_method_decl(self)
            else:
                return visitor.visitChildren(self)




    def func_and_method_decl(self):

        localctx = MiniGoParser.Func_and_method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_func_and_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(MiniGoParser.FUNC)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPARENTHESIS:
                self.state = 243
                self.match(MiniGoParser.LPARENTHESIS)
                self.state = 244
                self.match(MiniGoParser.ID)
                self.state = 245
                self.match(MiniGoParser.ID)
                self.state = 246
                self.match(MiniGoParser.RPARENTHESIS)


            self.state = 249
            self.match(MiniGoParser.ID)
            self.state = 250
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 251
                self.argument_func()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 252
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 253
                    self.argument_func()
                    self.state = 258
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 261
            self.match(MiniGoParser.RPARENTHESIS)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ATOMIC_TYPE or _la==MiniGoParser.ID:
                self.state = 262
                self.typedef()


            self.state = 265
            self.match(MiniGoParser.LBRACE)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 266
                self.statement()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            self.match(MiniGoParser.RBRACE)
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
            self.state = 274
            self.match(MiniGoParser.ID)
            self.state = 275
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

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

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
            self.state = 277
            self.match(MiniGoParser.RETURN)
            self.state = 278
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniGoParser.ID)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 281
                self.match(MiniGoParser.T__1)
                self.state = 282
                self.match(MiniGoParser.ID)


            self.state = 285
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.MINUS_OP) | (1 << MiniGoParser.LPARENTHESIS) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 286
                self.expression(0)
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 287
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 288
                    self.expression(0)
                    self.state = 293
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 296
            self.match(MiniGoParser.RPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def SEPARATOR(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR)
            else:
                return self.getToken(MiniGoParser.SEPARATOR, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.var_access()
            self.state = 299
            self.match(MiniGoParser.T__1)
            self.state = 300
            self.match(MiniGoParser.ID)
            self.state = 301
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.INTEGER) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.NOT_OP) | (1 << MiniGoParser.MINUS_OP) | (1 << MiniGoParser.LPARENTHESIS) | (1 << MiniGoParser.LBRACE) | (1 << MiniGoParser.STRING) | (1 << MiniGoParser.ID))) != 0):
                self.state = 302
                self.expression(0)
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR:
                    self.state = 303
                    self.match(MiniGoParser.SEPARATOR)
                    self.state = 304
                    self.expression(0)
                    self.state = 309
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 312
            self.match(MiniGoParser.RPARENTHESIS)
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

        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def ASSIGN_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_OP, 0)

        def ASSIGN_STMT_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_STMT_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.var_access()
            self.state = 315
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ASSIGN_OP or _la==MiniGoParser.ASSIGN_STMT_OP):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 316
            self.expression(0)
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

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExpressionContext,i)


        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def MINUS_OP(self):
            return self.getToken(MiniGoParser.MINUS_OP, 0)

        def NOT_OP(self):
            return self.getToken(MiniGoParser.NOT_OP, 0)

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def var_access(self):
            return self.getTypedRuleContext(MiniGoParser.Var_accessContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def MUL_OP(self):
            return self.getToken(MiniGoParser.MUL_OP, 0)

        def DIV_OP(self):
            return self.getToken(MiniGoParser.DIV_OP, 0)

        def MOD_OP(self):
            return self.getToken(MiniGoParser.MOD_OP, 0)

        def ADD_OP(self):
            return self.getToken(MiniGoParser.ADD_OP, 0)

        def COMPARE_OP(self):
            return self.getToken(MiniGoParser.COMPARE_OP, 0)

        def AND_OP(self):
            return self.getToken(MiniGoParser.AND_OP, 0)

        def OR_OP(self):
            return self.getToken(MiniGoParser.OR_OP, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 319
                self.match(MiniGoParser.LPARENTHESIS)
                self.state = 320
                self.expression(0)
                self.state = 321
                self.match(MiniGoParser.RPARENTHESIS)
                pass

            elif la_ == 2:
                self.state = 323
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.NOT_OP or _la==MiniGoParser.MINUS_OP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 324
                self.expression(10)
                pass

            elif la_ == 3:
                self.state = 325
                self.funccall()
                pass

            elif la_ == 4:
                self.state = 326
                self.methodcall()
                pass

            elif la_ == 5:
                self.state = 327
                self.var_access()
                pass

            elif la_ == 6:
                self.state = 328
                self.literal()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 348
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 331
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 332
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL_OP) | (1 << MiniGoParser.DIV_OP) | (1 << MiniGoParser.MOD_OP))) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 333
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 334
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 335
                        _la = self._input.LA(1)
                        if not(_la==MiniGoParser.ADD_OP or _la==MiniGoParser.MINUS_OP):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 336
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 337
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 338
                        self.match(MiniGoParser.COMPARE_OP)
                        self.state = 339
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 340
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 341
                        self.match(MiniGoParser.AND_OP)
                        self.state = 342
                        self.expression(7)
                        pass

                    elif la_ == 5:
                        localctx = MiniGoParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 343
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 344
                        self.match(MiniGoParser.OR_OP)
                        self.state = 345
                        self.expression(6)
                        pass

             
                self.state = 350
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_condition(self):
            return self.getTypedRuleContext(MiniGoParser.If_conditionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.if_condition()
            self.state = 352
            self.block()
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 353
                self.match(MiniGoParser.ELSE)
                self.state = 356
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IF]:
                    self.state = 354
                    self.if_stmt()
                    pass
                elif token in [MiniGoParser.LBRACE]:
                    self.state = 355
                    self.block()
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


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPARENTHESIS(self):
            return self.getToken(MiniGoParser.LPARENTHESIS, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPARENTHESIS(self):
            return self.getToken(MiniGoParser.RPARENTHESIS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_if_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = MiniGoParser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MiniGoParser.IF)
            self.state = 361
            self.match(MiniGoParser.LPARENTHESIS)
            self.state = 362
            self.expression(0)
            self.state = 363
            self.match(MiniGoParser.RPARENTHESIS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(MiniGoParser.LBRACE)
            self.state = 367 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 366
                self.statement()
                self.state = 369 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.VAR) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.FUNC) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.IF) | (1 << MiniGoParser.FOR) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.ID))) != 0)):
                    break

            self.state = 371
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignmentContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def SEPARATOR(self):
            return self.getToken(MiniGoParser.SEPARATOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN_STMT_OP(self):
            return self.getToken(MiniGoParser.ASSIGN_STMT_OP, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop" ):
                return visitor.visitFor_loop(self)
            else:
                return visitor.visitChildren(self)




    def for_loop(self):

        localctx = MiniGoParser.For_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_for_loop)
        self._la = 0 # Token type
        try:
            self.state = 393
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(MiniGoParser.FOR)
                self.state = 374
                self.expression(0)
                self.state = 375
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(MiniGoParser.FOR)
                self.state = 378
                self.assignment()
                self.state = 379
                self.match(MiniGoParser.SEMI)
                self.state = 380
                self.expression(0)
                self.state = 381
                self.match(MiniGoParser.SEMI)
                self.state = 382
                self.assignment()
                self.state = 383
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.match(MiniGoParser.FOR)
                self.state = 386
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.T__2 or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 387
                self.match(MiniGoParser.SEPARATOR)
                self.state = 388
                self.match(MiniGoParser.ID)
                self.state = 389
                self.match(MiniGoParser.ASSIGN_STMT_OP)
                self.state = 390
                self.match(MiniGoParser.RANGE)
                self.state = 391
                self.match(MiniGoParser.ID)
                self.state = 392
                self.block()
                pass


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
        self.enterRule(localctx, 62, self.RULE_literal)
        try:
            self.state = 401
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 395
                self.match(MiniGoParser.INTEGER)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 397
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 398
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 399
                self.array()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 6)
                self.state = 400
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




