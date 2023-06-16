from language.LanguageVisitor import LanguageVisitor
from language.LanguageParser import LanguageParser
from memory import Memory

import types_lang as tp

class Visitor(LanguageVisitor):
    memory : Memory = Memory()

    # Visit a parse tree produced by LanguageParser#program.
    def visitProgram(self, ctx:LanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#stmt.
    def visitStmt(self, ctx:LanguageParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#print.
    def visitPrint(self, ctx:LanguageParser.PrintContext):
        variable = self.visitExpr(ctx.getChild(1))
        print(variable)
        return self.defaultResult()


    # Visit a parse tree produced by LanguageParser#bind.
    def visitBind(self, ctx:LanguageParser.BindContext):
        name = self.visitId(ctx.id_())
        value = self.visitExpr(ctx.expr())
        self.memory[name] = value
        return self.defaultResult()

    # Visit a parse tree produced by LanguageParser#expr.
    def visitExpr(self, ctx:LanguageParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#lambda.
    def visitLambda(self, ctx:LanguageParser.LambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#val.
    def visitVal(self, ctx:LanguageParser.ValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#bool.
    def visitBool(self, ctx:LanguageParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#string.
    def visitString(self, ctx:LanguageParser.StringContext):
        return str(ctx.getText())


    # Visit a parse tree produced by LanguageParser#integer.
    def visitInteger(self, ctx:LanguageParser.IntegerContext):
        return int(ctx.getText())


    # Visit a parse tree produced by LanguageParser#edge.
    def visitEdge(self, ctx:LanguageParser.EdgeContext):
        fst = self.visit(ctx.integer(0))
        label = self.visit(ctx.string())
        snd =  self.visit(ctx.integer(1))
        return tp.Edge(fst, label, snd)


    # Visit a parse tree produced by LanguageParser#item.
    def visitItem(self, ctx:LanguageParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#list.
    def visitList(self, ctx:LanguageParser.ListContext):
        result = []
        n = ctx.getChildCount()
        for i in range(1,n-1,2):
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = ctx.getChild(i)
            child_result = c.accept(self)
            result.append(child_result)
        return result


    # Visit a parse tree produced by LanguageParser#graph.
    def visitGraph(self, ctx:LanguageParser.GraphContext):
        vertexes = self.visitList(ctx.getChild(1))
        edges =  self.visitList(ctx.getChild(3))
        return tp.Graph(vertexes, edges)


    # Visit a parse tree produced by LanguageParser#id.
    def visitId(self, ctx:LanguageParser.IdContext):
        return tp.Id(ctx.getText(), self.memory)


    # Visit a parse tree produced by LanguageParser#set_start.
    def visitSet_start(self, ctx:LanguageParser.Set_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#set_final.
    def visitSet_final(self, ctx:LanguageParser.Set_finalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#add_start.
    def visitAdd_start(self, ctx:LanguageParser.Add_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#add_final.
    def visitAdd_final(self, ctx:LanguageParser.Add_finalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_start.
    def visitGet_start(self, ctx:LanguageParser.Get_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_final.
    def visitGet_final(self, ctx:LanguageParser.Get_finalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_reachable.
    def visitGet_reachable(self, ctx:LanguageParser.Get_reachableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_vertices.
    def visitGet_vertices(self, ctx:LanguageParser.Get_verticesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_edges.
    def visitGet_edges(self, ctx:LanguageParser.Get_edgesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#get_labels.
    def visitGet_labels(self, ctx:LanguageParser.Get_labelsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#map.
    def visitMap(self, ctx:LanguageParser.MapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#load.
    def visitLoad(self, ctx:LanguageParser.LoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#filter.
    def visitFilter(self, ctx:LanguageParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#of.
    def visitOf(self, ctx:LanguageParser.OfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#to.
    def visitTo(self, ctx:LanguageParser.ToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#intersect.
    def visitIntersect(self, ctx:LanguageParser.IntersectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#concat.
    def visitConcat(self, ctx:LanguageParser.ConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#union.
    def visitUnion(self, ctx:LanguageParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#in.
    def visitIn(self, ctx:LanguageParser.InContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#kleene.
    def visitKleene(self, ctx:LanguageParser.KleeneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#equal.
    def visitEqual(self, ctx:LanguageParser.EqualContext):
        return self.visitChildren(ctx)
