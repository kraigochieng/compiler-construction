import pandas as pd
from pprint import pprint
from code import code
import re
import time


# Display Options for dataframes
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)

# Reading from Excel File
df = pd.read_excel("State Table.xlsx", index_col=0,
                                     dtype=str)  # dtype as string for ease

print(df.columns.tolist())
print()

# Change indices to be strings
df.columns = df.columns.astype(str)
df.index = df.index.astype(str)

# Minifying Code
code_without_whitespace = ''.join(code.split())
pprint(code_without_whitespace)
print()

# n = "26_146_147_148_149_157_176_177_180_198_27_28_33_38_46_167_197_181_186_187_188_190_191_46"

states_to_tokens = {
        "20_21": "T_Var",
        "22": "T_Identifier",
        "26_146_147_148_149_157_176_177_180_198_27_28_33_38_46_167_197_181_186_187_188_190_191_46": "T_AssignOperator",
        "0_1_2_5_9_13_21_49_50_106_139_140_141_197": "T_Punc",
        "82_83_84_86_87_93_94_95_97_98_103": "T_Punc",
        "31_193_196_183_179": "T_IntConst",
        "30_184_194": "T_Punc",
        "32_185_179_195_196": "T_IntConst",
        "23": "T_Punc",
        "24": "T_IntConst",
        "25": "T_Punc",
        "182_179_29_192_196" : "T_IntConst",
        "108": "T_If",
        "109_110_111_119": "T_Punc",
        "122": "T_Punc",
        "123": "T_Punc",
        "124": "T_Punc",
        "125": "T_Punc",
        "126_127_135": "T_LogicalOper",
        "118_120_121": "T_BoolConstOrIdentifier",
        "134_137": "T_BoolConstOrIdentifier",
        "138": "T_Punc",
        "145": "T_Else",
        "53" : "T_for",
        "37" : "T_CharConst",
        "48": "T_StringConst",
        "34": "T_Punc",
        "36": "T_CharValue",
        "47": "T_StringValue",
        "54": "T_Punc",
        "57" : "T_Int",
        "58" : "T_Identifier",
        "59": "T_Punc",
        "60": "T_IntConst",
        "61": "T_IntConst",
        "62_63": "T_Punc",
        "64_65" : "T_identifier",
        "70_71_78" : "T_LogicalOper",
        "79_80_81": "T_identifier",
        "89_92_100":"T_IntConst",
        "104":"T_Punc",
        "85_92":"T_Identifier",
        "88_92_99": "T_IntConst",
        "90_101": "T_Punc",
        "91_92_102": "T_IntConstOrOper",
        "156_158_159_178_189_196": "T_BoolConstOrIdentifier",
        "160":"T_LogicalOper",
        "161":"T_LogicalOper",
        "162":"T_LogicalOper",
        "163":"T_LogicalOper",
        "164_165_173" : "T_LogicalOper",
        "174_175": "T_BoolConstOrIdentifier"
}

token_lexeme_pairs = []

accepted = 0

current_state = "0_1_2_5_9_13_21_49_50_106_139_140_141_197"

buffers = {
    "22": [],
    "31_193_196_183_179": [],
    "32_185_179_195_196": [],
    "24": [],
    "118_120_121": [],
    "134_137": [],
    "48": [],
    "37": [],
    "58":[],
    "60":[],
    "61":[],
    "79_80_81": [],
    "85_92": [],
    "88_92_99": [],
    "85_92":[],
    "91_92_102": [],
    "156_158_159_178_189_196": [],
    "174_175": []
}


start_time = time.time()
# Check every letter in the code
for index, letter in enumerate(code_without_whitespace):
    # Changing letters
    if letter == "‘":
        letter = "'"

    if letter == "’":
        letter = "'"

    if letter == "“":
        letter = '"'

    if letter == '”':
        letter = '"'

    # We use the previous state to do the check
    next_state = df.loc[current_state, letter]
    
    print()
    print("=======================================================================")
    print()
    print(f"[ Current: {current_state}, Letter: {letter} ] -> Next: {next_state}")
    print()

    # Clearing any buffers
    if next_state != "22" and len(buffers["22"]) > 0:
        x = "".join(buffers["22"])
        buffers["22"].clear()
        token_lexeme_pairs.append(("T_Identifier", x))
        accepted = index

    if next_state != "31_193_196_183_179" and len(buffers["31_193_196_183_179"]) > 0:
        x = "".join(buffers["31_193_196_183_179"])
        buffers["31_193_196_183_179"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    if next_state != "32_185_179_195_196" and len(buffers["32_185_179_195_196"]) > 0:
        x = "".join(buffers["32_185_179_195_196"])
        buffers["32_185_179_195_196"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    if next_state != "24" and len(buffers["24"]) > 0:
        x = "".join(buffers["24"])
        buffers["24"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    if next_state != "118_120_121" and len(buffers["118_120_121"]) > 0:
        x = "".join(buffers["118_120_121"])
        buffers["118_120_121"].clear()
        token_lexeme_pairs.append(("T_BoolConstOrIdentifier", x))
        accepted = index

    if next_state != "134_137" and len(buffers["134_137"]) > 0:
        x = "".join(buffers["134_137"])
        buffers["134_137"].clear()
        token_lexeme_pairs.append(("T_BoolConstOrIdentifier", x))
        accepted = index

    if next_state not in ["47","48"] and len(buffers["48"]) > 0:
        x = "".join(buffers["48"])
        buffers["48"].clear()
        token_lexeme_pairs.append(("T_StringConst", x))
        accepted = index

    if next_state not in ["34", "36", "37"] and len(buffers["37"]) > 0:
        x = "".join(buffers["37"])
        buffers["37"].clear()
        token_lexeme_pairs.append(("T_CharConst", x))
        accepted = index

    if next_state != "58" and len(buffers["58"]) > 0:
        x = "".join(buffers["58"])
        buffers["58"].clear()
        token_lexeme_pairs.append(("T_Identifier", x))
        accepted = index

    if next_state != "79_80_81" and len(buffers["79_80_81"]) > 0:
        x = "".join(buffers["79_80_81"])
        buffers["79_80_81"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    if next_state != "85_92" and len(buffers["85_92"]) > 0:
        x = "".join(buffers["85_92"])
        buffers["85_92"].clear()
        token_lexeme_pairs.append(("T_Identifier", x))
        accepted = index
    
    if next_state != "88_92_99" and len(buffers["88_92_99"]) > 0:
        x = "".join(buffers["88_92_99"])
        buffers["88_92_99"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    if next_state != "91_92_102" and len(buffers["91_92_102"]) > 0:
        x = "".join(buffers["91_92_102"])
        buffers["91_92_102"].clear()
        token_lexeme_pairs.append(("T_IntConst", x))
        accepted = index

    # if next_state != "156_158_159_178_189_196" and len(buffers["156_158_159_178_189_196"]) > 0:
    #   if buffers["156_158_159_178_189_196"][-1] in ["+", "-", "*", "/"]:
    #     operator = buffers["156_158_159_178_189_196"].pop()
    #     x = "".join(buffers["156_158_159_178_189_196"])
    #     buffers["156_158_159_178_189_196"].clear()
    #     token_lexeme_pairs.append(("T_BoolConstOrIdentifier", x))
    #     token_lexeme_pairs.append(("T_LogicalOperator", operator))
    #     accepted = index
    #   else:
    #     x = "".join(buffers["156_158_159_178_189_196"])
    #     buffers["156_158_159_178_189_196"].clear()
    #     token_lexeme_pairs.append(("T_BoolConstOrIdentifier", x))
    #     accepted = index

    if next_state != "156_158_159_178_189_196" and len(buffers["156_158_159_178_189_196"]) > 0:
        x = "".join(buffers["156_158_159_178_189_196"])
        buffers["156_158_159_178_189_196"].clear()
        token_lexeme_pairs.append(("T_BoolConstOrIdentifier", x))
        accepted = index
    
    # Preprocessing
    if next_state in states_to_tokens:
        token = states_to_tokens[next_state]
        lexeme = code_without_whitespace[accepted:index + 1]
            
        print(f"*****Token: {token}, Lexeme: {lexeme}")
        print()
        print(f">>>>>Accepted Before: {accepted}, Index: {index}")
        print()

        bufferless_states = [
            "20_21",
"26_146_147_148_149_157_176_177_180_198_27_28_33_38_46_167_197_181_186_187_188_190_191_46",
            "30_184_194",
            "0_1_2_5_9_13_21_49_50_106_139_140_141_197",
            "23",
            "25",
            "108",
            "109_110_111_119",
            "122",
            "123",
            "124",
            "125",
            "126_127_135",
            "138",
            "145",
            "182_179_29_192_196",
            "53",
            "54",
            "57",
            "59",
            "62_63",
            "64_65",
            "66",
            "67",
            "68",
            "69",
            "70_71_78",
            "82_83_84_86_87_93_94_95_97_98_103",
            "104",
            "90_101",
            "160",
            "161",
            "162",
            "163",
            "164_165_173"
        ]
        
        if next_state in bufferless_states:
            token_lexeme_pairs.append((token, lexeme))
            accepted = index + 1

        # Appending to buffers
        if next_state == "22":
                print(f".....Buffer for 22 Before Append: {buffers['22']}")
                buffers["22"].append(letter)
                print(f".....Buffer for 22 After Append: {buffers['22']}")

        if next_state == "31_193_196_183_179":
            print(f".....Buffer for 31_193_196_183_179 Before Append: {buffers['31_193_196_183_179']}")
            buffers["31_193_196_183_179"].append(letter)
            print(f".....Buffer for 31_193_196_183_179 After Append: {buffers['31_193_196_183_179']}")

        if next_state == "32_185_179_195_196":
            print(f".....Buffer for 32_185_179_195_196 Before Append: {buffers['32_185_179_195_196']}")
            buffers["32_185_179_195_196"].append(letter)
            print(f".....Buffer for 32_185_179_195_196 After Append: {buffers['32_185_179_195_196']}")

        if next_state == "24":
            print(f".....Buffer for 24 Before Append: {buffers['24']}")
            buffers["24"].append(letter)
            print(f".....Buffer for 24 After Append: {buffers['24']}")

        if next_state == "118_120_121":
            print(f".....Buffer for 118_120_121 Before Append: {buffers['118_120_121']}")
            buffers["118_120_121"].append(letter)
            print(f".....Buffer for 118_120_121 After Append: {buffers['118_120_121']}")

        if next_state == "134_137":
            print(f".....Buffer for 134_137 Before Append: {buffers['134_137']}")
            buffers["134_137"].append(letter)
            print(f".....Buffer for 134_137 After Append: {buffers['134_137']}")

        if next_state in ["34", "36", "37"]:
            print(f".....Buffer for 37 Before Append: {buffers['37']}")
            buffers["37"].append(letter)
            print(f".....Buffer for 37 After Append: {buffers['37']}")

        if next_state in ["47", "48"]:
            print(f".....Buffer for 48 Before Append: {buffers['48']}")
            buffers["48"].append(letter)
            print(f".....Buffer for 48 After Append: {buffers['48']}")

        if next_state == "58":
            print(f".....Buffer for 58 Before Append: {buffers['58']}")
            buffers["48"].append(letter)
            print(f".....Buffer for 58 After Append: {buffers['58']}")

        if next_state == "79_80_81":
            print(f".....Buffer for 79_80_81 Before Append: {buffers['79_80_81']}")
            buffers["48"].append(letter)
            print(f".....Buffer for 79_80_81 After Append: {buffers['79_80_81']}")

        if next_state == "85_92":
            print(f".....Buffer for 85_92 Before Append: {buffers['85_92']}")
            buffers["85_92"].append(letter)
            print(f".....Buffer for 85_92 After Append: {buffers['85_92']}")
            
        if next_state == "88_92_99":
            print(f".....Buffer for 88_92_99 Before Append: {buffers['88_92_99']}")
            buffers["88_92_99"].append(letter)
            print(f".....Buffer for 88_92_99 After Append: {buffers['88_92_99']}")

        if next_state == "91_92_102":
            print(f".....Buffer for 91_92_102 Before Append: {buffers['91_92_102']}")
            buffers["48"].append(letter)
            print(f".....Buffer for 91_92_102 After Append: {buffers['91_92_102']}")

        if next_state == "156_158_159_178_189_196":
            print(f".....Buffer for 156_158_159_178_189_196 Before Append: {buffers['156_158_159_178_189_196']}")
            buffers["48"].append(letter)
            print(f".....Buffer for 156_158_159_178_189_196 After Append: {buffers['156_158_159_178_189_196']}")

        if next_state == "174_175":
            print(f".....Buffer for 174_175 Before Append: {buffers['174_175']}")
            buffers["174_175"].append(letter)
            print(f".....Buffer for 174_175 After Append: {buffers['174_175']}")
    current_state = next_state

end_time = time.time()
print("+++++Token Lexeme Pairs")
pprint(token_lexeme_pairs)
print()

duration =  end_time - start_time
print(f"Time taken: {duration}" )

# states = []
# for index, letter in enumerate(code_without_whitespace):
#   if current_state in states_to_tokens:
#     token = states_to_tokens[current_state]
#     lexeme = code_without_whitespace[accepted:index]
#     if states[-1] != current_state:
#       print(">>>>>Lexeme:", lexeme)
#       accepted = index

#   # Changing letters
#   if letter == "‘":
#     letter = "'"

#   if letter == "’":
#     letter = "'"

#   if letter == "“":
#     letter = '"'

#   if letter == '”':
#     letter = '"'

#   next_state = df.loc[current_state, letter]

#   print(f"[ Current: {current_state}, Letter: {letter} ] = Next: {next_state}")
#   states.append(current_state)
#   current_state = next_state

# if next_state in states_to_tokens:
#   token = states_to_tokens[next_state]
#   lexeme = code_without_whitespace[accepted:index + 1]
#   if next_state != current_state:
#     print(">>>>>Lexeme:", lexeme)
#     accepted = index

