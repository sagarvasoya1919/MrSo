def Answer(p,ans,pre):
    if(pre != '' and p != ''):
        if(int(pre) > int(p[0])):
            for i in range(int(pre)-int(p[0])):
                ans = ans + ')'

    if(p == ''):
        for i in range(int(pre)):
            ans = ans + ')'
        return ans

    if(int(p[0]) == 0):
        return Answer(p[1:],ans + p[0],p[0])

    if(int(p[0]) == 1):
        if(pre != ''):
            if(int(pre) == 0):
                ans = ans + '(' + p[0]
            else:
                ans = ans + p[0]
        else:
            ans = ans + '(' + p[0]
        return Answer(p[1:],ans,p[0])

    if(int(p[0]) > 1):
        if(pre != ''):
            for i in range(int(p[0]) - int(pre)):
                ans = ans + '('
            ans = ans + p[0]
        else:
            for i in range(int(p[0])):
                ans = ans + '('
            ans = ans + p[0]
        return Answer(p[1:],ans,p[0])

p = int(input())
for m in range(0,p):
    k = input()
    print('Case #{}: {}'.format(m + 1,Answer(k,'','')))
