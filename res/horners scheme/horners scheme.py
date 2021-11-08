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