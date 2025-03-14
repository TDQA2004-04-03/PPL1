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
        expect = """var,str3,=,Unclosed string: "QuocAnh;"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,24))

    def test_lexer_25(self):
        input = """var str4 = "Quoc\Anh";"""
        expect = """var,str4,=,Illegal escape in string: "Quoc\A"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,25))

    def test_lexer_26(self):
        input = """var str4 = "Bayern"Munich";"""
        expect = """var,str4,=,"Bayern",Munich,Unclosed string: ";"""
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
            real int
            imag int
        };"""
        expect = """type,Complex,struct,{,real,int,;,imag,int,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,47))

    def test_lexer_48(self):
        input = """type Whatever struct {
            arr [5] float
            side Complex
        };"""
        expect = """type,Whatever,struct,{,arr,[,5,],float,;,side,Complex,;,},;,<EOF>"""
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
        };"""
        expect = """type,Number,interface,{,getValue,(,),int,;,sum,(,y,Number,),Number,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,60))

    def test_lexer_61(self):
        input = """type Calculator interface{
            multiply(x, y int) int
            divide(x float, y float) float
            try(x, y int, z float)
        };"""
        expect = """type,Calculator,interface,{,multiply,(,x,,,y,int,),int,;,divide,(,x,float,,,y,float,),float,;,try,(,x,,,y,int,,,z,float,),;,},;,<EOF>"""
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
        };"""
        expect = """func,assign,(,x,int,),{,x,:=,1,;,x,*=,2,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,64))

    def test_lexer_65(self):
        input = """func pi() float{
            return 3.14;
        };"""
        expect = """func,pi,(,),float,{,return,3.14,;,},;,<EOF>"""
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
            return abs(p.y)
        };"""
        expect = """func,(,p,Point,),DistToOx,(,),int,{,return,abs,(,p,.,y,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,70))

    def test_lexer_71(self):
        input = """func (l List) first() Person {
            l.access += 1
            return list[0]
        };"""
        expect = """func,(,l,List,),first,(,),Person,{,l,.,access,+=,1,;,return,list,[,0,],;,},;,<EOF>"""
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
        };"""
        expect = """if,(,a,>,5,),{,b,:=,a,+,5,;,c,:=,b,*,3,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,84))

    def test_lexer_85(self):
        input = """if (age > 18) {
            putStringLn("You are an adult");
        } else {
            putStringLn("You are a kid");
        };"""
        expect = """if,(,age,>,18,),{,putStringLn,(,"You are an adult",),;,},else,{,putStringLn,(,"You are a kid",),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,85))

    def test_lexer_86(self):
        input = """if (a > 0.0) {
            putStringLn("Positive");
        } else if (a < 0.0) {
            putStringLn("Negative");
        } else {
            putStringLn("Zero");
        };"""
        expect = """if,(,a,>,0.0,),{,putStringLn,(,"Positive",),;,},else,if,(,a,<,0.0,),{,putStringLn,(,"Negative",),;,},else,{,putStringLn,(,"Zero",),;,},;,<EOF>"""
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
        expect = """if,(,a,==,0.0,),{,if,(,b,==,0.0,),{,putStringLn,(,"Infinite solution",),;,},else,{,putStringLn,(,"No solution",),;,},;,},else,{,x,:=,-,b,/,a,;,putStringLn,(,"Solution is ",+,x,),;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,87))

    def test_lexer_88(self):
        input = """if a > b {
            c := 5
        };"""
        expect = """if,a,>,b,{,c,:=,5,;,},;,<EOF>"""
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
        expect = """for,i,<,20,{,putIntLn,(,i,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,91))

    def test_lexer_92(self):
        input = """for i := 1; i < 20; i += 1 {
            putIntLn(i)   
        }
        """
        expect = """for,i,:=,1,;,i,<,20,;,i,+=,1,{,putIntLn,(,i,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,92))

    def test_lexer_93(self):
        input = """for index, value := range lst {
            s += value   
        }
        """
        expect = """for,index,,,value,:=,range,lst,{,s,+=,value,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,93))

    def test_lexer_94(self):
        input = """for _, val := range arr {
            s *= value + 2;   
        }
        """
        expect = """for,_,,,val,:=,range,arr,{,s,*=,value,+,2,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,94))

    def test_lexer_95(self):
        input = """for _, val := range arr {
            if (val % 5 == 0) {
                break
            }   
        }
        """
        expect = """for,_,,,val,:=,range,arr,{,if,(,val,%,5,==,0,),{,break,;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,95))

    def test_lexer_96(self):
        input = """for _, val := range arr {
            if ((2 * val + 3) % 7 == 4) {
                continue
            }   
        }
        """
        expect = """for,_,,,val,:=,range,arr,{,if,(,(,2,*,val,+,3,),%,7,==,4,),{,continue,;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,96))

    def test_lexer_97(self):
        input = """for _, _ := range arr {
            a := 3   
        }
        """
        expect = """for,_,,,_,:=,range,arr,{,a,:=,3,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,97))

    def test_lexer_98(self):
        input = """for _, val := range arr
            s += val;
        """
        expect = """for,_,,,val,:=,range,arr,s,+=,val,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,98))

    def test_lexer_99(self):
        input = """do_something(2 + x, y * 5);"""
        expect = """do_something,(,2,+,x,,,y,*,5,),;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,99))

    def test_lexer_100(self):
        input = """do_something("Hello, World", ",")"""
        expect = """do_something,(,"Hello, World",,,",",),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,100))

    def test_lexer_program_1(self):
        input = """func main() {
            putStringLn("Hello, World!")
        };"""
        expect = """func,main,(,),{,putStringLn,(,"Hello, World!",),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,101))
    
    def test_lexer_program_2(self):
        input = """func main() {
            var userName
            userName := "user"
            putStringLn(userName)
        };"""
        expect = """func,main,(,),{,var,userName,;,userName,:=,"user",;,putStringLn,(,userName,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,102))

    def test_lexer_program_3(self):
        input = """x := 2
        func main() {
            x = 3
            putInt(x)
        }
        """
        expect = """x,:=,2,;,func,main,(,),{,x,=,3,putInt,(,x,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,103))

    def test_lexer_program_4(self):
        input = """func main() {
            var x float = 13.5
            var y float = 2.5e+4
        }
        """
        expect = """func,main,(,),{,var,x,float,=,13.5,;,var,y,float,=,2.5e+4,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,104))

    def test_lexer_program_5(self):
        input = """func main() {
                    x := -3
                    // Assign negative value to x
                    putInt(x)
                }
        """
        expect = """func,main,(,),{,x,:=,-,3,;,putInt,(,x,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,105))

    def test_lexer_program_6(self):
        input = """func main() {
            const x = 2
            const y = 3
            var someVar = x + y
        }
        """
        expect = """func,main,(,),{,const,x,=,2,;,const,y,=,3,;,var,someVar,=,x,+,y,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,106))

    def test_lexer_program_7(self):
        input = """func main() {
            const X := 2
            putIntLn(X)
        }
        """
        expect = """func,main,(,),{,const,X,:=,2,;,putIntLn,(,X,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,107))

    def test_lexer_program_8(self):
        input = """func main() {
            x := 2017
            putBoolLn(x > 2022 && x <= 3000)
            putBool(x >= 2000 && x < 3000)              
        }
        """
        expect = """func,main,(,),{,x,:=,2017,;,putBoolLn,(,x,>,2022,&&,x,<=,3000,),;,putBool,(,x,>=,2000,&&,x,<,3000,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,108))

    def test_lexer_program_9(self):
        input = """func main() {
            x := true        

            putBoolLn(x)
            putBoolLn(!x)
            putBoolLn(!x && x)
            putBoolLn(!x || x)                   
        }
        """
        expect = """func,main,(,),{,x,:=,true,;,putBoolLn,(,x,),;,putBoolLn,(,!,x,),;,putBoolLn,(,!,x,&&,x,),;,putBoolLn,(,!,x,||,x,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,109))

    def test_lexer_program_10(self):
        input = """func main() {
            x := 3
            if (x > 0) {
                x := 5
        }
        """        
        expect = """func,main,(,),{,x,:=,3,;,if,(,x,>,0,),{,x,:=,5,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,110))

    def test_lexer_program_11(self):
        input = """func main() {
            var x int = randInt(100)
            if (x > 10) {
                putIntLn("yay!")
            } else {
                putIntln("nay!")
            }        
        }
        """        
        expect = """func,main,(,),{,var,x,int,=,randInt,(,100,),;,if,(,x,>,10,),{,putIntLn,(,"yay!",),;,},else,{,putIntln,(,"nay!",),;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,111))

    def test_lexer_program_12(self):
        input = """func main() {
            sum := 0
            for var i int = 0; i < 50; i += 1 {
                sum += i
            }
            putInt(sum)
        }
        """
        expect = """func,main,(,),{,sum,:=,0,;,for,var,i,int,=,0,;,i,<,50,;,i,+=,1,{,sum,+=,i,;,},;,putInt,(,sum,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,112))

    def test_lexer_program_13(self):
        input = """func main() {
            var x [4]int
            x[2] := 4
        }
        """
        expect = """func,main,(,),{,var,x,[,4,],int,;,x,[,2,],:=,4,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,113))

    def test_lexer_program_14(self):
        input = """func main() {
            x := 2
            var y [x]
        }
        """
        expect = """func,main,(,),{,x,:=,2,;,var,y,[,x,],;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,114))

    def test_lexer_program_15(self):
        input = """func main() {
            for {
                putStringLn("forever!")
            }        
        }
        """
        expect = """func,main,(,),{,for,{,putStringLn,(,"forever!",),;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,115))

    def test_lexer_program_16(self):
        input = """const OvenTime = 40;
        const TimeLayer = 2;
        func RemainingTime(time int) int {
            return OvenTime - time;
        };
        func PreparationTime(numberOfLayers int) int {
            return TimeLayer * numberOfLayers;
        };
        func main() {
            elapsedTime := RemainingTime(20) + PreparationTime(2);
            putInt(elapsedTime);
        };
        """
        expect = """const,OvenTime,=,40,;,const,TimeLayer,=,2,;,func,RemainingTime,(,time,int,),int,{,return,OvenTime,-,time,;,},;,func,PreparationTime,(,numberOfLayers,int,),int,{,return,TimeLayer,*,numberOfLayers,;,},;,func,main,(,),{,elapsedTime,:=,RemainingTime,(,20,),+,PreparationTime,(,2,),;,putInt,(,elapsedTime,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,116))

    def test_lexer_program_17(self):
        input = """func main() {
            var knightIsAwake = false;
            var archerIsAwake = true;
            var prisonerIsAwake = false;
            var petDogIsPresent = false;
            var canRescue = !archerIsAwake && (petDogIsPresent || (!knightIsAwake && prisonerIsAwake));
            putBoolLn(canRescue);
        };
        """
        expect = """func,main,(,),{,var,knightIsAwake,=,false,;,var,archerIsAwake,=,true,;,var,prisonerIsAwake,=,false,;,var,petDogIsPresent,=,false,;,var,canRescue,=,!,archerIsAwake,&&,(,petDogIsPresent,||,(,!,knightIsAwake,&&,prisonerIsAwake,),),;,putBoolLn,(,canRescue,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,117))

    def test_lexer_program_18(self):
        input = """func collatz_step(n int) int {
            count = 0;
            for n != 1 {
                if (n % 2 == 0) {
                    n /= 2;
                } else {
                    n := 3 * n + 1;
                };
                count += 1;
            };
            return count;
        };
        """
        expect = """func,collatz_step,(,n,int,),int,{,count,=,0,;,for,n,!=,1,{,if,(,n,%,2,==,0,),{,n,/=,2,;,},else,{,n,:=,3,*,n,+,1,;,},;,count,+=,1,;,},;,return,count,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,118))

    def test_lexer_program_19(self):
        input = """type Complex struct {
            real float;
            imaginary float;
        };
        func (x Complex) Add(y Complex) Complex {
            add_real := x.real + y.real;
            add_imag := x.imaginary + y.imaginary;
            return Complex{real: add_real, imaginary: add_imag};
        };
        func main() {
            x := Complex{real: 5.0e0, imaginary: 4.0e0};
            y := Complex{real: 4.3e0, imaginary: 2.9e0};
            z := x.Add(y);
            PutFloatLn(z.real);
            PutFloatLn(z.imaginary);
        };
        """
        expect = """type,Complex,struct,{,real,float,;,imaginary,float,;,},;,func,(,x,Complex,),Add,(,y,Complex,),Complex,{,add_real,:=,x,.,real,+,y,.,real,;,add_imag,:=,x,.,imaginary,+,y,.,imaginary,;,return,Complex,{,real,:,add_real,,,imaginary,:,add_imag,},;,},;,func,main,(,),{,x,:=,Complex,{,real,:,5.0e0,,,imaginary,:,4.0e0,},;,y,:=,Complex,{,real,:,4.3e0,,,imaginary,:,2.9e0,},;,z,:=,x,.,Add,(,y,),;,PutFloatLn,(,z,.,real,),;,PutFloatLn,(,z,.,imaginary,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,119))

    def test_lexer_program_20(self):
        input = """putString("Hello,);
        a := 5;"""
        expect = """putString,(,Unclosed string: "Hello,);"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,120))

    def test_lexer_program_21(self):
        input = """var int x, m, n;
                m := 10; 
                n := 15;"""
        expect = """var,int,x,,,m,,,n,;,m,:=,10,;,n,:=,15,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,121))

    def test_lexer_program_22(self):
        input = """func main () 
        {
            s := 0;
        };"""
        expect = """func,main,(,),;,{,s,:=,0,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,122))

    def test_lexer_program_23(self):
        input = """func main () {
            var s int = 0;
            for s < 10 {
                if (s > 5 && s < 10) {
                    continue;
                };
            };
        };"""
        expect = """func,main,(,),{,var,s,int,=,0,;,for,s,<,10,{,if,(,s,>,5,&&,s,<,10,),{,continue,;,},;,},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,123))

    def test_lexer_program_24(self):
        input = """arr := {1, 2+2};"""
        expect = """arr,:=,{,1,,,2,+,2,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,124))

    def test_lexer_program_25(self):
        input = """const pi = 3.14;
        func area(r float) float {
            return pi * r * r;
        };"""
        expect = """const,pi,=,3.14,;,func,area,(,r,float,),float,{,return,pi,*,r,*,r,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,125))

    def test_lexer_program_26(self):
        input = """const VAL = (157 + 2.35) * 4.62 / 35.28;"""
        expect = """const,VAL,=,(,157,+,2.35,),*,4.62,/,35.28,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,126))

    def test_lexer_program_27(self):
        input = """
            var a [20]int
            a[2+5] := 8
        """
        expect = """var,a,[,20,],int,;,a,[,2,+,5,],:=,8,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,127))

    def test_lexer_program_28(self):
        input = """var a int = nil;"""
        expect = """var,a,int,=,nil,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,128))

    def test_lexer_program_29(self):
        input = """type Class struct { name string; grade float; }
        func (c Class) print() {
            putStringLn(name);
            putFloatLn(grade);
        }
        """
        expect = """type,Class,struct,{,name,string,;,grade,float,;,},;,func,(,c,Class,),print,(,),{,putStringLn,(,name,),;,putFloatLn,(,grade,),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,129))

    def test_lexer_program_30(self):
        input = """func mul(a, b int) int {
            return a * b;
        };
        """
        expect = """func,mul,(,a,,,b,int,),int,{,return,a,*,b,;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,130))

    def test_lexer_program_31(self):
        input = """func fibonacci(a int) int {};"""
        expect = """func,fibonacci,(,a,int,),int,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,131))

    def test_lexer_program_32(self):
        input = """var a [4]int = [2]int {2,3} + [2]int {5,7};"""
        expect = """var,a,[,4,],int,=,[,2,],int,{,2,,,3,},+,[,2,],int,{,5,,,7,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,132))

    def test_lexer_program_33(self):
        input = """type Complex struct {
            a string;
            b [2]float;
            c Whatever;
        }
        func main() {
            c := Complex{a: "new_number", b: [2]int {14,2}, c: Whatever{line: "Now"}};
        }
        """
        expect = """type,Complex,struct,{,a,string,;,b,[,2,],float,;,c,Whatever,;,},;,func,main,(,),{,c,:=,Complex,{,a,:,"new_number",,,b,:,[,2,],int,{,14,,,2,},,,c,:,Whatever,{,line,:,"Now",},},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,133))

    def test_parser_program_34(self):
        input = """func main() {
            arr := [2][2][2] int {{{1,2}, {3, 4}}, {{5,6}, {7,8}}};
        };
        """
        expect = """func,main,(,),{,arr,:=,[,2,],[,2,],[,2,],int,{,{,{,1,,,2,},,,{,3,,,4,},},,,{,{,5,,,6,},,,{,7,,,8,},},},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,134))

    def test_parser_program_35(self):
        input = """func main() {
            result := (true || a) && !b && (c > 2.5))
        };
        """
        expect = """func,main,(,),{,result,:=,(,true,||,a,),&&,!,b,&&,(,c,>,2.5,),),;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,135))

    def test_lexer_program_36(self):
        input = """func main() {
            result := [2] Person {Person{id: 1}, Person{id: 5}};
        };
        """
        expect = """func,main,(,),{,result,:=,[,2,],Person,{,Person,{,id,:,1,},,,Person,{,id,:,5,},},;,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,136))
