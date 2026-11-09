import random

while True:
    try:
        k= int(input("Enter e whole number between 15 and 25: "))
        if k<15 or k>25:
            raise ValueError("The number has to be between 15 and 25.")
    except ValueError as er:
        print(f"Mistake : {er}")
    else:
        s=random.randint(-6000,-3000)
        t=random.randint(1000,4000)
        print(f"The diapason is {s},{t}")

        first=[]
        for i in range(k):
            number=int(input(f"Enter a number in list first[{i}] in interval {s},{t}: "))
            while not s<number<t:
                print("Enter a valid number in the interval")
                number=int(input(f"Enter a number in list first[{i}] in interval {s},{t}: "))
            first.append(number)
        print(f"the first list is : {first}")

        #a) proizv na otricatelni chisla, chiqto cifra na deseticite e kratna na 3 ILI e ravna na 7
        multiply=1
        negative_numbers=[i for i in first if i<0]
        for i in negative_numbers:
            digit=(abs(i)//10)%10
            if digit%3==0 or digit==7:
                multiply*=i
        print(f"The multiplication of the negative numbers in first, which desetica %3 or =7 is: {multiply}")
        #b) minimalna stoinost ot first, koito sa 4iricifreni i polozitelni
        pozitive_4_digit_numbers=[]
        for x in first:
            if x>0 and 1000<=x<=9999:
                pozitive_4_digit_numbers.append(x)
        if pozitive_4_digit_numbers:
            mini=min(pozitive_4_digit_numbers)
            print(f"Min value of the pozitive, four digit numbers is: {mini}")
        else:
            print("No pozitive 4-digit numbers found")

        #v) Syzdavane na list second i da ima elmentite ot first, koito sa dvucifreni ILI kratni na 11
        second=[]
        for i in first:
            if 10<=i<=99 or i%11==0:
                second.append(i)
        print(f'The second list is : {second}')

        #g) suma na elementi s chetna stoinost, koito sa na necheten indeks ot spisyk second
        sum=0
        for i in range(len(second)):
            if i%2 != 0: #necheten indeks
                if second[i]%2==0:
                    sum+=second[i]
        print(f"The sum of the even elements on odd index from list second is: {sum}")

        #d) iztrivane na elementite, koito sa dvucifreni i sa polozitelni ot second
        count_=len(second)
        for i in range(count_):
            for x in range(len(second)-1,-1,-1):
                if 10<=second[x]<=99 and second[x]>0:
                    del second[x]
        print(f"The second list after the deleted elements looks: {second}")

        #e) izravnqvane na dylzinite na dvata spisyka
        len_first=len(first)
        len_second=len(second)
        print(f"length of the first list is: {len(first)}")
        print(f"length of the second list is: {len(second)}")

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
            print(f"We have to add {diff} more elements to {shorter}")
            for i in range(diff):
                new_number=random.randint(s+1,t-1)
                shorter.append(new_number)

            print(f"length of the first list is: {len(first)}")
            print(f"length of the second list is: {len(second)}")
        else:
            print("Both lists are with the same length.")

        print(f"the first list: {first}")
        print(f"the second list: {second}")

