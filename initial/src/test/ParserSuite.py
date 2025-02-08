import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_parser_1(self):
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1001))

    def test_parser_2(self):
        input = """var y string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1002))

    def test_parser_3(self):
        input = "var abc&def string;"
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,1003))

    def test_parser_4(self):
        input = "var 12abc int;"
        expect = "Error on line 1 col 5: 12"
        self.assertTrue(TestParser.checkParser(input,expect,1004))

    def test_parser_5(self):
        input = """var float;"""
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input,expect,1005))

    def test_parser_6(self):
        input = """var int float;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,1006))

    def test_parser_7(self):
        input = """var a boolean"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,1007))

    def test_parser_8(self):
        input = "var a = 12;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1008))

    def test_parser_9(self):
        input = "var b int = 0;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1009))

    def test_parser_10(self):
        input = "var c = 0123;"
        expect = "Error on line 1 col 10: 123"
        self.assertTrue(TestParser.checkParser(input,expect,1010))

    def test_parser_11(self):
        input = "var d int = 0b1101101;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1011))

    def test_parser_12(self):
        input = "var d int = 0b110112101;"
        expect = "Error on line 1 col 20: 2101"
        self.assertTrue(TestParser.checkParser(input,expect,1012))

    def test_parser_13(self):
        input = "var e = 0O234765;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1013))

    def test_parser_14(self):
        input = "var e = 0o2348765;"
        expect = "Error on line 1 col 14: 8765"
        self.assertTrue(TestParser.checkParser(input,expect,1014))

    def test_parser_15(self):
        input = "var f int = 0x12BDf5A;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1015))

    def test_parser_16(self):
        input = "var f int = 0x12BDG5A;"
        expect = "Error on line 1 col 19: G5A"
        self.assertTrue(TestParser.checkParser(input,expect,1016))

    def test_parser_17(self):
        input = "var g = 0.69;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1017))

    def test_parser_18(self):
        input = "var h = 13.;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1018))

    def test_parser_19(self):
        input = "var i = 0.314e+1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1019))

    def test_parser_20(self):
        input = "var i = 1e;"
        expect = "Error on line 1 col 10: e"
        self.assertTrue(TestParser.checkParser(input,expect,1020))

    def test_parser_21(self):
        input = "var i = 1e3;"
        expect = "Error on line 1 col 10: e3"
        self.assertTrue(TestParser.checkParser(input,expect,1021))

    def test_parser_22(self):
        input = """var str1 = "abcdef";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1022))

    def test_parser_23(self):
        input = """var str2 = "abc\ndefgh";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1023))

    def test_parser_24(self):
        input = """var str3 = "QuocAnh;"""
        expect = """QuocAnh;"""
        self.assertTrue(TestParser.checkParser(input,expect,1024))

    def test_parser_25(self):
        input = """var str4 = "Quoc\Anh;"""
        expect = """Quoc\\"""
        self.assertTrue(TestParser.checkParser(input,expect,1025))

    def test_parser_26(self):
        input = """var str4 = "Quoc"Anh;"""
        expect = """Error on line 1 col 18: Anh"""
        self.assertTrue(TestParser.checkParser(input,expect,1026))

    def test_parser_27(self):
        input = """var check boolean = false;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1027))

    def test_parser_28(self):
        input = """var a = 1; //Assign 1 to a"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1028))

    def test_parser_29(self):
        input = """var e = 2.78; /*Assign value 2.78 
        to e*/"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1029))

    def test_parser_30(self):
        input = """var pi = 3.14; /*Assign value /* float 3.14 */ 
        to /* variable identified as */ pi */"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1030))

    def test_parser_31(self):
        input = """var pi = 3.14; /*Assign value"""
        expect = """Error on line 1 col 16: /"""
        self.assertTrue(TestParser.checkParser(input,expect,1031))

    def test_parser_32(self):
        input = """const pi = 3.14;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1032))

    def test_parser_33(self):
        input = """const e;"""
        expect = """Error on line 1 col 8: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,1033))

    def test_parser_34(self):
        input = """m := 5;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1034))

    def test_parser_35(self):
        input = """x *= 10;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1035))

    def test_parser_36(self):
        input = """var a [3] int;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1036))

    def test_parser_37(self):
        input = """var a [0.5] int;"""
        expect = """Error on line 1 col 8: 0.5"""
        self.assertTrue(TestParser.checkParser(input,expect,1037))

    def test_parser_38(self):
        input = """var m [5][5][5] int;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1038))

    def test_parser_39(self):
        input = """var a [2 int;"""
        expect = """Error on line 1 col 10: int"""
        self.assertTrue(TestParser.checkParser(input,expect,1039))

    def test_parser_40(self):
        input = """var a [3]int = {1,2,3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1040))

    def test_parser_41(self):
        input = """var a [2][3]int = {{1,2,3}, {4,5,6}};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1041))

    def test_parser_42(self):
        input = """var a [3] int = {1 2,3};"""
        expect = """Error on line 1 col 20: 2"""
        self.assertTrue(TestParser.checkParser(input,expect,1042))

    def test_parser_43(self):
        input = """var a [3] int = {1,2,3,};"""
        expect = """Error on line 1 col 24: }"""
        self.assertTrue(TestParser.checkParser(input,expect,1043))

    def test_parser_44(self):
        input = """m[2] := 8;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1044))

    def test_parser_45(self):
        input = """O[2][3] := {1,3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1045))

    def test_parser_46(self):
        input = """m[] := "abc";"""
        expect = """Error on line 1 col 3: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,1046))


    def test_parser_47(self):
        input = """type Complex struct {
            real int
            imag int
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1047))

    def test_parser_48(self):
        input = """type Whatever struct {
            arr [5] float
            side Complex
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1048))

    def test_parser_49(self):
        input = """a := Complex{real: 2, imag: 3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1049))

    def test_parser_50(self):
        input = """l := Line{Point1: Point{x: 1.2, y: 2.5}, Point2: Point{x: 3.4, y: 7.5}};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1050))

    def test_parser_51(self):
        input = """c := Choice{l: {1,2,3,4}, max: 5};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1051))

    def test_parser_52(self):
        input = """p := Person{};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1052))

    def test_parser_53(self):
        input = """p := Person{height: 1.75, weight:};"""
        expect = """Error on line 1 col 34: }"""
        self.assertTrue(TestParser.checkParser(input,expect,1053))

    def test_parser_54(self):
        input = """p.name := "John";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1054))

    def test_parser_55(self):
        input = """l.point1.x := 2.5;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1055))
    
    def test_parser_56(self):
        input = """var myClass [50]Student;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1056))

    def test_parser_57(self):
        input = """myClass[21].name := "Harry";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1057))

    def test_parser_58(self):
        input = """myClass.name[11] := "Kid";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1058))

    def test_parser_59(self):
        input = """myClass.name[20].fname := "Kaitou Kid";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1059))

    def test_parser_60(self):
        input = """type Number interface{
            getValue() int;
            sum(y Number) Number
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1060))

    def test_parser_61(self):
        input = """type Calculator interface{
            multiply(x, y int) int
            divide(x float, y float) float
            try(x, y int, z float)
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1061))

    def test_parser_62(self):
        input = """type Number interface{
            sum(x);
        };"""
        expect = """Error on line 2 col 18: )"""
        self.assertTrue(TestParser.checkParser(input,expect,1062))

    def test_parser_63(self):
        input = """type Number interface{
            sum(x, y int,,z float) float;
        };"""
        expect = """Error on line 2 col 26: ,"""
        self.assertTrue(TestParser.checkParser(input,expect,1063))

    def test_parser_64(self):
        input = """func assign(x int){
            x := 1
            x *= 2
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1064))

    def test_parser_65(self):
        input = """func pi() float{
            return 3.14;
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1065))

    def test_parser_66(self):
        input = """func euler() float{
            return 2.78;"""
        expect = """Error on line 2 col 25: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,1066))

    def test_parser_67(self):
        input = """result := Fibonacci(5);"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1067))

    def test_parser_68(self):
        input = """putStringLn("Hello, World");"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1068))

    def test_parser_69(self):
        input = """putStringLn("Hello, World";"""
        expect = """Error on line 1 col 27: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,1069))

    def test_parser_70(self):
        input = """func (p Point) DistToOx() int {
            return abs(p.y);
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1070))

    def test_parser_71(self):
        input = """func (l List) first() Person {
            l.access += 1
            return list[0]
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1071))

    def test_parser_72(self):
        input = """result := calculator.calculate();"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1072))

    def test_parser_73(self):
        input = """height := class.list[n].toFeet();"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1073))

    def test_parser_74(self):
        input = """a := 2 + 3 * 5;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1074))

    def test_parser_75(self):
        input = """result := a[5] / point.x;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1075))

    def test_parser_76(self):
        input = """x1 := (-b + sqrt(delta)) / (2.0 * a);"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1076))

    def test_parser_77(self):
        input = """m := 2.15 - 3) * 4.78;"""
        expect = """Error on line 1 col 14: )"""
        self.assertTrue(TestParser.checkParser(input,expect,1077))

    def test_parser_78(self):
        input = """output := "Hello, " + "World";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1078))

    def test_parser_79(self):
        input = """output := "My" + c.method1("Name");"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1079))

    def test_parser_80(self):
        input = """result := 2 * a + 5 >= 3 * b - 7;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1080))

    def test_parser_81(self):
        input = """result := a != b && (b == c || d == e);"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1081))

    def test_parser_82(self):
        input = """a[5][6] += b[2][4][8];"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1082))

    def test_parser_83(self):
        input = """p.name := getString();"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1083))

    def test_parser_84(self):
        input = """if (a > 5) {
            b := a + 5
            c := b * 3
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1084))

    def test_parser_85(self):
        input = """if (age > 18) {
            putStringLn("You are an adult");
        } else {
            putStringLn("You are a kid");
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1085))

    def test_parser_86(self):
        input = """if (a > 0.0) {
            putStringLn("Positive");
        } else if (a < 0.0) {
            putStringLn("Negative");
        } else {
            putStringLn("Zero");
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1086))

    def test_parser_87(self):
        input = """if (a == 0.0) {
            if (b == 0.0) {
                putStringLn("Infinite solution")
            } else {
                putStringLn("No solution")
            }
        } else {
            x := -b / a
            putStringLn("Solution is " + x)
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1087))

    def test_parser_88(self):
        input = """if a > b {
            c := 5
        }"""
        expect = """Error on line 1 col 4: a"""
        self.assertTrue(TestParser.checkParser(input,expect,1088))

    def test_parser_89(self):
        input = """if (a > b)
            c := 5
        """
        expect = """Error on line 2 col 13: c"""
        self.assertTrue(TestParser.checkParser(input,expect,1089))

    def test_parser_90(self):
        input = """if (a > b) {
            c := 5"""
        expect = """Error on line 2 col 19: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,1090))

    def test_parser_91(self):
        input = """for i < 20 {
            putIntLn(i)   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1091))

    def test_parser_92(self):
        input = """for i := 1; i < 20; i += 1 {
            putIntLn(i)   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1092))

    def test_parser_93(self):
        input = """for index, value := range lst {
            s += value   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1093))

    def test_parser_94(self):
        input = """for _, val := range arr {
            s *= value + 2;   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1094))

    def test_parser_95(self):
        input = """for _, val := range arr {
            if (val % 5 == 0) {
                break
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1095))

    def test_parser_96(self):
        input = """for _, val := range arr {
            if ((2 * val + 3) % 7 == 4) {
                continue
            }   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1096))

    def test_parser_97(self):
        input = """for _, _ := range arr {
            a := 3   
        }
        """
        expect = """Error on line 1 col 8: _"""
        self.assertTrue(TestParser.checkParser(input,expect,1097))

    def test_parser_98(self):
        input = """for _, val := range arr
            s += val;
        """
        expect = """Error on line 2 col 13: s"""
        self.assertTrue(TestParser.checkParser(input,expect,1098))

    def test_parser_99(self):
        input = """do_something(2 + x, y * 5);"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1099))

    def test_parser_100(self):
        input = """do_something("Hello, World", ",")"""
        expect = """Error on line 1 col 34: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,1100))

    def test_parser_program_1(self):
        input = """func main() {
            putStringLn("Hello, World!")
        };"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1101))

    def test_parser_program_2(self):
        input = """func main() {
            var userName
            userName := "user"
            putStringLn(userName)
        };"""
        expect = """Error on line 2 col 26: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,1102))

    def test_parser_program_3(self):
        input = """x := 2
        func main() {
            x = 3
            putInt(x)
        }
        """
        expect = """Error on line 3 col 15: ="""
        self.assertTrue(TestParser.checkParser(input,expect,1103))

    def test_lexer_program_4(self):
        input = """func main() {
            var x float = 13.5
            var y float = 2.5e+4
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1104))

    def test_parser_program_5(self):
        input = """func main() {
                    x := -3
                    // Assign negative value to x
                    putInt(x)
                }
                """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1105))

    def test_parser_program_6(self):
        input = """func main() {
            const x = 2
            const y = 3
            var someVar = x + y
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1106))

    def test_parser_program_7(self):
        input = """func main() {
            const X:= 2
            putIntLn(X)
        }
        """
        expect = """Error on line 2 col 20: :="""
        self.assertTrue(TestParser.checkParser(input,expect,1107))

    def test_parser_program_8(self):
        input = """func main() {
            x := 2017
            putBoolLn(x > 2022 && x <= 3000)
            putBool(x >= 2000 && x < 3000)              
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1108))

    def test_lexer_program_9(self):
        input = """func main() {
            x := true        

            putBoolLn(x)
            putBoolLn(!x)
            putBoolLn(!x && x)
            putBoolLn(!x || x)                   
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1109))

    def test_parser_program_10(self):
        input = """func main() {
            x := 3
            if (x > 0) {
                x := 5
        }
        """        
        expect = """Error on line 6 col 9: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,1110))

    def test_parser_program_11(self):
        input = """func main() {
            var x int = randInt(100)
            if (x > 10) {
                putIntLn("yay!")
            } else {
                putIntln("nay!")
            }        
        }
        """        
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1111))

    def test_parser_program_12(self):
        input = """func main() {
            sum := 0
            for var i int = 0; i < 50; i += 1 {
                sum += i
            }
            putInt(sum)
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1112))

    def test_parser_program_13(self):
        input = """func main() {
            var x [4]int
            x[2] := 4
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1113))

    def test_parser_program_14(self):
        input = """func main() {
            x := 2
            var y [x]
        }
        """
        expect = """Error on line 3 col 23: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,1114))

    def test_parser_program_15(self):
        input = """func main() {
            for {
                putStringLn("forever!")
            }        
        }
        """
        expect = """Error on line 2 col 17: {"""
        self.assertTrue(TestParser.checkParser(input,expect,1115))

    def test_parser_program_16(self):
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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1116))

    def test_parser_program_17(self):
        input = """func main() {
            var knightIsAwake = false;
            var archerIsAwake = true;
            var prisonerIsAwake = false;
            var petDogIsPresent = false;
            var canRescue = !archerIsAwake && (petDogIsPresent || (!knightIsAwake && prisonerIsAwake));
            putBoolLn(canRescue);
        };
        """
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1117))

    def test_parser_program_18(self):
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
        expect = """Error on line 2 col 19: ="""
        self.assertTrue(TestParser.checkParser(input,expect,1118))

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
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1119))

