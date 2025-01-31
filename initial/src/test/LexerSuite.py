import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lexer_1(self):
        input = "var x int;"
        expect = "var,x,int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,1))

    def test_lexer_2(self):
        input = "var y string;"
        expect = "var,y,string,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,2))

    def test_lexer_3(self):
        input = "var abc&def string;"
        expect = "var,abc,ErrorToken &"
        self.assertTrue(TestLexer.checkLexeme(input,expect,3))

    def test_lexer_4(self):
        input = "var 12abc int;"
        expect = "var,12,abc,int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,4))

    def test_lexer_5(self):
        input = "var float;"
        expect = "var,float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,5))

    def test_lexer_6(self):
        input = "var int float;"
        expect = "var,int,float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,6))
    
    def test_lexer_7(self):
        input = "var a boolean"
        expect = "var,a,boolean,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,7))

    def test_lexer_8(self):
        input = "var a = 12;"
        expect = "var,a,=,12,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,8))

    def test_lexer_9(self):
        input = "var b int = 0;"
        expect = "var,b,int,=,0,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,9))

    def test_lexer_10(self):
        input = "var c = 0123;"
        expect = "var,c,=,0,123,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,10))

    def test_lexer_11(self):
        input = "var d int = 0b1101101;"
        expect = "var,d,int,=,0b1101101,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,11))

    def test_lexer_12(self):
        input = "var d int = 0b110112101;"
        expect = "var,d,int,=,0b11011,2101,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,12))

    def test_lexer_13(self):
        input = "var e = 0O1234765;"
        expect = "var,e,=,0O1234765,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,13))

    def test_lexer_14(self):
        input = "var e = 0o2348765;"
        expect = "var,e,=,0o234,8765,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,14))

    def test_lexer_15(self):
        input = "var f int = 0x12BDf5A;"
        expect = "var,f,int,=,0x12BDf5A,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,15))

    def test_lexer_16(self):
        input = "var f int = 0x12BDG5A;"
        expect = "var,f,int,=,0x12BD,G5A,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,16))

    def test_lexer_17(self):
        input = "var g = 0.69;"
        expect = "var,g,=,0.69,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,17))

    def test_lexer_18(self):
        input = "var h = 13.;"
        expect = "var,h,=,13.,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,18))

    def test_lexer_19(self):
        input = "var i = 0.314e+1;"
        expect = "var,i,=,0.314e+1,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,19))

    def test_lexer_20(self):
        input = "var i = 1e;"
        expect = "var,i,=,1,e,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,20))

    def test_lexer_21(self):
        input = "var i = 1e3;"
        expect = "var,i,=,1,e3,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,21))

    def test_lexer_22(self):
        input = """var str1 = "abcdef";"""
        expect = """var,str1,=,"abcdef",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,22))

    def test_lexer_23(self):
        input = """var str2 = "abc\ndefgh";"""
        expect = """var,str2,=,"abc\n\ndefgh",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,23))

    def test_lexer_24(self):
        input = """var str3 = "QuocAnh;"""
        expect = """var,str3,=,Unclosed string: QuocAnh;"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,24))

    def test_lexer_25(self):
        input = """var str4 = "Quoc\Anh;"""
        expect = """var,str4,=,Illegal escape in string: Quoc\\"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,25))

    def test_lexer_26(self):
        input = """var str4 = "Bayern"Munich";"""
        expect = """var,str4,=,"Bayern",Munich,Unclosed string: ;"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,26))

    def test_lexer_27(self):
        input = """var check boolean = false;"""
        expect = """var,check,boolean,=,false,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,27))

    def test_lexer_28(self):
        input = """var a = 1; //Assign 1 to a"""
        expect = """var,a,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,28))

    def test_lexer_29(self):
        input = """var e = 2.78; /*Assign value 2.78 
        to e*/"""
        expect = """var,e,=,2.78,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,29))

    def test_lexer_30(self):
        input = """var pi = 3.14; /*Assign value /* float 3.14 */ 
        to /* variable identified as */ pi */"""
        expect = """var,pi,=,3.14,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,30))

    def test_lexer_31(self):
        input = """var pi = 3.14; /*Assign value"""
        expect = """var,pi,=,3.14,;,/,*,Assign,value,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,31))

    def test_lexer_32(self):
        input = """const pi = 3.14;"""
        expect = """const,pi,=,3.14,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,32))

    def test_lexer_33(self):
        input = """const e;"""
        expect = """const,e,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,33))

    def test_lexer_34(self):
        input = """m := 5;"""
        expect = """m,:=,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,34))

    def test_lexer_35(self):
        input = """x *= 10;"""
        expect = """x,*=,10,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,35))

    def test_lexer_36(self):
        input = """var a [3] int;"""
        expect = """var,a,[,3,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,36))
    
    def test_lexer_37(self):
        input = """var a [0.5] int;"""
        expect = """var,a,[,0.5,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,37))

    def test_lexer_38(self):
        input = """var m [5][5][5] int;"""
        expect = """var,m,[,5,],[,5,],[,5,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,38))

    def test_lexer_39(self):
        input = """var a [2 int;"""
        expect = """var,a,[,2,int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,39))

    def test_lexer_40(self):
        input = """var a [3] int = {1,2,3};"""
        expect = """var,a,[,3,],int,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,40))

    def test_lexer_41(self):
        input = """var a [2][3] int = { {1,2,3}, {4,5,6}};"""
        expect = """var,a,[,2,],[,3,],int,=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,41))

    def test_lexer_42(self):
        input = """var a [3] int = {1 2,3};"""
        expect = """var,a,[,3,],int,=,{,1,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,42))

    def test_lexer_43(self):
        input = """var a [3] int = {1,2,3,};"""
        expect = """var,a,[,3,],int,=,{,1,,,2,,,3,,,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,43))

    def test_lexer_44(self):
        input = """m[2] := 8;"""
        expect = """m,[,2,],:=,8,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,44))

    def test_lexer_45(self):
        input = """O[2][3] := {1,3};"""
        expect = """O,[,2,],[,3,],:=,{,1,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,45))

    def test_lexer_46(self):
        input = """m[] := "abc";"""
        expect = """m,[,],:=,"abc",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,46))

    def test_lexer_47(self):
        input = """type Complex struct {
            real int;
            imag int;
        }"""
        expect = """type,Complex,struct,{,real,int,;,imag,int,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,47))

    def test_lexer_48(self):
        input = """type Whatever struct {
            arr [5] float;
            side Complex;
        }"""
        expect = """type,Whatever,struct,{,arr,[,5,],float,;,side,Complex,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,48))

    def test_lexer_49(self):
        input = """a := Complex{real: 2, imag: 3};"""
        expect = """a,:=,Complex,{,real,:,2,,,imag,:,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,49))

    def test_lexer_50(self):
        input = """l := Line{Point1: Point{x: 1.2, y: 2.5}, Point2: Point{x: 3.4, y: 7.5}};"""
        expect = """l,:=,Line,{,Point1,:,Point,{,x,:,1.2,,,y,:,2.5,},,,Point2,:,Point,{,x,:,3.4,,,y,:,7.5,},},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,50))

    def test_lexer_51(self):
        input = """c := Choice{l: {1,2,3,4}, max: 5};"""
        expect = """c,:=,Choice,{,l,:,{,1,,,2,,,3,,,4,},,,max,:,5,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,51))

    def test_lexer_52(self):
        input = """p := Person{};"""
        expect = """p,:=,Person,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,52))

    def test_lexer_53(self):
        input = """p := Person{height: 1.75, weight:};"""
        expect = """p,:=,Person,{,height,:,1.75,,,weight,:,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,53))

    def test_lexer_54(self):
        input = """p.name := "John";"""
        expect = """p,.,name,:=,"John",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,54))

    def test_lexer_55(self):
        input = """l.point1.x := 2.5;"""
        expect = """l,.,point1,.,x,:=,2.5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,55))

    def test_lexer_56(self):
        input = """var myClass [50]Student;"""
        expect = """var,myClass,[,50,],Student,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,56))

    def test_lexer_57(self):
        input = """myClass[21].name := "Harry";"""
        expect = """myClass,[,21,],.,name,:=,"Harry",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,57))

    def test_lexer_58(self):
        input = """myClass.name[11] := "Kid";"""
        expect = """myClass,.,name,[,11,],:=,"Kid",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,58))

    def test_lexer_59(self):
        input = """myClass.name[20].fname := "Kaitou Kid";"""
        expect = """myClass,.,name,[,20,],.,fname,:=,"Kaitou Kid",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,59))

    def test_lexer_60(self):
        input = """type Number interface{
            getValue() int;
            sum(y Number) Number
        }"""
        expect = """type,Number,interface,{,getValue,(,),int,;,sum,(,y,Number,),Number,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,60))

    def test_lexer_61(self):
        input = """type Calculator interface{
            multiply(x, y int) int
            divide(x float, y float) float
            try(x, y int, z float)
        }"""
        expect = """type,Calculator,interface,{,multiply,(,x,,,y,int,),int,;,divide,(,x,float,,,y,float,),float,;,try,(,x,,,y,int,,,z,float,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,61))

    def test_lexer_62(self):
        input = """type Number interface{
            sum(x);
        }"""
        expect = """type,Number,interface,{,sum,(,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,62))

    def test_lexer_63(self):
        input = """type Number interface{
            sum(x, y int,,z float) float;
        }"""
        expect = """type,Number,interface,{,sum,(,x,,,y,int,,,,,z,float,),float,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,63))

    def test_lexer_64(self):
        input = """func assign(x int){
            x := 1
            x *= 2
        }"""
        expect = """func,assign,(,x,int,),{,x,:=,1,;,x,*=,2,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,64))

    def test_lexer_65(self):
        input = """func pi() float{
            return 3.14;
        }"""
        expect = """func,pi,(,),float,{,return,3.14,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,65))
    
    def test_lexer_66(self):
        input = """func euler() float{
            return 2.78;
        """
        expect = """func,euler,(,),float,{,return,2.78,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,66))

    def test_lexer_67(self):
        input = """result := Fibonacci(5);"""
        expect = """result,:=,Fibonacci,(,5,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,67))

    def test_lexer_68(self):
        input = """putStringLn("Hello, World");"""
        expect = """putStringLn,(,"Hello, World",),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,68))

    def test_lexer_69(self):
        input = """putStringLn("Hello, World";"""
        expect = """putStringLn,(,"Hello, World",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,69))


    def test_lexer_70(self):
        input = """func (p Point) DistToOx() int {
            return abs(p.y);
        }"""
        expect = """func,(,p,Point,),DistToOx,(,),int,{,return,abs,(,p,.,y,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,70))

    def test_lexer_71(self):
        input = """func (l List) first() Person {
            l.access += 1
            return list[0]
        }"""
        expect = """func,(,l,List,),first,(,),Person,{,l,.,access,+=,1,;,return,list,[,0,],;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,71))

    def test_lexer_72(self):
        input = """result := calculator.calculate();"""
        expect = """result,:=,calculator,.,calculate,(,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,72))

    def test_lexer_73(self):
        input = """height := class.list[n].toFeet();"""
        expect = """height,:=,class,.,list,[,n,],.,toFeet,(,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,73))

    def test_lexer_74(self):
        input = """a := 2 + 3 * 5;"""
        expect = """a,:=,2,+,3,*,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,74))

    def test_lexer_75(self):
        input = """result := a[5] / point.x;"""
        expect = """result,:=,a,[,5,],/,point,.,x,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,75))

    def test_lexer_76(self):
        input = """x1 := (-b + sqrt(delta)) / (2.0 * a);"""
        expect = """x1,:=,(,-,b,+,sqrt,(,delta,),),/,(,2.0,*,a,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,76))

    def test_lexer_77(self):
        input = """m := 2.15 - 3) * 4.78;"""
        expect = """m,:=,2.15,-,3,),*,4.78,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,77))

    def test_lexer_78(self):
        input = """output := "Hello, " + "World";"""
        expect = """output,:=,"Hello, ",+,"World",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,78))

    def test_lexer_79(self):
        input = """output := "My" + c.method1("Name");"""
        expect = """output,:=,"My",+,c,.,method1,(,"Name",),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,79))

    def test_lexer_80(self):
        input = """result := 2 * a + 5 >= 3 * b - 7;"""
        expect = """result,:=,2,*,a,+,5,>=,3,*,b,-,7,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,80))

    def test_lexer_81(self):
        input = """result := (a != b) && (b == c || d == e);"""
        expect = """result,:=,(,a,!=,b,),&&,(,b,==,c,||,d,==,e,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,81))
    
    def test_lexer_82(self):
        input = """a[5][6] += b[2][4][8];"""
        expect = """a,[,5,],[,6,],+=,b,[,2,],[,4,],[,8,],;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,82))

    def test_lexer_83(self):
        input = """p.name := getString();"""
        expect = """p,.,name,:=,getString,(,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,83))

    def test_lexer_84(self):
        input = """if (a > 5) {
            b := a + 5
            c := b * 3
        }"""
        expect = """if,(,a,>,5,),{,b,:=,a,+,5,;,c,:=,b,*,3,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,84))

    def test_lexer_85(self):
        input = """if (age > 18) {
            putStringLn("You are an adult");
        } else {
            putStringLn("You are a kid");
        }"""
        expect = """if,(,age,>,18,),{,putStringLn,(,"You are an adult",),;,},else,{,putStringLn,(,"You are a kid",),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,85))

    def test_lexer_86(self):
        input = """if (a > 0.0) {
            putStringLn("Positive");
        } else if (a < 0.0) {
            putStringLn("Negative");
        } else {
            putStringLn("Zero");
        }"""
        expect = """if,(,a,>,0.0,),{,putStringLn,(,"Positive",),;,},else,if,(,a,<,0.0,),{,putStringLn,(,"Negative",),;,},else,{,putStringLn,(,"Zero",),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,86))

    def test_lexer_87(self):
        input = """if (a == 0.0) {
            if (b == 0.0) {
                putStringLn("Infinite solution")
            } else {
                putStringLn("No solution")
            }
        } else {
            x := -b / a
            putStringLn("Solution is " + x)
        }"""
        expect = """if,(,a,==,0.0,),{,if,(,b,==,0.0,),{,putStringLn,(,"Infinite solution",),;,},else,{,putStringLn,(,"No solution",),;,},},else,{,x,:=,-,b,/,a,;,putStringLn,(,"Solution is ",+,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,87))

    def test_lexer_88(self):
        input = """if a > b {
            c := 5
        }"""
        expect = """if,a,>,b,{,c,:=,5,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,88))

    def test_lexer_89(self):
        input = """if (a > b)
            c := 5
        """
        expect = """if,(,a,>,b,),c,:=,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,89))

    def test_lexer_90(self):
        input = """if (a > b) {
            c := 5
        """
        expect = """if,(,a,>,b,),{,c,:=,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,90))

    def test_lexer_91(self):
        input = """for i < 20 {
            putIntLn(i)   
        }
        """
        expect = """for,i,<,20,{,putIntLn,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,91))

    def test_lexer_92(self):
        input = """for i := 1; i < 20; i += 1 {
            putIntLn(i)   
        }
        """
        expect = """for,i,:=,1,;,i,<,20,;,i,+=,1,{,putIntLn,(,i,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,92))