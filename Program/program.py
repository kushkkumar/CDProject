# compiler designed for following syntax by Ankith Bhandary and Ankush Kumar N

'''
print "string"
input _var
for i = 3 to 4
_var := _var++
next i
end
'''

import sys

# list of tokens in the language
tokens = ['print', 'input', 'for', 'i', 'to', 'id', 'next', 'end', '"', "=", ':']
print(tokens)

# reference parsing table
parse_table = {
    '0': {'print': 'S 2', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': '1', 'A': 'NA'}
    ,
    '1': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'ACCEPT', 'S': 'NA', 'A': 'NA'}
    ,
    '2': {'print': 'NA', ' ': 'S 3', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '3': {'print': 'NA', ' ': 'NA', '"': 'S 4', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '4': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'S 5', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '5': {'print': 'NA', ' ': 'NA', '"': 'S 6', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '6': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'S 7', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '7': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'S 8', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '8': {'print': 'NA', ' ': 'S 9', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '9': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'S 10', 'for': 'NA',
          'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
          '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '10': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'S 11', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '11': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'S 12',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '12': {'print': 'NA', ' ': 'S 13', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '13': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'S 14', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA',
           '--': 'NA', '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '14': {'print': 'NA', ' ': 'S 15', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '15': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'S 16', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA',
           '--': 'NA', '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '16': {'print': 'NA', ' ': 'S 17', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '17': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'S 18', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA',
           '--': 'NA', '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '18': {'print': 'NA', ' ': 'S 19', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '19': {'print': 'NA', ' ': 'NA', '"': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA', '=': 'NA', 'num': 'NA', 'to': 'S 20', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA',
           '--': 'NA', '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '20': {'print': 'NA', ' ': 'S 21', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '21': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'S 22', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '22': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'S 23', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA"', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '23': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'S 24', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '24': {'print': 'NA', ' ': 'S 25', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '25': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'S 26', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '26': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'S 27', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '27': {'print': 'NA', ' ': 'S 28', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '28': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'S 30', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'S 31', '--': 'S 32',
           '$': 'NA', 'S': 'NA', 'A': '29'}
    ,
    '29': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'S 33', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '30': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'S 34', '--': 'S 35',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '31': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'S 36', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '32': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'S 37', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '33': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'S 38', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '34': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'R 2', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '35': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'R 4', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '36': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'R 3', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '37': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'R 5', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '38': {'print': 'NA', ' ': 'S 39', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '39': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'S 40',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '40': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'S 41', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '41': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'S 42', '++': 'NA', '--': 'NA',
           '$': 'NA', 'S': 'NA', 'A': 'NA'}
    ,
    '42': {'print': 'NA', ' ': 'NA', '""': 'NA', 'string': 'NA', '\n': 'NA', 'input': 'NA', 'var': 'NA', 'for': 'NA',
           'i': 'NA',
           '=': 'NA', 'num': 'NA', 'to': 'NA', ':': 'NA', 'next': 'NA', 'end': 'NA', '++': 'NA', '--': 'NA',
           '$': 'R 1', 'S': 'NA', 'A': 'NA'}
    }

# 2 * (number of elements in the grammar)
no_ele = {'1': 68, '2': 4, '3': 4, '4': 4, '5': 4}

#grammar head (non-terminal)
gram_name = {'1': 'S', '2': 'A', '3': 'A', '4': 'A', '5': 'A'}


def error_handler(pointer):
    print('Sorry Error has occured in ',pointer)
    x = 6
    return x


# Tokenizer... This function converts the program string to token string
def tokenizer(program_string):
    program_string += '$'
    pointer = 0
    lis = []

    while program_string[pointer] != "$":
        current_string = ""

        if program_string[pointer].isalpha():
            current_string += program_string[pointer]
            pointer += 1
            while program_string[pointer].isalnum():
                current_string += program_string[pointer]
                pointer += 1
            if current_string in tokens:
                lis.append(current_string)
            else:
                lis.append('var')


        elif program_string[pointer] == '"':
            pointer += 1
            while program_string[pointer] != '"':
                pointer += 1
            lis.append('"')
            lis.append('string')
            lis.append('"')
            pointer += 1

        elif program_string[pointer] == '_' or program_string[pointer].isalpha():
            current_string += program_string[pointer]
            pointer += 1
            while program_string[pointer].isalnum() or program_string[pointer] == '_':
                pointer += 1
            lis.append('var')

        elif program_string[pointer].isnumeric():
            current_string += program_string[pointer]
            pointer += 1
            dot_count = 0
            while program_string[pointer].isnumeric() or program_string[pointer] == ".":
                if program_string[pointer] == ".":
                    dot_count += 1
                current_string += program_string[pointer]
                pointer += 1
            if dot_count > 1:
                x = error_handler(pointer)
                print('Error in Tokenizer Line No. : ' + x + ' unidentified token ' + current_string)
                exit()
            else:
                lis.append('num')

        else:
            if program_string[pointer] == " ":
                lis.append(' ')
                pointer += 1
            elif program_string[pointer] == "\n":
                lis.append('\n')
                pointer += 1
            elif program_string[pointer] == '+':
                pointer += 1
                if program_string[pointer] == '+':
                    lis.append('++')
                    pointer += 1
            elif program_string[pointer] == '-':
                pointer += 1
                if program_string[pointer] == '-':
                    lis.append('--')
                    pointer += 1

            elif program_string[pointer] != " " and program_string[pointer] != "\n":
                lis.append(tokens[tokens.index(program_string[pointer])])
                pointer += 1
            else:
                pointer += 1
    return lis


# Syntax Analyser... This function analyses the correctness of the program in terms of the syntax

def syntax_analyser(token_list):
    top = 0
    stack_token = ['0']
    j = len(token_list)
    i = 0
    while (i < j):
        x = parse_table[stack_token[top]][token_list[i]].split()
        if (x[0] == 'S'):
            print('shift')
            stack_token.append(token_list[i])
            stack_token.append(x[1])
            top += 2
            i += 1
            print(stack_token)
        elif (x[0] == 'R'):
            print('reduce')
            stack_token = stack_token[:(top - no_ele[x[1]]) + 1]
            top -= no_ele[x[1]]
            stack_token.append(gram_name[x[1]])
            top += 1
            stack_token.append(parse_table[stack_token[top - 1]][stack_token[top]])
            top += 1
            print(stack_token)
        elif (x[0] == 'NA'):
            print("syntax error..!")
            exit()
        elif (x[0] == 'ACCEPT'):
            print("accepted..!\n")
            exit()
        else:
            break;

# Main function

def main():
    program_string = open("inp", 'r').read()
    print("\nProgram\n")
    print(program_string)

    token_list = tokenizer(program_string)
    print("\nTokens\n")
    print(token_list)
    token_list.append('$')
    print("analysing syntax for the obtained tokens...")
    syntax_analyser(token_list)


# Call to main() function
try:
    main()
except Exception as e:
    print("Compiler: Unkown compile time Exception occured..." + e)
