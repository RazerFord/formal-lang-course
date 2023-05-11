// Generated from /home/razerford/Рабочий стол/formalLang/formal-lang-course/project/graph_query_language/Language.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LanguageLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		String=1, Int=2, Vertex=3, Edge=4, Graph=5, Bool=6, T=7, LIST=8, PRINT=9, 
		ASSIGN=10, CHAR=11, DIGIT=12, CHAR_D=13, VAR=14, STRING=15, BOOL=16, TRUE=17, 
		FALSE=18, COMMA=19, QUOT=20, LP=21, RP=22, LB=23, RB=24, SPACE=25, WS=26, 
		SEMICOLON=27, EOL=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"String", "Int", "Vertex", "Edge", "Graph", "Bool", "T", "LIST", "PRINT", 
			"ASSIGN", "CHAR", "DIGIT", "CHAR_D", "VAR", "STRING", "BOOL", "TRUE", 
			"FALSE", "COMMA", "QUOT", "LP", "RP", "LB", "RB", "SPACE", "WS", "SEMICOLON", 
			"EOL"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, "'true'", "'false'", "','", "'\"'", "'('", 
			"')'", "'{'", "'}'", "' '"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "String", "Int", "Vertex", "Edge", "Graph", "Bool", "T", "LIST", 
			"PRINT", "ASSIGN", "CHAR", "DIGIT", "CHAR_D", "VAR", "STRING", "BOOL", 
			"TRUE", "FALSE", "COMMA", "QUOT", "LP", "RP", "LB", "RB", "SPACE", "WS", 
			"SEMICOLON", "EOL"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public LanguageLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Language.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\36\u00c8\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\3\2\3\2\3\3\6\3?\n\3\r\3"+
		"\16\3@\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7"+
		"\3\7\3\b\3\b\3\b\3\b\3\b\3\b\5\bZ\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\7\td\n\t\f\t\16\tg\13\t\3\t\3\t\5\tk\n\t\3\n\5\nn\n\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\5\nw\n\n\3\13\5\13z\n\13\3\13\3\13\5\13~\n\13\3\f\3\f\3\r"+
		"\3\r\3\16\3\16\5\16\u0086\n\16\3\17\3\17\7\17\u008a\n\17\f\17\16\17\u008d"+
		"\13\17\3\20\3\20\3\20\7\20\u0092\n\20\f\20\16\20\u0095\13\20\3\20\3\20"+
		"\3\21\3\21\5\21\u009b\n\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23"+
		"\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31"+
		"\3\32\3\32\3\33\6\33\u00b7\n\33\r\33\16\33\u00b8\3\33\3\33\3\34\5\34\u00be"+
		"\n\34\3\34\3\34\5\34\u00c2\n\34\3\35\6\35\u00c5\n\35\r\35\16\35\u00c6"+
		"\2\2\36\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17"+
		"\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35"+
		"9\36\3\2\7\4\2C\\c|\3\2\62;\4\2\"\"aa\5\2\13\13\17\17\"\"\3\2\f\f\2\u00dc"+
		"\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2"+
		"\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2"+
		"\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2"+
		"\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2"+
		"\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\3;\3"+
		"\2\2\2\5>\3\2\2\2\7B\3\2\2\2\tD\3\2\2\2\13K\3\2\2\2\rQ\3\2\2\2\17Y\3\2"+
		"\2\2\21j\3\2\2\2\23m\3\2\2\2\25y\3\2\2\2\27\177\3\2\2\2\31\u0081\3\2\2"+
		"\2\33\u0085\3\2\2\2\35\u0087\3\2\2\2\37\u008e\3\2\2\2!\u009a\3\2\2\2#"+
		"\u009c\3\2\2\2%\u00a1\3\2\2\2\'\u00a7\3\2\2\2)\u00a9\3\2\2\2+\u00ab\3"+
		"\2\2\2-\u00ad\3\2\2\2/\u00af\3\2\2\2\61\u00b1\3\2\2\2\63\u00b3\3\2\2\2"+
		"\65\u00b6\3\2\2\2\67\u00bd\3\2\2\29\u00c4\3\2\2\2;<\5\37\20\2<\4\3\2\2"+
		"\2=?\5\31\r\2>=\3\2\2\2?@\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\6\3\2\2\2BC\5\5"+
		"\3\2C\b\3\2\2\2DE\5+\26\2EF\5\5\3\2FG\5\'\24\2GH\5\37\20\2HI\5\'\24\2"+
		"IJ\5-\27\2J\n\3\2\2\2KL\5+\26\2LM\5\21\t\2MN\5\'\24\2NO\5\21\t\2OP\5-"+
		"\27\2P\f\3\2\2\2QR\5!\21\2R\16\3\2\2\2SZ\5!\21\2TZ\5\31\r\2UZ\5\27\f\2"+
		"VZ\5\37\20\2WZ\5\7\4\2XZ\5\t\5\2YS\3\2\2\2YT\3\2\2\2YU\3\2\2\2YV\3\2\2"+
		"\2YW\3\2\2\2YX\3\2\2\2Z\20\3\2\2\2[\\\5/\30\2\\]\5\61\31\2]k\3\2\2\2^"+
		"_\5/\30\2_e\5\17\b\2`a\5\'\24\2ab\5\17\b\2bd\3\2\2\2c`\3\2\2\2dg\3\2\2"+
		"\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2\2\2hi\5\61\31\2ik\3\2\2\2j[\3\2"+
		"\2\2j^\3\2\2\2k\22\3\2\2\2ln\5\65\33\2ml\3\2\2\2mn\3\2\2\2no\3\2\2\2o"+
		"p\7r\2\2pq\7t\2\2qr\7k\2\2rs\7p\2\2st\7v\2\2tv\3\2\2\2uw\5\65\33\2vu\3"+
		"\2\2\2vw\3\2\2\2w\24\3\2\2\2xz\5\65\33\2yx\3\2\2\2yz\3\2\2\2z{\3\2\2\2"+
		"{}\7?\2\2|~\5\65\33\2}|\3\2\2\2}~\3\2\2\2~\26\3\2\2\2\177\u0080\t\2\2"+
		"\2\u0080\30\3\2\2\2\u0081\u0082\t\3\2\2\u0082\32\3\2\2\2\u0083\u0086\5"+
		"\27\f\2\u0084\u0086\5\31\r\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2\u0086"+
		"\34\3\2\2\2\u0087\u008b\5\27\f\2\u0088\u008a\5\33\16\2\u0089\u0088\3\2"+
		"\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c"+
		"\36\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u0093\5)\25\2\u008f\u0092\5\33\16"+
		"\2\u0090\u0092\t\4\2\2\u0091\u008f\3\2\2\2\u0091\u0090\3\2\2\2\u0092\u0095"+
		"\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095"+
		"\u0093\3\2\2\2\u0096\u0097\5)\25\2\u0097 \3\2\2\2\u0098\u009b\5#\22\2"+
		"\u0099\u009b\5%\23\2\u009a\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\"\3"+
		"\2\2\2\u009c\u009d\7v\2\2\u009d\u009e\7t\2\2\u009e\u009f\7w\2\2\u009f"+
		"\u00a0\7g\2\2\u00a0$\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3\7c\2\2\u00a3"+
		"\u00a4\7n\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7g\2\2\u00a6&\3\2\2\2\u00a7"+
		"\u00a8\7.\2\2\u00a8(\3\2\2\2\u00a9\u00aa\7$\2\2\u00aa*\3\2\2\2\u00ab\u00ac"+
		"\7*\2\2\u00ac,\3\2\2\2\u00ad\u00ae\7+\2\2\u00ae.\3\2\2\2\u00af\u00b0\7"+
		"}\2\2\u00b0\60\3\2\2\2\u00b1\u00b2\7\177\2\2\u00b2\62\3\2\2\2\u00b3\u00b4"+
		"\7\"\2\2\u00b4\64\3\2\2\2\u00b5\u00b7\t\5\2\2\u00b6\u00b5\3\2\2\2\u00b7"+
		"\u00b8\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\3\2"+
		"\2\2\u00ba\u00bb\b\33\2\2\u00bb\66\3\2\2\2\u00bc\u00be\5\65\33\2\u00bd"+
		"\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c1\7="+
		"\2\2\u00c0\u00c2\5\65\33\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2"+
		"8\3\2\2\2\u00c3\u00c5\t\6\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2"+
		"\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7:\3\2\2\2\24\2@Yejmvy}\u0085"+
		"\u008b\u0091\u0093\u009a\u00b8\u00bd\u00c1\u00c6\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}