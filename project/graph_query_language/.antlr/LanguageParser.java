// Generated from /home/razerford/Рабочий стол/formalLang/formal-lang-course/project/graph_query_language/Language.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class LanguageParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		String=1, Int=2, Vertex=3, Edge=4, Graph=5, Bool=6, T=7, LIST=8, PRINT=9, 
		ASSIGN=10, CHAR=11, DIGIT=12, CHAR_D=13, VAR=14, STRING=15, BOOL=16, TRUE=17, 
		FALSE=18, COMMA=19, QUOT=20, LP=21, RP=22, LB=23, RB=24, SPACE=25, WS=26, 
		SEMICOLON=27, EOL=28;
	public static final int
		RULE_program = 0, RULE_stmt = 1, RULE_expr = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "stmt", "expr"
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

	@Override
	public String getGrammarFileName() { return "Language.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public LanguageParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(LanguageParser.EOF, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(LanguageParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(LanguageParser.SEMICOLON, i);
		}
		public List<TerminalNode> EOL() { return getTokens(LanguageParser.EOL); }
		public TerminalNode EOL(int i) {
			return getToken(LanguageParser.EOL, i);
		}
		public List<TerminalNode> WS() { return getTokens(LanguageParser.WS); }
		public TerminalNode WS(int i) {
			return getToken(LanguageParser.WS, i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINT) | (1L << VAR) | (1L << WS) | (1L << EOL))) != 0)) {
				{
				{
				setState(7);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==EOL) {
					{
					setState(6);
					match(EOL);
					}
				}

				setState(10);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==WS) {
					{
					setState(9);
					match(WS);
					}
				}

				setState(12);
				stmt();
				setState(13);
				match(SEMICOLON);
				setState(15);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
				case 1:
					{
					setState(14);
					match(EOL);
					}
					break;
				}
				}
				}
				setState(21);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(22);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public TerminalNode PRINT() { return getToken(LanguageParser.PRINT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode VAR() { return getToken(LanguageParser.VAR, 0); }
		public TerminalNode ASSIGN() { return getToken(LanguageParser.ASSIGN, 0); }
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stmt);
		try {
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINT:
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				match(PRINT);
				setState(25);
				expr();
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				match(VAR);
				setState(27);
				match(ASSIGN);
				setState(28);
				expr();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(LanguageParser.LP, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RP() { return getToken(LanguageParser.RP, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(LP);
			setState(32);
			expr();
			setState(33);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\36&\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\3\2\5\2\n\n\2\3\2\5\2\r\n\2\3\2\3\2\3\2\5\2\22\n\2\7\2\24\n"+
		"\2\f\2\16\2\27\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3 \n\3\3\4\3\4\3\4\3"+
		"\4\3\4\2\2\5\2\4\6\2\2\2\'\2\25\3\2\2\2\4\37\3\2\2\2\6!\3\2\2\2\b\n\7"+
		"\36\2\2\t\b\3\2\2\2\t\n\3\2\2\2\n\f\3\2\2\2\13\r\7\34\2\2\f\13\3\2\2\2"+
		"\f\r\3\2\2\2\r\16\3\2\2\2\16\17\5\4\3\2\17\21\7\35\2\2\20\22\7\36\2\2"+
		"\21\20\3\2\2\2\21\22\3\2\2\2\22\24\3\2\2\2\23\t\3\2\2\2\24\27\3\2\2\2"+
		"\25\23\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2\27\25\3\2\2\2\30\31\7\2\2\3"+
		"\31\3\3\2\2\2\32\33\7\13\2\2\33 \5\6\4\2\34\35\7\20\2\2\35\36\7\f\2\2"+
		"\36 \5\6\4\2\37\32\3\2\2\2\37\34\3\2\2\2 \5\3\2\2\2!\"\7\27\2\2\"#\5\6"+
		"\4\2#$\7\30\2\2$\7\3\2\2\2\7\t\f\21\25\37";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}