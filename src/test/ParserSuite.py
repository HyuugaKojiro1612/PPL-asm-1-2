import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test201(self):
        input = """ main: function void() {arr[2,2] = true;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
        
    def test202(self):
        input = """ main : function void(){ if (a == 1 || b == 2 && c == 3 && !(a== 5)) return 1;} """
        expect = """Error on line 1 col 41: =="""
        self.assertTrue(TestParser.test(input, expect, 202))
        
    def test203(self):
        input = """ a, b, c: integer;
                    d: string;
                    flag: boolean;
                    arr: array[5,"abc"];"""
        expect = "Error on line 4 col 33: abc"
        self.assertTrue(TestParser.test(input, expect, 203))
        
    def test204(self):
        input = """ a, b, c: integer;
                    d: string;
                    flag: boolean;
                    arr: array[5,2];"""
        expect = "Error on line 4 col 35: ;"
        self.assertTrue(TestParser.test(input, expect, 204))
        
    def test205(self):
        input = """ a, b, c: integer;
                    d: string;
                    flag: boolean;
                    arr: array[5,2] of float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
        
    def test206(self):
        input = """ main: function void() {arr[] = true;}"""
        expect = "Error on line 1 col 28: ]"
        self.assertTrue(TestParser.test(input, expect, 206))
        
    def test207(self):
        input = """ main: function void() {i == 2;}"""
        expect = "Error on line 1 col 26: =="
        self.assertTrue(TestParser.test(input, expect, 207))
        
    def test208(self):
        input = """ main : function void(){ if (a == 1 && !(a == 5)) return .2;} """
        expect = """Error on line 1 col 57: ."""
        self.assertTrue(TestParser.test(input, expect, 208))
        
    def test209(self):
        input = """a,: integer = 1;"""
        expect = """Error on line 1 col 2: :"""
        self.assertTrue(TestParser.test(input, expect, 209))
        
    def test210(self):
        input = """ main: function void() {
                        if (a == true && b != 2 || c > 0) {}
                        return 0;
                    }"""
        expect = """Error on line 2 col 43: !="""
        self.assertTrue(TestParser.test(input, expect, 210))    
        
    def test211(self):
        input = """main: function void(){while(a == 0 && b != false || c > -5) {print();}}"""
        expect = """Error on line 1 col 40: !="""
        self.assertTrue(TestParser.test(input, expect, 211))
        
    def test212(self):
        input = """ main: function void() {
                        if (a == true && b) {}
                        return 0;
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 212))
        
    def test213(self):
        input = """ main: function void() {
                        if (a == true && b) {return 0;}
                        eles return 1;
                    }"""
        expect = """Error on line 3 col 29: return"""
        self.assertTrue(TestParser.test(input, expect, 213))
        
    def test214(self):
        input = """ main: function void() {
                        if (a == true && b) {return 0;}
                        else return 1;
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 214))
        
    def test215(self):
        input = """ main: function void (){
                        for(i = 1, i < 4, i + 1) {
                        
                        };
                    } """
        expect = """Error on line 4 col 25: ;"""
        self.assertTrue(TestParser.test(input, expect, 215))
        
    def test216(self):
        input = """ main: function void (){
                        for(i = 1, i < 4, i + 1) {
                            while(str1::str2::str3);
                        };
                    } """
        expect = """Error on line 3 col 44: ::"""
        self.assertTrue(TestParser.test(input, expect, 216))
        
    def test217(self):
        input = """ main: function void (){
                        for(i = 1, i < 4, i + 1) {
                            while(str1::str2 != true * 3);
                        };
                    } """
        expect = """Error on line 4 col 25: ;"""
        self.assertTrue(TestParser.test(input, expect, 217))
        
    def test218(self):
        input = """ main: function void (){
                        for(i = 1, i < 4, i + 1) {
                            while(str1::str2 != true * 3);
                        }
                    } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 218))
        
    def test219(self):
        input = """ x : array [2,2] of float ;
                    continue; """
        expect = """Error on line 2 col 20: continue"""
        self.assertTrue(TestParser.test(input, expect, 219))
        
    def test220(self):
        input = """ x : array [2,2] of float ;
                    while () continue; """
        expect = """Error on line 2 col 20: while"""
        self.assertTrue(TestParser.test(input, expect, 220))
        
    def test221(self):
        input = """ x : array [2,2] of float ;
                    {while () continue;} """
        expect = """Error on line 2 col 20: {"""
        self.assertTrue(TestParser.test(input, expect, 221))
        
    def test222(self):
        input = """ x : array [2,2] of float ;
                    y : auto = "Hello World!" """
        expect = """Error on line 2 col 46: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 222))
        
    def test223(self):
        input = """ x : array [2,2] of float ;
                    y : auto = "Hello World!"; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test224(self):
        input = """ a, b : integer = "" :: 2, true && false; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test225(self):
        input = """ a, b : integer = "" :: 2, true && false, .e; """
        expect = """Error on line 1 col 40: ,"""
        self.assertTrue(TestParser.test(input, expect, 225))
    
    def test226(self):
        input = """ a, b : integer = "" :: 2, true && .e; """
        expect = """Error on line 1 col 35: ."""
        self.assertTrue(TestParser.test(input, expect, 226))
    
    def test227(self):
        input = """ a, b : integer = "" :: 2, true && .e2; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 227))
        
    def test228(self):
        input = """ a, b, x : integer = "" :: 2, true && .e2; """
        expect = """Error on line 1 col 41: ;"""
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test229(self):
        input = """ a, b, x : integer = "" :: 2, true && .e2, k; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 229))
        
    def test230(self):
        input = """ a, b, c: integer;
                    d: string;
                    flag: boolean;
                    arr: array[5,"abc"];
                    main: function integer(a: integer, out c: string) inherit newcase {a: integer;}"""
        expect = "Error on line 4 col 33: abc"""
        self.assertTrue(TestParser.test(input, expect, 230))    
        
    def test231(self):
        input = """main: function integer(inherit out x: integer, out inherit str: string) inherit foo {y: float;}"""
        expect = """Error on line 1 col 51: inherit"""
        self.assertTrue(TestParser.test(input, expect, 231))
    
    def test232(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 232))         
        
    def test233(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a + 2;
                    }"""
        expect = """Error on line 3 col 26: +"""
        self.assertTrue(TestParser.test(input, expect, 233))  
    
    def test234(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a += 2;
                    }"""
        expect = """Error on line 3 col 26: +"""
        self.assertTrue(TestParser.test(input, expect, 234))
        
    def test235(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a = a + 2;
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test236(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a = a + 2;
                        for (,,) a--;
                    }"""
        expect = """Error on line 4 col 29: ,"""
        self.assertTrue(TestParser.test(input, expect, 236))        
        
    def test237(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a = a + 2;
                        for (i : integer = 2, i < 10, i + 1) a--;
                    }"""
        expect = """Error on line 4 col 31: :"""
        self.assertTrue(TestParser.test(input, expect, 237))  
        
    def test238(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a = a + 2;
                        for (i = 2, i < 10, i + 1) a--;
                    }"""
        expect = """Error on line 4 col 52: -"""
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test239(self):
        input = """ main: function integer(x: integer, out str: string) inherit foo {
                        a: integer;
                        a = a + 2;
                        for (i = 2, i < 10, i + 1) a = a - 2 :: str;
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 239))  
        
    def test240(self):
        input = """ x == 1 + 2; """
        expect = """Error on line 1 col 3: =="""
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test241(self):
        input = """ x : bool == 1 + 2; """
        expect = """Error on line 1 col 5: bool"""
        self.assertTrue(TestParser.test(input, expect, 241))
        
    def test242(self):
        input = """ x : boolean == true + false :: 3; """
        expect = """Error on line 1 col 13: =="""
        self.assertTrue(TestParser.test(input, expect, 242))
        
    def test243(self):
        input = """ x : boolean = true + false :: 3; """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 243))
        
    def test244(self):
        input = """ x : boolean = true + false :: 3; 
                    return x;"""
        expect = """Error on line 2 col 20: return"""
        self.assertTrue(TestParser.test(input, expect, 244))
        
    def test245(self):
        input = """ func: function integer() {
                        for (i = 1, i < 10, i :: foo(8 )) {
                            a = ---a;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        
    def test246(self):
        input = """ func: function integer() {
                        for (i = 1, i < 10, i :: foo(8 )) {
                            return a >= ---a;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        
    def test247(self):
        input = """ func: function integer() {
                        for (i = 1, i < 10, i :: foo(8 )) {
                            do continue; while (true);
                            return a >= ---a;
                        }
                    } """
        expect = "Error on line 3 col 31: continue"
        self.assertTrue(TestParser.test(input, expect, 247))
        
    def test248(self):
        input = """ func: function integer() {
                        for (i = 1, i < 10, i :: foo(8 )) {
                            do {continue;} while (true);
                            return a >= ---a;
                        }
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))
        
    def test249(self):
        input = """ func: function integer() {
                        a=---a--a---a;
                    } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))
    
    def test250(self):
        input = """ func: function integer() {
                    for (i = 1, i < 10, i :: -2 :: 3E-10) {
                        a = ---a;
                    }
                } """
        expect = "Error on line 2 col 48: ::"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    def test251(self):
        input = """ main: function void () {
                __a__ : integer = arr[2][3];
            } """
        expect = """Error on line 2 col 40: ["""
        self.assertTrue(TestParser.test(input, expect, 251))
    
    def test252(self):
        input = """ main: function void () {
                __a__ : integer = arr[2,3,];
            } """
        expect = """Error on line 2 col 42: ]"""
        self.assertTrue(TestParser.test(input, expect, 252))
        
    def test253(self):
        input = """ main: function void () {
                __a__ : integer = arr[2,3,4];
            } """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 253))
        
    def test254(self):
        input = """ main: function void () {
                        __a__ : integer = arr[2,3,4];
                    }
                    main: function void () {
                        a : auto [10] of integer;
                    }    """
        expect = """Error on line 5 col 33: ["""
        self.assertTrue(TestParser.test(input, expect, 254))
        
    def test255(self):
        input = """ main: function void () {
                        __a__ : integer = arr[2,3,4];
                    }
                    main: function void () {
                        a : array [10] of integer;
                    }    """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 255))
        
    def test256(self):
        input = """ main: function void () {
                        __a__ : integer = arr[2,3,4];
                    }
                    main: function void () {
                        a : array [10] of integer;
                    }    
                    a : array [10] of integer = {{}}"""
        expect = """Error on line 7 col 52: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 256))
        
    def test257(self):
        input = """ main: function void () {
                        __a__ : integer = arr[2,3,4];
                    }
                    main: function void () {
                        a : array [10] of integer;
                    }    
                    a : array [10] of integer = {{}};"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 257))
        
    def test258(self):
        input = """ main: function void () {
                        __a__ : integer = arr[2,3,4];
                    }
                    main: function void () {
                        a : array [10] of integer;
                    }    
                    if a : array [10] of integer = {{}};"""
        expect = """Error on line 7 col 20: if"""
        self.assertTrue(TestParser.test(input, expect, 258))
        
    def test259(self):
        input = """ main: function void () {
                        a : array [10] of integer;
                    }    
                    a : array [10] of intege;
                    a = {};"""
        expect = """Error on line 4 col 38: intege"""
        self.assertTrue(TestParser.test(input, expect, 259))
        
    def test260(self):
        input = """ m: function integer() {
                        a: array[10] of integer;
                        a = {1 + 2, 2 / 4, 3 % 2, {3, 4, 5}};
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))
        
    def test261(self):
        input = """ main: function integer() {
                        a: array[10] of integer;
                     = {1 + 2, 2 / 4, 3 % 2, {3, 4, 5}};
                    }"""
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 261))
        
    def test262(self):
        input = """ main: function void() {
                        a: array[10] of integer
                     = {1 + 2, 2 / 4, 3 % 2, {3, 4, 5}};
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
        
    def test263(self):
        input = """ main: function void() {
                        a: array[10] of integer
                     = {foo(1, str, foo2())};
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))
    
    def test264(self):
        input = """ {a : integer = 1;} """
        expect = """Error on line 1 col 1: {"""
        self.assertTrue(TestParser.test(input, expect, 264))
        
    def test265(self):
        input = """ if (a = 1) a == 2; """
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.test(input, expect, 265))
        
    def test266(self):
        input = """ if (a = 1) a == 2; """
        expect = "Error on line 1 col 1: if"
        self.assertTrue(TestParser.test(input, expect, 266))
        
    def test267(self):
        input = """ main: function void (n: string) {       
                        if (a == 1) a == 2;
                    }"""
        expect = "Error on line 2 col 38: =="
        self.assertTrue(TestParser.test(input, expect, 267))
        
    def test268(self):
        input = """ main: function void (n: string) {       
                        if (a == 1) b = a == 2;
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 268))
        
    def test269(self):
        input = """ main: function void (n: string) {       
                        if (a == 1) b = a == 2;
                        {
                            y = foo(2) + 3 * 8;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 269))
        
    def test270(self):
        input = """ main: function void (n: string) {       
                        while(x == 1 || x != 5) y = true;
                    }"""
        expect = "Error on line 2 col 42: !="
        self.assertTrue(TestParser.test(input, expect, 270))
        
    def test271(self):
        input = """ main: function void (n: string) {       
                        while(x == 1 || 5) y = true;
                        return foo("bye");
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 271))
        
    def test272(self):
        input = """ main: function void (n: string) {       
                        while(x == 1 || 5);
                        return foo("bye");
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 272))
        
    def test273(self):
        input = """ main: function void (n: string) {       
                        while();
                        return foo("bye");
                    }"""
        expect = "Error on line 2 col 30: )"
        self.assertTrue(TestParser.test(input, expect, 273))
        
    def test274(self):
        input = """ main: function void (n: string = "abc") {       
                        while();
                        return foo("bye");
                    }"""
        expect = "Error on line 1 col 32: ="
        self.assertTrue(TestParser.test(input, expect, 274))
        
    def test275(self):
        input = """ main: function void (out n: integer) {       
                        while(true);
                        return foo(2 :: n + 1 % 3);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 275))
        
    def test276(self):
        input = """ main: function void (out n: integer) {       
                        while(true);
                        return foo(2 :: n + 1 % 3);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 276))
        
    def test277(self):
        input = """ main: function void (out n: integer) {       
                        while(true);
                        return foo(2 :: n + 1 % 3);
                        do {i = i + 1} while (a < b);
                    }"""
        expect = "Error on line 4 col 37: }"
        self.assertTrue(TestParser.test(input, expect, 277))
        
    def test278(self):
        input = """ main: function void (out n: integer) {       
                        while(true);
                        return foo(2 :: n + 1 % 3);
                        do {i * 2 % 3 = n;} while (a < b);
                    }"""
        expect = "Error on line 4 col 30: *"
        self.assertTrue(TestParser.test(input, expect, 278))
        
    def test279(self):
        input = """ main: function void (out n: integer) {       
                        while(true);
                        return foo(2 :: n + 1 % 3);
                        do {i = 3 % n;} while (a < b);
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))
    
    def test280(self):
        input = """ main: function void() {
                        num: integer = 1;
                        for (i = 0, i < n, i + 1) {
                            for (j = 0, j < n, j + 1) {
                                if (arr[i][j] != true) {
                                    num = 0;
                                    break;
                                }
                            }
                            if (ctr == 0) continue;
                        }
                    }"""
        expect = "Error on line 5 col 42: ["
        self.assertTrue(TestParser.test(input, expect, 280))
        
    def test281(self):
        input = """ main: function void() {
                        num: integer = 1;
                        for (i = 0, i < n, i + 1) {
                            for (j = 0, j < n, j + 1) {
                                if (arr[i, j] != true) {
                                    num = 0;
                                    break;
                                }
                            }
                            if (ctr == 0) continue;
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))    
        
    def test282(self):
        input = """ main: function void() {
                        num: integer = 1;
                        for (i = 0, i < n, i + 1) {
                            if (ctr == 0) continue;
                            else {
                                while (a <= b * c[2]);
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282)) 
        
    def test283(self):
        input = """ main: function void() {
                        num: integer = 1;
                        for (i = 0, i < n, i + 1) {
                            if (ctr == 0) {
                                foo(a == 2);
                            }
                            else {
                                while (a <= b * c[2]);
                            }
                        }
                    }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283)) 
        
    def test284(self):
        input = """ main: function void() {
                        num: integer = 1;
                        for (i = 0, i < n, i + 1) {
                            if (ctr == 0) {
                                foo(a = 2);
                            }
                            else {
                                while (a <= b * c[2]);
                            }
                        }
                    }"""
        expect = "Error on line 5 col 38: ="
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test285(self):
        input = """ main: function void () {
                        a : array [10] of integer;
                    }    
                    a : array [10] of integer;
                    a = {};"""
        expect = """Error on line 5 col 22: ="""
        self.assertTrue(TestParser.test(input, expect, 285))
        
    def test286(self):
        input = """ """
        expect = """Error on line 1 col 1: <EOF>"""
        self.assertTrue(TestParser.test(input, expect, 286))
        
    def test287(self):
        input = """ main: function void () {
                        a : array [10] of integer;
                        a = {};
                    }    
                    """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 287))
        
    def test288(self):
        input = """ main: function void () {
                        a : array [10] of integer;
                        a = {}};
                    }    
                    """
        expect = """Error on line 3 col 30: }"""
        self.assertTrue(TestParser.test(input, expect, 288))
    
    def test289(self):
        input = """ main: function void () {out a : integer = 2}    
                    """
        expect = """Error on line 1 col 25: out"""
        self.assertTrue(TestParser.test(input, expect, 289))
        
    def test290(self):
        input = """ main: function void (out a : integer = 2) {}    
                    """
        expect = """Error on line 1 col 38: ="""
        self.assertTrue(TestParser.test(input, expect, 290))
        
    def test291(self):
        input = """ main: function void (out a, b : integer) {}"""
        expect = """Error on line 1 col 27: ,"""
        self.assertTrue(TestParser.test(input, expect, 291))
    
    def test292(self):
        input = """ main: function void (out b : integer) {}"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 292))
        
    def test293(self):
        input = """arr : integer = [1,2,3];"""
        expect = """Error on line 1 col 16: ["""
        self.assertTrue(TestParser.test(input, expect, 293))
    
    def test294(self):
        input = """ main: function void() {
                        arr: array [1,2,3] of float;
                        arr[1,1,1] = 0;
                        return arr[1,1,1];
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 294))
    

    def test295(self):
        input = """ main: function void() {
                        arr: array [3] of integer = {1,2,3};
                        for (i = 0; i < 3; i+1) {
                            if (arr[i] == 1) {
                                arr[i] = 0;
                            } else arr[i] = 1;
                        }
                    }"""
        expect = """Error on line 3 col 34: ;"""
        self.assertTrue(TestParser.test(input, expect, 295))
    
    def test296(self):
        input = """ main: function void() {
                        arr: array [3] of integer = {1,2,3};
                        for (i = 0, i < 3, i=i+1) {
                            if (arr[i] == 1) {
                                arr[i] = 0
                            } else arr[i] = 1;
                        }
                    }"""
        expect = """Error on line 3 col 44: ="""
        self.assertTrue(TestParser.test(input, expect, 296))
    
    def test297(self):
        input = """ main: function void() {
                        arr: array [3] ofinteger = {1,2,3};
                        for (i = 0, i < 3, i+1) {
                            if (arr[i] == 1) {
                                arr[i] = 0
                            } else arr[i] = 1;
                        }
                    }"""
        expect = """Error on line 2 col 39: ofinteger"""
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test298(self):
        input = """ main: function void() {
                        arr: array [3] of integer = {1,2,3};
                        for (i = 0, i < 3, i+1) {
                            if (arr[i] == 1) {
                                arr[i] = 0
                            } else arr[i] = 1;
                        }
                    }"""
        expect = """Error on line 6 col 28: }"""
        self.assertTrue(TestParser.test(input, expect, 298))
        
    def test299(self):
        input = """ main: function void() {
                        arr: array [3] of integer = {1,2,3};
                        for (i = 0, i < 3, i+1) {
                            if (arr[i] == 1) {
                                arr[i] = 0;
                            } else arr[i] = 1;
                        }
                    }"""
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 299))
        
    def test300(self):
        input = """
                main: function void(inherit out a : integer, b : float) inherit a{
                    for(i = 2, i < 5, i + 1){
                        for(j =0, j < 5 , j + 1){
                            print(x)
                        }
                    }
                }
            """
        expect = """successful"""
        self.assertTrue(TestParser.test(input, expect, 300))
        
    # def test_short_vardecl(self):
    #     """Test short variable declaration"""
    #     input = """delta: integer = 3;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 301))

    # def test_full_vardecl(self):
    #     """Test full variable declaration"""
    #     input = """a, b, c: integer = 3, 4, 6;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 302))

    # def test_wrong_full_vardecl(self):
    #     """Test wrong full variable declaration"""
    #     input = """a, b, c, d: integer = 3, 4, 6;"""
    #     expect = "Error on line 1 col 29: ;"
    #     self.assertTrue(TestParser.test(input, expect, 303))

    # def test_simple_program(self):
    #     """Test simple program"""
    #     input = """main: function void () {}"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 304))

    # def test_full_program(self):
    #     """Test full program"""
    #     input = """x: integer = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #     main: function void() {
    #         delta: integer = fact(3);
    #         inc(x, delta);
    #         printInteger(x);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 305))
        