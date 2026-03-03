from tests.utils_tests import run_test


# Base skeleton for testcase
# def test_(tmp_path):
#     input_text = """

# """.lstrip()

#     expected_output = ""

#     # Optional user input file (can be empty or contain user input)
#     input_file = tmp_path / "input.txt"
#     input_file.write_text("")  # Empty for this test

#     run_test(str(input_file), input_text, expected_output)


def test_equalTo1(tmp_path):
# class MyInt : Integer { }
# class Main : Object {
#     run [|
#         x := 1. y := 1. z := Integer from: 1.
#         u := MyInt from: 1. w := MyInt from: 1.

#         a := (x equalTo: y) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyInt" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="w"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="a"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("ANO")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_equalTo2(tmp_path):
# class MyInt : Integer { }
# class Main : Object {
#     run [|
#         x := 1. y := 1. z := Integer from: 1.
#         u := MyInt from: 1. w := MyInt from: 1.

#         a := (x equalTo: z) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyInt" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="w"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="a"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="z"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_equalTo3(tmp_path):
# class MyInt : Integer { }
# class Main : Object {
#     run [|
#         x := 1. y := 1. z := Integer from: 1.
#         u := MyInt from: 1. w := MyInt from: 1.

#         a := (u equalTo: x) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyInt" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="w"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="a"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="x"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="u"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_equalTo4(tmp_path):
# class MyInt : Integer { }
# class Main : Object {
#     run [|
#         x := 1. y := 1. z := Integer from: 1.
#         u := MyInt from: 1. w := MyInt from: 1.

#         a := (u equalTo: w) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyInt" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="w"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="a"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="w"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="u"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_equalTo5(tmp_path):
# class MyInt : Integer { }
# class Main : Object {
#     run [|
#         x := 1. y := 1. z := Integer from: 1.
#         u := MyInt from: 1. w := MyInt from: 1.

#         a := (u identicalTo: x) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyInt" parent="Integer"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <literal class="Integer" value="1"/>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="w"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyInt"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="a"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="identicalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="x"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="u"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "NE"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_string_equality(tmp_path):
# class MyStr : String { }
# class Main : Object {
#     run [|
#         x := 'miluju'. 
#         y := String from: 'IPP'.
#         u := MyStr from: 'miluju'.

#         _ := (x equalTo: y)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].

#         _ := (x equalTo: u) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].

#         _ := (x identicalTo: u) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].

#         _ := (u isString)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="MyStr" parent="String"/>
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <literal class="String" value="miluju"/>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="IPP"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="u"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="miluju"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="MyStr"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="u"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="identicalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="u"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isString">
                                    <expr>
                                        <var name="u"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "NE ANO NE ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_nil_equality(tmp_path):
# class Main : Object {
#     run [|
#         x := Nil new. 
#         y := Nil new.

#         _ := (x equalTo: y)
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := (x identicalTo: y) 
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := (x isNil) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Nil"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Nil"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="identicalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isNil">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO ANO ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_isBlock(tmp_path):
# class Main : Object {
# run [|
#         a := [ :x | _ := 42. ].

#         _ := (a isBlock)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="a"/>
                    <expr>
                        <block arity="1">
                            <parameter order="1" name="x"/>
                            <assign order="1">
                                <var name="_"/>
                                <expr>
                                    <literal class="Integer" value="42"/>
                                </expr>
                            </assign>
                        </block>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isBlock">
                                    <expr>
                                        <var name="a"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_True_equality(tmp_path):
# class Main : Object {
#     run [|
#         x := True new. 
#         y := True new.

#         _ := (x equalTo: y)
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := (x identicalTo: y) 
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="True"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="True"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="equalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="identicalTo:">
                                    <arg order="1">
                                        <expr>
                                            <var name="y"/>
                                        </expr>
                                    </arg>
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ANO ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_object1(tmp_path):
# class Main : Object {
#     run [|
#         x := (self asString) print. 
#     ]
# }
    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="self"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = ""

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_string_as_int(tmp_path):
# class Main : Object {
#     run [|
#         x := String from: '5'.
#         f := String from: 'ahoj'.

#         x := (x asInteger) plus: 2.
#         _ := (x asString) print.

#         f := f asInteger.

#         _ := (f isNil)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="f"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="x"/>
                    <expr>
                        <send selector="plus:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="2"/>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="asInteger">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <send selector="asString">
                                    <expr>
                                        <var name="x"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="f"/>
                    <expr>
                        <send selector="asInteger">
                            <expr>
                                <var name="f"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isNil">
                                    <expr>
                                        <var name="f"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "7ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_concatenate(tmp_path):
# class Main : Object {
#     run [|
#         x := String from: '5'.
#         y := Integer from: 1.
#         f := String from: 'ahoj'.

#         f := f concatenateWith: x.
#         _ := f print.

#         y := f concatenateWith: y.

#         _ := (y isNil)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="1"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="Integer"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="f"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="ahoj"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="f"/>
                    <expr>
                        <send selector="concatenateWith:">
                            <arg order="1">
                                <expr>
                                    <var name="x"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="f"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="f"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="y"/>
                    <expr>
                        <send selector="concatenateWith:">
                            <arg order="1">
                                <expr>
                                    <var name="y"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="f"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isNil">
                                    <expr>
                                        <var name="y"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ahoj5ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_substring(tmp_path):
# class Main : Object {
#     run [|
#         x := String from: 'milujuIPP'.

#         y := x startsWith: 4 endsBefore: 9.
#         _ := y print.

#         y := x startsWith: 6 endsBefore: 5.
#         _ := y print.

#         y := x startsWith: 0 endsBefore: 5.

#         _ := (y isNil)
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="from:">
                            <arg order="1">
                                <expr>
                                    <literal class="String" value="milujuIPP"/>
                                </expr>
                            </arg>
                            <expr>
                                <literal class="class" value="String"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="startsWith:endsBefore:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="4"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="9"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="y"/>
                    <expr>
                        <send selector="startsWith:endsBefore:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="6"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="print">
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="y"/>
                    <expr>
                        <send selector="startsWith:endsBefore:">
                            <arg order="1">
                                <expr>
                                    <literal class="Integer" value="0"/>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <literal class="Integer" value="5"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <send selector="isNil">
                                    <expr>
                                        <var name="y"/>
                                    </expr>
                                </send>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "ujuIPANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)



def test_not_or_and(tmp_path):
# class Main : Object {
#     run [|
#         x := True new.

#         y := x not.
#         z := x and: [| _ := False new.].
#         u := x or: [| _ := False new.].

#         _ := y
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := z
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := u
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="True"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="y"/>
                    <expr>
                        <send selector="not">
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="z"/>
                    <expr>
                        <send selector="and:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="new">
                                                    <expr>
                                                        <literal class="class" value="False"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="u"/>
                    <expr>
                        <send selector="or:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="new">
                                                    <expr>
                                                        <literal class="class" value="False"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="z"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="u"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "NE NE ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)


def test_or_and2(tmp_path):
# class Main : Object {
#     run [|
#         x := True new.

#         w := Object new.
#         _ := w value: (False new).

#         y := x and: w.
#         z := x or: w.

#         _ := y
#         ifTrue: [| _ := 'ANO ' print.]
#         ifFalse: [| _ := 'NE ' print.].

#         _ := z
#         ifTrue: [| _ := 'ANO' print.]
#         ifFalse: [| _ := 'NE' print.].
#     ]
# }

    input_text = """
<?xml version="1.0" encoding="UTF-8"?>
<program language="SOL25">
    <class name="Main" parent="Object">
        <method selector="run">
            <block arity="0">
                <assign order="1">
                    <var name="x"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="True"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="2">
                    <var name="w"/>
                    <expr>
                        <send selector="new">
                            <expr>
                                <literal class="class" value="Object"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="3">
                    <var name="_"/>
                    <expr>
                        <send selector="value:">
                            <arg order="1">
                                <expr>
                                    <send selector="new">
                                        <expr>
                                            <literal class="class" value="False"/>
                                        </expr>
                                    </send>
                                </expr>
                            </arg>
                            <expr>
                                <var name="w"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="4">
                    <var name="y"/>
                    <expr>
                        <send selector="and:">
                            <arg order="1">
                                <expr>
                                    <var name="w"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="5">
                    <var name="z"/>
                    <expr>
                        <send selector="or:">
                            <arg order="1">
                                <expr>
                                    <var name="w"/>
                                </expr>
                            </arg>
                            <expr>
                                <var name="x"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="6">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE "/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="y"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
                <assign order="7">
                    <var name="_"/>
                    <expr>
                        <send selector="ifTrue:ifFalse:">
                            <arg order="1">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="ANO"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <arg order="2">
                                <expr>
                                    <block arity="0">
                                        <assign order="1">
                                            <var name="_"/>
                                            <expr>
                                                <send selector="print">
                                                    <expr>
                                                        <literal class="String" value="NE"/>
                                                    </expr>
                                                </send>
                                            </expr>
                                        </assign>
                                    </block>
                                </expr>
                            </arg>
                            <expr>
                                <var name="z"/>
                            </expr>
                        </send>
                    </expr>
                </assign>
            </block>
        </method>
    </class>
</program>
""".lstrip()

    expected_output = "NE ANO"

    # Optional user input file (can be empty or contain user input)
    input_file = tmp_path / "input.txt"
    input_file.write_text("")  # Empty for this test

    run_test(str(input_file), input_text, expected_output)

