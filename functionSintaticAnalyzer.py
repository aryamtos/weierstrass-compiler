''''
# Ariadne Nascimento Matos
# Matrícula: 201711751
# Professor: Dr Paulo André Sperandio Giacomin
# Disciiplina: Compiladores  Assunto: Analisador Sintático

#Informações:

1. A gramática aqui utilizada é específica somente para o programa, uma vez que, foi criada uma tabela própria pra cada
identificador da função

2. Portanto, ao inserir identificadores "estranhos", ela não aceita

3. Por esse motivo, ela é extensa (pois é específica somente para essa função dentro do python)

4. Os Warnings na geração do parser.out são avisos da gramática, uma vez que, ela foi adaptada para gerar pequenos comandos
por linha também, mas em geral ela funciona para o arquivo da função: weierstrassFunction.py

5. Para esse programa executar é necessário importar os tokens presentes no arquivo FunctionLexicalAnalyzer.py

6. Ao final no main desse programa, basta inserir o diretório referente ao programa weierstrassFunction.py presente na pasta
Files

'''

from functionLexicalAnalyzer import tokens
import ply.yacc as yacc


precedence = (
    ('nonassoc','DIF'),
    ('nonassoc','LT','GT','EQ'),
    ('left','PLUS','MINUS'),
    ('left','MUL','DIVIDE'),
    ('left','RPAREN','LPAREN'),
    ('right','UMINUS'),
    )


names = { }

def p_statement_compound(p):
    '''stmt_compound :
                     | coco_rand_gauss
                     | coco_reshape
                     | coco_rand_uniform
                     | diagonal_matrix
                     | c1_value_function
                     | c2_value_function
                     | tosz_function
                     | weierstrass_function
                     | if_main
                     | zi_function
                     | input_def
                     | x_hat_function
                     | sign_function
                     | fpen_function
                     | x_column
                     | fzero_function
                     | gvector_generator
                     | rotacao_gaussiana
                     | callFunction
                     | for_stmt
                     | for_gauss
                     | if_stmt_g
                     | print_stmt
                     | call_main
                     | call_main2
                     | call_main3
                     | from_stmt
                     | import_stmt
                     | return_stmt'''

def p_statement_assign(p):
    '''statement : IDENTIFIER EQUAL IDENTIFIER
                 | IDENTIFIER EQUAL expression
                 | LOW EQUAL IDENTIFIER
                 | LOW EQUAL expression
                 | HIGH EQUAL expression
                 | G EQUAL np_ones
                 | PRODUCTQ_TOSZ EQUAL Q DOT DOT_math LPAREN TOSZ RPAREN
                 | PRODUCTLAMBDA_Q EQUAL DIAGONAL DOT DOT_math LPAREN  PRODUCTQ_TOSZ RPAREN
                 | ZI EQUAL R_ DOT DOT_math LPAREN PRODUCTLAMBDA_Q RPAREN
                 | matriz EQUAL INT CONST MINUS INT
                 | matriz EQUAL FLOAT
                 | matriz EQUAL INT
                 | X_HAT LBRACKET INCREMENTO RBRACKET EQUAL INT
                 | FX EQUAL INT MUL math_pow1 PLUS LPAREN LPAREN INT DIVIDE DIM RPAREN MUL FPEN RPAREN
                 | matriz EQUAL matriz
                 | matriz MINUSEQUAL PRODUTO MUL matriz
                 | g EQUAL callFunction
                 | X_VECTOR EQUAL callFunction
                 | R_ EQUAL callFunction
                 | FPEN EQUAL callFunction
                 | X_COLUNA EQUAL callFunction
                 | C1 EQUAL callFunction
                 | C2 EQUAL callFunction
                 | C1 EQUAL np_ndarray
                 | TOSZ EQUAL np_ndarray
                 | HAT EQUAL callFunction
                 | SIGNAL EQUAL callFunction
                 | TOSZ EQUAL callFunction
                 | ZI EQUAL callFunction
                 | Q EQUAL callFunction
                 | WEIER EQUAL callFunction
                 | FZERO EQUAL callFunction
                 | LAMBDA_ EQUAL callFunction
                 | matriz EQUAL matriz MUL matriz
                 | PRODUTO EQUAL INT
                 | WEIER EQUAL INT
                 | WEIER EQUAL WEIER PLUS math_pow MUL math_cos MINUS math_pow MUL math_cos
                 | PRODUTO PLUSEQUAL matriz MUL matriz
                 | matriz SLASHEQUAL expression
                 | FZERO EQUAL math_pow MUL LPAREN math_cos MUL expression RPAREN
                 | LAMBDA_ EQUAL np_zeros
                 | UNIFTMP_ EQUAL callFunction
                 | matriz EQUAL math_pow
                 | matriz EQUAL  ABS LPAREN matriz RPAREN
                 | FPEN EQUAL INT
                 | FLOAT EQUAL expression
                 | INT EQUAL expression
                 | FPEN EQUAL math_pow
                 | X_VECTOR EQUAL LBRACKET RBRACKET
                 | SIGN_ EQUAL np_sign
                 | statement EQUAL np_ndarray
                 | matriz EQUAL matriz MUL math_exp
                 | X_HAT LBRACKET INCREMENTO RBRACKET EQUAL math_log
                 | DIM EQUAL INT_math expression
                 | DIM EQUAL INT_math LPAREN input_def RPAREN
                 | SEED_R EQUAL INT_math LPAREN input_def RPAREN
                 | SEED_Q EQUAL INT_math LPAREN input_def RPAREN
                 | X_VECTOR DOT APPEND LPAREN math_float RPAREN
                 | R_ DOT math_dot
                 '''

    names[p[1]] = p[3]

def p_import_stmt(p):
    """import_stmt : IMPORT NUMPY AS NP from_stmt
                   | IMPORT NUMPY AS NP
                   | import_stmt coco_rand_uniform """
    print(p[1], p[2], p[3], p[4])

def p_from_stmt(p):
    """from_stmt : FROM NUMPY IMPORT MUL coco_rand_uniform
                 | FROM NUMPY IMPORT MUL """
    print(p[1], p[2], p[3], p[4])


def p_statement_expr(p):
    """statement : expression
                 | UNIFTMP
                 | G
                 | M_
                 | g
                 | C1
                 | N
                 | R_
                 | SIGNAL
                 | DIM
                 | X_HAT
                 | TOSZ
                 | Q
                 | K
                 | B_
                 | X_
                 | SEED_R
                 | SEED_Q
                 | X_COL
                 | FX
                 | X_COLUNA
                 | PRODUCTQ_TOSZ
                 | PRODUCTLAMBDA_Q
                 | WEIER
                 | DIAGONAL
                 | ZI
                 | C2_VALUE
                 | LAMBDA_
                 | FZERO
                 | matriz
                 | PRODUTO
                 | SIGN_
                 | FPEN
                 | X_VECTOR
                 | comp_logic
                 | npFloat64
                 | math_acos
                 | math_max
                 | math_sqrt
                 | math_cos
                 | math_log
                 | math_dot
                 | math_sin
                 | math_exp
                 | np_ndarray
                 | math_abs
                 | math_float
                 | math_op
                 | np_zeros
                 | math_pow1
                 | math_pow
                 | np_random
                 | np_sign
                 | np_ones """
    print('Definições')

def p_matriz(p):

    """ matriz : G LBRACKET INT RBRACKET
               | G LBRACKET INT RBRACKET LBRACKET INCREMENTO RBRACKET
               | G LBRACKET INT RBRACKET LBRACKET INT RBRACKET
               | UNIFTMP_ LBRACKET INT RBRACKET LBRACKET INT RBRACKET
               | X_VECTOR LBRACKET INCREMENTO RBRACKET
               | g LBRACKET K RBRACKET LBRACKET INCREMENTO RBRACKET
               | X_HAT LBRACKET INCREMENTO RBRACKET
               | g LBRACKET K RBRACKET LBRACKET J RBRACKET
               | C2_VALUE LBRACKET INCREMENTO RBRACKET
               | TOSZ LBRACKET INCREMENTO RBRACKET
               | C2 LBRACKET INCREMENTO RBRACKET
               | SIGNAL LBRACKET INCREMENTO RBRACKET
               | ZI LBRACKET INCREMENTO RBRACKET
               | X_COL LBRACKET INCREMENTO RBRACKET
               | B_ LBRACKET INCREMENTO RBRACKET LBRACKET J RBRACKET
               | C1 LBRACKET INCREMENTO RBRACKET
               | VETOR LBRACKET INT RBRACKET LBRACKET J MUL M_ PLUS INCREMENTO RBRACKET
               | UNIFTMP_ LBRACKET INT RBRACKET LBRACKET INCREMENTO RBRACKET
               | LAMBDA_ LBRACKET INCREMENTO RBRACKET LBRACKET INCREMENTO RBRACKET
               | UNIFTMP_ LBRACKET INT RBRACKET LBRACKET DIM PLUS INCREMENTO RBRACKET"""

    print('Matriz e vetor')

def p_call_Function(p):
    '''callFunction : COCO_RAND_UNIFORM expression
                    | COCO_RAND_GAUSS expression
                    | GVECTOR_GENERATOR expression
                    | FPEN_FUNCTION expression
                    | ROTACAO_GAUSSIANA expression
                    | FZERO_FUNCTION expression
                    | C1_VALUE_FUNCTION expression
                    | C2_VALUE_FUNCTION expression
                    | TOSZ_FUNCTION expression
                    | SIGN_FUNCTION expression
                    | ZI_FUNCTION expression
                    | X_COLUMN expression
                    | DIAGONAL_MATRIX expression
                    | X_HAT_FUNCTION expression
                    | COCO_RESHAPE expression
                    | WEIERSTRASS_FUNCTION expression'''
    print(p[1])

def p_math_log(p):
    """math_log : LOG LPAREN matriz RPAREN
                | LOG LPAREN X_HAT PLUS FLOAT RPAREN
                | LOG LPAREN math_abs RPAREN"""
    print('log( matriz) ')

def p_math_sqrt(p):
    """math_sqrt : SQRT LPAREN FABS LPAREN MINUS FLOAT MUL math_log RPAREN RPAREN"""
    print(p[1], p[2], p[3], p[4], p[5], p[6], p[7], 'log(uniftmp_[0][i])', p[9], p[10])

def p_math_pow1(p):
    """math_pow1 : POW LPAREN LPAREN INT DIVIDE DIM RPAREN MUL WEIER COMMA INT RPAREN"""
    print(p[1], [2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10])

def p_math_pow(p):
    """math_pow : POW LPAREN FLOAT COMMA expression MUL expression RPAREN
                | POW LPAREN math_max COMMA INT RPAREN
                | POW LPAREN expression COMMA expression RPAREN
                | POW LPAREN expression COMMA K RPAREN
                | POW LPAREN INT MUL PI MUL INT COMMA K RPAREN"""
    print(p[1], p[2], 'expression', p[4], p[5], p[6], 'Pow math')


def p_math_sin(p):
    """math_sin :
                | SIN LPAREN matriz MUL matriz RPAREN
                | SIN LPAREN statement RPAREN"""

    print(p[1],p[2],'expression',')','SIN math')

def p_math_exp(p):
    """math_exp : EXP LPAREN matriz PLUS FLOAT MUL LPAREN math_sin PLUS math_sin RPAREN RPAREN"""
    print(p[1], p[2], 'matriz', p[4], p[5], p[6], p[7], 'sin(c1[i] * x_hat[i])', p[9], 'sin(c2[i] * x_hat[i])', p[11],p[12])

def p_math_acos(p):

    """math_acos : MATH DOT ACOS LPAREN MINUS INT RPAREN"""
    print(p[1], p[2], p[3], p[4], p[5], p[6], p[7])

def p_math_cos(p):
    """math_cos : COS LPAREN FLOAT MUL math_acos MUL matriz RPAREN
                | COS LPAREN math_pow RPAREN
                | COS LPAREN math_pow MUL expression RPAREN
                | COS LPAREN math_pow MUL LPAREN matriz PLUS expression RPAREN RPAREN"""
    print(p[1], p[2], 'expression', ')', 'COS math')

def p_math_abs(p):
    """math_abs : ABS LPAREN matriz RPAREN"""
    print(p[1], p[2], 'matriz', p[4])

def p_math_max(p):
    '''math_max : MAX LPAREN INT COMMA math_abs expression RPAREN
                | MAX LPAREN INT COMMA expression RPAREN'''
    print(p[1], p[2], p[3], p[4], 'expression', ')', 'MAX math')

def p_math_op(p):
    """math_op : math_sqrt MUL math_cos"""
    print('sqrt(expression)', p[2], 'cos(expression)')

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIVIDE expression'''
    print('Operações Aritméticas')

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]


def p_expression_group(p):
    '''expression : LPAREN expression RPAREN
                  | LPAREN IDENTIFIER RPAREN
                  | LPAREN LOW RPAREN
                  | LPAREN DIM COMMA SEED RPAREN
                  | LPAREN INPUT LPAREN  STRING  RPAREN RPAREN
                  | LPAREN DIM MUL DIM COMMA SEED RPAREN
                  | LPAREN GVECT COMMA DIM COMMA DIM RPAREN
                  | LPAREN TOSZ COMMA Q COMMA R_ COMMA DIAGONAL RPAREN
                  | LPAREN TOSZ COMMA Q COMMA R_ COMMA LAMBDA_ RPAREN
                  | LPAREN LOW EQUAL FLOAT COMMA HIGH EQUAL LPAREN SEED RPAREN COMMA SIZE EQUAL expression RPAREN
                  | LPAREN SEED RPAREN
                  | LPAREN M_ RPAREN
                  | LPAREN N RPAREN
                  | LPAREN X_COLUNA RPAREN
                  | LPAREN X_COLUNA COMMA DIM RPAREN
                  | LPAREN RPAREN
                  | LPAREN DIM COMMA C1 COMMA C2 COMMA SIGNAL COMMA X_HAT RPAREN
                  | LPAREN DIM COMMA C1 COMMA C2 COMMA SIGNAL COMMA HAT RPAREN
                  | LPAREN DIM RPAREN
                  | LPAREN DIM COMMA DIM RPAREN
                  | LPAREN INCREMENTO RPAREN
                  | LPAREN INT RPAREN
                  | LPAREN HIGH RPAREN
                  | LPAREN SIZE RPAREN
                  | LPAREN DIM COMMA X_VECTOR RPAREN
                  | LPAREN DIM COMMA ZI COMMA FPEN RPAREN
                  | LPAREN INCREMENTO MINUS INT RPAREN
                  | LPAREN DIM MINUS INT RPAREN
                  | LPAREN INT MUL DIM COMMA SEED RPAREN
                  | LPAREN DIM COMMA SEED_R RPAREN
                  | LPAREN DIM COMMA SEED_Q RPAREN
                  | LPAREN INT  COMMA DIM RPAREN
                  | LPAREN M_ COMMA N RPAREN
                  | LPAREN VETOR COMMA M_ COMMA N RPAREN
                  | LPAREN X_COL RPAREN
                  | LPAREN X_COL COMMA DIM RPAREN
                  | LPAREN R_ COMMA X_VECTOR RPAREN
                  | SQRT LPAREN FABS LPAREN PRODUTO RPAREN RPAREN'''
    #p[0] = p[2]
    print(p[1], p[2], ')', 'Parâmetros')

def p_expression_float(p):
    'expression : FLOAT'
    p[0] = p[1]

def p_expression_int(p):
    'expression : INT'
    p[0] = p[1]

def p_for_gauss(p):
    '''for_gauss : FOR INCREMENTO IN RANGE expression COLON matriz EQUAL math_op if_stmt_g
                 | FOR INCREMENTO IN RANGE expression COLON matriz EQUAL math_op'''
    print(p[1],p[2],p[3],p[4],'(dim)',p[6],'matriz',p[8],'sqrt(expression)*cos(expression)')


def p_for_stmt(p):
    '''for_stmt : FOR INCREMENTO IN RANGE expression COLON PASS
                | FOR J IN RANGE expression COLON return_stmt
                | FOR INCREMENTO IN RANGE expression COLON statement
                | FOR INCREMENTO IN RANGE expression COLON for_stmt
                | FOR K IN RANGE expression COLON return_stmt
                | FOR K IN RANGE expression COLON for_stmt
                | FOR K IN RANGE expression COLON statement
                | FOR J IN RANGE expression COLON statement
                | FOR J IN RANGE expression COLON for_stmt
                | FOR INCREMENTO IN RANGE expression COLON if_stmt_g
                | FOR INCREMENTO IN RANGE expression COLON stmt_compound'''

    print(p[1], p[2], p[3], p[4], '(dim):')

def p_math_dot(p):
    """math_dot : DOT_math LPAREN statement RPAREN """
    print(p[1], p[2], 'statement', p[4])

def p_math_float(p):
    '''math_float : FLOAT_ LPAREN RPAREN
                  | FLOAT_ LPAREN input_def RPAREN'''

    print(p[1], p[2], 'input())')

def p_expression_npFloat(p):
    '''npFloat64 : DTYPE EQUAL NP DOT FLOAT64'''

    print(p[1], p[2], p[3], p[4], p[5])

def p_np_sign(p):
    """np_sign : NP DOT SIGN LPAREN statement RPAREN"""

    print(p[1], p[2], p[3], p[4], 'statement', p[6])

def p_np_Zeros(p):
    '''np_zeros :  NP DOT ZEROS LPAREN expression COMMA npFloat64 RPAREN'''

    print(p[1], p[2], p[3], p[4], 'expression', p[6], 'dtype=np.float64', p[8])

def p_np_ones(p):
    '''np_ones : NP DOT ONES LPAREN statement COMMA npFloat64 RPAREN'''

    print(p[1], p[2], p[3], p[4], 'statement', p[6], 'dtype=np.float64', p[8])

def p_np_ndarray(p):
    """np_ndarray : NP DOT NDARRAY LPAREN statement COMMA npFloat64 RPAREN"""
    print(p[1],p[2],p[3],p[4],'statement',p[6],'dtype=np.float64',p[8])

def p_np_random(p):
    '''np_random : NP DOT RANDOM DOT UNIFORM expression '''
    print(p[1],p[2],p[3],p[4],p[5],'(expression)')


def p_coco_rand_gauss(p):
    '''coco_rand_gauss : DEF COCO_RAND_GAUSS expression COLON statement statement for_gauss
                       | DEF COCO_RAND_GAUSS expression COLON statement statement'''
    print(p[1], p[2], '(params)', p[4])

def p_coco_rand_uniform(p):

    '''coco_rand_uniform : DEF COCO_RAND_UNIFORM expression COLON  UNIFTMP EQUAL np_random return_stmt coco_rand_gauss
                         | DEF COCO_RAND_UNIFORM expression COLON  PASS
                         | DEF COCO_RAND_UNIFORM expression COLON  UNIFTMP EQUAL np_random return_stmt
                         | DEF COCO_RAND_UNIFORM expression COLON return_stmt
                         | DEF COCO_RAND_UNIFORM expression COLON statement'''
    print(p[1], p[2], '(params)', p[4])

def p_diagonal_matrix(p):
    """diagonal_matrix : DEF DIAGONAL_MATRIX expression COLON statement for_stmt return_stmt fzero_function
                       | DEF DIAGONAL_MATRIX expression COLON statement
                       | DEF DIAGONAL_MATRIX expression COLON PASS
                       | DEF DIAGONAL_MATRIX expression COLON return_stmt"""
    print(p[1], p[2], '(params)', p[4])


def p_rotacao_gaussiana(p):
    """rotacao_gaussiana : DEF ROTACAO_GAUSSIANA expression COLON GVECT EQUAL callFunction statement for_stmt for_stmt for_stmt statement for_stmt for_stmt return_stmt diagonal_matrix
                         | DEF ROTACAO_GAUSSIANA expression COLON  statement"""
    print(p[1], p[2], '(params)', p[4])

def p_fzero_function(p):
    """fzero_function : DEF FZERO_FUNCTION expression COLON for_stmt gvector_generator """
    print(p[1], p[2], '(params)', p[4])

def p_expression_return_stmt(p):

    '''return_stmt : RETURN
                   | RETURN statement
                   '''
    print(p[1],'statement')

def p_coco_reshape(p):
    """coco_reshape : DEF COCO_RESHAPE expression COLON B_ EQUAL np_ones for_stmt return_stmt rotacao_gaussiana
                    | DEF COCO_RESHAPE expression COLON B_ EQUAL np_ones
                    | DEF COCO_RESHAPE expression COLON PASS
                    | DEF COCO_RESHAPE expression COLON statement"""
    print(p[1], p[2], '(params)', p[4], p[5], p[6], 'np.ones((m,n),dtype=np.float64)')

def p_gvector_generator(p):
    """gvector_generator : DEF GVECTOR_GENERATOR expression COLON statement for_stmt return_stmt fpen_function
                         | DEF GVECTOR_GENERATOR expression COLON statement"""
    print(p[1], p[2], '(params)', p[4])

def p_com_logic(p):
    """comp_logic : LT
                  |  GT
                  | DIF
                  | EQ"""

    print('Logic Operators')

def p_if_stmt(p):
    """if_stmt_g : IF LPAREN matriz EQUAL EQUAL INT DOT RPAREN COLON statement return_stmt coco_reshape
                 | IF LPAREN statement EQUAL EQUAL INT DOT RPAREN COLON statement return_stmt
                 | IF LPAREN expression RPAREN COLON statement
                 | IF LPAREN expression RPAREN COLON PASS
                 | IF LPAREN statement comp_logic INT RPAREN COLON statement ELSE COLON statement
                 | IF LPAREN statement comp_logic INT RPAREN COLON statement ELSE COLON statement return_stmt
                 | IF LPAREN statement comp_logic INT RPAREN COLON statement  """
    print(p[1], p[2], 'statement):')


def p_input_def(p):
    """input_def : INPUT LPAREN RPAREN
                 | INPUT LPAREN  STRING  RPAREN"""
    print(p[1], p[2], ')')

def p_fpen_function(p):
    """fpen_function : DEF FPEN_FUNCTION expression COLON statement for_stmt return_stmt x_column
                     | DEF FPEN_FUNCTION expression COLON statement
                     | DEF FPEN_FUNCTION expression COLON PASS
                     | DEF FPEN_FUNCTION expression COLON return_stmt
                     | DEF FPEN_FUNCTION expression COLON stmt_compound"""
    print(p[1], p[2], '(params)', p[4])

def p_x_column(p):
    """x_column : DEF X_COLUMN expression COLON return_stmt sign_function
                | DEF X_COLUMN expression COLON statement
                | DEF X_COLUMN expression COLON stmt_compound """
    print(p[1], p[2], '(params)', p[4])

def p_sign_function(p):
    """sign_function : DEF SIGN_FUNCTION expression COLON statement return_stmt x_hat_function
                     | DEF SIGN_FUNCTION expression COLON statement return_stmt
                     | DEF SIGN_FUNCTION expression COLON statement """
    print(p[1], p[2], '(params)', p[4])

def p_x_hat_function(p):
    """ x_hat_function : DEF X_HAT_FUNCTION expression COLON statement for_stmt c1_value_function
                       | DEF X_HAT_FUNCTION expression COLON statement return_stmt
                       | DEF X_HAT_FUNCTION expression COLON statement"""
    print(p[1], p[2], '(params)', p[4])

def p_c1_value_function(p):
    """c1_value_function : DEF C1_VALUE_FUNCTION expression COLON statement for_stmt c2_value_function
                         | DEF C1_VALUE_FUNCTION expression COLON statement
                         | DEF C1_VALUE_FUNCTION expression COLON return_stmt """
    print(p[1], p[2], '(params)', p[4])

def p_c2_value_function(p):
    """c2_value_function : DEF C2_VALUE_FUNCTION expression COLON statement for_stmt tosz_function
                         | DEF C2_VALUE_FUNCTION expression COLON statement
                         | DEF C2_VALUE_FUNCTION expression COLON return_stmt"""
    print(p[1], p[2], '(params)', p[4])

def p_tosz_function(p):
    """tosz_function : DEF TOSZ_FUNCTION expression COLON statement for_stmt return_stmt zi_function
                     | DEF TOSZ_FUNCTION expression COLON statement
                     | DEF TOSZ_FUNCTION expression COLON return_stmt"""
    print(p[1], p[2], '(params)', p[4])

def p_zi_function(p):
    """zi_function : DEF ZI_FUNCTION expression COLON statement statement statement return_stmt weierstrass_function
                   | DEF ZI_FUNCTION expression COLON statement
                   | DEF ZI_FUNCTION expression COLON return_stmt"""
    print(p[1], p[2], '(params)', p[4])

def p_weierstrass_function(p):
    """weierstrass_function : DEF WEIERSTRASS_FUNCTION expression COLON statement for_stmt statement return_stmt if_main
                            | DEF WEIERSTRASS_FUNCTION expression COLON statement for_stmt statement return_stmt call_main3
                            | DEF WEIERSTRASS_FUNCTION expression COLON statement return_stmt
                            | DEF WEIERSTRASS_FUNCTION expression COLON statement for_stmt statement return_stmt"""
    print(p[1], p[2], '(params)', p[4])

def p_print_stmt(p):
  """print_stmt : PRINT LPAREN STRING COMMA X_VECTOR RPAREN
                | PRINT LPAREN STRING COMMA R_ RPAREN
                | PRINT LPAREN STRING COMMA Q RPAREN
                | PRINT LPAREN LAMBDA_ RPAREN
                | PRINT LPAREN STRING RPAREN
                | PRINT LPAREN STRING COMMA TOSZ RPAREN
                | PRINT LPAREN STRING COMMA ZI RPAREN
                | PRINT LPAREN STRING COMMA WEIER RPAREN"""
  print(p[1],p[2],p[3],')')

def p_if_main(p):
    """if_main : IF __NAME__ EQUAL EQUAL  STRING  COLON statement statement print_stmt statement statement
               | IF __NAME__ EQUAL EQUAL STRING COLON statement statement statement
               | IF __NAME__ EQUAL EQUAL STRING COLON statement
               | IF __NAME__ EQUAL EQUAL STRING COLON PASS
               """
    print('if __name__ == __main__')

def p_call_main(p):
    """call_main : if_main statement statement statement print_stmt print_stmt print_stmt """
    print('Call Main1')

def p_call_main2(p):
    """call_main2 : call_main statement statement statement statement statement statement statement statement statement"""
    print('Call main Function2')

def p_call_main3(p):
    """ call_main3 : call_main2 print_stmt print_stmt statement print_stmt
                   | call_main2 print_stmt
    """
    print('Call main Function3')

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    try:
        p[0] = names[p[1]]
    except LookupError:
        print(f"Undefined name {p[1]!r}")
        p[0] = 0

def p_error(p):
    print(f"Syntax error at {p.value!r}")


yacc.yacc()

if __name__=="__main__":

    #iNSERIR DIRETÓRIO ONDE ESTÁ LOCALIZADO O WEIERSTRASSFUNCTION.py
    filename = 'diretorio'
    source = open(filename)
    data = source.read()
    yacc.parse(data)
    '''
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        yacc.parse(s)
    '''
