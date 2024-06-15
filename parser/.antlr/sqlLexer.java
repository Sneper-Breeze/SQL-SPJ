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
		EQ=10, NE=11, LT=12, LE=13, GT=14, GE=15, WORD=16, NUM=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "ALL", 
			"EQ", "NE", "LT", "LE", "GT", "GE", "WORD", "NUM", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'.'", "'JOIN'", "'ON'", "'WHERE'", "'SELECT'", "','", "'FROM'", 
			"'*'", "'='", "'!='", "'<'", "'<='", "'>'", "'>='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "ALL", "EQ", "NE", 
			"LT", "LE", "GT", "GE", "WORD", "NUM", "WS"
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
		"\u0004\u0000\u0012g\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000fX\b\u000f\u000b"+
		"\u000f\f\u000fY\u0001\u0010\u0004\u0010]\b\u0010\u000b\u0010\f\u0010^"+
		"\u0001\u0011\u0004\u0011b\b\u0011\u000b\u0011\f\u0011c\u0001\u0011\u0001"+
		"\u0011\u0000\u0000\u0012\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017"+
		"\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012\u0001\u0000"+
		"\u0003\u0002\u0000AZaz\u0001\u000009\u0003\u0000\t\n\r\r  i\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0001%\u0001\u0000\u0000\u0000\u0003"+
		"\'\u0001\u0000\u0000\u0000\u0005)\u0001\u0000\u0000\u0000\u0007.\u0001"+
		"\u0000\u0000\u0000\t1\u0001\u0000\u0000\u0000\u000b7\u0001\u0000\u0000"+
		"\u0000\r>\u0001\u0000\u0000\u0000\u000f@\u0001\u0000\u0000\u0000\u0011"+
		"E\u0001\u0000\u0000\u0000\u0013G\u0001\u0000\u0000\u0000\u0015I\u0001"+
		"\u0000\u0000\u0000\u0017L\u0001\u0000\u0000\u0000\u0019N\u0001\u0000\u0000"+
		"\u0000\u001bQ\u0001\u0000\u0000\u0000\u001dS\u0001\u0000\u0000\u0000\u001f"+
		"W\u0001\u0000\u0000\u0000!\\\u0001\u0000\u0000\u0000#a\u0001\u0000\u0000"+
		"\u0000%&\u0005;\u0000\u0000&\u0002\u0001\u0000\u0000\u0000\'(\u0005.\u0000"+
		"\u0000(\u0004\u0001\u0000\u0000\u0000)*\u0005J\u0000\u0000*+\u0005O\u0000"+
		"\u0000+,\u0005I\u0000\u0000,-\u0005N\u0000\u0000-\u0006\u0001\u0000\u0000"+
		"\u0000./\u0005O\u0000\u0000/0\u0005N\u0000\u00000\b\u0001\u0000\u0000"+
		"\u000012\u0005W\u0000\u000023\u0005H\u0000\u000034\u0005E\u0000\u0000"+
		"45\u0005R\u0000\u000056\u0005E\u0000\u00006\n\u0001\u0000\u0000\u0000"+
		"78\u0005S\u0000\u000089\u0005E\u0000\u00009:\u0005L\u0000\u0000:;\u0005"+
		"E\u0000\u0000;<\u0005C\u0000\u0000<=\u0005T\u0000\u0000=\f\u0001\u0000"+
		"\u0000\u0000>?\u0005,\u0000\u0000?\u000e\u0001\u0000\u0000\u0000@A\u0005"+
		"F\u0000\u0000AB\u0005R\u0000\u0000BC\u0005O\u0000\u0000CD\u0005M\u0000"+
		"\u0000D\u0010\u0001\u0000\u0000\u0000EF\u0005*\u0000\u0000F\u0012\u0001"+
		"\u0000\u0000\u0000GH\u0005=\u0000\u0000H\u0014\u0001\u0000\u0000\u0000"+
		"IJ\u0005!\u0000\u0000JK\u0005=\u0000\u0000K\u0016\u0001\u0000\u0000\u0000"+
		"LM\u0005<\u0000\u0000M\u0018\u0001\u0000\u0000\u0000NO\u0005<\u0000\u0000"+
		"OP\u0005=\u0000\u0000P\u001a\u0001\u0000\u0000\u0000QR\u0005>\u0000\u0000"+
		"R\u001c\u0001\u0000\u0000\u0000ST\u0005>\u0000\u0000TU\u0005=\u0000\u0000"+
		"U\u001e\u0001\u0000\u0000\u0000VX\u0007\u0000\u0000\u0000WV\u0001\u0000"+
		"\u0000\u0000XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001"+
		"\u0000\u0000\u0000Z \u0001\u0000\u0000\u0000[]\u0007\u0001\u0000\u0000"+
		"\\[\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000"+
		"\u0000^_\u0001\u0000\u0000\u0000_\"\u0001\u0000\u0000\u0000`b\u0007\u0002"+
		"\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"ef\u0006\u0011\u0000\u0000f$\u0001\u0000\u0000\u0000\u0004\u0000Y^c\u0001"+
		"\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}