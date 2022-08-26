'''
receba 3 números e informe o maior, menor, do meio e se houver iguais
'''
x1 = float(input("Informe um número: "))
x2 = float(input("Informe outro número: "))
x3 = float(input("Informe mais um número: "))
if x1 > x2:
    if x1 > x3:
        if x2 > x3:
            print  (f"{x1} é maior do que {x2}, que é maior do que {x3}.")
        else:
            print  (f"{x1} é maior do que {x3}, que é maior do que {x2}.")
    else: 
        print  (f"{x3} é maior do que {x1}, que é maior do que {x2}.")
else:
    if x2 > x3: 
        if x3 > x1:
            print  (f"{x2} é maior do que {x3}, que é maior do que {x1}.")
        else:
            if x1 == x3:
                print  (f"{x2} é maior do que {x1}, que é maior do que {x2}.")
            print  (f"{x2} é maior do que {x1}, que é maior do que {x2}.")
    else: 
        if x2 > x1:
            print  (f"{x3} é maior do que {x2}, que é maior do que {x1}.")
        else:
            print  (f"{x3} é maior do que {x1}, que é maior do que {x2}.")