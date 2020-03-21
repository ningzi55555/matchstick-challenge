'''
移动一根火柴
ref存储每一个数增加/移动/减少一根火柴后会变成什么数字,比如ref[0]为{0:(6,9), 1:(8,)}，代表“0”内部移动一根火柴变成“6”和“9”,
“0”增加一根火柴变成“8”. 再比如ref[8]为 {-1:(0,6,9)},代表"8"减少一根火柴可以变成“0”,“6”,“9”
'''

ref=({0:(6,9), 1:(8,)},  {1:(7,)},  {0:(3,)},  {0:(2,5), 1:(9,)},  {},
    {1:(6,9), 0:(3,)},  {-1:(5,), 0:(0,9), 1:(8,)},  {-1:(1,)},  {-1:(0,6,9)},  {0:(0,6), 1:(8,), -1:(3,5)})

#formula[0:1]为第一个数字，formula[2:3]为第二个数字，formula[4:8]为第三个数字（结果），若高位不存在用''表示
#formula[8]为运算符，minus[0]为第一个数字的负号，minus[1]为第二个数字的负号，若数字为正则用''表示
#测试移动一根火柴后的式子是否成立，若成立则return True
def test(formula,minus):
    if(formula[0]==''):
        num1=formula[1]
    else:
        num1=formula[0]*10+formula[1]
    if (formula[2] == ''):
        num2 = formula[3]
    else:
        num2 = formula[2] * 10 + formula[3]
    len_num3=4
    while formula[len_num3]=='':
        len_num3+=1
    num3=0
    for i in range(len_num3,8):
        num3=num3*10+formula[i]
    if(minus[0]=='-'):
        minus[0]='-'
        num1=-num1

    if (minus[1]=='-'):
        minus[1] = '-'
        num3 = -num3

    if(formula[8]=='+'):
        if(num1+num2==num3):
            return True
        else:
            return False
    if (formula[8] == '-'):
        if (num1 - num2 == num3):
            return True
        else:
            return False
    if (formula[8] == '*'):
        if (num1 * num2 == num3):
            return True
        else:
            return False

#若test(formula,minus) return True，等式成立，将其存入result中
def print_formula(formula,result,minus):
    for i in range(9):
        if((i==0 and minus[0]=='-') or (i == 4 and minus[1] == '-')):
            result.append('-')
        elif((i==0 and minus[0]=='') or (i == 4 and minus[1] == '')):
            result.append('')
        result.append(formula[i])

#此处num1(operator)num2=num3，由这四个数字或符号生成formula和minus
def init_formula(num1,num2,num3,operator,minus):
    formula=[0,1,2,3,4,5,6,7,8]
    num1=int(num1)
    num2=int(num2)
    if(int(num1/10)==0):
        formula[0]=''
        formula[1]=abs(num1)
    else:
        formula[0]=int(abs(num1)/10)
        formula[1]=abs(num1)%10
    if(int(num2/10)==0):
        formula[2]=''
        formula[3]=num2
    else:
        formula[2]=int(num2/10)
        formula[3]=num2%10
    if(num3[0]=='-'):
        len_num3=len(num3)-1
    else:
        len_num3=len(num3)
    for i in range(4-len_num3):
        formula[4+i]=''
    for i in range(len_num3):
        if (num3[0] == '-'):
            formula[7-i]=int(num3[len_num3-i])
        else:
            formula[7 - i] = int(num3[len_num3 - i-1])
    if (num3[0] == '-'):
        minus[1]='-'
    else:
        minus[1]=''
    if(num1<0):
        minus[0]='-'
    else:
        minus[0]=''
    formula[8]=operator
    return formula


#a+b=c，遍历所有情况找到答案
def make_equation(list):
    minus=['','']
    result=[]
    a = list[0]
    operator=list[3]
    b = list[1]
    c = list[2]
    formula=init_formula(a,b,c,operator,minus)
    if (test(formula,minus)):
        print_formula(formula,result,minus)
    for i in range(8):
        if(formula[i]!=''):
            num = formula[i]
            # 第一种情况：在某一个数字内部移动火柴
            if (0 in ref[num]):
                for j in range(len(ref[num][0])):
                    formula[i] = ref[num][0][j]
                    if (test(formula,minus)):
                        print_formula(formula,result,minus)
                        break
                formula[i]=num

            #第二种情况：数字a增加一根火柴，数字b减少一根火柴
            for t in (-1, 1):
                num1 = formula[i]
                if (t in ref[num1]):
                    for k in range(len(ref[num1][t])):
                        formula[i] = ref[num1][t][k]
                        j = i + 1
                        while j < 8:
                            if (formula[j]!=''):
                                num2 = formula[j]
                                if (-t in ref[num2]):
                                    for r in range(len(ref[num2][-t])):
                                        formula[j] = ref[num2][-t][r]
                                        if (test(formula,minus)):
                                            print_formula(formula,result,minus)
                                            break
                                    formula[j]=num2
                            j += 1
                    formula[i]=num1

            #第三种情况：某一个数字减少一根火柴，加到第一或第三个数字的负号位置上
            if (-1 in ref[num]):
                for j in range(len(ref[num][-1])):
                    for x in range(2):
                        if (minus[x] == ''):
                            minus[x] = '-'
                            formula[i] = ref[num][-1][j]
                            if (test(formula, minus)):
                                print_formula(formula, result,minus)
                            minus[x]=''
                    formula[i] = num
            # 第四种情况：第一或第三个数字的负号去掉，某一个数字增加一根火柴
            if (1 in ref[num]):
                for j in range(len(ref[num][1])):
                    for x in range(2):
                        if (minus[x] == '-'):
                            minus[x] = ''
                            formula[i] = ref[num][1][j]
                            if (test(formula, minus)):
                                print_formula(formula, result,minus)
                            minus[x]='-'
                    formula[i] = num

            #第五种情况：运算符若是‘+’，则变成‘-’，某一个数字增加一根火柴
            formula = init_formula(a, b, c, operator,minus)
            if (formula[8] == '+'):
                formula[8] = '-'
                if (1 in ref[num]):
                    for j in range(len(ref[num][1])):
                        formula[i] = ref[num][1][j]
                        if (test(formula,minus)):
                            print_formula(formula,result,minus)
                            break
                    formula[i]=num
                formula[8] = '+'
            # 第六种情况：运算符若是‘-’，则变成‘+’，某一个数字减少一根火柴
            if (formula[8] == '-'):
                formula[8] = '+'
                if (-1 in ref[num]):
                    for j in range(len(ref[num][-1])):
                        formula[i] = ref[num][-1][j]
                        if (test(formula,minus)):
                            print_formula(formula,result,minus)
                            break
                    formula[i]=num
                formula[8] = '-'

    #第七种情况：‘=’变‘-’，‘-’变‘=’
    if ((operator == '-') and (int(a) == int(b) - int(c))):
        for i in range(8):
            if ((i == 0 and minus[0] == '-') or (i == 4 and minus[1] == '-')):
                result.append('-')
            elif ((i == 0 and minus[0] == '') or (i == 4 and minus[1] == '')):
                result.append('')
            result.append(formula[i])
        result.append('=')
    #第八种情况：‘+’变‘-’，加到第一或第三个数字的负号位置上
    if (formula[8] == '+'):
        formula[8]='-'
        for x in range(2):
            if (minus[x] != '-'):
                minus[x] = '-'
                if (test(formula, minus)):
                    print_formula(formula, result,minus)
                minus[x] = ''
            formula[8] = '+'
    #第九种情况：第一或第三个数字的负号去掉，‘-’变‘+’
    if (formula[8] == '-'):
        formula[8]='+'
        for x in range(2):
            if (minus[x] == '-'):
                minus[x] = ''
                if (test(formula, minus)):
                    print_formula(formula, result,minus)
                minus[x] = '-'
            formula[8] = '-'

    #第十种情况：第一个数字的负号移到第三个数字的负号位置上，或第三个数字的负号移到第一个数字的负号位置上
    for y in range(2):
        if(minus[y]=='-' and minus[1-y]==''):
            swap(minus)
            if (test(formula, minus)):
                print_formula(formula, result, minus)
            swap(minus)

    return result

def swap(a):
    tmp=a[0]
    a[0]=a[1]
    a[1]=tmp
    return