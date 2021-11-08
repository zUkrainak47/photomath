type = input("Input task type (binom): ")

if type == "binom":
    from math import factorial
    def c(n, k):
        return (factorial(n)/(factorial(k)*factorial(n-k)))

    print('Input the Binom. For input instructions input 1.')
    binom = list(input().split())
    if binom == ['1']:
        print('<term 1> <term 2> <power>\nNow input the Binom')
        binom = list(input().split())

    a, b, n = binom
    n = int(n)

    def input_to_list(a):
        if '^' in a:
            power = a[a.index('^')+1:]
            a = a[:a.index('^')]
        else:
            power = 1
        if len(a) > 1 and a[0] != '-':
            a = [int(a[:-1]), a[-1]]
        elif len(a) > 2 and a[0] == '-':
            a = [int(a[:-1]), a[-1]]
        elif a[-1].isalpha():
            if a[0] == '-':
                a = [-1, int(a[1:])]
            else:
                a = [1, a]
        else:
            a = [int(a), '']
        a.append(power)
        return a

    a, b = input_to_list(a), input_to_list(b)

    ans = ''
    #print("Coeffs:", a, b, n)    coeffs from input

    def add(a, n, k):
        global flag
        term = ''
        if a[1] != '' and (n-k) != 0:
            if flag:
                term += '*'
            if (n-k) == 1:
                if a[-1] == 1:
                    term += a[1]
                else:
                    term += a[1] + '^' + a[-1]
            else:
                term += a[1] + '^' + str((n-k)*int(a[-1]))
            flag = True
            return term
        else:
            return ''

    for k in range(n+1):
        flag = False
        if int(c(n, k)) * (a[0]**(n-k)) * b[0]**(k) != 1:
            ans += str(abs(int(c(n, k)) * (a[0]**(n-k)) * b[0]**(k)))
            flag = True
        
        ans += add(a, n, k) + add(b, 2*k, k)
        try:
            if str(int(c(n, k+1)) * (a[0]**(n-k-1)) * b[0]**(k+1))[0] == '-':
                ans += ' - '
            else:
                ans += ' + '
        except:
            pass

    print("Binom:", ans)