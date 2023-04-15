# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\3\2\3\2\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\5\61\u0138\n\61\3\62\3\62\7\62\u013c\n\62\f\62\16")
        buf.write("\62\u013f\13\62\3\63\3\63\3\63\7\63\u0144\n\63\f\63\16")
        buf.write("\63\u0147\13\63\3\63\3\63\6\63\u014b\n\63\r\63\16\63\u014c")
        buf.write("\7\63\u014f\n\63\f\63\16\63\u0152\13\63\3\63\5\63\u0155")
        buf.write("\n\63\3\64\3\64\5\64\u0159\n\64\3\64\6\64\u015c\n\64\r")
        buf.write("\64\16\64\u015d\3\65\3\65\3\65\7\65\u0163\n\65\f\65\16")
        buf.write("\65\u0166\13\65\3\65\5\65\u0169\n\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\7\65\u0173\n\65\f\65\16\65\u0176")
        buf.write("\13\65\3\65\3\65\3\65\5\65\u017b\n\65\3\66\3\66\3\66\3")
        buf.write("\67\3\67\3\67\3\67\5\67\u0184\n\67\38\38\38\58\u0189\n")
        buf.write("8\39\39\79\u018d\n9\f9\169\u0190\139\39\39\39\3:\6:\u0196")
        buf.write("\n:\r:\16:\u0197\3:\3:\3;\3;\3;\3;\7;\u01a0\n;\f;\16;")
        buf.write("\u01a3\13;\3;\3;\3<\3<\3<\3<\7<\u01ab\n<\f<\16<\u01ae")
        buf.write("\13<\3<\3<\3<\3<\3<\3=\3=\3>\3>\7>\u01b9\n>\f>\16>\u01bc")
        buf.write("\13>\3>\5>\u01bf\n>\3?\3?\7?\u01c3\n?\f?\16?\u01c6\13")
        buf.write("?\3?\3?\3\u01ac\2@\3\3\5\4\7\5\t\6\13\7\r\2\17\b\21\t")
        buf.write("\23\n\25\13\27\f\31\r\33\16\35\2\37\17!\20#\21%\22\'\23")
        buf.write(")\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?")
        buf.write("\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\2i")
        buf.write("\63k\2m\2o\2q\64s\65u\66w\67y8{9}:\3\2\20\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\63;\3\2\62;\3\2aa\4\2GGgg\4\2--//\t")
        buf.write("\2))^^ddhhppttvv\6\2\f\f$$))^^\3\2^^\3\2$$\5\2\n\f\16")
        buf.write("\17\"\"\4\2\f\f\17\17\4\3\f\f\17\17\2\u01d8\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2i\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2")
        buf.write("\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\3\177")
        buf.write("\3\2\2\2\5\u0084\3\2\2\2\7\u008a\3\2\2\2\t\u0092\3\2\2")
        buf.write("\2\13\u0095\3\2\2\2\r\u009a\3\2\2\2\17\u00a0\3\2\2\2\21")
        buf.write("\u00a6\3\2\2\2\23\u00aa\3\2\2\2\25\u00b3\3\2\2\2\27\u00b6")
        buf.write("\3\2\2\2\31\u00be\3\2\2\2\33\u00c5\3\2\2\2\35\u00cc\3")
        buf.write("\2\2\2\37\u00d1\3\2\2\2!\u00d7\3\2\2\2#\u00dc\3\2\2\2")
        buf.write("%\u00e0\3\2\2\2\'\u00e9\3\2\2\2)\u00ec\3\2\2\2+\u00f4")
        buf.write("\3\2\2\2-\u00fa\3\2\2\2/\u00fc\3\2\2\2\61\u00fe\3\2\2")
        buf.write("\2\63\u0100\3\2\2\2\65\u0102\3\2\2\2\67\u0104\3\2\2\2")
        buf.write("9\u0106\3\2\2\2;\u0109\3\2\2\2=\u010c\3\2\2\2?\u010f\3")
        buf.write("\2\2\2A\u0112\3\2\2\2C\u0114\3\2\2\2E\u0116\3\2\2\2G\u0119")
        buf.write("\3\2\2\2I\u011c\3\2\2\2K\u011f\3\2\2\2M\u0121\3\2\2\2")
        buf.write("O\u0123\3\2\2\2Q\u0125\3\2\2\2S\u0127\3\2\2\2U\u0129\3")
        buf.write("\2\2\2W\u012b\3\2\2\2Y\u012d\3\2\2\2[\u012f\3\2\2\2]\u0131")
        buf.write("\3\2\2\2_\u0133\3\2\2\2a\u0137\3\2\2\2c\u0139\3\2\2\2")
        buf.write("e\u0154\3\2\2\2g\u0156\3\2\2\2i\u017a\3\2\2\2k\u017c\3")
        buf.write("\2\2\2m\u0183\3\2\2\2o\u0188\3\2\2\2q\u018a\3\2\2\2s\u0195")
        buf.write("\3\2\2\2u\u019b\3\2\2\2w\u01a6\3\2\2\2y\u01b4\3\2\2\2")
        buf.write("{\u01b6\3\2\2\2}\u01c0\3\2\2\2\177\u0080\7c\2\2\u0080")
        buf.write("\u0081\7w\2\2\u0081\u0082\7v\2\2\u0082\u0083\7q\2\2\u0083")
        buf.write("\4\3\2\2\2\u0084\u0085\7d\2\2\u0085\u0086\7t\2\2\u0086")
        buf.write("\u0087\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089\7m\2\2\u0089")
        buf.write("\6\3\2\2\2\u008a\u008b\7d\2\2\u008b\u008c\7q\2\2\u008c")
        buf.write("\u008d\7q\2\2\u008d\u008e\7n\2\2\u008e\u008f\7g\2\2\u008f")
        buf.write("\u0090\7c\2\2\u0090\u0091\7p\2\2\u0091\b\3\2\2\2\u0092")
        buf.write("\u0093\7f\2\2\u0093\u0094\7q\2\2\u0094\n\3\2\2\2\u0095")
        buf.write("\u0096\7g\2\2\u0096\u0097\7n\2\2\u0097\u0098\7u\2\2\u0098")
        buf.write("\u0099\7g\2\2\u0099\f\3\2\2\2\u009a\u009b\7h\2\2\u009b")
        buf.write("\u009c\7c\2\2\u009c\u009d\7n\2\2\u009d\u009e\7u\2\2\u009e")
        buf.write("\u009f\7g\2\2\u009f\16\3\2\2\2\u00a0\u00a1\7h\2\2\u00a1")
        buf.write("\u00a2\7n\2\2\u00a2\u00a3\7q\2\2\u00a3\u00a4\7c\2\2\u00a4")
        buf.write("\u00a5\7v\2\2\u00a5\20\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7")
        buf.write("\u00a8\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\22\3\2\2\2\u00aa")
        buf.write("\u00ab\7h\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7p\2\2\u00ad")
        buf.write("\u00ae\7e\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0")
        buf.write("\u00b1\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\24\3\2\2\2\u00b3")
        buf.write("\u00b4\7k\2\2\u00b4\u00b5\7h\2\2\u00b5\26\3\2\2\2\u00b6")
        buf.write("\u00b7\7k\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9")
        buf.write("\u00ba\7g\2\2\u00ba\u00bb\7i\2\2\u00bb\u00bc\7g\2\2\u00bc")
        buf.write("\u00bd\7t\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7t\2\2\u00bf")
        buf.write("\u00c0\7g\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2\7w\2\2\u00c2")
        buf.write("\u00c3\7t\2\2\u00c3\u00c4\7p\2\2\u00c4\32\3\2\2\2\u00c5")
        buf.write("\u00c6\7u\2\2\u00c6\u00c7\7v\2\2\u00c7\u00c8\7t\2\2\u00c8")
        buf.write("\u00c9\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\u00cb\7i\2\2\u00cb")
        buf.write("\34\3\2\2\2\u00cc\u00cd\7v\2\2\u00cd\u00ce\7t\2\2\u00ce")
        buf.write("\u00cf\7w\2\2\u00cf\u00d0\7g\2\2\u00d0\36\3\2\2\2\u00d1")
        buf.write("\u00d2\7y\2\2\u00d2\u00d3\7j\2\2\u00d3\u00d4\7k\2\2\u00d4")
        buf.write("\u00d5\7n\2\2\u00d5\u00d6\7g\2\2\u00d6 \3\2\2\2\u00d7")
        buf.write("\u00d8\7x\2\2\u00d8\u00d9\7q\2\2\u00d9\u00da\7k\2\2\u00da")
        buf.write("\u00db\7f\2\2\u00db\"\3\2\2\2\u00dc\u00dd\7q\2\2\u00dd")
        buf.write("\u00de\7w\2\2\u00de\u00df\7v\2\2\u00df$\3\2\2\2\u00e0")
        buf.write("\u00e1\7e\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7p\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6\7p\2\2\u00e6")
        buf.write("\u00e7\7w\2\2\u00e7\u00e8\7g\2\2\u00e8&\3\2\2\2\u00e9")
        buf.write("\u00ea\7q\2\2\u00ea\u00eb\7h\2\2\u00eb(\3\2\2\2\u00ec")
        buf.write("\u00ed\7k\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7j\2\2\u00ef")
        buf.write("\u00f0\7g\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2")
        buf.write("\u00f3\7v\2\2\u00f3*\3\2\2\2\u00f4\u00f5\7c\2\2\u00f5")
        buf.write("\u00f6\7t\2\2\u00f6\u00f7\7t\2\2\u00f7\u00f8\7c\2\2\u00f8")
        buf.write("\u00f9\7{\2\2\u00f9,\3\2\2\2\u00fa\u00fb\7-\2\2\u00fb")
        buf.write(".\3\2\2\2\u00fc\u00fd\7/\2\2\u00fd\60\3\2\2\2\u00fe\u00ff")
        buf.write("\7,\2\2\u00ff\62\3\2\2\2\u0100\u0101\7\61\2\2\u0101\64")
        buf.write("\3\2\2\2\u0102\u0103\7\'\2\2\u0103\66\3\2\2\2\u0104\u0105")
        buf.write("\7#\2\2\u01058\3\2\2\2\u0106\u0107\7(\2\2\u0107\u0108")
        buf.write("\7(\2\2\u0108:\3\2\2\2\u0109\u010a\7~\2\2\u010a\u010b")
        buf.write("\7~\2\2\u010b<\3\2\2\2\u010c\u010d\7?\2\2\u010d\u010e")
        buf.write("\7?\2\2\u010e>\3\2\2\2\u010f\u0110\7#\2\2\u0110\u0111")
        buf.write("\7?\2\2\u0111@\3\2\2\2\u0112\u0113\7>\2\2\u0113B\3\2\2")
        buf.write("\2\u0114\u0115\7@\2\2\u0115D\3\2\2\2\u0116\u0117\7>\2")
        buf.write("\2\u0117\u0118\7?\2\2\u0118F\3\2\2\2\u0119\u011a\7@\2")
        buf.write("\2\u011a\u011b\7?\2\2\u011bH\3\2\2\2\u011c\u011d\7<\2")
        buf.write("\2\u011d\u011e\7<\2\2\u011eJ\3\2\2\2\u011f\u0120\7.\2")
        buf.write("\2\u0120L\3\2\2\2\u0121\u0122\7=\2\2\u0122N\3\2\2\2\u0123")
        buf.write("\u0124\7<\2\2\u0124P\3\2\2\2\u0125\u0126\7}\2\2\u0126")
        buf.write("R\3\2\2\2\u0127\u0128\7\177\2\2\u0128T\3\2\2\2\u0129\u012a")
        buf.write("\7*\2\2\u012aV\3\2\2\2\u012b\u012c\7+\2\2\u012cX\3\2\2")
        buf.write("\2\u012d\u012e\7]\2\2\u012eZ\3\2\2\2\u012f\u0130\7_\2")
        buf.write("\2\u0130\\\3\2\2\2\u0131\u0132\7?\2\2\u0132^\3\2\2\2\u0133")
        buf.write("\u0134\7\60\2\2\u0134`\3\2\2\2\u0135\u0138\5\35\17\2\u0136")
        buf.write("\u0138\5\r\7\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0138b\3\2\2\2\u0139\u013d\t\2\2\2\u013a\u013c\t\3\2")
        buf.write("\2\u013b\u013a\3\2\2\2\u013c\u013f\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013ed\3\2\2\2\u013f\u013d")
        buf.write("\3\2\2\2\u0140\u0155\4\62;\2\u0141\u0145\t\4\2\2\u0142")
        buf.write("\u0144\t\5\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2\2")
        buf.write("\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0150\3")
        buf.write("\2\2\2\u0147\u0145\3\2\2\2\u0148\u014a\t\6\2\2\u0149\u014b")
        buf.write("\t\5\2\2\u014a\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("\u014a\3\2\2\2\u014c\u014d\3\2\2\2\u014d\u014f\3\2\2\2")
        buf.write("\u014e\u0148\3\2\2\2\u014f\u0152\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153\3\2\2\2\u0152\u0150")
        buf.write("\3\2\2\2\u0153\u0155\b\63\2\2\u0154\u0140\3\2\2\2\u0154")
        buf.write("\u0141\3\2\2\2\u0155f\3\2\2\2\u0156\u0158\t\7\2\2\u0157")
        buf.write("\u0159\t\b\2\2\u0158\u0157\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159\u015b\3\2\2\2\u015a\u015c\t\5\2\2\u015b\u015a\3")
        buf.write("\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b\3\2\2\2\u015d\u015e")
        buf.write("\3\2\2\2\u015eh\3\2\2\2\u015f\u0160\5e\63\2\u0160\u0164")
        buf.write("\7\60\2\2\u0161\u0163\t\5\2\2\u0162\u0161\3\2\2\2\u0163")
        buf.write("\u0166\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0168\3\2\2\2\u0166\u0164\3\2\2\2\u0167\u0169\5")
        buf.write("g\64\2\u0168\u0167\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\3\2\2\2\u016a\u016b\b\65\3\2\u016b\u017b\3\2\2\2\u016c")
        buf.write("\u016d\5e\63\2\u016d\u016e\5g\64\2\u016e\u016f\b\65\4")
        buf.write("\2\u016f\u017b\3\2\2\2\u0170\u0174\7\60\2\2\u0171\u0173")
        buf.write("\t\5\2\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174")
        buf.write("\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0177\u0178\5g\64\2\u0178\u0179\b")
        buf.write("\65\5\2\u0179\u017b\3\2\2\2\u017a\u015f\3\2\2\2\u017a")
        buf.write("\u016c\3\2\2\2\u017a\u0170\3\2\2\2\u017bj\3\2\2\2\u017c")
        buf.write("\u017d\7^\2\2\u017d\u017e\t\t\2\2\u017el\3\2\2\2\u017f")
        buf.write("\u0184\n\n\2\2\u0180\u0181\t\13\2\2\u0181\u0184\t\f\2")
        buf.write("\2\u0182\u0184\5k\66\2\u0183\u017f\3\2\2\2\u0183\u0180")
        buf.write("\3\2\2\2\u0183\u0182\3\2\2\2\u0184n\3\2\2\2\u0185\u0186")
        buf.write("\7^\2\2\u0186\u0189\n\t\2\2\u0187\u0189\7^\2\2\u0188\u0185")
        buf.write("\3\2\2\2\u0188\u0187\3\2\2\2\u0189p\3\2\2\2\u018a\u018e")
        buf.write("\7$\2\2\u018b\u018d\5m\67\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018f\u0191\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0192\7")
        buf.write("$\2\2\u0192\u0193\b9\6\2\u0193r\3\2\2\2\u0194\u0196\t")
        buf.write("\r\2\2\u0195\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0195")
        buf.write("\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("\u019a\b:\7\2\u019at\3\2\2\2\u019b\u019c\7\61\2\2\u019c")
        buf.write("\u019d\7\61\2\2\u019d\u01a1\3\2\2\2\u019e\u01a0\n\16\2")
        buf.write("\2\u019f\u019e\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4\3\2\2\2\u01a3")
        buf.write("\u01a1\3\2\2\2\u01a4\u01a5\b;\7\2\u01a5v\3\2\2\2\u01a6")
        buf.write("\u01a7\7\61\2\2\u01a7\u01a8\7,\2\2\u01a8\u01ac\3\2\2\2")
        buf.write("\u01a9\u01ab\13\2\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ae")
        buf.write("\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad")
        buf.write("\u01af\3\2\2\2\u01ae\u01ac\3\2\2\2\u01af\u01b0\7,\2\2")
        buf.write("\u01b0\u01b1\7\61\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3")
        buf.write("\b<\7\2\u01b3x\3\2\2\2\u01b4\u01b5\13\2\2\2\u01b5z\3\2")
        buf.write("\2\2\u01b6\u01ba\7$\2\2\u01b7\u01b9\5m\67\2\u01b8\u01b7")
        buf.write("\3\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bb\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3\2\2\2")
        buf.write("\u01bd\u01bf\t\17\2\2\u01be\u01bd\3\2\2\2\u01bf|\3\2\2")
        buf.write("\2\u01c0\u01c4\7$\2\2\u01c1\u01c3\5m\67\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c7\3\2\2\2\u01c6\u01c4\3\2\2\2")
        buf.write("\u01c7\u01c8\5o8\2\u01c8~\3\2\2\2\30\2\u0137\u013d\u0145")
        buf.write("\u014c\u0150\u0154\u0158\u015d\u0164\u0168\u0174\u017a")
        buf.write("\u0183\u0188\u018e\u0197\u01a1\u01ac\u01ba\u01be\u01c4")
        buf.write("\b\3\63\2\3\65\3\3\65\4\3\65\5\39\6\b\2\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    ELSE = 5
    FLOAT = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INTEGER = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    ADD = 20
    SUB = 21
    MUL = 22
    DIV = 23
    REMAINDER = 24
    BOOL_NEGA = 25
    BOOL_CONJ = 26
    BOOL_DISJ = 27
    EQUAL = 28
    NOT_EQUAL = 29
    LESS_THAN = 30
    GREATER_THAN = 31
    LESS_THAN_EQ = 32
    GREATER_THAN_EQ = 33
    DOUBLE_COLON = 34
    COMMA = 35
    SEMI = 36
    COLON = 37
    LB = 38
    RB = 39
    LP = 40
    RP = 41
    LSB = 42
    RSB = 43
    ASSIGN = 44
    DOT = 45
    BOOLEANLIT = 46
    ID = 47
    INTLIT = 48
    FLOATLIT = 49
    STRINGLIT = 50
    WS = 51
    SINGLE_LINE_COMMENT = 52
    MULTI_LINE_COMMENT = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'float'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'::'", 
            "','", "';'", "':'", "'{'", "'}'", "'('", "')'", "'['", "']'", 
            "'='", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FLOAT", "FOR", "FUNCTION", 
            "IF", "INTEGER", "RETURN", "STRING", "WHILE", "VOID", "OUT", 
            "CONTINUE", "OF", "INHERIT", "ARRAY", "ADD", "SUB", "MUL", "DIV", 
            "REMAINDER", "BOOL_NEGA", "BOOL_CONJ", "BOOL_DISJ", "EQUAL", 
            "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "LESS_THAN_EQ", "GREATER_THAN_EQ", 
            "DOUBLE_COLON", "COMMA", "SEMI", "COLON", "LB", "RB", "LP", 
            "RP", "LSB", "RSB", "ASSIGN", "DOT", "BOOLEANLIT", "ID", "INTLIT", 
            "FLOATLIT", "STRINGLIT", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
                  "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
                  "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "ADD", "SUB", "MUL", "DIV", "REMAINDER", "BOOL_NEGA", 
                  "BOOL_CONJ", "BOOL_DISJ", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                  "GREATER_THAN", "LESS_THAN_EQ", "GREATER_THAN_EQ", "DOUBLE_COLON", 
                  "COMMA", "SEMI", "COLON", "LB", "RB", "LP", "RP", "LSB", 
                  "RSB", "ASSIGN", "DOT", "BOOLEANLIT", "ID", "INTLIT", 
                  "EXP", "FLOATLIT", "ESC_CHAR", "STR_CHAR", "ILL_CHAR", 
                  "STRINGLIT", "WS", "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[49] = self.INTLIT_action 
            actions[51] = self.FLOATLIT_action 
            actions[55] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	intlit = str(self.text)
            	self.text = intlit.replace("_", "")

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	floatlit = str(self.text)
            	self.text = floatlit.replace("_", "")

     

        if actionIndex == 2:

            	floatlit = str(self.text)
            	self.text = floatlit.replace("_", "")

     

        if actionIndex == 3:

            	floatlit = str(self.text)
            	self.text = floatlit.replace("_", "")

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	stringlit = str(self.text)
            	self.text = stringlit[1:-1]

     


