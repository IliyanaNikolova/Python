import random

while True:
    try:
        n=int(input("Enter a number between 22 and 32: "))
        if n<22 or n>32:
            raise ValueError("The number has to be between 22 and 32!")

    except ValueError as er:
        print(f"Mistake: {er}")

    else:
        a=random.randint(-5500,-2500)
        b=random.randint(1500,4500)
        print(f"The diapason is {a}:{b}")

        first=[]
        for i in range(n):
            number=int(input(f"Enter a number in list first[{i}] in diapason {a}:{b}: "))
            while not a<number<b:
                print("Enter a valid number!")
                number = int(input(f"Enter a number in list first[{i}] in diapason {a}:{b}: "))
            first.append(number)
        print(f"The first list is: {first}")

        #a)suma na otricatelni chisla ot first, chiqto cifra na stoticite e chetna ILI e ravna na 9
        sum1=0
        numbers_found=[]
        for x in first:
            if x<0:
                digit= (x/100)%10
                if digit%2==0 or digit==9:
                    sum1+=x
                    numbers_found.append(x)
        if numbers_found:
            print(f"The sum of negative numbers in first, where stotica is even or =9: {sum1}")
        else:
            print("There are no negative numbers with hundreds=9 or even hundreds")

        #b)sredna stoinost na elementite, koito sa dvucifreni i polozitelni
        pozitive_2_digit_numbers=[]
        for i in first:
            if 10<=i<=99 and i>0:
                pozitive_2_digit_numbers.append(i)

        if len(pozitive_2_digit_numbers)>0:
            average=sum(pozitive_2_digit_numbers)/len(pozitive_2_digit_numbers)
            print(f"The average of pozitive 2 digit numbers is : {average}")
        else:
            print("No pozitive 2 digit numbers found")

        #v) syzdavame vtori spisyk i da se vkluchat tezi elementi, koito sa 4icifreni ILI sa kratni
        ### na 9 ot spisyk first
        second=[]
        for i in first:
            if 1000<=abs(i)<=9999 or i%9==0:
                second.append(i)
        print(f"The second list is : {second}")

        #g) proizvedenie na elementite s nechetna stoinost, koito sa na necheten indeks ot second
        multiply=1
        for i in range(len(second)):
            if i%2!=0:
                if second[i]%2!=0:
                    multiply*=second[i]
        print(f"The multiplication of the odd numbers on odd index is : {multiply}")

        #d) iztrivane na elementi ot second, koito sa 4icifreni i polozitelni
        count2=len(second)
        for i in range(count2):
            for x in range(len(second)-1,-1,-1):
                if 1000<=second[x]<=9999 and second[x]>0:
                    del second[x]
        print(f"The second list after the deleted element: {second}")

        #e) izravnqvane na spisycite
        len_first=len(first)
        len_second=len(second)
        print(f"The length of the first list is: {len_first}")
        print(f"The length of the second list is: {len_second}")

        if len_first!=len_second:
            if len_first<len_second:
                shorter=first
                longer=second
                print(f"The shorter list is: {shorter}")
            else:
                shorter=second
                longer=first
                print(f"The shorter list is: {shorter}")

            diff=len(longer)-len(shorter)
            print(f"We have to add {diff} elements to {shorter}")

            for i in range(diff):
                new_number=random.randint(a+1,b-1)
                shorter.insert(0,new_number)
                print(f"The length of the first list is :{len(first)}")
                print(f"The length of the second list is :{len(second)}")
        else:
            print("Both lists are with the same length")
        print(f"First list is: {first}")
        print(f"Second list is: {second}")