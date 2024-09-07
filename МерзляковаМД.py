import math
# №19
def task1(H):
    
    try:
        N = 2 ** H
    except:
        return 0
    return N

if __name__ == "__main__":
    inp1 = int(input("Введите количество информации: "))
    print(task1(inp1), "этажей")
exit

# №20
def task2(H):
    
    try:
        N = 2 ** H
    except:
        return 0
    return N

if __name__ == "__main__":
    inp2 = int(input("Введите количество информации: "))
    print(task2(inp2), "подъезда")
exit

# №18
def task3(I, a, b, c):
    
    try:
        i = (I * 8) / (a * b * c)
        N = 2 ** i
    except:
        return 0
    return N

if __name__ == "__main__":
    inp3 = int(input("Введите количество байтов: "))
    inp4 = int(input("Введите количество страниц: "))
    inp5 = int(input("Введите количество строк на странице: "))
    inp6 = int(input("Введите количество символов в строке: "))
    print(task3(inp3, inp4, inp5, inp6), "символа")
exit


# №19
def task4(N1, N2):
    
    try:
        i1 = math.log2(N1)
        i2 = math.log2(N2)
        V = i2 / i1
    except:
        return 0
    return V

if __name__ == "__main__":
    inp7 = int(input("Введите мощность алфавита первого текста: "))
    inp8 = int(input("Введите мощность алфавита второго текста: "))
    print(task4(inp7, inp8))
exit



# №20
def task5(I, N):
    
    try:
        i = math.log2(N)
        K = I / i
    except:
        return 0
    return K

if __name__ == "__main__":
    inp7 = int(input("Введите количесво информации в тексте: "))
    inp8 = int(input("Введите мощность алфавита: "))
    print(task5(inp7, inp8), "символа")
exit
