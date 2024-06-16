// Generated from /home/maxim/SQL/parser/sql.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class sqlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, ALL=9, 
		EQ=10, LT=11, GT=12, WORD=13, NUM=14, WS=15;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "ALL", 
			"EQ", "LT", "GT", "WORD", "NUM", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'.'", "'JOIN'", "'ON'", "'WHERE'", "'SELECT'", "','", "'FROM'", 
			"'*'", "'='", "'<'", "'>'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "ALL", "EQ", "LT", 
			"GT", "WORD", "NUM", "WS"
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


	public sqlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "sql.g4"; }

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
		"\u0004\u0000\u000fX\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0004\fI\b\f\u000b\f\f\fJ\u0001\r\u0004\rN"+
		"\b\r\u000b\r\f\rO\u0001\u000e\u0004\u000eS\b\u000e\u000b\u000e\f\u000e"+
		"T\u0001\u000e\u0001\u000e\u0000\u0000\u000f\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u0001\u0000\u0003"+
		"\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t\n\r\r  Z\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0001\u001f\u0001\u0000\u0000\u0000\u0003!\u0001\u0000\u0000\u0000"+
		"\u0005#\u0001\u0000\u0000\u0000\u0007(\u0001\u0000\u0000\u0000\t+\u0001"+
		"\u0000\u0000\u0000\u000b1\u0001\u0000\u0000\u0000\r8\u0001\u0000\u0000"+
		"\u0000\u000f:\u0001\u0000\u0000\u0000\u0011?\u0001\u0000\u0000\u0000\u0013"+
		"A\u0001\u0000\u0000\u0000\u0015C\u0001\u0000\u0000\u0000\u0017E\u0001"+
		"\u0000\u0000\u0000\u0019H\u0001\u0000\u0000\u0000\u001bM\u0001\u0000\u0000"+
		"\u0000\u001dR\u0001\u0000\u0000\u0000\u001f \u0005;\u0000\u0000 \u0002"+
		"\u0001\u0000\u0000\u0000!\"\u0005.\u0000\u0000\"\u0004\u0001\u0000\u0000"+
		"\u0000#$\u0005J\u0000\u0000$%\u0005O\u0000\u0000%&\u0005I\u0000\u0000"+
		"&\'\u0005N\u0000\u0000\'\u0006\u0001\u0000\u0000\u0000()\u0005O\u0000"+
		"\u0000)*\u0005N\u0000\u0000*\b\u0001\u0000\u0000\u0000+,\u0005W\u0000"+
		"\u0000,-\u0005H\u0000\u0000-.\u0005E\u0000\u0000./\u0005R\u0000\u0000"+
		"/0\u0005E\u0000\u00000\n\u0001\u0000\u0000\u000012\u0005S\u0000\u0000"+
		"23\u0005E\u0000\u000034\u0005L\u0000\u000045\u0005E\u0000\u000056\u0005"+
		"C\u0000\u000067\u0005T\u0000\u00007\f\u0001\u0000\u0000\u000089\u0005"+
		",\u0000\u00009\u000e\u0001\u0000\u0000\u0000:;\u0005F\u0000\u0000;<\u0005"+
		"R\u0000\u0000<=\u0005O\u0000\u0000=>\u0005M\u0000\u0000>\u0010\u0001\u0000"+
		"\u0000\u0000?@\u0005*\u0000\u0000@\u0012\u0001\u0000\u0000\u0000AB\u0005"+
		"=\u0000\u0000B\u0014\u0001\u0000\u0000\u0000CD\u0005<\u0000\u0000D\u0016"+
		"\u0001\u0000\u0000\u0000EF\u0005>\u0000\u0000F\u0018\u0001\u0000\u0000"+
		"\u0000GI\u0007\u0000\u0000\u0000HG\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\u001a"+
		"\u0001\u0000\u0000\u0000LN\u0007\u0001\u0000\u0000ML\u0001\u0000\u0000"+
		"\u0000NO\u0001\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000OP\u0001\u0000"+
		"\u0000\u0000P\u001c\u0001\u0000\u0000\u0000QS\u0007\u0002\u0000\u0000"+
		"RQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000"+
		"\u0000TU\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VW\u0006\u000e"+
		"\u0000\u0000W\u001e\u0001\u0000\u0000\u0000\u0004\u0000JOT\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}