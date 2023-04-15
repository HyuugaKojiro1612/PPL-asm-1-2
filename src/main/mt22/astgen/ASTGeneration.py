from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program				: decllist EOF ;
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        # lst = self.visit(ctx.decllist())
        # print(type(lst))
        return Program(self.visit(ctx.decllist()))


    # decllist			: decl decllist | decl ;
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.decllist():
            return self.visit(ctx.decl()) + self.visit(ctx.decllist())
        return self.visit(ctx.decl())
        # return ctx.decl().accept(self)


    # decl				: vardecl | funcdecl ;
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        return self.visit(ctx.funcdecl())
        


    # vardecl				: vardecl_short | vardecl_full ;
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        if ctx.vardecl_short():
            return self.visit(ctx.vardecl_short())
        # if ctx.vardecl_full() is not None: print("Vardecl_full is not None")
        return self.visit(ctx.vardecl_full())


    # vardecl_short		: idlist COLON var_type SEMI ;
    def visitVardecl_short(self, ctx:MT22Parser.Vardecl_shortContext):
        # return [str(ID)]
        idlist = self.visit(ctx.idlist())   
        var_type = self.visit(ctx.var_type())
        return [VarDecl(x, var_type, None) for x in idlist]   


    # vardecl_full		: varrec SEMI ;
    def visitVardecl_full(self, ctx:MT22Parser.Vardecl_fullContext):
        varrec = self.visit(ctx.varrec())
        n = len(varrec)
        ret = []
        for i in range(n):
            ret += [
                VarDecl(varrec[i][0], varrec[i][1], varrec[n - 1 - i][2])
            ]
        return ret
        
        # varrec = self.visit(ctx.varrec())
        # idlist = [varrec[i][0] for i in range(len(varrec))]
        # exprlist = [varrec[i][1] for i in range(len(varrec))]
        # exprlist.reverse()
        # var_type = varrec[0][2]
        # return [VarDecl(idlist[i], var_type, exprlist[i]) for i in range(len(idlist))]
        

    # varbase             : ID COLON var_type EQUAL expr ;
    def visitVarbase(self, ctx:MT22Parser.VarbaseContext):
        id = ctx.ID().getText()
        var_type = self.visit(ctx.var_type())
        expr = self.visit(ctx.expr())
        return [(id, expr, var_type)]
    

    # varrec				: ID COMMA varrec COMMA expr 
    #                       | ID COLON var_type EQUAL expr ;
    def visitVarrec(self, ctx:MT22Parser.VarrecContext):
        # [ (Id(), Type(), Expr()) ]
        id = ctx.ID().getText()
        # print(id)
        rhs = self.visit(ctx.expr())
        if ctx.varrec():
            rest = self.visit(ctx.varrec())
            typ = rest[-1][1]
            return [(id, typ, rhs)] + rest
        return [(id, self.visit(ctx.var_type()), rhs)]
        # if ctx.varbase():
        #     return self.visit(ctx.varbase())
        # id = ctx.ID().getText()
        # expr = self.visit(ctx.expr())
        # return [(id, expr)] + self.visit(ctx.varrec())


    # paramdecllist		: paramdeclprime |  ;
    def visitParamdecllist(self, ctx:MT22Parser.ParamdecllistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.paramdeclprime())


    # paramdeclprime		: paramdecl COMMA paramdeclprime | paramdecl ;
    def visitParamdeclprime(self, ctx:MT22Parser.ParamdeclprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.paramdecl())]
        return [self.visit(ctx.paramdecl())] + self.visit(ctx.paramdeclprime())


    # paramdecl			: INHERIT? OUT? ID COLON var_type ;
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        id = ctx.ID().getText()
        typ = self.visit(ctx.var_type())
        out = False
        inherit = False
        if ctx.INHERIT(): inherit = True
        if ctx.OUT(): out = True
        return ParamDecl(id, typ, out, inherit)


    # funcdecl			: funcprototype funcbody ;
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        proto = self.visit(ctx.funcprototype())
        body = self.visit(ctx.funcbody())
        inherit = None
        if len(proto) == 4: inherit = proto[3]
        # print(type(proto[2]))
        return [FuncDecl(proto[0], proto[1], proto[2], inherit, body)]


    # funcprototype		: ID COLON FUNCTION return_type LP paramdecllist RP INHERIT ID 
    #                   | ID COLON FUNCTION return_type LP paramdecllist RP ;
    def visitFuncprototype(self, ctx:MT22Parser.FuncprototypeContext):
        typ = self.visit(ctx.return_type())
        params = self.visit(ctx.paramdecllist())
        if ctx.INHERIT():
            return (ctx.ID(0).getText(), typ, params, ctx.ID(1).getText())
        return (ctx.ID(0).getText(), typ, params)


    # funcbody			: block_stmt ;
    def visitFuncbody(self, ctx:MT22Parser.FuncbodyContext):
        return self.visit(ctx.block_stmt())


    # element_type 		: INTEGER | FLOAT | STRING |BOOLEAN ;
    def visitElement_type(self, ctx:MT22Parser.Element_typeContext):
        if ctx.INTEGER():
            return IntegerType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        return BooleanType()


    # var_type			: element_type | AUTO | array_type ;
    def visitVar_type(self, ctx:MT22Parser.Var_typeContext):
        if ctx.element_type():
            return self.visit(ctx.element_type())
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.array_type())


    # return_type			: element_type | VOID | AUTO | array_type ;
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        if ctx.element_type():
            return self.visit(ctx.element_type())
        if ctx.VOID():
            return VoidType()
        if ctx.AUTO():
            return AutoType()
        return self.visit(ctx.array_type())


    # array   			: ID COLON array_type ;
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        return [VarDecl(ctx.ID().getText(), self.visit(ctx.array_type()), None)]


    # array_type          : ARRAY LSB dim RSB OF element_type ;
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return ArrayType(self.visit(ctx.dim()), self.visit(ctx.element_type()))


    # idlist 				: ID COMMA idlist | ID ;
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        id = ctx.ID().getText()
        if ctx.getChildCount() == 1:
            return [id]
        return [id] + self.visit(ctx.idlist())


    # dim 			    : INTLIT COMMA dim | INTLIT ;
    def visitDim(self, ctx:MT22Parser.DimContext):
        if ctx.dim():
            return [int(ctx.INTLIT().getText())] + self.visit(ctx.dim())
        return [int(ctx.INTLIT().getText())]


    # exprlist 			: expr COMMA exprlist | expr ;
    def visitExprlist(self, ctx:MT22Parser.ExprlistContext):
        # expr = self.visit(ctx.expr())
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist())


    # expr				: exp1 DOUBLE_COLON exp1 | exp1 ;
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        # exp1 = self.visit(ctx.exp1())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(ctx.getChild(1).getText(),
            self.visit(ctx.getChild(0)),
            self.visit(ctx.getChild(2)))


    # exp1				: exp2 relationalOp exp2 | exp2 ;
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        # exp2 = self.visit(ctx.exp2())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinExpr(self.visit(ctx.getChild(1)),
            self.visit(ctx.getChild(0)),
            self.visit(ctx.getChild(2)))


    # exp2				: exp2 (BOOL_CONJ | BOOL_DISJ) exp3 | exp3 ;
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        exp3 = self.visit(ctx.exp3())
        if ctx.getChildCount() == 1:
            return exp3
        exp2 = self.visit(ctx.exp2())
        return BinExpr(ctx.getChild(1).getText(), exp2, exp3)


    # exp3				: exp3 (ADD | SUB) exp4 | exp4 ;
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        # exp4 = self.visit(ctx.exp4())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        # exp3 = self.visit(ctx.exp3())
        return BinExpr(ctx.getChild(1).getText(),
            self.visit(ctx.getChild(0)),
            self.visit(ctx.getChild(2)))


    # exp4				: exp4 (MUL | DIV | REMAINDER) exp5 | exp5 ;
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        # exp5 = self.visit(ctx.exp5())
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        # exp4 = self.visit(ctx.exp4())
        return BinExpr(ctx.getChild(1).getText(),
            self.visit(ctx.getChild(0)),
            self.visit(ctx.getChild(2)))


    # exp5				: BOOL_NEGA exp5 | exp6 ;
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp6())
        return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.exp5()))


    # exp6				: SUB exp6 | exp7 ;
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp7())
        return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.exp6()))


    # exp7				: ID indexOp | operand ;
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        if ctx.operand():
            return self.visit(ctx.operand())
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.indexOp()))


    # relationalOp		: EQUAL | NOT_EQUAL | GREATER_THAN | LESS_THAN | GREATER_THAN_EQ | LESS_THAN_EQ ;
    def visitRelationalOp(self, ctx:MT22Parser.RelationalOpContext):
        return ctx.getChild(0).getText()


    # indexOp 			: LSB exprlist RSB ;
    def visitIndexOp(self, ctx:MT22Parser.IndexOpContext):
        return self.visit(ctx.exprlist())


    # stmtlist			: (stmt | vardecl) stmtlist |  ;
    def visitStmtlist(self, ctx:MT22Parser.StmtlistContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.stmtlist())
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmtlist())
        return []


    # stmt				: /*vardecl |*/ asm_stmt | if_stmt | for_stmt 
    #                   | while_stmt | dowhile_stmt | break_stmt 
    #                   | continue_stmt | return_stmt | call_stmt 
    #                   | block_stmt ;
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        # if ctx.vardecl():
        #     return self.visit(ctx.vardecl())
        if ctx.asm_stmt():
            return self.visit(ctx.asm_stmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.dowhile_stmt():
            return self.visit(ctx.dowhile_stmt())
        if ctx.break_stmt():
            return self.visit(ctx.break_stmt())
        if ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
        if ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        if ctx.call_stmt():
            # print(type(self.visit(ctx.call_stmt())))
            return self.visit(ctx.call_stmt())
        return self.visit(ctx.block_stmt())


    # asm_stmt			: ID ASSIGN expr SEMI
    #                   | ID indexOp ASSIGN expr SEMI ;
    def visitAsm_stmt(self, ctx:MT22Parser.Asm_stmtContext):
        if ctx.indexOp():
            arr = ArrayCell(ctx.ID().getText(), self.visit(ctx.indexOp()))
            return AssignStmt(arr, self.visit(ctx.expr()))
        return AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr()))


    # if_stmt				: IF LP expr RP stmt
    #                       | IF LP expr RP stmt ELSE stmt ;
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), None)


    # for_stmt			: FOR LP ID indexOp? ASSIGN expr COMMA expr COMMA expr RP stmt ;
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        if ctx.indexOp():
            arr = ArrayCell(ctx.ID().getText(), self.visit(ctx.indexOp()))
            asm_stmt = AssignStmt(arr, self.visit(ctx.expr(0)))
            return ForStmt(asm_stmt, self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))
        asm_stmt = AssignStmt(Id(ctx.ID().getText()), self.visit(ctx.expr(0)))
        return ForStmt(asm_stmt, self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))


    # while_stmt			: WHILE LP expr RP stmt ;
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))


    # dowhile_stmt		: DO block_stmt WHILE LP expr RP SEMI ;
    def visitDowhile_stmt(self, ctx:MT22Parser.Dowhile_stmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.block_stmt()))


    # break_stmt			: BREAK SEMI ;
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return BreakStmt()


    # continue_stmt		: CONTINUE SEMI ;
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return ContinueStmt()


    # return_stmt			: RETURN expr SEMI | RETURN SEMI ;
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)


    # call_stmt			: funccall SEMI ;
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        funccall = self.visit(ctx.funccall())
        return CallStmt(funccall.name, funccall.args)


    # block_stmt			: LB stmtlist RB ;
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        # print(type(self.visit(ctx.stmtlist())))
        return BlockStmt(self.visit(ctx.stmtlist()))


    # constant			: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT  | arraylit ;
    def visitConstant(self, ctx:MT22Parser.ConstantContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        if ctx.FLOATLIT():
            str = ctx.FLOATLIT().getText()
            if str[0] == '.' and (str[1] == 'e' or str[1] == 'E'):
                return FloatLit(float("0.0"))
            return FloatLit(float(str))
        if ctx.BOOLEANLIT():
            return BooleanLit(True) if ctx.BOOLEANLIT().getText() == "true" else BooleanLit(False)
        if ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        return ArrayLit(self.visit(ctx.arraylit()))


    # funccall			: ID LP argumentlist RP ;
    def visitFunccall(self, ctx:MT22Parser.FunccallContext):
        return FuncCall(ctx.ID().getText(), self.visit(ctx.argumentlist()))


    # argumentlist		: argumentprime |  ;
    def visitArgumentlist(self, ctx:MT22Parser.ArgumentlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.argumentprime())


    # argumentprime 		: argument COMMA argumentprime | argument ;
    def visitArgumentprime(self, ctx:MT22Parser.ArgumentprimeContext):
        # argument = self.visit(ctx.argument())
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.argument())]
        return [self.visit(ctx.argument())] + self.visit(ctx.argumentprime())


    # argument			: operand | expr ;
    def visitArgument(self, ctx:MT22Parser.ArgumentContext):
        if ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.operand())


    # operand			    : ID | constant | funccall | LP expr RP ; 
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.constant():
            return self.visit(ctx.constant())
        if ctx.funccall():
            return self.visit(ctx.funccall())
        return self.visit(ctx.expr())


    # arraylit 			: LB exprlist RB | LB RB ;
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        if ctx.exprlist():
            return self.visit(ctx.exprlist())
        return []
