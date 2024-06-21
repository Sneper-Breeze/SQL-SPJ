# Generated from parser/sql.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,1,1,1,1,1,1,
        1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,39,8,4,1,4,4,4,42,8,4,11,
        4,12,4,43,1,4,1,4,3,4,48,8,4,1,5,4,5,51,8,5,11,5,12,5,52,1,6,1,6,
        1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,5,8,66,8,8,10,8,12,8,69,9,8,
        1,9,1,9,1,9,3,9,74,8,9,1,9,5,9,77,8,9,10,9,12,9,80,9,9,1,9,1,9,3,
        9,84,8,9,1,9,1,9,1,10,1,10,1,10,5,10,91,8,10,10,10,12,10,94,9,10,
        1,10,3,10,97,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,2,1,
        0,14,15,1,0,11,13,97,0,22,1,0,0,0,2,25,1,0,0,0,4,30,1,0,0,0,6,32,
        1,0,0,0,8,38,1,0,0,0,10,50,1,0,0,0,12,54,1,0,0,0,14,56,1,0,0,0,16,
        61,1,0,0,0,18,70,1,0,0,0,20,87,1,0,0,0,22,23,3,18,9,0,23,24,5,1,
        0,0,24,1,1,0,0,0,25,26,3,4,2,0,26,27,5,2,0,0,27,28,1,0,0,0,28,29,
        3,10,5,0,29,3,1,0,0,0,30,31,3,10,5,0,31,5,1,0,0,0,32,33,3,2,1,0,
        33,34,5,11,0,0,34,35,3,2,1,0,35,7,1,0,0,0,36,39,3,2,1,0,37,39,3,
        10,5,0,38,36,1,0,0,0,38,37,1,0,0,0,39,41,1,0,0,0,40,42,3,12,6,0,
        41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,47,1,
        0,0,0,45,48,3,2,1,0,46,48,3,10,5,0,47,45,1,0,0,0,47,46,1,0,0,0,48,
        9,1,0,0,0,49,51,7,0,0,0,50,49,1,0,0,0,51,52,1,0,0,0,52,50,1,0,0,
        0,52,53,1,0,0,0,53,11,1,0,0,0,54,55,7,1,0,0,55,13,1,0,0,0,56,57,
        5,3,0,0,57,58,3,4,2,0,58,59,5,4,0,0,59,60,3,6,3,0,60,15,1,0,0,0,
        61,62,5,5,0,0,62,67,3,8,4,0,63,64,5,6,0,0,64,66,3,8,4,0,65,63,1,
        0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,17,1,0,0,0,69,
        67,1,0,0,0,70,78,5,7,0,0,71,74,5,10,0,0,72,74,3,2,1,0,73,71,1,0,
        0,0,73,72,1,0,0,0,74,75,1,0,0,0,75,77,5,8,0,0,76,73,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,83,1,0,0,0,80,78,1,0,0,0,
        81,84,5,10,0,0,82,84,3,2,1,0,83,81,1,0,0,0,83,82,1,0,0,0,84,85,1,
        0,0,0,85,86,3,20,10,0,86,19,1,0,0,0,87,88,5,9,0,0,88,92,3,4,2,0,
        89,91,3,14,7,0,90,89,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,1,
        0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,95,97,3,16,8,0,96,95,1,0,0,0,96,
        97,1,0,0,0,97,21,1,0,0,0,10,38,43,47,52,67,73,78,83,92,96
    ]

class sqlParser ( Parser ):

    grammarFileName = "sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "'JOIN'", "'ON'", "'WHERE'", 
                     "'AND'", "'SELECT'", "','", "'FROM'", "'*'", "'='", 
                     "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ALL", "EQ", "LT", "GT", 
                      "WORD", "NUM", "WS" ]

    RULE_query = 0
    RULE_attribute = 1
    RULE_table = 2
    RULE_join_condition = 3
    RULE_condition = 4
    RULE_var = 5
    RULE_comparison = 6
    RULE_join = 7
    RULE_where = 8
    RULE_select = 9
    RULE_from = 10

    ruleNames =  [ "query", "attribute", "table", "join_condition", "condition", 
                   "var", "comparison", "join", "where", "select", "from" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ALL=10
    EQ=11
    LT=12
    GT=13
    WORD=14
    NUM=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select(self):
            return self.getTypedRuleContext(sqlParser.SelectContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = sqlParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.select()
            self.state = 23
            self.match(sqlParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(sqlParser.VarContext,0)


        def table(self):
            return self.getTypedRuleContext(sqlParser.TableContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = sqlParser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.table()
            self.state = 26
            self.match(sqlParser.T__1)
            self.state = 28
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(sqlParser.VarContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_table

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable" ):
                listener.enterTable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable" ):
                listener.exitTable(self)




    def table(self):

        localctx = sqlParser.TableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_table)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(sqlParser.AttributeContext,i)


        def EQ(self):
            return self.getToken(sqlParser.EQ, 0)

        def getRuleIndex(self):
            return sqlParser.RULE_join_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_condition" ):
                listener.enterJoin_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_condition" ):
                listener.exitJoin_condition(self)




    def join_condition(self):

        localctx = sqlParser.Join_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_join_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.attribute()
            self.state = 33
            self.match(sqlParser.EQ)
            self.state = 34
            self.attribute()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(sqlParser.AttributeContext,i)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.VarContext)
            else:
                return self.getTypedRuleContext(sqlParser.VarContext,i)


        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(sqlParser.ComparisonContext,i)


        def getRuleIndex(self):
            return sqlParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = sqlParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 36
                self.attribute()
                pass

            elif la_ == 2:
                self.state = 37
                self.var()
                pass


            self.state = 41 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 40
                self.comparison()
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    break

            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 45
                self.attribute()
                pass

            elif la_ == 2:
                self.state = 46
                self.var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(sqlParser.WORD)
            else:
                return self.getToken(sqlParser.WORD, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(sqlParser.NUM)
            else:
                return self.getToken(sqlParser.NUM, i)

        def getRuleIndex(self):
            return sqlParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = sqlParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 49
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 52 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==14 or _la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(sqlParser.EQ, 0)

        def LT(self):
            return self.getToken(sqlParser.LT, 0)

        def GT(self):
            return self.getToken(sqlParser.GT, 0)

        def getRuleIndex(self):
            return sqlParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = sqlParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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


    class JoinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table(self):
            return self.getTypedRuleContext(sqlParser.TableContext,0)


        def join_condition(self):
            return self.getTypedRuleContext(sqlParser.Join_conditionContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_join

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin" ):
                listener.enterJoin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin" ):
                listener.exitJoin(self)




    def join(self):

        localctx = sqlParser.JoinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_join)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(sqlParser.T__2)
            self.state = 57
            self.table()
            self.state = 58
            self.match(sqlParser.T__3)
            self.state = 59
            self.join_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.ConditionContext)
            else:
                return self.getTypedRuleContext(sqlParser.ConditionContext,i)


        def getRuleIndex(self):
            return sqlParser.RULE_where

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere" ):
                listener.enterWhere(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere" ):
                listener.exitWhere(self)




    def where(self):

        localctx = sqlParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(sqlParser.T__4)
            self.state = 62
            self.condition()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 63
                self.match(sqlParser.T__5)
                self.state = 64
                self.condition()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def from_(self):
            return self.getTypedRuleContext(sqlParser.FromContext,0)


        def ALL(self, i:int=None):
            if i is None:
                return self.getTokens(sqlParser.ALL)
            else:
                return self.getToken(sqlParser.ALL, i)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.AttributeContext)
            else:
                return self.getTypedRuleContext(sqlParser.AttributeContext,i)


        def getRuleIndex(self):
            return sqlParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = sqlParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(sqlParser.T__6)
            self.state = 78
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 73
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 71
                        self.match(sqlParser.ALL)
                        pass
                    elif token in [14, 15]:
                        self.state = 72
                        self.attribute()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 75
                    self.match(sqlParser.T__7) 
                self.state = 80
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 81
                self.match(sqlParser.ALL)
                pass
            elif token in [14, 15]:
                self.state = 82
                self.attribute()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 85
            self.from_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table(self):
            return self.getTypedRuleContext(sqlParser.TableContext,0)


        def join(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.JoinContext)
            else:
                return self.getTypedRuleContext(sqlParser.JoinContext,i)


        def where(self):
            return self.getTypedRuleContext(sqlParser.WhereContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_from

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom" ):
                listener.enterFrom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom" ):
                listener.exitFrom(self)




    def from_(self):

        localctx = sqlParser.FromContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_from)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(sqlParser.T__8)
            self.state = 88
            self.table()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 89
                self.join()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 95
                self.where()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





