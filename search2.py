'''
移动两根火柴
standard里每一个元组代表每一个数字和符号用火柴棍拼成的七位0和1，从左到右分别为0，1，2，3，4，5，6，7，8，9，+，-，*，=
'''

standard=[(1,1,1,1,1,1,0),(0,1,1,0,0,0,0),(1,1,0,1,1,0,1),(1,1,1,1,0,0,1),(0,1,1,0,0,1,1),(1,0,1,1,0,1,1),(1,0,1,1,1,1,1),
          (1,1,1,0,0,0,0),(1,1,1,1,1,1,1),(1,1,1,1,0,1,1),(0,1,0,0,0,0,1),(0,0,0,0,0,0,1),(0,0,1,0,0,1,0),(0,0,0,1,0,0,1)]

#将formula中的数字转化为火柴棍，存进matches中
#formula[0:1]为第一个数字，formula[2:3]为第二个数字，formula[4:8]为第三个数字（结果），若高位不存在用''表示
#formula[8]为运算符，formula[9]为等号，formula[10]为第一个数字的负号，formula[11]为第三个数字的负号，若数字为正则用''表示
#比如-2+3=1，其formula为['', 2, '', 3, '', '', '', 1, '+', '=', '-', '']
def transform(formula):
    matches=[]
    for i in range(12):
        if(formula[i]==''):
            matches.append([0,0,0,0,0,0,0])
        elif(formula[i]=='+'):
            matches.append(list(standard[10]))
        elif(formula[i]=='-'):
            matches.append(list(standard[11]))
        elif(formula[i]=='*'):
            matches.append(list(standard[12]))
        elif(formula[i]=='='):
            matches.append(list(standard[13]))
        else:
            matches.append(list(standard[formula[i]]))
    return matches

#测试移动两根火柴后的式子是否有效，若有效则将火柴棍转化为数字存入new_formula
# new_formula每一位代表的数字或符号与formula一样
def test_matches(matches,new_formula):
    #matches[0:8]是0~9数字中的一个，或者为空字符串''
    for i in range(8):
        flag=False
        if(matches[i]==[0,0,0,0,0,0,0]):
            new_formula[i]=''
            continue
        for j in range(10):
            if(matches[i]==list(standard[j])):
                new_formula[i]=j
                flag=True
                break
        if(flag==False): return False
    if((new_formula[0]=='' and new_formula[1]=='') or (new_formula[2]=='' and new_formula[3]=='') or (new_formula[4]=='' and new_formula[5]==''
    and new_formula[6]=='' and new_formula[7]=='')):
        return False
    for i in range(8,10):
        flag = False
        if (matches[i] == list(standard[10])):
            new_formula[i] = '+'
            flag = True
        if (matches[i] == list(standard[11])):
            new_formula[i] = '-'
            flag = True
        if (matches[i] == list(standard[12])):
            new_formula[i] = '*'
            flag = True
        if (matches[i] == list(standard[13])):
            new_formula[i] = '='
            flag = True
        if(flag==False):
            return False
    for i in range(10,12):
        if(matches[i]==list(standard[11])):
            new_formula[i]='-'
        elif(matches[i]==[0,0,0,0,0,0,0]):
            new_formula[i]=''
        else:
            return False

    if(new_formula[8]=='=' and new_formula[9]=='='):
        return False
    if (new_formula[8] != '=' and new_formula[9] != '='):
        return False
    if(new_formula[8]=='=' and new_formula[11]=='-'):
        return False
    return True

#测试等式是否成立，若成立则return True，就可以输出了，此处的list就是new_formula
def test_equation(list):
    if (list[0] == ''):
        num1 = list[1]
    elif(list[1]==''):
        num1=list[0]
    else:
        num1 = list[0] * 10 + list[1]
    if(list[10]=='-'): num1=-num1

    if (list[2] == ''):
        num2 = list[3]
    elif (list[3] == ''):
        num2 = list[2]
    else:
        num2 = list[2] * 10 + list[3]
    num3=0
    for i in range(4,8):
        if(list[i]!=''):
            num3 = num3 * 10 + list[i]
    if (list[11] == '-'): num3 = -num3
    #当formula[8]由运算符变成等号时，三个数字的顺序需要变化
    if(list[8]=='='):
        tmp1=num2
        num2=num3
        num3=num1
        num1=tmp1
        operator=list[9]
    else:
        operator=list[8]
    if (operator == '+'):
        if (num1 + num2 == num3):
            return True
        else:
            return False
    if (operator == '-'):
        if (num1 - num2 == num3):
            return True
        else:
            return False
    if (operator == '*'):
        if (num1 * num2 == num3):
            return True
        else:
            return False

#此处num1(operator)num2=num3，由这四个数字或符号生成formula
def init_formula(num1,num2,num3,operator):
    formula=[0,1,2,3,4,5,6,7,8,9,10,11]
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
        formula[11]='-'
    else:
        formula[11]=''
    if(num1<0):
        formula[10]='-'
    else:
        formula[10]=''
    formula[8]=operator
    formula[9]='='
    return formula

#四重循环，移动两根火柴等价于matches中的两个1变成0，两个0变成1，每个情况都判断一下等式是否成立，若成立，存入result中
def make_equation2(list):
    a = list[0]
    op = list[3]
    b = list[1]
    c = list[2]
    formula = init_formula(a, b, c, op)
    new_formula = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10,11]
    matches = transform(formula)
    #列表marker标记有哪两个0被转化为1，这样后面循环将1转化为0时就可以跳过这两个1
    marker = [0, 0]
    result = []
    for i in range(84):
        i1 = int(i / 7)
        i2 = int(i % 7)
        #当第三个数字的某一位和下一位都不存在时，matches显示全0，这两行0不需要变成1，因为即使变了也肯定是错的，此时直接跳过可减少用时
        #比如2+3=5，其formula为['', 2, '', 3, '', '', '', 5, '+', '=', '', ''],则['', 2, '', 3, x, '', '', 5, '+', '=', '', '']
        #或['', 2, '', 3, '', x, '', 5, '+', '=', '', '']肯定是错的。
        if (i1<10 and matches[i1] == [0, 0, 0, 0, 0, 0, 0] and matches[i1 + 1] == [0, 0, 0, 0, 0, 0, 0]):
            continue
        if (matches[i1][i2] == 0):
            marker[0] = i
            matches[i1][i2] = 1
            for j in range(i + 1, 84):
                j1 = int(j / 7)
                j2 = int(j % 7)
                if (j1<10 and matches[j1] == [0, 0, 0, 0, 0, 0, 0] and matches[j1 + 1] == [0, 0, 0, 0, 0, 0, 0]):
                    continue
                if (matches[j1][j2] == 0):
                    marker[1] = j
                    matches[j1][j2] = 1
                    for k in range(84):
                        k1 = int(k / 7)
                        k2 = int(k % 7)
                        if (matches[k1][k2] == 1 and k != marker[0] and k != marker[1]):
                            matches[k1][k2] = 0
                            for h in range(k + 1, 84):
                                h1 = int(h / 7)
                                h2 = int(h % 7)
                                if (matches[h1][h2] == 1 and h != marker[0] and h != marker[1]):
                                    matches[h1][h2] = 0
                                    if (test_matches(matches, new_formula)):
                                        if (test_equation(new_formula)):
                                            #等式成立
                                            for i in range(12):
                                                result.append(new_formula[i])
                                    matches[h1][h2] = 1
                            matches[k1][k2] = 1
                    matches[j1][j2] = 0
            matches[i1][i2] = 0
    return result