// Generated from /home/maxim/SQL/parser/sql.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class sqlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, ALL=9, 
		EQ=10, NE=11, LT=12, LE=13, GT=14, GE=15, WORD=16, NUM=17, WS=18;
	public static final int
		RULE_query = 0, RULE_attribute = 1, RULE_table = 2, RULE_join_condition = 3, 
		RULE_condition = 4, RULE_var = 5, RULE_comparison = 6, RULE_join = 7, 
		RULE_where = 8, RULE_select = 9, RULE_from = 10;
	private static String[] makeRuleNames() {
		return new String[] {
			"query", "attribute", "table", "join_condition", "condition", "var", 
			"comparison", "join", "where", "select", "from"
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

	@Override
	public String getGrammarFileName() { return "sql.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public sqlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public SelectContext select() {
			return getRuleContext(SelectContext.class,0);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_query);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			select();
			setState(23);
			match(T__0);
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

	@SuppressWarnings("CheckReturnValue")
	public static class AttributeContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public AttributeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attribute; }
	}

	public final AttributeContext attribute() throws RecognitionException {
		AttributeContext _localctx = new AttributeContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_attribute);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(25);
				table();
				setState(26);
				match(T__1);
				}
				break;
			}
			setState(30);
			var();
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

	@SuppressWarnings("CheckReturnValue")
	public static class TableContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public TableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table; }
	}

	public final TableContext table() throws RecognitionException {
		TableContext _localctx = new TableContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			var();
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

	@SuppressWarnings("CheckReturnValue")
	public static class Join_conditionContext extends ParserRuleContext {
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public TerminalNode EQ() { return getToken(sqlParser.EQ, 0); }
		public Join_conditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_join_condition; }
	}

	public final Join_conditionContext join_condition() throws RecognitionException {
		Join_conditionContext _localctx = new Join_conditionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_join_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			attribute();
			setState(35);
			match(EQ);
			setState(36);
			attribute();
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

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public List<TerminalNode> NUM() { return getTokens(sqlParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(sqlParser.NUM, i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				setState(38);
				attribute();
				}
				break;
			case 2:
				{
				setState(39);
				match(NUM);
				}
				break;
			}
			setState(42);
			comparison();
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(43);
				attribute();
				}
				break;
			case 2:
				{
				setState(44);
				match(NUM);
				}
				break;
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public List<TerminalNode> WORD() { return getTokens(sqlParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(sqlParser.WORD, i);
		}
		public List<TerminalNode> NUM() { return getTokens(sqlParser.NUM); }
		public TerminalNode NUM(int i) {
			return getToken(sqlParser.NUM, i);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_var);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(48); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(47);
				_la = _input.LA(1);
				if ( !(_la==WORD || _la==NUM) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(50); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD || _la==NUM );
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

	@SuppressWarnings("CheckReturnValue")
	public static class ComparisonContext extends ParserRuleContext {
		public TerminalNode EQ() { return getToken(sqlParser.EQ, 0); }
		public TerminalNode NE() { return getToken(sqlParser.NE, 0); }
		public TerminalNode LT() { return getToken(sqlParser.LT, 0); }
		public TerminalNode LE() { return getToken(sqlParser.LE, 0); }
		public TerminalNode GT() { return getToken(sqlParser.GT, 0); }
		public TerminalNode GE() { return getToken(sqlParser.GE, 0); }
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 64512L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class JoinContext extends ParserRuleContext {
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public Join_conditionContext join_condition() {
			return getRuleContext(Join_conditionContext.class,0);
		}
		public JoinContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_join; }
	}

	public final JoinContext join() throws RecognitionException {
		JoinContext _localctx = new JoinContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_join);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__2);
			setState(55);
			table();
			setState(56);
			match(T__3);
			setState(57);
			join_condition();
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

	@SuppressWarnings("CheckReturnValue")
	public static class WhereContext extends ParserRuleContext {
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public WhereContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where; }
	}

	public final WhereContext where() throws RecognitionException {
		WhereContext _localctx = new WhereContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_where);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__4);
			setState(60);
			condition();
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

	@SuppressWarnings("CheckReturnValue")
	public static class SelectContext extends ParserRuleContext {
		public FromContext from() {
			return getRuleContext(FromContext.class,0);
		}
		public List<TerminalNode> ALL() { return getTokens(sqlParser.ALL); }
		public TerminalNode ALL(int i) {
			return getToken(sqlParser.ALL, i);
		}
		public List<AttributeContext> attribute() {
			return getRuleContexts(AttributeContext.class);
		}
		public AttributeContext attribute(int i) {
			return getRuleContext(AttributeContext.class,i);
		}
		public SelectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_select; }
	}

	public final SelectContext select() throws RecognitionException {
		SelectContext _localctx = new SelectContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_select);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__5);
			setState(70);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(65);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case ALL:
						{
						setState(63);
						match(ALL);
						}
						break;
					case WORD:
					case NUM:
						{
						setState(64);
						attribute();
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(67);
					match(T__6);
					}
					} 
				}
				setState(72);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ALL:
				{
				setState(73);
				match(ALL);
				}
				break;
			case WORD:
			case NUM:
				{
				setState(74);
				attribute();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(77);
			from();
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

	@SuppressWarnings("CheckReturnValue")
	public static class FromContext extends ParserRuleContext {
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public List<JoinContext> join() {
			return getRuleContexts(JoinContext.class);
		}
		public JoinContext join(int i) {
			return getRuleContext(JoinContext.class,i);
		}
		public List<WhereContext> where() {
			return getRuleContexts(WhereContext.class);
		}
		public WhereContext where(int i) {
			return getRuleContext(WhereContext.class,i);
		}
		public FromContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_from; }
	}

	public final FromContext from() throws RecognitionException {
		FromContext _localctx = new FromContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_from);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__7);
			setState(80);
			table();
			setState(84);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__2) {
				{
				{
				setState(81);
				join();
				}
				}
				setState(86);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(90);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(87);
				where();
				}
				}
				setState(92);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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
		"\u0004\u0001\u0012^\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u001d\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0003\u0004)\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0003\u0004.\b\u0004\u0001\u0005\u0004"+
		"\u00051\b\u0005\u000b\u0005\f\u00052\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0003\tB\b\t\u0001\t\u0005\tE\b\t\n\t\f\tH"+
		"\t\t\u0001\t\u0001\t\u0003\tL\b\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0005\nS\b\n\n\n\f\nV\t\n\u0001\n\u0005\nY\b\n\n\n\f\n\\\t\n\u0001"+
		"\n\u0000\u0000\u000b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0000\u0002\u0001\u0000\u0010\u0011\u0001\u0000\n\u000f[\u0000\u0016"+
		"\u0001\u0000\u0000\u0000\u0002\u001c\u0001\u0000\u0000\u0000\u0004 \u0001"+
		"\u0000\u0000\u0000\u0006\"\u0001\u0000\u0000\u0000\b(\u0001\u0000\u0000"+
		"\u0000\n0\u0001\u0000\u0000\u0000\f4\u0001\u0000\u0000\u0000\u000e6\u0001"+
		"\u0000\u0000\u0000\u0010;\u0001\u0000\u0000\u0000\u0012>\u0001\u0000\u0000"+
		"\u0000\u0014O\u0001\u0000\u0000\u0000\u0016\u0017\u0003\u0012\t\u0000"+
		"\u0017\u0018\u0005\u0001\u0000\u0000\u0018\u0001\u0001\u0000\u0000\u0000"+
		"\u0019\u001a\u0003\u0004\u0002\u0000\u001a\u001b\u0005\u0002\u0000\u0000"+
		"\u001b\u001d\u0001\u0000\u0000\u0000\u001c\u0019\u0001\u0000\u0000\u0000"+
		"\u001c\u001d\u0001\u0000\u0000\u0000\u001d\u001e\u0001\u0000\u0000\u0000"+
		"\u001e\u001f\u0003\n\u0005\u0000\u001f\u0003\u0001\u0000\u0000\u0000 "+
		"!\u0003\n\u0005\u0000!\u0005\u0001\u0000\u0000\u0000\"#\u0003\u0002\u0001"+
		"\u0000#$\u0005\n\u0000\u0000$%\u0003\u0002\u0001\u0000%\u0007\u0001\u0000"+
		"\u0000\u0000&)\u0003\u0002\u0001\u0000\')\u0005\u0011\u0000\u0000(&\u0001"+
		"\u0000\u0000\u0000(\'\u0001\u0000\u0000\u0000)*\u0001\u0000\u0000\u0000"+
		"*-\u0003\f\u0006\u0000+.\u0003\u0002\u0001\u0000,.\u0005\u0011\u0000\u0000"+
		"-+\u0001\u0000\u0000\u0000-,\u0001\u0000\u0000\u0000.\t\u0001\u0000\u0000"+
		"\u0000/1\u0007\u0000\u0000\u00000/\u0001\u0000\u0000\u000012\u0001\u0000"+
		"\u0000\u000020\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u00003\u000b"+
		"\u0001\u0000\u0000\u000045\u0007\u0001\u0000\u00005\r\u0001\u0000\u0000"+
		"\u000067\u0005\u0003\u0000\u000078\u0003\u0004\u0002\u000089\u0005\u0004"+
		"\u0000\u00009:\u0003\u0006\u0003\u0000:\u000f\u0001\u0000\u0000\u0000"+
		";<\u0005\u0005\u0000\u0000<=\u0003\b\u0004\u0000=\u0011\u0001\u0000\u0000"+
		"\u0000>F\u0005\u0006\u0000\u0000?B\u0005\t\u0000\u0000@B\u0003\u0002\u0001"+
		"\u0000A?\u0001\u0000\u0000\u0000A@\u0001\u0000\u0000\u0000BC\u0001\u0000"+
		"\u0000\u0000CE\u0005\u0007\u0000\u0000DA\u0001\u0000\u0000\u0000EH\u0001"+
		"\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000"+
		"GK\u0001\u0000\u0000\u0000HF\u0001\u0000\u0000\u0000IL\u0005\t\u0000\u0000"+
		"JL\u0003\u0002\u0001\u0000KI\u0001\u0000\u0000\u0000KJ\u0001\u0000\u0000"+
		"\u0000LM\u0001\u0000\u0000\u0000MN\u0003\u0014\n\u0000N\u0013\u0001\u0000"+
		"\u0000\u0000OP\u0005\b\u0000\u0000PT\u0003\u0004\u0002\u0000QS\u0003\u000e"+
		"\u0007\u0000RQ\u0001\u0000\u0000\u0000SV\u0001\u0000\u0000\u0000TR\u0001"+
		"\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000UZ\u0001\u0000\u0000\u0000"+
		"VT\u0001\u0000\u0000\u0000WY\u0003\u0010\b\u0000XW\u0001\u0000\u0000\u0000"+
		"Y\\\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000"+
		"\u0000[\u0015\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000\u0000\t\u001c"+
		"(-2AFKTZ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}