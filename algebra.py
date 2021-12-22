task = input("Input task type (binom/horner): ")

if task == "binom":
    from math import factorial

    def input_to_list(a):
        """
        :param a: first or 2nd term of the input
        :return: "a" transformed into a proper list of coefficients
        """
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

    def c(n, k):
        'Binomial coefficient (n choose k)'
        return (factorial(n)/(factorial(k)*factorial(n-k)))

    def add(a, n, k):
        """
        funtion returns factors containing inputted variables.
        they are multiplied by values recieved by the c(n, k) function and are added to the output.
        the way this funtion works is now unknown due to lack of documentation.
        """
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


    #Input
    print('Input the Binom. For input instructions input 1.')
    binom = list(input().split())

    if binom == ['1']:
        print('Input format is: <term 1> <term 2> <power>\nThe program was written for real humans, so dont try to break it.\nInputs like "2*a" instead of "2a" will not work.\nNow input the Binom.')
        binom = list(input().split())

    a, b, n = input_to_list(binom[0]), input_to_list(binom[1]), int(binom[-1])
    #print("Coeffs:", a, b, n) #coeffs recieved from input by the input_to_list function


    #Output
    ans = ''
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



elif task == "horner":
    from math import factorial

    def transform(field, array, a):
        """
        :param field: a type of field of numbers
        :param array: some string array
        :param a: some string value
        :return: the transformed (into integer or complex number) value of "x" and an array with transformed elements
        """
        length = len(array)
        if field == "real":
            for i in range(length):
                array[i] = int(array[i])
            return int(a), array

        elif field == "complex":
            for i in range(length):
                array[i] = complex(array[i])
            return complex(a), array


    def Horner_scheme(field, poly_coeffs, x0):
        """
        Horner's scheme.
        :param field: a type of field of numbers
        :param poly_coeffs: a string array of polynomial coefficients
        :param x0: a polynomial root
        :return: an array (integer or complex) of the results of diving a polynomial by x-x0 on each iteration
        """
        table = []
        x0, poly_coeffs = transform(field, poly_coeffs, x0)
        l = len(poly_coeffs)
        for i in range(l):
            table.append([poly_coeffs[0]])
            for j in range(1, l-i):
                r = poly_coeffs[j] if i == 0 else table[i - 1][j]
                table[i].append(x0 * table[i][j-1] + r)
        return table


    def poly_derivative(table, k):
        """
        :param table: Horner`s table
        :param k: index of remainder of division
        :return: polynomial`s k-th derivative
        """
        return factorial(k)*table[k][-1]


    # Input
    f_type = input("Number type (real/complex): ")
    coeffs = list(map(str, input("Coeffs: ").split()))
    x = input("x0 = ")
    Table = Horner_scheme(f_type, coeffs, x)

    # Output
    print()
    print("Horner`s Table:")
    for t in range(len(Table)):
        print(*Table[t], "\t")

    print()
    print("Polynomial`s derivatives on x0:")
    for t in range(1, len(Table)):
        print(f'k={t}: {poly_derivative(Table, t)}')
    print(f'f(k)(x0) = 0 ∀ k>{t}, k є N')