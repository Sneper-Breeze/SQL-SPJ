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
        4,1,16,111,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,41,8,4,1,4,4,4,
        44,8,4,11,4,12,4,45,1,4,1,4,3,4,50,8,4,1,5,4,5,53,8,5,11,5,12,5,
        54,1,6,1,6,1,7,1,7,1,7,5,7,62,8,7,10,7,12,7,65,9,7,1,7,1,7,1,7,1,
        8,1,8,1,8,1,9,1,9,1,9,1,9,5,9,77,8,9,10,9,12,9,80,9,9,1,10,1,10,
        1,10,1,10,5,10,86,8,10,10,10,12,10,89,9,10,1,10,3,10,92,8,10,1,11,
        1,11,1,11,3,11,97,8,11,1,11,5,11,100,8,11,10,11,12,11,103,9,11,1,
        11,1,11,3,11,107,8,11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,
        18,20,22,0,2,1,0,14,15,1,0,11,13,110,0,24,1,0,0,0,2,27,1,0,0,0,4,
        32,1,0,0,0,6,34,1,0,0,0,8,40,1,0,0,0,10,52,1,0,0,0,12,56,1,0,0,0,
        14,58,1,0,0,0,16,69,1,0,0,0,18,72,1,0,0,0,20,81,1,0,0,0,22,93,1,
        0,0,0,24,25,3,22,11,0,25,26,5,1,0,0,26,1,1,0,0,0,27,28,3,4,2,0,28,
        29,5,2,0,0,29,30,1,0,0,0,30,31,3,10,5,0,31,3,1,0,0,0,32,33,3,10,
        5,0,33,5,1,0,0,0,34,35,3,2,1,0,35,36,5,11,0,0,36,37,3,2,1,0,37,7,
        1,0,0,0,38,41,3,2,1,0,39,41,3,10,5,0,40,38,1,0,0,0,40,39,1,0,0,0,
        41,43,1,0,0,0,42,44,3,12,6,0,43,42,1,0,0,0,44,45,1,0,0,0,45,43,1,
        0,0,0,45,46,1,0,0,0,46,49,1,0,0,0,47,50,3,2,1,0,48,50,3,10,5,0,49,
        47,1,0,0,0,49,48,1,0,0,0,50,9,1,0,0,0,51,53,7,0,0,0,52,51,1,0,0,
        0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,11,1,0,0,0,56,57,
        7,1,0,0,57,13,1,0,0,0,58,59,5,3,0,0,59,63,3,4,2,0,60,62,3,16,8,0,
        61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,
        0,0,0,65,63,1,0,0,0,66,67,5,4,0,0,67,68,3,6,3,0,68,15,1,0,0,0,69,
        70,5,5,0,0,70,71,3,4,2,0,71,17,1,0,0,0,72,73,5,6,0,0,73,78,3,8,4,
        0,74,75,5,7,0,0,75,77,3,8,4,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,
        1,0,0,0,78,79,1,0,0,0,79,19,1,0,0,0,80,78,1,0,0,0,81,82,5,8,0,0,
        82,87,3,4,2,0,83,86,3,14,7,0,84,86,3,16,8,0,85,83,1,0,0,0,85,84,
        1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,0,88,91,1,0,0,0,
        89,87,1,0,0,0,90,92,3,18,9,0,91,90,1,0,0,0,91,92,1,0,0,0,92,21,1,
        0,0,0,93,101,5,9,0,0,94,97,5,10,0,0,95,97,3,2,1,0,96,94,1,0,0,0,
        96,95,1,0,0,0,97,98,1,0,0,0,98,100,5,5,0,0,99,96,1,0,0,0,100,103,
        1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,106,1,0,0,0,103,101,1,
        0,0,0,104,107,5,10,0,0,105,107,3,2,1,0,106,104,1,0,0,0,106,105,1,
        0,0,0,107,108,1,0,0,0,108,109,3,20,10,0,109,23,1,0,0,0,12,40,45,
        49,54,63,78,85,87,91,96,101,106
    ]

class sqlParser ( Parser ):

    grammarFileName = "sql.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'.'", "'JOIN'", "'ON'", "','", 
                     "'WHERE'", "'AND'", "'FROM'", "'SELECT'", "'*'", "'='", 
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
    RULE_cross_product = 8
    RULE_where = 9
    RULE_from = 10
    RULE_select = 11

    ruleNames =  [ "query", "attribute", "table", "join_condition", "condition", 
                   "var", "comparison", "join", "cross_product", "where", 
                   "from", "select" ]

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
            self.state = 24
            self.select()
            self.state = 25
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
            self.state = 27
            self.table()
            self.state = 28
            self.match(sqlParser.T__1)
            self.state = 30
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
            self.state = 32
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
            self.state = 34
            self.attribute()
            self.state = 35
            self.match(sqlParser.EQ)
            self.state = 36
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
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 38
                self.attribute()
                pass

            elif la_ == 2:
                self.state = 39
                self.var()
                pass


            self.state = 43 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self.comparison()
                self.state = 45 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
                    break

            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 47
                self.attribute()
                pass

            elif la_ == 2:
                self.state = 48
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
            self.state = 52 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 51
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 54 
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
            self.state = 56
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


        def cross_product(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.Cross_productContext)
            else:
                return self.getTypedRuleContext(sqlParser.Cross_productContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(sqlParser.T__2)
            self.state = 59
            self.table()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 60
                self.cross_product()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(sqlParser.T__3)
            self.state = 67
            self.join_condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cross_productContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table(self):
            return self.getTypedRuleContext(sqlParser.TableContext,0)


        def getRuleIndex(self):
            return sqlParser.RULE_cross_product

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCross_product" ):
                listener.enterCross_product(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCross_product" ):
                listener.exitCross_product(self)




    def cross_product(self):

        localctx = sqlParser.Cross_productContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cross_product)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(sqlParser.T__4)
            self.state = 70
            self.table()
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
        self.enterRule(localctx, 18, self.RULE_where)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(sqlParser.T__5)
            self.state = 73
            self.condition()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 74
                self.match(sqlParser.T__6)
                self.state = 75
                self.condition()
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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


        def cross_product(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sqlParser.Cross_productContext)
            else:
                return self.getTypedRuleContext(sqlParser.Cross_productContext,i)


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
            self.state = 81
            self.match(sqlParser.T__7)
            self.state = 82
            self.table()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==5:
                self.state = 85
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3]:
                    self.state = 83
                    self.join()
                    pass
                elif token in [5]:
                    self.state = 84
                    self.cross_product()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 90
                self.where()


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
        self.enterRule(localctx, 22, self.RULE_select)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(sqlParser.T__8)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 96
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 94
                        self.match(sqlParser.ALL)
                        pass
                    elif token in [14, 15]:
                        self.state = 95
                        self.attribute()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 98
                    self.match(sqlParser.T__4) 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 104
                self.match(sqlParser.ALL)
                pass
            elif token in [14, 15]:
                self.state = 105
                self.attribute()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 108
            self.from_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





