import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_2(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_3(self):
        input = """x, y, z: integer = 1, 2, 3;
        a, b: float;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        """Simple program"""
        input = """main: function void () {
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        """More complex program"""
        input = """main: function void () {
            printInteger(4);
        }"""
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 305))
    
    def test_6(self):
        input = """
        a: integer;
        main: function void() {
            return 1;
        }
        b_als__a_2_o, __init__, __define__, _A0_2_1: float;
        c: string = "m";
        d, e: string;
        """
        expect ="""Program([
	VarDecl(a, IntegerType)
	FuncDecl(main, VoidType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
	VarDecl(b_als__a_2_o, FloatType)
	VarDecl(__init__, FloatType)
	VarDecl(__define__, FloatType)
	VarDecl(_A0_2_1, FloatType)
	VarDecl(c, StringType, StringLit(m))
	VarDecl(d, StringType)
	VarDecl(e, StringType)
])"""
        self.assertTrue(TestAST.test(input, expect, 306))
    
    def test_7(self):
        input = """is_check: boolean = true;
        is_not_check, is_prime: boolean = false, (false || true);
        a, b: auto;
        """
        expect = """Program([
	VarDecl(is_check, BooleanType, BooleanLit(True))
	VarDecl(is_not_check, BooleanType, BooleanLit(False))
	VarDecl(is_prime, BooleanType, BinExpr(||, BooleanLit(False), BooleanLit(True)))
	VarDecl(a, AutoType)
	VarDecl(b, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input = """
        is_check: boolean = (true || false) && (false && is_check);
        main: function void() {
            a = (true || false);
        }"""
        expect = """Program([
	VarDecl(is_check, BooleanType, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BinExpr(&&, BooleanLit(False), Id(is_check))))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), BinExpr(||, BooleanLit(True), BooleanLit(False)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """
        c, d, e, f: float = 1.e23, 4.e-1, .e2, .1e+2;
        m: function integer() {
            a: array[10] of integer;
            a = {1,2,3,{3,4,5}};
        }"""
        expect = """Program([
	VarDecl(c, FloatType, FloatLit(1e+23))
	VarDecl(d, FloatType, FloatLit(0.4))
	VarDecl(e, FloatType, FloatLit(0.0))
	VarDecl(f, FloatType, FloatLit(10.0))
	FuncDecl(m, IntegerType, [], None, BlockStmt([VarDecl(a, ArrayType([10], IntegerType)), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_10(self):
        input = """
        a, b, c: integer;
        d: string;
        e_2sad_, mu_w2__a: float = 1.23, 6.2e4;
        __init: boolean;
        main: function integer() inherit person {}
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(d, StringType)
	VarDecl(e_2sad_, FloatType, FloatLit(1.23))
	VarDecl(mu_w2__a, FloatType, FloatLit(62000.0))
	VarDecl(__init, BooleanType)
	FuncDecl(main, IntegerType, [], person, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 310))                

    def test_11(self):
        input = """
        a, b, c: integer;
        pi, e_math: float = 3.14, 0.2718e1;
        d: string;
        __init: boolean;
        __def: array[5, 1_45_2] of string;
        main: function integer(a: integer, inherit out c: string) inherit person {a: integer;}
        """
        expect = """Program([
	VarDecl(a, IntegerType)
	VarDecl(b, IntegerType)
	VarDecl(c, IntegerType)
	VarDecl(pi, FloatType, FloatLit(3.14))
	VarDecl(e_math, FloatType, FloatLit(2.718))
	VarDecl(d, StringType)
	VarDecl(__init, BooleanType)
	VarDecl(__def, ArrayType([5, 1452], StringType))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), InheritOutParam(c, StringType)], person, BlockStmt([VarDecl(a, IntegerType)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 311))                

    def test_12(self):
        input = """
        a, b, c: integer = 1_23_45, 987, 650; 
        main: function integer(m: array[1] of integer) {
            return;
        }
        foo: function void() {
            parser(2, 4);
            __init__(c % d, false && true);
            readInteger();
        }
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(12345))
	VarDecl(b, IntegerType, IntegerLit(987))
	VarDecl(c, IntegerType, IntegerLit(650))
	FuncDecl(main, IntegerType, [Param(m, ArrayType([1], IntegerType))], None, BlockStmt([ReturnStmt()]))
	FuncDecl(foo, VoidType, [], None, BlockStmt([CallStmt(parser, IntegerLit(2), IntegerLit(4)), CallStmt(__init__, BinExpr(%, Id(c), Id(d)), BinExpr(&&, BooleanLit(False), BooleanLit(True))), CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 312))                

    def test_13(self):
        input = """        
        x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return a;
            else return n * fact(n - 1);
        }
        inc: function void (out n: integer, delta: integer) {
            n = n + delta;
        }
        main: function void()
        {
            delta: integer = fact(3);
            inc(x, delta);
            printInteger(x);
            for (i = 1, i < 10, i + 1) {
                writeInt(i);
            }
        }
        """
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(Id(a)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta)), CallStmt(printInteger, Id(x)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 313))                

    def test_14(self):
        input = """
        multi: function boolean(inherit c: float, out dimen_to_string: integer) {}
        """
        expect = """Program([
	FuncDecl(multi, BooleanType, [InheritParam(c, FloatType), OutParam(dimen_to_string, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 314))                

    def test_15(self):
        input = """
        int: array[1,2] of integer;
        fl: array[1_2, 22_1] of float;
        bool: array[1,2_0] of boolean;
        str: array[86_9,9] of string;
        main: function void(argv: integer, out kwarg: string){}
        """
        expect = """Program([
	VarDecl(int, ArrayType([1, 2], IntegerType))
	VarDecl(fl, ArrayType([12, 221], FloatType))
	VarDecl(bool, ArrayType([1, 20], BooleanType))
	VarDecl(str, ArrayType([869, 9], StringType))
	FuncDecl(main, VoidType, [Param(argv, IntegerType), OutParam(kwarg, StringType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 315))                

    def test_16(self):
        input = """
        children: array[1_2,3_4,5_6] of float = {1., .e-5, 2.e+1, 1e-10};
        m,n,p,q: array[2] of boolean = true, (false && "0"), true, (true || abc);
        """
        expect = """Program([
	VarDecl(children, ArrayType([12, 34, 56], FloatType), ArrayLit([FloatLit(1.0), FloatLit(0.0), FloatLit(20.0), FloatLit(1e-10)]))
	VarDecl(m, ArrayType([2], BooleanType), BooleanLit(True))
	VarDecl(n, ArrayType([2], BooleanType), BinExpr(&&, BooleanLit(False), StringLit(0)))
	VarDecl(p, ArrayType([2], BooleanType), BooleanLit(True))
	VarDecl(q, ArrayType([2], BooleanType), BinExpr(||, BooleanLit(True), Id(abc)))
])"""
        self.assertTrue(TestAST.test(input, expect, 316))                

    def test_17(self):
        input = """
        newcastle, func: auto = {1,2,"abc", m, {9,20}}, custom;
        foo: string = "abc" :: mn + 1 - (-2) * 6 / 4 + 12%3;
        """
        expect = """Program([
	VarDecl(newcastle, AutoType, ArrayLit([IntegerLit(1), IntegerLit(2), StringLit(abc), Id(m), ArrayLit([IntegerLit(9), IntegerLit(20)])]))
	VarDecl(func, AutoType, Id(custom))
	VarDecl(foo, StringType, BinExpr(::, StringLit(abc), BinExpr(+, BinExpr(-, BinExpr(+, Id(mn), IntegerLit(1)), BinExpr(/, BinExpr(*, UnExpr(-, IntegerLit(2)), IntegerLit(6)), IntegerLit(4))), BinExpr(%, IntegerLit(12), IntegerLit(3)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 317))                

    def test_18(self):
        input = """
        main: function void() {
            a: array[6_2] of integer;
            a = expr + (true || false) - a[3,4];
            a = 2 + 5;
            b = a;
            /*for (i = 0, i < 4, i + 1){
                return 6;
            }*/
            for (i = 0, i < 4, i + 1){
                return 6;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([62], IntegerType)), AssignStmt(Id(a), BinExpr(-, BinExpr(+, Id(expr), BinExpr(||, BooleanLit(True), BooleanLit(False))), ArrayCell(a, [IntegerLit(3), IntegerLit(4)]))), AssignStmt(Id(a), BinExpr(+, IntegerLit(2), IntegerLit(5))), AssignStmt(Id(b), Id(a)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(4)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(6))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 318))                

    def test_19(self):
        input = """
        main: function void() {
            a: array[12_23] of float;
            ex = expr + (true || false) - a[3,4];
            a[3,4] = 2.e3;
            a[4,5] = {1.e-2, .e-4, .e-5, 0.3e4};
            m: array[2] of string;
            m[0] = "abc\\n";
            m[1] = "\\"";
            return returntype;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([1223], FloatType)), AssignStmt(Id(ex), BinExpr(-, BinExpr(+, Id(expr), BinExpr(||, BooleanLit(True), BooleanLit(False))), ArrayCell(a, [IntegerLit(3), IntegerLit(4)]))), AssignStmt(ArrayCell(a, [IntegerLit(3), IntegerLit(4)]), FloatLit(2000.0)), AssignStmt(ArrayCell(a, [IntegerLit(4), IntegerLit(5)]), ArrayLit([FloatLit(0.01), FloatLit(0.0), FloatLit(0.0), FloatLit(3000.0)])), VarDecl(m, ArrayType([2], StringType)), AssignStmt(ArrayCell(m, [IntegerLit(0)]), StringLit(abc\\n)), AssignStmt(ArrayCell(m, [IntegerLit(1)]), StringLit(\\")), ReturnStmt(Id(returntype))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 319))                

    def test_20(self):
        input = """
        member, employee: string = a :: b, c::d;
        main: function void(){
            gat = a > b;
            gae = a >= b;
            left = a < b;
            equal = a == b;
            nequal = a != b;
            leftequal = a <= b;
        }
        """     
        expect = """Program([
	VarDecl(member, StringType, BinExpr(::, Id(a), Id(b)))
	VarDecl(employee, StringType, BinExpr(::, Id(c), Id(d)))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(gat), BinExpr(>, Id(a), Id(b))), AssignStmt(Id(gae), BinExpr(>=, Id(a), Id(b))), AssignStmt(Id(left), BinExpr(<, Id(a), Id(b))), AssignStmt(Id(equal), BinExpr(==, Id(a), Id(b))), AssignStmt(Id(nequal), BinExpr(!=, Id(a), Id(b))), AssignStmt(Id(leftequal), BinExpr(<=, Id(a), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 320))                

    def test_21(self):
        input = """
        main: function void() {
            m = func(mul+1-2, is_check(a&&b));
            a[1,2] = func(main(1_2_3));
        }
        """ 
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(m), FuncCall(func, [BinExpr(-, BinExpr(+, Id(mul), IntegerLit(1)), IntegerLit(2)), FuncCall(is_check, [BinExpr(&&, Id(a), Id(b))])])), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), FuncCall(func, [FuncCall(main, [IntegerLit(123)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 321))                

    def test_22(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            a: array[3,3] of integer;
            a[0,0] = true && false;
            a[0, 1] = false && false;
            a[0, 2 ] = true && true;
            a[ 1, 1] = false && true;
            return a;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, ArrayType([3, 3], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), BinExpr(&&, BooleanLit(True), BooleanLit(False))), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), BinExpr(&&, BooleanLit(False), BooleanLit(False))), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(2)]), BinExpr(&&, BooleanLit(True), BooleanLit(True))), AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), BinExpr(&&, BooleanLit(False), BooleanLit(True))), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 322))                

    def test_23(self):
        input = """
        main: function void() {
            codium : integer = 1.2e-4;
            bracket : integer = "sweep"::"meet";
            annotation = bracket;
            best = foo(a&&b);
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(codium, IntegerType, FloatLit(0.00012)), VarDecl(bracket, IntegerType, BinExpr(::, StringLit(sweep), StringLit(meet))), AssignStmt(Id(annotation), Id(bracket)), AssignStmt(Id(best), FuncCall(foo, [BinExpr(&&, Id(a), Id(b))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 323))                

    def test_24(self):
        input = """main: function integer(out c: array[1,2_3] of integer) inherit fff {
            cycle: integer = mul012_23(22-foo(a + foo(a)));
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [OutParam(c, ArrayType([1, 23], IntegerType))], fff, BlockStmt([VarDecl(cycle, IntegerType, FuncCall(mul012_23, [BinExpr(-, IntegerLit(22), FuncCall(foo, [BinExpr(+, Id(a), FuncCall(foo, [Id(a)]))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 324))                

    def test_25(self):
        input = """
        main: function auto(){
            match: array[2] of boolean;
            match[0] = tonumber != tostring;
            match[1] = !false && true;
            a = !(a != !b);
        }
        Function: function void() {}"""
        expect = """Program([
	FuncDecl(main, AutoType, [], None, BlockStmt([VarDecl(match, ArrayType([2], BooleanType)), AssignStmt(ArrayCell(match, [IntegerLit(0)]), BinExpr(!=, Id(tonumber), Id(tostring))), AssignStmt(ArrayCell(match, [IntegerLit(1)]), BinExpr(&&, UnExpr(!, BooleanLit(False)), BooleanLit(True))), AssignStmt(Id(a), UnExpr(!, BinExpr(!=, Id(a), UnExpr(!, Id(b)))))]))
	FuncDecl(Function, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 325))                

    def test_26(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            x = 1;
            y = 2;
            z = 3;
            if(x != y) {
                temp = x;
                x = y;
                y = temp;
            }
            return {1,2,3,4} +  (false && false) || true;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([AssignStmt(Id(x), IntegerLit(1)), AssignStmt(Id(y), IntegerLit(2)), AssignStmt(Id(z), IntegerLit(3)), IfStmt(BinExpr(!=, Id(x), Id(y)), BlockStmt([AssignStmt(Id(temp), Id(x)), AssignStmt(Id(x), Id(y)), AssignStmt(Id(y), Id(temp))])), ReturnStmt(BinExpr(||, BinExpr(+, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), BinExpr(&&, BooleanLit(False), BooleanLit(False))), BooleanLit(True)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 326))                

    def test_27(self):
        input = """fact: function integer(a: integer, out c: float) {
            is_check = (n == 0 || false);
            if (n== 0) return 1;
            else return n * fact(n-1, c);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(a, IntegerType), OutParam(c, FloatType)], None, BlockStmt([AssignStmt(Id(is_check), BinExpr(==, Id(n), BinExpr(||, IntegerLit(0), BooleanLit(False)))), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1)), Id(c)]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 327))                

    def test_28(self):
        input = """def: function string(getbyID: array[2] of string) inherit getCurrentValue {
            y = x * 2 + t - 1/2;
            z = y && x + 2 * 5;
            return y || z;
        }"""
        expect = """Program([
	FuncDecl(def, StringType, [Param(getbyID, ArrayType([2], StringType))], getCurrentValue, BlockStmt([AssignStmt(Id(y), BinExpr(-, BinExpr(+, BinExpr(*, Id(x), IntegerLit(2)), Id(t)), BinExpr(/, IntegerLit(1), IntegerLit(2)))), AssignStmt(Id(z), BinExpr(&&, Id(y), BinExpr(+, Id(x), BinExpr(*, IntegerLit(2), IntegerLit(5))))), ReturnStmt(BinExpr(||, Id(y), Id(z)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 328))                

    def test_29(self):
        input = """m: function integer() {
            a: array[10] of integer;
            a = {1 +2, 2/4, 7- 5, 2-3, 3 % a[b[3, 4], 1], {3, 4, 5}, {2,3} * 2, 3};
        }"""
        expect = """Program([
	FuncDecl(m, IntegerType, [], None, BlockStmt([VarDecl(a, ArrayType([10], IntegerType)), AssignStmt(Id(a), ArrayLit([BinExpr(+, IntegerLit(1), IntegerLit(2)), BinExpr(/, IntegerLit(2), IntegerLit(4)), BinExpr(-, IntegerLit(7), IntegerLit(5)), BinExpr(-, IntegerLit(2), IntegerLit(3)), BinExpr(%, IntegerLit(3), ArrayCell(a, [ArrayCell(b, [IntegerLit(3), IntegerLit(4)]), IntegerLit(1)])), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)]), BinExpr(*, ArrayLit([IntegerLit(2), IntegerLit(3)]), IntegerLit(2)), IntegerLit(3)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 329))                

    def test_30(self):
        input = """
        current: boolean = false && true && true || false;
        a,b,c,d: float = .e-1, 1.e14, 8.e15, 6.e16;
        main: function void() {}
        """
        expect = """Program([
	VarDecl(current, BooleanType, BinExpr(||, BinExpr(&&, BinExpr(&&, BooleanLit(False), BooleanLit(True)), BooleanLit(True)), BooleanLit(False)))
	VarDecl(a, FloatType, FloatLit(0.0))
	VarDecl(b, FloatType, FloatLit(100000000000000.0))
	VarDecl(c, FloatType, FloatLit(8000000000000000.0))
	VarDecl(d, FloatType, FloatLit(6e+16))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 330))                

    def test_31(self):
        input = """
        many_to_one: function string() {
            //as, n : string = "q423 \\", "dwaf"::"dwad";
            if (as){
                return true;
            }
        }
        """   
        expect = """Program([
	FuncDecl(many_to_one, StringType, [], None, BlockStmt([IfStmt(Id(as), BlockStmt([ReturnStmt(BooleanLit(True))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 331))                

    def test_32(self):
        input = """
        main: function void() {
            int: integer;
            do{do{}while(false);}while(false);
            readBoolean("true");
            printBoolean(false);
            readString();
            printString("abc", "def");
            super(a + b, c + true, f + "antlr");
            preventDefault();
        }        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(int, IntegerType), DoWhileStmt(BooleanLit(False), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([]))])), CallStmt(readBoolean, StringLit(true)), CallStmt(printBoolean, BooleanLit(False)), CallStmt(readString, ), CallStmt(printString, StringLit(abc), StringLit(def)), CallStmt(super, BinExpr(+, Id(a), Id(b)), BinExpr(+, Id(c), BooleanLit(True)), BinExpr(+, Id(f), StringLit(antlr))), CallStmt(preventDefault, )]))
])"""        
        self.assertTrue(TestAST.test(input, expect, 332))                

    def test_33(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            if (a == 1) return 1; else if (a == 2) return 2; else if (a == 3) return 3; else return "default";
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), ReturnStmt(IntegerLit(3)), ReturnStmt(StringLit(default)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 333))                

    def test_34(self):
        input = """
        is_checked: boolean = true;
        main: function integer(a: integer, inherit is_save: boolean, out c: string, inherit out d: array[5] of integer) inherit newcase {
            a: integer;
            if (true) {
                if (c == "") return 1;
                else if (c == "\\t") {
                    return 2;
                }
                else if (c == "\\n") {
                    return 3;
                }
                else readInteger();
            }
            else printInteger(0);
            return 4;
        }"""
        expect = """Program([
	VarDecl(is_checked, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), InheritParam(is_save, BooleanType), OutParam(c, StringType), InheritOutParam(d, ArrayType([5], IntegerType))], newcase, BlockStmt([VarDecl(a, IntegerType), IfStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(c), StringLit()), ReturnStmt(IntegerLit(1)), IfStmt(BinExpr(==, Id(c), StringLit(\\t)), BlockStmt([ReturnStmt(IntegerLit(2))]), IfStmt(BinExpr(==, Id(c), StringLit(\\n)), BlockStmt([ReturnStmt(IntegerLit(3))]), CallStmt(readInteger, ))))]), CallStmt(printInteger, IntegerLit(0))), ReturnStmt(IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 334))                

    def test_35(self):
        input = """
        is_checked: boolean = true;
        check_func: function void() {
            if (is_checked) {
                a = 5;
                c = 6;
                return 7;
            }
        }
        main: function integer(argv: integer, kwargs: string) {return 0;}"""
        expect = """Program([
	VarDecl(is_checked, BooleanType, BooleanLit(True))
	FuncDecl(check_func, VoidType, [], None, BlockStmt([IfStmt(Id(is_checked), BlockStmt([AssignStmt(Id(a), IntegerLit(5)), AssignStmt(Id(c), IntegerLit(6)), ReturnStmt(IntegerLit(7))]))]))
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 335))                

    def test_36(self):
        input = """
        foo: function boolean() {
            for(ini = 0, i - (-2), {1,2,3,4}) print(i);
        }
        """
        expect = """Program([
	FuncDecl(foo, BooleanType, [], None, BlockStmt([ForStmt(AssignStmt(Id(ini), IntegerLit(0)), BinExpr(-, Id(i), UnExpr(-, IntegerLit(2))), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), CallStmt(print, Id(i)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 336))                

    def test_37(self):
        input = """
        is_prime: function boolean(NumBer: integer){
            if (Number == 2) return true;
            for (i = 2, i < NumBer, i + 1){
                if (Number % i == 0) return false;
            }
        }
        main: function integer(argv: integer, kwargs: string){
            is_prime(1_221);
            return 0;
        }
        """
        expect = """Program([
	FuncDecl(is_prime, BooleanType, [Param(NumBer, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(Number), IntegerLit(2)), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<, Id(i), Id(NumBer)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(Number), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(False)))]))]))
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([CallStmt(is_prime, IntegerLit(1221)), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 337))                

    def test_38(self):
        input = """
        is_divide: function auto(n: integer) {
            result: array[100] of integer;
            index: integer = 0;
            for (i = 1, i < n, i + 1) {
                if(n % i == 0) {
                    arr[index] = i;
                    index = index + 1;
                }
            }
            return result;
        }
        main: function integer(argv: integer, kwargs: string){
            print(is_divide(1_22_1));
            return 0;
        }
        """
        expect = """Program([
	FuncDecl(is_divide, AutoType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(result, ArrayType([100], IntegerType)), VarDecl(index, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(index)]), Id(i)), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1)))]))])), ReturnStmt(Id(result))]))
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([CallStmt(print, FuncCall(is_divide, [IntegerLit(1221)])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 338))                

    def test_39(self):
        input = """main: function integer(argv: integer, kwargs: string){
            is_check = true;
            for (i = 0, is_check && true, i + 2){
                if (i % 2 == 0) print(i, "\\n");
                else if (i == 99) is_check = false;
                else continue;
            }
            return 0;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([AssignStmt(Id(is_check), BooleanLit(True)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(&&, Id(is_check), BooleanLit(True)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), CallStmt(print, Id(i), StringLit(\\n)), IfStmt(BinExpr(==, Id(i), IntegerLit(99)), AssignStmt(Id(is_check), BooleanLit(False)), ContinueStmt()))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 339))                

    def test_40(self):
        input = """
        main: function integer(argv: integer, kwargs: string){
            while (main == true) {
                divide = 1 && true + 2/3;
                subtract: float = 1.e-1;
            }
            print(is_divide(1_22_1));
            return 0;
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(main), BooleanLit(True)), BlockStmt([AssignStmt(Id(divide), BinExpr(&&, IntegerLit(1), BinExpr(+, BooleanLit(True), BinExpr(/, IntegerLit(2), IntegerLit(3))))), VarDecl(subtract, FloatType, FloatLit(0.1))])), CallStmt(print, FuncCall(is_divide, [IntegerLit(1221)])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 340))                

    def test_41(self):
        input = """
        fe2o3 : function integer() inherit augment {
            while (arr[foo()]::arr[1_2,3_4]) {}
        }
        """
        expect = """Program([
	FuncDecl(fe2o3, IntegerType, [], augment, BlockStmt([WhileStmt(BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), ArrayCell(arr, [IntegerLit(12), IntegerLit(34)])), BlockStmt([]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 341))                

    def test_42(self):
        input = """
        main: function void() {
            while (foo(true || false + f0123(12_1) != 12 + 34 + 56 && A))
            {
                continue;
                a = b / c * (d + e);
                break;
            }
        }        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(FuncCall(foo, [BinExpr(!=, BinExpr(||, BooleanLit(True), BinExpr(+, BooleanLit(False), FuncCall(f0123, [IntegerLit(121)]))), BinExpr(&&, BinExpr(+, BinExpr(+, IntegerLit(12), IntegerLit(34)), IntegerLit(56)), Id(A)))]), BlockStmt([ContinueStmt(), AssignStmt(Id(a), BinExpr(*, BinExpr(/, Id(b), Id(c)), BinExpr(+, Id(d), Id(e)))), BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 342))                

    def test_43(self):
        input = """main: function void() {
            do {
                n : integer;
                print("Enter n: ");
                n = readInt();
                printFloat(caclPi(n));
                print("Pi = ");
                print("\\n");
            } while (n != 0);
        }        
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(n), IntegerLit(0)), BlockStmt([VarDecl(n, IntegerType), CallStmt(print, StringLit(Enter n: )), AssignStmt(Id(n), FuncCall(readInt, [])), CallStmt(printFloat, FuncCall(caclPi, [Id(n)])), CallStmt(print, StringLit(Pi = )), CallStmt(print, StringLit(\\n))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 343))                

    def test_44(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            i: integer = 0;
            do {
                i = i + 1;
                print("Hello world");
            }
            while(i < 1);
        }
        mat : array[3,1_2_3_3] of integer = {{1,2,3},{4,5,6},{7,8,9}};
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), DoWhileStmt(BinExpr(<, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), CallStmt(print, StringLit(Hello world))]))]))
	VarDecl(mat, ArrayType([3, 1233], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 344))                

    def test_45(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            i,j : integer = 0, 1;
            do {
                print("Hello world");
            }
            while("23r"::"23432aa");
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(1)), DoWhileStmt(BinExpr(::, StringLit(23r), StringLit(23432aa)), BlockStmt([CallStmt(print, StringLit(Hello world))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 345))                

    def test_46(self):
        input = """main_test_63: function integer(inherit a: integer, out c: string) {
            i,j : integer = 0, 1;
            isCheck, isDivide: boolean = true, false;
            do {
                print("Hello world");
                isCheck = false;
            }
            while(true || isCheck);
        }
        """
        expect = """Program([
	FuncDecl(main_test_63, IntegerType, [InheritParam(a, IntegerType), OutParam(c, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(1)), VarDecl(isCheck, BooleanType, BooleanLit(True)), VarDecl(isDivide, BooleanType, BooleanLit(False)), DoWhileStmt(BinExpr(||, BooleanLit(True), Id(isCheck)), BlockStmt([CallStmt(print, StringLit(Hello world)), AssignStmt(Id(isCheck), BooleanLit(False))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 346))                

    def test_47(self):
        input = """
        main: function void() {
            do {
                continue;
                }
            while (func != 1_2 + 2.3e-1);
            readInteger();
            printInteger(1_2_3 - an);
            readFloat();
            writeFloat(1.e-2, 4.e-5);
        }       
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(!=, Id(func), BinExpr(+, IntegerLit(12), FloatLit(0.23))), BlockStmt([ContinueStmt()])), CallStmt(readInteger, ), CallStmt(printInteger, BinExpr(-, IntegerLit(123), Id(an))), CallStmt(readFloat, ), CallStmt(writeFloat, FloatLit(0.01), FloatLit(4e-05))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 347))                

    def test_48(self):
        input = """
        main: function void() inherit classdiagram{
            if (true && is_check) {
                a = b;
                e = a :: "stmt";
                if (m == n) return 0;
                return FaLsE;
            } else 
                break;
            return;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [], classdiagram, BlockStmt([IfStmt(BinExpr(&&, BooleanLit(True), Id(is_check)), BlockStmt([AssignStmt(Id(a), Id(b)), AssignStmt(Id(e), BinExpr(::, Id(a), StringLit(stmt))), IfStmt(BinExpr(==, Id(m), Id(n)), ReturnStmt(IntegerLit(0))), ReturnStmt(Id(FaLsE))]), BreakStmt()), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 348))                

    def test_49(self):
        input = """
        main: function integer(a: integer, out c: string) {
            if (a == 1) return 1; else if (a == 2) return 2; else if (a == 3) return 3; else return "default";
            for (i = 0, i < 10, i + 1) {
                if(i == 5) break;
            }
            return 0;
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), ReturnStmt(IntegerLit(3)), ReturnStmt(StringLit(default))))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(5)), BreakStmt())])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 349))                

    def test_50(self):
        input = """
        main: function integer(a: integer, inherit out a: array[2,2] of integer){
            while(is_check == false) {
                break;
            }
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), InheritOutParam(a, ArrayType([2, 2], IntegerType))], None, BlockStmt([WhileStmt(BinExpr(==, Id(is_check), BooleanLit(False)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 350))                

    def test_51(self):
        input = """
        main: function void(a: integer, out c: string) inherit newcase {
            break;
            continue;
            break; break;
        }
        """
        expect = """Program([
	FuncDecl(main, VoidType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([BreakStmt(), ContinueStmt(), BreakStmt(), BreakStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 351))                

    def test_52(self):
        input = """
        main: function integer(a: integer, out c: string) {
            if (a == 1) return 1; else if (a == 2) return 2; else if (a == 3) return 3; else return "default";
            for (i = 0, i < 10, i + 1) {
                if(i % 2 == 0) continue;
                print(i, "\\n");
            }
            return 0;
        }
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(IntegerLit(1)), IfStmt(BinExpr(==, Id(a), IntegerLit(2)), ReturnStmt(IntegerLit(2)), IfStmt(BinExpr(==, Id(a), IntegerLit(3)), ReturnStmt(IntegerLit(3)), ReturnStmt(StringLit(default))))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(2)), IntegerLit(0)), ContinueStmt()), CallStmt(print, Id(i), StringLit(\\n))])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 352))                

    def test_53(self):
        input = """
        a: integer;
        /*This is a comment*/
        main: function integer(a: integer, inherit out c: string, out d: float) inherit newcase {
            for(i = 0, true, i + 2){
                if(i == 100) break;
            }
            continue;
        }"""
        expect = """Program([
	VarDecl(a, IntegerType)
	FuncDecl(main, IntegerType, [Param(a, IntegerType), InheritOutParam(c, StringType), OutParam(d, FloatType)], newcase, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BooleanLit(True), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(100)), BreakStmt())])), ContinueStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 353))                

    def test_54(self):
        input = """main: function auto(bool: integer, out c: string) inherit newcase {
            a = !bool  && c;
            return !bool;
            return 12_23;
            return a&&b+c;
            return comma + {1,2,3,{4,5}};
            return arr[2,2];
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [Param(bool, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([AssignStmt(Id(a), BinExpr(&&, UnExpr(!, Id(bool)), Id(c))), ReturnStmt(UnExpr(!, Id(bool))), ReturnStmt(IntegerLit(1223)), ReturnStmt(BinExpr(&&, Id(a), BinExpr(+, Id(b), Id(c)))), ReturnStmt(BinExpr(+, Id(comma), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(4), IntegerLit(5)])]))), ReturnStmt(ArrayCell(arr, [IntegerLit(2), IntegerLit(2)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 354))                

    def test_55(self):
        input = input = """
        fact: function integer (n: integer) {
            if ((n == 0) || (n == 1)) return a;
            else return n * fact(n - 1) * fact(n-2);
        }
        main: function integer(a: integer, out c: string) inherit newcase {
            x: integer = 65;
            return fact(x);
        }"""
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), ReturnStmt(Id(a)), ReturnStmt(BinExpr(*, BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(2))]))))]))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(x, IntegerType, IntegerLit(65)), ReturnStmt(FuncCall(fact, [Id(x)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 355))                

    def test_56(self):
        input = """
        leaf_to_leave: function integer(out c: boolean) {
                return !!!!!12;
        }
        """
        expect = """Program([
	FuncDecl(leaf_to_leave, IntegerType, [OutParam(c, BooleanType)], None, BlockStmt([ReturnStmt(UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, UnExpr(!, IntegerLit(12)))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 356))                

    def test_57(self):
        input = """
        m_t_o: function array[5] of integer() {
            return foo(1_2 + 2 || 4 :: 5);
        }        
        """
        expect = """Program([
	FuncDecl(m_t_o, ArrayType([5], IntegerType), [], None, BlockStmt([ReturnStmt(FuncCall(foo, [BinExpr(::, BinExpr(||, BinExpr(+, IntegerLit(12), IntegerLit(2)), IntegerLit(4)), IntegerLit(5))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 357))                

    def test_58(self):
        input = """ 
        inc: function void(out n: integer) {
            n  = n+ 1;
            return n;
        }"""
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), IntegerLit(1))), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 358))                

    def test_59(self):
        input = """
        is_divide: function array[99] of integer(n: integer) {
            result: array[100] of integer;
            index: integer = 0;
            for (i = 1, i < n, i + 1) {
                if(n % i == 0) {
                    result[index] = i;
                    index = index + 1;
                }
            }
            return result;
        }
        """
        expect = """Program([
	FuncDecl(is_divide, ArrayType([99], IntegerType), [Param(n, IntegerType)], None, BlockStmt([VarDecl(result, ArrayType([100], IntegerType)), VarDecl(index, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(ArrayCell(result, [Id(index)]), Id(i)), AssignStmt(Id(index), BinExpr(+, Id(index), IntegerLit(1)))]))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 359))                

    def test_60(self):
        input = """
        fact: function integer (n: integer) {
            if ((n == 0) || (n == 1)) return a;
            else return n * fact(n - 1) * fact(n-2);
        }
        """
        expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(==, Id(n), IntegerLit(0)), BinExpr(==, Id(n), IntegerLit(1))), ReturnStmt(Id(a)), ReturnStmt(BinExpr(*, BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))])), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(2))]))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 360))                

    def test_61(self):
        input = """
        main: function integer(a: integer, out c: string) inherit newcase {
            /*foo: function string() { 
                for (i = implement(i), str(i), i == 2) 
                    a = a + 1;
            }*/
            // array, void: string = 012, 2b;
            return 0;
        }
        
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 361))                

    def test_62(self):
        input = """main: function integer(a: integer, out c: string) {
            n = {1,2,3}::{1,2,3};
            str1 = "2r323"::"2asf1";
            return str1 || n;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(::, ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))), AssignStmt(Id(str1), BinExpr(::, StringLit(2r323), StringLit(2asf1))), ReturnStmt(BinExpr(||, Id(str1), Id(n)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 362))                

    def test_63(self):
        input = """
        main: function integer(argv: integer, kwargs: string){
            while (main == true) {}
            print(is_divide(1_22_1));
            return 0;
        }        
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(argv, IntegerType), Param(kwargs, StringType)], None, BlockStmt([WhileStmt(BinExpr(==, Id(main), BooleanLit(True)), BlockStmt([])), CallStmt(print, FuncCall(is_divide, [IntegerLit(1221)])), ReturnStmt(IntegerLit(0))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 363))                

    def test_64(self):
        input = """
        a,v: array[1,2,3,4,5] of integer = {1,2,3,4,5}, {1,2,3,4,5};
        main: function integer(a: integer, out c: string) inherit newcase {a: integer;
            return a(v(0));
        }
        """
        expect = """Program([
	VarDecl(a, ArrayType([1, 2, 3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	VarDecl(v, ArrayType([1, 2, 3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, IntegerType), ReturnStmt(FuncCall(a, [FuncCall(v, [IntegerLit(0)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 364))                

    def test_65(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            a: integer;
            printInteger(a(m[1]));
        }
        
        """
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, IntegerType), CallStmt(printInteger, FuncCall(a, [ArrayCell(m, [IntegerLit(1)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 365))                

    def test_66(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {a: integer;
            if( a== 1) return menu[0];
            else return double(double(menu[1]));
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, IntegerType), IfStmt(BinExpr(==, Id(a), IntegerLit(1)), ReturnStmt(ArrayCell(menu, [IntegerLit(0)])), ReturnStmt(FuncCall(double, [FuncCall(double, [ArrayCell(menu, [IntegerLit(1)])])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 366))                

    def test_67(self):
        input = """
        fefef : function integer() {
            do {}
            while ( arr[foo()]::arr[1,2] > 1 + 2 );
            return 1;
        }        
        """
        expect = """Program([
	FuncDecl(fefef, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(::, ArrayCell(arr, [FuncCall(foo, [])]), BinExpr(>, ArrayCell(arr, [IntegerLit(1), IntegerLit(2)]), BinExpr(+, IntegerLit(1), IntegerLit(2)))), BlockStmt([])), ReturnStmt(IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 367))                

    def test_68(self):
        input = """
        m_t_o: function string() {
            a = !-12;
            b = !3;
            c = --2;
            return a(b(c));
        }"""
        expect = """Program([
	FuncDecl(m_t_o, StringType, [], None, BlockStmt([AssignStmt(Id(a), UnExpr(!, UnExpr(-, IntegerLit(12)))), AssignStmt(Id(b), UnExpr(!, IntegerLit(3))), AssignStmt(Id(c), UnExpr(-, UnExpr(-, IntegerLit(2)))), ReturnStmt(FuncCall(a, [FuncCall(b, [Id(c)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 368))                

    def test_69(self):
        input = """main: function auto(bool: integer, out c: string) inherit newcase {
            a = !bool  && c;
            return !bool;
            return a&&b+c;
            return comma + {1,2,3,{4,5}};
        }"""
        expect = """Program([
	FuncDecl(main, AutoType, [Param(bool, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([AssignStmt(Id(a), BinExpr(&&, UnExpr(!, Id(bool)), Id(c))), ReturnStmt(UnExpr(!, Id(bool))), ReturnStmt(BinExpr(&&, Id(a), BinExpr(+, Id(b), Id(c)))), ReturnStmt(BinExpr(+, Id(comma), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), ArrayLit([IntegerLit(4), IntegerLit(5)])])))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 369))                

    def test_70(self):
        input = """
        sigma: boolean = ((abc && true) || false);
        a: float = 23.e2;
        b: string = "asdc_asjd_1";
        c, d: integer = 1_2_3_222_2, f;
        main: function integer(a: integer, out c: string) inherit newcase {a: integer;
            mul = a && b && c;
            return ;
        }"""
        expect = """Program([
	VarDecl(sigma, BooleanType, BinExpr(||, BinExpr(&&, Id(abc), BooleanLit(True)), BooleanLit(False)))
	VarDecl(a, FloatType, FloatLit(2300.0))
	VarDecl(b, StringType, StringLit(asdc_asjd_1))
	VarDecl(c, IntegerType, IntegerLit(1232222))
	VarDecl(d, IntegerType, Id(f))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, IntegerType), AssignStmt(Id(mul), BinExpr(&&, BinExpr(&&, Id(a), Id(b)), Id(c))), ReturnStmt()]))
])"""
        self.assertTrue(TestAST.test(input, expect, 370))                

    def test_71(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {a: integer;
            return main(main());
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([VarDecl(a, IntegerType), ReturnStmt(FuncCall(main, [FuncCall(main, [])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 371))                

    def test_72(self):
        input = """main: function integer(a: integer, out c: string) inherit newcase {
            passFulltest();
            return 10000;
        }"""
        expect = """Program([
	FuncDecl(main, IntegerType, [Param(a, IntegerType), OutParam(c, StringType)], newcase, BlockStmt([CallStmt(passFulltest, ), ReturnStmt(IntegerLit(10000))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 372))                

    def test_73(self):
        input = """
        is_checked: boolean = true;
        main: function integer(a: integer, inherit is_save: boolean, out c: string, inherit out d: array[5] of integer) inherit newcase {
            a: integer;
            if (true) {
                if (c == "") return 1;
                else if (c == "\\t") {
                    return 2;
                }
                else if (c == "\\n") {
                    return 3;
                }
                else readInteger();
            }
            else printInteger(0);
            return 4;
        }"""
        expect = """Program([
	VarDecl(is_checked, BooleanType, BooleanLit(True))
	FuncDecl(main, IntegerType, [Param(a, IntegerType), InheritParam(is_save, BooleanType), OutParam(c, StringType), InheritOutParam(d, ArrayType([5], IntegerType))], newcase, BlockStmt([VarDecl(a, IntegerType), IfStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(==, Id(c), StringLit()), ReturnStmt(IntegerLit(1)), IfStmt(BinExpr(==, Id(c), StringLit(\\t)), BlockStmt([ReturnStmt(IntegerLit(2))]), IfStmt(BinExpr(==, Id(c), StringLit(\\n)), BlockStmt([ReturnStmt(IntegerLit(3))]), CallStmt(readInteger, ))))]), CallStmt(printInteger, IntegerLit(0))), ReturnStmt(IntegerLit(4))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 373))                

    def test_74(self):
        input = """
        int: array[1,2] of integer;
        fl: array[1_2, 22_1] of float;
        bool: array[1,2_0] of boolean;
        str: array[86_9,9] of string;
        f: function array[5] of float() {}      
        """
        expect = """Program([
	VarDecl(int, ArrayType([1, 2], IntegerType))
	VarDecl(fl, ArrayType([12, 221], FloatType))
	VarDecl(bool, ArrayType([1, 20], BooleanType))
	VarDecl(str, ArrayType([869, 9], StringType))
	FuncDecl(f, ArrayType([5], FloatType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 374))                

    def test_75(self):
        input = """
            // Solo Comment, INT
            a, b ,c : integer = 1, 2, 3 ;
            /* multipline comment
            69 = 420 ? 69 : 420;
            */
            b : integer = 1_2; // coment commeeenasdk
            c : integer = 1_2_3;
            d: integer = a[1,2] + 69/69;
            //FLOAT
            _65 : float = 1.23; //_65 is an ID
            y : float = 1.2e3;
            z : auto = 7E-10;
            a : float = 1_5_6.9e123;
            b : float = 1.E-12;
            c : float = .9e3;
            d : auto = .e32;
            e : float = y + 69. - 69.0 * 0.0 / b % 3;
            

            /* STRING*/
            str2 : string = "Multiple line string";
            str3 : string = str1 :: str2;
            x : string = "abc";
            y : string = "ab // cd";
            z : string = " ab /* cd */";
            c : string = " ab unclose";
        """
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(b, IntegerType, IntegerLit(12))
	VarDecl(c, IntegerType, IntegerLit(123))
	VarDecl(d, IntegerType, BinExpr(+, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), BinExpr(/, IntegerLit(69), IntegerLit(69))))
	VarDecl(_65, FloatType, FloatLit(1.23))
	VarDecl(y, FloatType, FloatLit(1200.0))
	VarDecl(z, AutoType, FloatLit(7e-10))
	VarDecl(a, FloatType, FloatLit(1.569e+125))
	VarDecl(b, FloatType, FloatLit(1e-12))
	VarDecl(c, FloatType, FloatLit(900.0))
	VarDecl(d, AutoType, FloatLit(0.0))
	VarDecl(e, FloatType, BinExpr(-, BinExpr(+, Id(y), FloatLit(69.0)), BinExpr(%, BinExpr(/, BinExpr(*, FloatLit(69.0), FloatLit(0.0)), Id(b)), IntegerLit(3))))
	VarDecl(str2, StringType, StringLit(Multiple line string))
	VarDecl(str3, StringType, BinExpr(::, Id(str1), Id(str2)))
	VarDecl(x, StringType, StringLit(abc))
	VarDecl(y, StringType, StringLit(ab // cd))
	VarDecl(z, StringType, StringLit( ab /* cd */))
	VarDecl(c, StringType, StringLit( ab unclose))
])"""
        self.assertTrue(TestAST.test(input, expect, 375))                

    def test_76(self):
        input = """
        truer : boolean = true;
        falser : boolean = false;
        truer_than_truth : boolean = true || false && true;
        _hanser_bronya : boolean = x >= y;
        nestedtruth : auto = (x>=y) != ((y<=x) == (1 < 2));
        /* Array
        Test ? Array is still bug bruh*/
        a : array[2,2] of float;
        a,b,c : array[1,2] of integer = {a[1,1],a[1,2]}, {2,3}, {4,5};
        c : array[1,1] of boolean = {};

        mulfu: function integer (e : integer, f: float){
            return e * f;
        }

        inc: function auto(out n: integer, inherit delta: integer, inherit out hallo: auto) {
            return a[1,2] && b;
        }        
        """
        expect = """Program([
	VarDecl(truer, BooleanType, BooleanLit(True))
	VarDecl(falser, BooleanType, BooleanLit(False))
	VarDecl(truer_than_truth, BooleanType, BinExpr(&&, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)))
	VarDecl(_hanser_bronya, BooleanType, BinExpr(>=, Id(x), Id(y)))
	VarDecl(nestedtruth, AutoType, BinExpr(!=, BinExpr(>=, Id(x), Id(y)), BinExpr(==, BinExpr(<=, Id(y), Id(x)), BinExpr(<, IntegerLit(1), IntegerLit(2)))))
	VarDecl(a, ArrayType([2, 2], FloatType))
	VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])]))
	VarDecl(b, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(2), IntegerLit(3)]))
	VarDecl(c, ArrayType([1, 2], IntegerType), ArrayLit([IntegerLit(4), IntegerLit(5)]))
	VarDecl(c, ArrayType([1, 1], BooleanType), ArrayLit([]))
	FuncDecl(mulfu, IntegerType, [Param(e, IntegerType), Param(f, FloatType)], None, BlockStmt([ReturnStmt(BinExpr(*, Id(e), Id(f)))]))
	FuncDecl(inc, AutoType, [OutParam(n, IntegerType), InheritParam(delta, IntegerType), InheritOutParam(hallo, AutoType)], None, BlockStmt([ReturnStmt(BinExpr(&&, ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 376))                

    def test_77(self):
        input = """
            add: function float(i: float) /*salad
            kabab 
            */{
                return i;
            }
            inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                a[1,2] = b[1,2];
                a[1, a[1,2]] = b[6,9];
                n = n + delta + hallo;
                n = n - delta - hallo;
                n = n * delta * hallo;
                /* multiple
                    line
                    comment
                */
                n = n / delta / hallo;
                n = true;
                n = n % 1 + hallo - 1+2;
                n = n && delta && hallo;
                n = n || delta || hallo;
                n = n :: n;
                n = n + add(delta);
                n = a[1, a[1, a[1,2]]]; // n[1,2] = 2 => n = a[1,2];
                n = (!n > FAsLE(!true)) != (bool == (lean >= bool));
                n = !n && n || n == n || !n;
                return n*a[1,1]+12/foo(12,4);
                return n;
                break;
                continue;
                return;
                return add(1, add(1,2));
            }        
        """
        expect = """Program([
	FuncDecl(add, FloatType, [Param(i, FloatType)], None, BlockStmt([ReturnStmt(Id(i))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), InheritParam(delta, IntegerType), InheritOutParam(hallo, AutoType)], add, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1), IntegerLit(2)]), ArrayCell(b, [IntegerLit(1), IntegerLit(2)])), AssignStmt(ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])]), ArrayCell(b, [IntegerLit(6), IntegerLit(9)])), AssignStmt(Id(n), BinExpr(+, BinExpr(+, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(-, BinExpr(-, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(*, BinExpr(*, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(/, BinExpr(/, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BooleanLit(True)), AssignStmt(Id(n), BinExpr(+, BinExpr(-, BinExpr(+, BinExpr(%, Id(n), IntegerLit(1)), Id(hallo)), IntegerLit(1)), IntegerLit(2))), AssignStmt(Id(n), BinExpr(&&, BinExpr(&&, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(||, BinExpr(||, Id(n), Id(delta)), Id(hallo))), AssignStmt(Id(n), BinExpr(::, Id(n), Id(n))), AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(add, [Id(delta)]))), AssignStmt(Id(n), ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])])])), AssignStmt(Id(n), BinExpr(!=, BinExpr(>, UnExpr(!, Id(n)), FuncCall(FAsLE, [UnExpr(!, BooleanLit(True))])), BinExpr(==, Id(bool), BinExpr(>=, Id(lean), Id(bool))))), AssignStmt(Id(n), BinExpr(==, BinExpr(||, BinExpr(&&, UnExpr(!, Id(n)), Id(n)), Id(n)), BinExpr(||, Id(n), UnExpr(!, Id(n))))), ReturnStmt(BinExpr(+, BinExpr(*, Id(n), ArrayCell(a, [IntegerLit(1), IntegerLit(1)])), BinExpr(/, IntegerLit(12), FuncCall(foo, [IntegerLit(12), IntegerLit(4)])))), ReturnStmt(Id(n)), BreakStmt(), ContinueStmt(), ReturnStmt(), ReturnStmt(FuncCall(add, [IntegerLit(1), FuncCall(add, [IntegerLit(1), IntegerLit(2)])]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 377))                

    def test_78(self):
        input = """
            inc: function void(out n: integer, inherit delta: integer, inherit out hallo: auto) inherit add{
                if (!true) return true;
                else return false;
                for( i = 0, i < 10, i + 1)
                    if (i > 0) continue;
                    else break;
                while (true)
                    return a[1, a[1,2]] == b[6,9];
                do{
                    n = n + add(delta);
                    readInteger();
                    printInteger(1_23 - 12);
                    readFloat();
                    writeFloat(1.e+10 * 1.2);
                    readBoolean();
                    printBoolean(!n);
                    readString();
                    printString("hello" :: "world!");
                    super(a, b, c);
                    preventDefault();
                } while (a != b);
                return n; 
            }       
        """
        expect = """Program([
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), InheritParam(delta, IntegerType), InheritOutParam(hallo, AutoType)], add, BlockStmt([IfStmt(UnExpr(!, BooleanLit(True)), ReturnStmt(BooleanLit(True)), ReturnStmt(BooleanLit(False))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(>, Id(i), IntegerLit(0)), ContinueStmt(), BreakStmt())), WhileStmt(BooleanLit(True), ReturnStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), ArrayCell(a, [IntegerLit(1), IntegerLit(2)])]), ArrayCell(b, [IntegerLit(6), IntegerLit(9)])))), DoWhileStmt(BinExpr(!=, Id(a), Id(b)), BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), FuncCall(add, [Id(delta)]))), CallStmt(readInteger, ), CallStmt(printInteger, BinExpr(-, IntegerLit(123), IntegerLit(12))), CallStmt(readFloat, ), CallStmt(writeFloat, BinExpr(*, FloatLit(10000000000.0), FloatLit(1.2))), CallStmt(readBoolean, ), CallStmt(printBoolean, UnExpr(!, Id(n))), CallStmt(readString, ), CallStmt(printString, BinExpr(::, StringLit(hello), StringLit(world!))), CallStmt(super, Id(a), Id(b), Id(c)), CallStmt(preventDefault, )])), ReturnStmt(Id(n))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 378))                

    def test_79(self):
        input = """"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 379))                

    def test_80(self):
        input = """"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 380))                

    def test_81(self):
        input = """"""
        expect = """Program([
	
])"""
        self.assertTrue(TestAST.test(input, expect, 381))                



