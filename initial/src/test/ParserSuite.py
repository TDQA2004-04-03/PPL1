import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_assignment_declaration_1(self):
        input = """var x int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1001))

    def test_assignment_declaration_2(self):
        input = """var y string;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1002))

    def test_variable_not_allowed_id(self):
        input = "var abc&def string;"
        expect = "&"
        self.assertTrue(TestParser.checkParser(input,expect,1003))

    def test_variable_id_started_with_literal(self):
        input = "var 12abc int;"
        expect = "Error on line 1 col 5: 12"
        self.assertTrue(TestParser.checkParser(input,expect,1004))

    def test_assignment_no_id(self):
        input = """var float;"""
        expect = "Error on line 1 col 5: float"
        self.assertTrue(TestParser.checkParser(input,expect,1005))

    def test_assignment_name_is_type(self):
        input = """var int float;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,1006))

    def test_assignment_no_semicolon(self):
        input = """var a boolean"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1007))

    def test_assignment_integer_1(self):
        input = "var a = 12;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1008))

    def test_assignment_integer_2(self):
        input = "var b int = 0;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1009))

    def test_assignment_integer_decimal_start_0(self):
        input = "var c = 0123;"
        expect = "Error on line 1 col 10: 123"
        self.assertTrue(TestParser.checkParser(input,expect,1010))

    def test_assignment_integer_binary(self):
        input = "var d int = 0b1101101;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1011))

    def test_assignment_integer_binary_not_allowed_digit(self):
        input = "var d int = 0b110112101;"
        expect = "Error on line 1 col 20: 2101"
        self.assertTrue(TestParser.checkParser(input,expect,1012))

    def test_assignment_integer_octal(self):
        input = "var e = 0O234765;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1013))

    def test_assignment_integer_octal_not_allowed_digit(self):
        input = "var e = 0o2348765;"
        expect = "Error on line 1 col 14: 8765"
        self.assertTrue(TestParser.checkParser(input,expect,1014))

    def test_assignment_integer_hexadecimal(self):
        input = "var f int = 0x12BDf5A;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1015))

    def test_assignment_integer_hexadecimal_not_allowed_digit(self):
        input = "var f int = 0x12BDG5A;"
        expect = "Error on line 1 col 19: G5A"
        self.assertTrue(TestParser.checkParser(input,expect,1016))

    def test_assignment_float_1(self):
        input = "var g = 0.69;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1017))

    def test_assignment_float_2(self):
        input = "var h = 13.;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1018))

    def test_assignment_float_3(self):
        input = "var i = 0.314e+1;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,1019))

    def test_assignment_float_e(self):
        input = "var i = 1e;"
        expect = "Error on line 1 col 10: e"
        self.assertTrue(TestParser.checkParser(input,expect,1020))

    def test_assignment_float_e_no_sign(self):
        input = "var i = 1e3;"
        expect = "Error on line 1 col 10: e3"
        self.assertTrue(TestParser.checkParser(input,expect,1021))

    def test_assignment_string_1(self):
        input = """var str1 = "abcdef";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1022))

    def test_assignment_string_2(self):
        input = """var str2 = "abc\ndefgh";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1023))

    def test_assignment_unclosed_string(self):
        input = """var str3 = "QuocAnh;"""
        expect = """QuocAnh;"""
        self.assertTrue(TestParser.checkParser(input,expect,1024))

    def test_assignment_illegal_escape(self):
        input = """var str4 = "Quoc\Anh;"""
        expect = """Quoc\\"""
        self.assertTrue(TestParser.checkParser(input,expect,1025))

    def test_assignment_double_quote_in_string(self):
        input = """var str4 = "Quoc"Anh;"""
        expect = """Error on line 1 col 18: Anh"""
        self.assertTrue(TestParser.checkParser(input,expect,1026))

    def test_assignment_boolean(self):
        input = """var check boolean = false;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1027))

    def test_comment_1(self):
        input = """var a = 1; //Assign 1 to a"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1028))

    def test_comment_2(self):
        input = """var e = 2.78; /*Assign value 2.78 
        to e*/"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1029))

    def test_comment_nested(self):
        input = """var pi = 3.14; /*Assign value /* float 3.14 */ 
        to /* variable identified as */ pi */"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1030))

    def test_comment_unclosed(self):
        input = """var pi = 3.14; /*Assign value"""
        expect = """Error on line 1 col 16: /"""
        self.assertTrue(TestParser.checkParser(input,expect,1031))

    def test_constant_declaration(self):
        input = """const pi = 3.14;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1032))

    def test_constant_declaration_no_value(self):
        input = """const e;"""
        expect = """Error on line 1 col 8: ;"""
        self.assertTrue(TestParser.checkParser(input,expect,1033))

    def test_assignment_1(self):
        input = """m = 5;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1034))

    def test_assignment_2(self):
        input = """x *= 10;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1035))


    def test_array_1(self):
        input = """var a [3] int;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1036))

    def test_array_not_allowed_index(self):
        input = """var a [0.5] int;"""
        expect = """Error on line 1 col 8: 0.5"""
        self.assertTrue(TestParser.checkParser(input,expect,1037))

    def test_array_2(self):
        input = """var m [5][5][5] int;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1038))

    def test_array_unclosed_access(self):
        input = """var a [2 int;"""
        expect = """Error on line 1 col 10: int"""
        self.assertTrue(TestParser.checkParser(input,expect,1039))

    def test_array_literal(self):
        input = """var a [3]int = {1,2,3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1040))

    def test_array_literal_2(self):
        input = """var a [2][3]int = {{1,2,3}, {4,5,6}};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1041))

    def test_array_literal_forget_comma(self):
        input = """var a [3] int = {1 2,3};"""
        expect = """Error on line 1 col 20: 2"""
        self.assertTrue(TestParser.checkParser(input,expect,1042))

    def test_array_last_comma(self):
        input = """var a [3] int = {1,2,3,};"""
        expect = """Error on line 1 col 24: }"""
        self.assertTrue(TestParser.checkParser(input,expect,1043))

    def test_array_access_1(self):
        input = """m[2] := 8;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1044))

    def test_array_access_2(self):
        input = """O[2][3] = {1,3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1045))

    def test_array_invalid_access(self):
        input = """m[] := "abc";"""
        expect = """Error on line 1 col 3: ]"""
        self.assertTrue(TestParser.checkParser(input,expect,1046))


    def test_struct_decl_1(self):
        input = """type Complex struct {\nreal int;\nimag int;\n}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1047))

    def test_struct_decl_2(self):
        input = """type Whatever struct {\narr [5]float;\nside Complex;\n}"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1048))

    def test_struct_literal_1(self):
        input = """a = Complex{real: 2, imag: 3};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1049))

    def test_struct_literal_2(self):
        input = """l = Line{Point1: Point{x: 1.2, y: 2.5}, Point2: Point{x: 3.4, y: 7.5}};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1050))

    def test_struct_literal_3(self):
        input = """c = Choice{l: {1,2,3,4}, max: 5};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1051))

    def test_struct_literal_null(self):
        input = """p = Person{};"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1052))

    def test_struct_missing_value(self):
        input = """p = Person{height: 1.75, weight:};"""
        expect = """Error on line 1 col 33: }"""
        self.assertTrue(TestParser.checkParser(input,expect,1053))

    def test_struct_access_1(self):
        input = """p.name = "John";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1054))

    def test_struct_access_2(self):
        input = """l.point1.x = 2.5;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1055))
    
    def test_array_of_struct(self):
        input = """var myClass [50]Student;"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1056))

    def test_array_of_struct_access(self):
        input = """myClass[21].name = "Harry";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1057))

    def test_array_member_in_struct_access(self):
        input = """myClass.name[11] = "Kid";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1058))

    def test_array_struct_mixed(self):
        input = """myClass.name[20].fname = "Kaitou Kid";"""
        expect = """successful"""
        self.assertTrue(TestParser.checkParser(input,expect,1059))


