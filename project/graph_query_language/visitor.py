from language.LanguageVisitor import LanguageVisitor
from language.LanguageParser import LanguageParser
from memory import Memory
from typing import Union
from exceptions import InvalidArgument

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
        args = self.visitList(ctx.list_())
        body = ctx.expr()
        return tp.Lambda(args, body)


    # Visit a parse tree produced by LanguageParser#val.
    def visitVal(self, ctx:LanguageParser.ValContext):
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
        for item in ctx.item():
            if not self.shouldVisitNextChild(ctx, result):
                return result

            c = item
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
        if ctx.getText() == "true":
            return tp.Bool(True)
        if ctx.getText() == "false":
            return tp.Bool(False)
        return tp.Id(ctx.getText(), self.memory)


    # Visit a parse tree produced by LanguageParser#set_start.
    def visitSet_start(self, ctx:LanguageParser.Set_startContext):
        source = self._get_source(ctx)
        target = self._get_target_graph(ctx)
        target.set_start_nodes(source)
        return target


    # Visit a parse tree produced by LanguageParser#set_final.
    def visitSet_final(self, ctx:LanguageParser.Set_finalContext):
        source = self._get_source(ctx)
        target = self._get_target_graph(ctx)
        target.set_final_nodes(source)
        return target


    # Visit a parse tree produced by LanguageParser#add_start.
    def visitAdd_start(self, ctx:LanguageParser.Add_startContext):
        source = self._get_source(ctx)
        target = self._get_target_graph(ctx)
        target.add_start_nodes(source)
        return target


    # Visit a parse tree produced by LanguageParser#add_final.
    def visitAdd_final(self, ctx:LanguageParser.Add_finalContext):
        source = self._get_source(ctx)
        target = self._get_target_graph(ctx)
        target.add_final_nodes(source)
        return target
    

    # Visit a parse tree produced by LanguageParser#get_start.
    def visitGet_start(self, ctx:LanguageParser.Get_startContext):
        target = self._get_target_graph(ctx)
        return target.start_nodes


    # Visit a parse tree produced by LanguageParser#get_final.
    def visitGet_final(self, ctx:LanguageParser.Get_finalContext):
        target = self._get_target_graph(ctx)
        return target.final_nodes


    # Visit a parse tree produced by LanguageParser#get_reachable.
    def visitGet_reachable(self, ctx:LanguageParser.Get_reachableContext):
        target = self._get_target_graph(ctx)
        return target.get_reachable()


    # Visit a parse tree produced by LanguageParser#get_vertices.
    def visitGet_vertices(self, ctx:LanguageParser.Get_verticesContext):
        target = self._get_target_graph(ctx)
        return target.get_vertices()


    # Visit a parse tree produced by LanguageParser#get_edges.
    def visitGet_edges(self, ctx:LanguageParser.Get_edgesContext):
        target = self._get_target_graph(ctx)
        return target.get_edges()


    # Visit a parse tree produced by LanguageParser#get_labels.
    def visitGet_labels(self, ctx:LanguageParser.Get_labelsContext):
        target = self._get_target_graph(ctx)
        return target.get_labels()

    # Visit a parse tree produced by LanguageParser#map.
    def visitMap(self, ctx:LanguageParser.MapContext):
        lam = self._get_lambda(ctx)
        iterable = self._get_iterable(ctx)
        result = []
        for args in iterable:
            if not isinstance(args, list):
                args = [args]
            if len(args) != len(lam.args):
                raise InvalidArgument("the number of arguments and the number of parameters in the lambda are not the same")
            for n, v in zip(lam.args, args):
                self.memory[n] = v
            result.append(self.memory[self.visitExpr(lam.body)])
        return result


    # Visit a parse tree produced by LanguageParser#load.
    def visitLoad(self, ctx:LanguageParser.LoadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LanguageParser#filter.
    def visitFilter(self, ctx:LanguageParser.FilterContext):
        lam = self._get_lambda(ctx)
        iterable = self._get_iterable(ctx)
        result = []
        for args in iterable:
            _iter = args
            if not isinstance(args, list):
                _iter = [_iter]
            if len(_iter) != len(lam.args):
                raise InvalidArgument("the number of arguments and the number of parameters in the lambda are not the same")
            for n, v in zip(lam.args, _iter):
                self.memory[n] = v
            if self.memory[self.visitExpr(lam.body)].value == True:
                result.append(args)
        return result


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

    def _get_lambda(self, ctx:LanguageParser.MapContext) -> tp.Lambda:
        if ctx.lambda_() is not None:
            return self.visitLambda(ctx.lambda_())
        if ctx.var() is not None:
            return self.memory.get(ctx.var().getText())

    def _get_iterable(self, ctx:LanguageParser.MapContext) -> tp.Lambda:
        iterable = ctx.iterable()
        if iterable.list_() is not None:
            return self.visitList(iterable.list_())
        if iterable.var() is not None:
            return self.memory.get(iterable.var().getText())

    def _get_source(self, ctx: Union[
        LanguageParser.Set_startContext, 
        LanguageParser.Set_finalContext,
        LanguageParser.Add_startContext,
        LanguageParser.Add_finalContext]):
        source = ctx.source()
        if source.var() is not None:
            return self.memory.get(source.var().getText()).start_nodes
        if source.integer() is not None:
            return [int(source.integer())]
        if source.list_() is not None:
            return self.visitList(source.list_())

    def _get_target_graph(self, ctx: Union[
        LanguageParser.Set_startContext, 
        LanguageParser.Set_finalContext,
        LanguageParser.Add_startContext,
        LanguageParser.Add_finalContext]):
        target = ctx.target()
        if target.var() is not None:
            name = target.var().getText()
            graph = self.memory.get(name)
            if isinstance(graph, tp.Graph):
                return graph
            raise InvalidArgument(f"target argument '{name}' is not a graph")
        if target.graph() is not None:
            return self.visitGraph(target.graph())
