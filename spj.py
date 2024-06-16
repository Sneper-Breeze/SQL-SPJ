from antlr4 import *
import csv
from parser.sqlLexer import sqlLexer
from parser.sqlParser import sqlParser
from parser.sqlListener import sqlListener
from nodes import *




class SQLLogic(sqlListener):   
    root = None
    curr_node = None
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
        attr = [el.table().getText()+'.'+el.var().getText() for el in ctx.join_condition().attribute()]
        rtable = self.curr_node.give_LChind()
        self.curr_node.set_LChild(JoinNode(attr[0], attr[1]))
        self.curr_node = self.curr_node.give_LChind()
        self.curr_node.set_RChild(rtable)
        self.curr_node.set_LChild(TableNode(ctx.table().var().getText())) 


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
        collumns = []
        for el in ctx.ALL():
            collumns.append(el.getText())
        for attr in ctx.attribute():
            collumns.append(attr.table().getText()+'.'+attr.var().getText())

        self.root = SelectNode(collumns)
        self.curr_node = self.root

    # Exit a parse tree produced by sqlParser#select.
    def exitSelect(self, ctx:sqlParser.SelectContext):
        pass

    # Enter a parse tree produced by sqlParser#from.
    def enterFrom(self, ctx:sqlParser.FromContext):
        if(ctx.where()):
            cond = ctx.where()[0].condition()
            attr = [el.table().getText()+'.'+el.var().getText() for el in cond.attribute()]

            if(len(cond.NUM()) != 0):
                self.curr_node.set_LChild(WhereNode(attr[0], cond.NUM()[0].getText(), [comp.getText() for comp in cond.comparison()]))
            else:
                self.curr_node.set_LChild(WhereNode(attr[0], attr[1], cond.comparison().getText()))
            self.curr_node = self.curr_node.give_LChind()

        self.curr_node.set_LChild(TableNode(ctx.table().var().getText()))


    # Exit a parse tree produced by sqlParser#from.
    def exitFrom(self, ctx:sqlParser.FromContext):
        pass

    def getRoot(self):
        return self.root
