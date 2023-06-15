from language.LanguageVisitor import LanguageVisitor
from language.LanguageParser import LanguageParser

class Visitor(LanguageVisitor):

    # Visit a parse tree produced by LanguageParser#program.
    def visitProgram(self, ctx:LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#stmt.
    def visitStmt(self, ctx:LanguageParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#print.
    def visitPrint(self, ctx:LanguageParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#bind.
    def visitBind(self, ctx:LanguageParser.BindContext):
        print("i am here")
        print(ctx.depth.__annotations__)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#expr.
    def visitExpr(self, ctx:LanguageParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#lambda.
    def visitLambda(self, ctx:LanguageParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#var.
    def visitVar(self, ctx:LanguageParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#val.
    def visitVal(self, ctx:LanguageParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#bool.
    def visitBool(self, ctx:LanguageParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#string.
    def visitString(self, ctx:LanguageParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#integer.
    def visitInteger(self, ctx:LanguageParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#vertex.
    def visitVertex(self, ctx:LanguageParser.VertexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#edge.
    def visitEdge(self, ctx:LanguageParser.EdgeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#item.
    def visitItem(self, ctx:LanguageParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#list.
    def visitList(self, ctx:LanguageParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#graph.
    def visitGraph(self, ctx:LanguageParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#id.
    def visitId(self, ctx:LanguageParser.IdContext):
        return self.visitChildren(ctx)
