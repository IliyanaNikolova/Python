import random
while True:
    try:
        n=int(input("Enter a number between 18 and 28: "))
        if n<18 or n>28:
            raise ValueError("You have to enter a number between 18 and 28!")
    except ValueError as er:
        print(f"Mistake: {er}")

    else:
        a=random.randint(-7000,-4000)
        b=random.randint(800,3800)
        print(f"The diapason is {a};{b}. ")

        first=[]
        for i in range(n):
            number=int(input(f"Enter a whole number in list first[{i}] in diapason {a}:{b}: "))
            while not a<=number<=b:
                print("The number is not in the interval.")
                number=int(input(f"Enter a whole number in list first[{i}] in diapason {a}:{b}: "))
            first.append(number)
        print(f"the first list is : {first}")

        #a) broi polozitelni chisla ot first, chiqto cifra na edinicite e po-golqma ot 5 ILI e ravna na 0
        count1=0
        pozitive_numbers=[x for x in first if x>0]
        for i in pozitive_numbers:
            digit=i%10
            if digit>5 or digit==0:
                count1+=1
        print(f"The count of pozitive numbers where edinica>5 or edinica=0 is : {count1}")

        #b) maksimalna stoinost ot first, ot elementite koito sa tricifreni i otricatelni
        negative_3_digit_number=[]
        for i in first:
            if 100<=abs(i)<=999 and i<0:
                negative_3_digit_number.append(i)
        if negative_3_digit_number:
            maxi=max(negative_3_digit_number)
            print(f"The max value of the negative three-digit number is : {maxi}")
        else:
            print("No negative three-digit numbers found")

        #v) Syzdavane na second list i da se vkluchat ot first, tezi koito sa ednocifreni ILI
        #kratni na 13
        second=[]
        for i in first:
            if 0<=abs(i)<=9 or i%13==0:
                second.append(i)
        print(f"The second list is : {second}")

        #g)srednoaritmetichno na elementite s nechetna stoinost , koito sa na cheten indeks ot second
        odd_number_even_index=[]
        for i in range(len(second)):
            if i%2==0:
                if second[i]%2!=0:
                    odd_number_even_index.append(second[i])

        if len(odd_number_even_index)>0:
            average=sum(odd_number_even_index)/len(odd_number_even_index)
            print(f"The average of odd numbers in second list on even index is : {average}")
        else:
            print("No odd numbers found")

        #d) iztrivane na elementi ot second koito sa ednocifreni i sa otricatelni
        count2=len(second)
        for i in range(count2):
            for x in range(len(second)-1,-1,-1):
                if (second[x])<0 and 0<=abs(second[x])<=9:
                    del second[x]
        print(f"The second list after the deleted elements: {second}")

        #e) izravnqvane na spisycite
        len_first=len(first)
        len_second=len(second)
        print(f"the length of the first list: {len_first}")
        print(f"the length of the second list: {len_second}")

        if len_first!=len_second:
            if len_first<len_second:
                shorter=first
                longer=second
                print(f"The shorter list is : {shorter}")
            else:
                shorter=second
                longer=first
                print(f"The shorter list is : {shorter}")

            diff=len(longer)-len(shorter)
            print(f"We have to add {diff} more elements to {shorter}.")

            index_insert=len(shorter)//2
            for i in range(diff):
                new_number=random.randint(a+1, b-1)
                shorter.insert(index_insert,new_number)
            print(f"The length of the first list: {len(first)}")
            print(f"The length of the second list: {len(second)}")
        else:
            print("Both lists have the same length.")

        print(f"First list: {first}")
        print(f"Second list: {second}")

