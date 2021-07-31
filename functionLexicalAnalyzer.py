import ply.lex as lex
import codecs
import os
import sys

rotacao_gaussiana ={
    'rotacao_gaussiana':'ROTACAO_GAUSSIANA',
    'produto':'PRODUTO','G':'g','seed_R':'SEED_R','seed_Q':'SEED_Q','Q':'Q','R':'R_','k':'K'
}

coco_rand_uniform ={
    'coco_rand_uniform':'COCO_RAND_UNIFORM','uniftmp':'UNIFTMP','low':'LOW','high':'HIGH','seed':'SEED','dim':'DIM'
}
x_column={
    'x_column':'X_COLUMN'
}
fzero_function={
    'fzero':'FZERO','fzero_function':'FZERO_FUNCTION'
}
fpen_function={
    'max':'MAX','abs':'ABS','fpen_function':'FPEN_FUNCTION','fpen':'FPEN'
}
diagonal_matrix={
    'lambda_':'LAMBDA_','diagonal_matrix':'DIAGONAL_MATRIX'
}
sign_function={
    'sign_':'SIGN_','sign_function':'SIGN_FUNCTION','x_col':'X_COL'
}
x_hat_function={
     'x_hat':'X_HAT','ndarray':'NDARRAY','x_hat_function':'X_HAT_FUNCTION'
}
c1_value_function={
    'c1_value_function':'C1_VALUE_FUNCTION','x_coluna':'X_COLUNA','c1':'C1'
}
c2_value_function={
    'c2_value':'C2_VALUE','c2_value_function':'C2_VALUE_FUNCTION','c2':'C2'
}
tosz_function={
    'sin':'SIN','c1':'C1_value','c2':'C2_value',
    'tosz_function':'TOSZ_FUNCTION','exp':'EXP','tosz':'TOSZ','signal':'SIGNAL','hat':'HAT'
}
zi_function={
    'productQ_tosz':'PRODUCTQ_TOSZ','productLambda_q':'PRODUCTLAMBDA_Q',
   'zi_function':'ZI_FUNCTION','zi':'ZI','diagonal':'DIAGONAL'
}

weierstrass_function={
   'weierstrass_function':'WEIERSTRASS_FUNCTION','fx':'FX','weier':'WEIER'
}

coco_reshape = {
    'coco_reshape':'COCO_RESHAPE','B':'B_',
    'i':'INCREMENTO','j':'J','vetor':'VETOR','m':'M_','n':'N','gvect':'GVECT'
}

coco_rand_gauss = {

    'g':'G','coco_rand_gauss':'COCO_RAND_GAUSS','e':'CONST','uniftmp_':'UNIFTMP_'

}
gvector_generator={
   'gvector_generator':'GVECTOR_GENERATOR','x_vector':'X_VECTOR','x':'X_'
}

reserved ={

    'enumerate':'ENUMERATE','len':'LEN','if':'IF','else':'ELSE','np':'NP','sign':'SIGN','size':'SIZE','random':'RANDOM','uniform':'UNIFORM','return':'RETURN','dtype':'DTYPE','global':'GLOBAL',
    'float64':'FLOAT64','numpy':'NUMPY','import':'IMPORT','from':'FROM','ones':'ONES','for':'FOR','pass':'PASS','elif':'ELIF',
    'in':'IN','range':'RANGE', 'sqrt':'SQRT','fabs':'FABS','log':'LOG','math':'MATH','def':'DEF','break':'BREAK','or':'OR','and':'AND',
    'as':'AS','cos':'COS','acos':'ACOS','zeros':'ZEROS','pow':'POW','input':'INPUT','int':'INT_math','continue':'CONTINUE','not':'NOT',
    '__name__':'__NAME__', '__main__':'__MAIN__', 'append':'APPEND','1e':'Elog', 'print':'PRINT','object':'OBJECT','dot':'DOT_math','pi':'PI','float':'FLOAT_'
}
functions_list = list(coco_rand_gauss.values())+\
                 list(reserved.values())+\
                 list(coco_rand_uniform.values())+list(coco_reshape.values())+list(rotacao_gaussiana.values())+\
                 list(diagonal_matrix.values())+list(gvector_generator.values())+\
                 list(fpen_function.values())+list(fzero_function.values())+list(x_column.values())+\
                 list(sign_function.values())+list(x_hat_function.values())+list(c1_value_function.values())+\
                 list(c2_value_function.values())+list(tosz_function.values())+\
                 list(zi_function.values())+list(weierstrass_function.values())

tokens = ['PLUS', 'MINUS', 'MUL', 'DIVIDE','NEWLINE', 'LPAREN', 'RPAREN','LBRACKET','RBRACKET', 'DIF','BARRAIG',
          'EQUAL', 'LT', 'GT', 'EQ', 'FLOAT', 'INT','IDENTIFIER', 'COLON', 'QUOTE', 'COMMA','COMNT','DOT','BARRA','POTENC',
          'COMPARISON','STRING','WHSPACE','TRACEQUAL','RESERVED','IGUALPERCENT','MINUSEQUAL','SEMI',]+functions_list

#t_EQ  = r'=='


t_ignore_COMMENT = r'\#.*'

def t_DIF(t):
    r'\!='
    return t

def t_STRING(t):
	r'(\"(\\.|[^\"\n]|(\\\n))*\") | (\'(\\.|[^\'\n]|(\\\n))*\')'
	return t


def t_MINUSEQUAL(t):
    r'-='
    return t


def t_BARRAIG(t):
    r'/='
    return t

def t_COLON(t):
    r':'
    return t

def t_COMMA(t):
    r','
    return t

def t_SEMI(t):
    r';'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_MINUS(t):
    r'\-'
    return t

def t_MUL(t):
    r'\*'
    return t

def t_DIVIDE(t):
    r'/'
    return t

def t_BARRA(t):
    r'\|'
    return t

def t_LT(t):
    r'<'
    return t

def t_GT(t):
    r'>'
    return t

def t_EQUAL(t):
    r'='
    return t


def t_DOT(t):
    r'\.'
    return t

def t_QUOTE(t):
    r'\''
    return t

def t_POTENC(t):
    r'\^'
    return t

def t_LPAREN(t):
    r"\("
    return t

def t_RPAREN(t):
    r"\)"
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_COMNT(t):
    r'\#.*'
    pass

def t_FLOAT(t):
    r'\d(\d)*\.\d(\d)*'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9_]*'
    if t.value in coco_rand_gauss:
        t.type = coco_rand_gauss.get(t.value)
        return t
    elif (t.value in coco_rand_uniform):
        t.type = coco_rand_uniform.get(t.value)
        return t
    elif (t.value in coco_reshape):
        t.type = coco_reshape.get(t.value)
        return t
    elif (t.value in rotacao_gaussiana):
        t.type = rotacao_gaussiana.get(t.value)
        return t
    elif (t.value in diagonal_matrix):
        t.type = diagonal_matrix.get(t.value)
        return t
    elif (t.value in fzero_function):
        t.type = fzero_function.get(t.value)
        return t
    elif (t.value in gvector_generator):
        t.type = gvector_generator.get(t.value)
        return t
    elif (t.value in fpen_function):
        t.type = fpen_function.get(t.value)
        return t
    elif (t.value in x_column):
        t.type = x_column.get(t.value)
        return t
    elif (t.value in sign_function):
        t.type = sign_function.get(t.value)
        return t
    elif (t.value in x_hat_function):
        t.type = x_hat_function.get(t.value)
        return t
    elif (t.value in c1_value_function):
        t.type = c1_value_function.get(t.value)
        return t
    elif (t.value in c2_value_function):
        t.type = c2_value_function.get(t.value)
        return t
    elif (t.value in tosz_function):
        t.type = tosz_function.get(t.value)
        return t
    elif (t.value in zi_function):
        t.type = zi_function.get(t.value)
        return t
    elif (t.value in weierstrass_function):
        t.type = weierstrass_function.get(t.value)
        return t
    else:
        t.type = reserved.get(t.value, "IDENTIFIER")
        return t


#https://docs.python.org/2/reference/lexical_analysis.html - identacao

def t_WHSPACE(t):

    r" [ \t\f]+"
    value = t.value
    value = value.rsplit("\f", 1)[-1]
    pos = 0
    while True:
        pos = value.find("\t")
        if pos == -1:
            break
        n = 8 - (pos % 8)
        value = value[:pos] + " " * n + value[pos + 1:]
    t.value = value
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def inputFile(path):

    list_path = []
    number_file = ''
    input_choose = False
    cont = 1

    for base, dirs, files in os.walk(path):
        list_path.append(files)
    for file in files:
        print (str(cont)+'. '+file)
        cont = cont+1

    while input_choose == False:
        number_file = input('\nNumber:')
        for file in files:
            if file == files[int(number_file)-1]:
                input_choose = True
                break
    return files[int(number_file)-1]


##INSERIR DIRETÓRIO ONDE SE ENCONTRA O ARQUIVO (está dentro de FILES) basta especificar o diretório files e ecolher
##weierstrassFunction.py

if __name__=='__main__':

    lexer = lex.lex()

    path= 'C:\\Users\\Ariadne\\PycharmProjects\\Weierstrass\\AnalisadorLex\\Files\\'
    file = inputFile(path)
    test = path+file
    fp = codecs.open(test,'r','utf-8')
    code = fp.read()
    fp.close()
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok: break
        print(f'{tok.type:20} | {tok.value:20} |{tok.lineno:10d} | {tok.lexpos:10d}')

