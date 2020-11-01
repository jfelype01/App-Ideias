x = 0
n = 2
binary = []
while x < 8:
    while n != "0" and n != "1":
        n = input("Digite o número 1 ou 0: ")
        print()
    n = int(n)
    binary.append(n)
    x += 1
    n = 2
y = 0
while x > 0:
    if x == 8:
        o = binary[y]
        binary[y] = str(binary[y])
        y += 1
    else:
        o = o * 2 + binary[y]
        binary[y] = str(binary[y])
        y = y + 1
    x -= 1
binary = ''.join(binary)
print("O número binário {} equivale ao número decimal {}".format(binary, o))