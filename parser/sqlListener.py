# Generated from parser/sql.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):

    # Enter a parse tree produced by sqlParser#query.
    def enterQuery(self, ctx:sqlParser.QueryContext):
        pass

    # Exit a parse tree produced by sqlParser#query.
    def exitQuery(self, ctx:sqlParser.QueryContext):
        pass


    # Enter a parse tree produced by sqlParser#attribute.
    def enterAttribute(self, ctx:sqlParser.AttributeContext):
        pass

    # Exit a parse tree produced by sqlParser#attribute.
    def exitAttribute(self, ctx:sqlParser.AttributeContext):
        pass


    # Enter a parse tree produced by sqlParser#table.
    def enterTable(self, ctx:sqlParser.TableContext):
        pass

    # Exit a parse tree produced by sqlParser#table.
    def exitTable(self, ctx:sqlParser.TableContext):
        pass


    # Enter a parse tree produced by sqlParser#join_condition.
    def enterJoin_condition(self, ctx:sqlParser.Join_conditionContext):
        pass

    # Exit a parse tree produced by sqlParser#join_condition.
    def exitJoin_condition(self, ctx:sqlParser.Join_conditionContext):
        pass


    # Enter a parse tree produced by sqlParser#condition.
    def enterCondition(self, ctx:sqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by sqlParser#condition.
    def exitCondition(self, ctx:sqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by sqlParser#var.
    def enterVar(self, ctx:sqlParser.VarContext):
        pass

    # Exit a parse tree produced by sqlParser#var.
    def exitVar(self, ctx:sqlParser.VarContext):
        pass


    # Enter a parse tree produced by sqlParser#comparison.
    def enterComparison(self, ctx:sqlParser.ComparisonContext):
        pass

    # Exit a parse tree produced by sqlParser#comparison.
    def exitComparison(self, ctx:sqlParser.ComparisonContext):
        pass


    # Enter a parse tree produced by sqlParser#join.
    def enterJoin(self, ctx:sqlParser.JoinContext):
        pass

    # Exit a parse tree produced by sqlParser#join.
    def exitJoin(self, ctx:sqlParser.JoinContext):
        pass


    # Enter a parse tree produced by sqlParser#where.
    def enterWhere(self, ctx:sqlParser.WhereContext):
        pass

    # Exit a parse tree produced by sqlParser#where.
    def exitWhere(self, ctx:sqlParser.WhereContext):
        pass


    # Enter a parse tree produced by sqlParser#select.
    def enterSelect(self, ctx:sqlParser.SelectContext):
        pass

    # Exit a parse tree produced by sqlParser#select.
    def exitSelect(self, ctx:sqlParser.SelectContext):
        pass


    # Enter a parse tree produced by sqlParser#from.
    def enterFrom(self, ctx:sqlParser.FromContext):
        pass

    # Exit a parse tree produced by sqlParser#from.
    def exitFrom(self, ctx:sqlParser.FromContext):
        pass



del sqlParser