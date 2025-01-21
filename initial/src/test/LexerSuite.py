import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_variable_declaration_1(self):
        input = "var x int;"
        expect = "var,x,int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,1))


    def test_variable_declaration_2(self):
        input = "var y string;"
        expect = "var,y,string,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,2))

    def test_variable_not_allowed_id(self):
        input = "var abc&def string;"
        expect = "var,abc,ErrorToken &"
        self.assertTrue(TestLexer.checkLexeme(input,expect,3))

    def test_variable_id_started_with_literal(self):
        input = "var 12abc int;"
        expect = "var,12,abc,int,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,4))

    def test_variable_no_id(self):
        input = "var float;"
        expect = "var,float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,5))

    def test_variable_name_is_type(self):
        input = "var int float;"
        expect = "var,int,float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,6))
    
    def test_variable_no_semicolon(self):
        input = "var a boolean"
        expect = "var,a,boolean,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,7))

    def test_integer_1(self):
        input = "var a = 12;"
        expect = "var,a,=,12,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,8))

    def test_integer_2(self):
        input = "var b int = 0;"
        expect = "var,b,int,=,0,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,9))

    def test_integer_decimal_start_0(self):
        input = "var c = 0123;"
        expect = "var,c,=,0,123,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,10))

    def test_integer_binary(self):
        input = "var d int = 0b1101101;"
        expect = "var,d,int,=,0b1101101,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,11))

    def test_integer_binary_not_allowed_digit(self):
        input = "var d int = 0b110112101;"
        expect = "var,d,int,=,0b11011,2101,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,12))

    def test_integer_octal(self):
        input = "var e = 0O1234765;"
        expect = "var,e,=,0O1234765,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,13))

    def test_integer_octal_not_allowed_digit(self):
        input = "var e = 0o2348765;"
        expect = "var,e,=,0o234,8765,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,14))

    def test_integer_hexadecimal(self):
        input = "var f int = 0x12BDf5A;"
        expect = "var,f,int,=,0x12BDf5A,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,15))

    def test_integer_hexadecimal_not_allowed_digit(self):
        input = "var f int = 0x12BDG5A;"
        expect = "var,f,int,=,0x12BD,G5A,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,16))

    def test_float_1(self):
        input = "var g = 0.69;"
        expect = "var,g,=,0.69,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,17))

    def test_float_2(self):
        input = "var h = 13.;"
        expect = "var,h,=,13.,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,18))

    def test_float_3(self):
        input = "var i = 0.314e+1;"
        expect = "var,i,=,0.314e+1,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,19))

    def test_float_e(self):
        input = "var i = 1e;"
        expect = "var,i,=,1,e,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,20))

    def test_float_e_no_sign(self):
        input = "var i = 1e3;"
        expect = "var,i,=,1,e3,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input,expect,21))

    def test_string_1(self):
        input = """var str1 = "abcdef";"""
        expect = """var,str1,=,"abcdef",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,22))

    def test_string_2(self):
        input = """var str2 = "abc\ndefgh";"""
        expect = """var,str2,=,"abc\n\ndefgh",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,23))

    def test_unclosed_string(self):
        input = """var str3 = "QuocAnh;"""
        expect = """var,str3,=,Unclosed string: QuocAnh;"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,24))

    def test_illegal_escape(self):
        input = """var str4 = "Quoc\Anh;"""
        expect = """var,str4,=,Illegal escape in string: Quoc\\"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,25))

    def test_double_quote_in_string(self):
        input = """var str4 = "Bayern"Munich";"""
        expect = """var,str4,=,"Bayern",Munich,Unclosed string: ;"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,26))

    def test_boolean(self):
        input = """var check boolean = false;"""
        expect = """var,check,boolean,=,false,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,27))

    def test_comment_1(self):
        input = """var a = 1; //Assign 1 to a"""
        expect = """var,a,=,1,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,28))

    def test_comment_2(self):
        input = """var e = 2.78; /*Assign value 2.78 
        to e*/"""
        expect = """var,e,=,2.78,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,29))

    def test_comment_nested(self):
        input = """var pi = 3.14; /*Assign value /* float 3.14 */ 
        to /* variable identified as */ pi */"""
        expect = """var,pi,=,3.14,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,30))

    def test_comment_unclosed(self):
        input = """var pi = 3.14; /*Assign value"""
        expect = """var,pi,=,3.14,;,/,*,Assign,value,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,31))

    def test_constant_declaration(self):
        input = """const pi = 3.14;"""
        expect = """const,pi,=,3.14,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,32))

    def test_constant_declaration_no_value(self):
        input = """const e;"""
        expect = """const,e,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,33))

    def test_assignment_1(self):
        input = """m = 5;"""
        expect = """m,=,5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,34))

    def test_assignment_2(self):
        input = """x *= 10;"""
        expect = """x,*=,10,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,35))


    def test_array_1(self):
        input = """var a [3] int;"""
        expect = """var,a,[,3,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,36))
    
    def test_array_not_allowed_index(self):
        input = """var a [0.5] int;"""
        expect = """var,a,[,0.5,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,37))

    def test_array_2(self):
        input = """var m [5][5][5] int;"""
        expect = """var,m,[,5,],[,5,],[,5,],int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,38))

    def test_array_unclosed_access(self):
        input = """var a [2 int;"""
        expect = """var,a,[,2,int,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,39))

    def test_array_literal_1(self):
        input = """var a [3] int = {1,2,3};"""
        expect = """var,a,[,3,],int,=,{,1,,,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,40))

    def test_array_literal_2(self):
        input = """var a [2][3] int = { {1,2,3}, {4,5,6}};"""
        expect = """var,a,[,2,],[,3,],int,=,{,{,1,,,2,,,3,},,,{,4,,,5,,,6,},},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,41))

    def test_array_literal_forget_comma(self):
        input = """var a [3] int = {1 2,3};"""
        expect = """var,a,[,3,],int,=,{,1,2,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,42))

    def test_array_last_comma(self):
        input = """var a [3] int = {1,2,3,};"""
        expect = """var,a,[,3,],int,=,{,1,,,2,,,3,,,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,43))

    def test_array_access_1(self):
        input = """m[2] := 8;"""
        expect = """m,[,2,],:=,8,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,44))

    def test_array_access_2(self):
        input = """O[2][3] = {1,3};"""
        expect = """O,[,2,],[,3,],=,{,1,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,45))

    def test_array_invalid_access(self):
        input = """m[] := "abc";"""
        expect = """m,[,],:=,"abc",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,46))


    def test_struct_decl_1(self):
        input = """type Complex struct {
            real int;
            imag int;
        }"""
        expect = """type,Complex,struct,{,real,int,;,imag,int,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,47))

    def test_struct_decl_2(self):
        input = """type Whatever struct {
            arr [5] float;
            side Complex;
        }"""
        expect = """type,Whatever,struct,{,arr,[,5,],float,;,side,Complex,;,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,48))

    def test_struct_literal_1(self):
        input = """a := Complex{real: 2, imag: 3};"""
        expect = """a,:=,Complex,{,real,:,2,,,imag,:,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,49))

    def test_struct_literal_2(self):
        input = """l = Line{Point1: Point{x: 1.2, y: 2.5}, Point2: Point{x: 3.4, y: 7.5}};"""
        expect = """l,=,Line,{,Point1,:,Point,{,x,:,1.2,,,y,:,2.5,},,,Point2,:,Point,{,x,:,3.4,,,y,:,7.5,},},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,50))

    def test_struct_literal_3(self):
        input = """c = Choice{l: {1,2,3,4}, max: 5};"""
        expect = """c,=,Choice,{,l,:,{,1,,,2,,,3,,,4,},,,max,:,5,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,51))

    def test_struct_literal_null(self):
        input = """p = Person{};"""
        expect = """p,=,Person,{,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,52))

    def test_struct_missing_value(self):
        input = """p = Person{height: 1.75, weight:};"""
        expect = """p,=,Person,{,height,:,1.75,,,weight,:,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,53))

    def test_struct_access_1(self):
        input = """p.name = "John";"""
        expect = """p,.,name,=,"John",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,54))

    def test_struct_access_2(self):
        input = """l.point1.x = 2.5;"""
        expect = """l,.,point1,.,x,=,2.5,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,55))

    def test_array_of_struct(self):
        input = """var myClass [50]Student;"""
        expect = """var,myClass,[,50,],Student,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,56))

    def test_array_of_struct_access(self):
        input = """myClass[21].name = "Harry";"""
        expect = """myClass,[,21,],.,name,=,"Harry",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,57))

    def test_array_member_in_struct_access(self):
        input = """myClass.name[11] = "Kid";"""
        expect = """myClass,.,name,[,11,],=,"Kid",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,58))

    def test_array_struct_mixed(self):
        input = """myClass.name[20].fname = "Kaitou Kid";"""
        expect = """myClass,.,name,[,20,],.,fname,=,"Kaitou Kid",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,59))

    def test_interface_1(self):
        input = """type ;"""
        expect = """myClass,.,name,[,20,],.,fname,=,"Kaitou Kid",;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,expect,59))
