import random
#try-except proverka
while True:
    try:
        n=int(input("Enter a whole number between 25 and 35: "))
        if n<25 or n>35:
            raise ValueError("The number has to be between 25 and 35")

    except ValueError as er:
        print(f"Mistake :{er}")
    else:
        x=random.randint(-5000,-2000)
        y=random.randint(3000, 6000)
        print(f"the diapason of the numbers you have to enter is : {x}; {y}")

        #spisyk 1vi
        list1=[]
        for i in range(n):
            number=int(input(f"Enter a whole number in list1[{i}] in diapason {x};{y}: "))
            while not x<number<y:
                print("Enter a valid number.")
                number = int(input(f"Enter a whole number in list1[{i}] in diapason {x};{y}: "))

            list1.append(number)
        print(f"list1: {list1}")

        #a) broi otricatelni chisla ot list1, chiqto cifra na edinici e chetna ili e ravna na 5
        count1=0
        negative_numbers=[i for i in list1 if i<0]
        for i in negative_numbers:
            digit=i%10
            if digit%2==0 or digit == 5:
                count1+=1
        print(f"Count of the negative numbers in list1 with last number % 2 or number = 5: {count1}")

        #b) suma na elementi ot list1, chiqto stoinost e tricifrena i polozitelna
        sum1=0
        for i in list1:
            if 100<=i<=999 and i>0:
                sum1+=i
        print(f"Sum of the tree-digit pozitive numbers is : {sum1}")

        #v) 2ri spisyk list2 i da se vkluchat elementi ot list1, koito sa ednocifreni ILI sa kratni na 5
        list2=[]
        for i in list1:
            if -9<=i<=9 or i%5==0:
                list2.append(i)
        print(f"list2: {list2}")

        #g) proizvedenie na elementi ot list2, koito sa CHETNI na NECHETEN indeks
        multiply=1
        for i in range(len(list2)):
            if i%2!=0: #necheten indeks
                if list2[i]%2==0: #chetna stoinost
                    multiply*=list2[i]
        print(f"Multiplication of the even numbers on odd index is: {multiply}")

        #d) iztrivane na elementi ot list2, koito sa ednocifreni i sa polozitelni
        count2=len(list2)
        for x in range(count2):
            for i in range(len(list2)-1,-1,-1):
                if 0<=list2[i]<=9:
                    del list2[i]
        print(F"list2 after the deleted element: {list2}")

        #e) sravnqvane na spisycite, izravnqvane na dylzinite na dvata spisyka
        len_list1=len(list1)
        len_list2=len(list2)
        if len_list1!=len(list2):
            if len_list1<len_list2:
                shorter=list1
                longer=list2
                print("list1 is shorter than list2")
            else:
                shorter=list2
                longer=list1
                print("list2 is shorter than list1")

            diffrence=len(longer)-len(shorter)
            print(f"We have to add {diffrence} elements to {shorter}")

            insert_place = len(shorter) // 2
            for i in range(diffrence):
                new_number=random.randint(x+1,y-1)
                shorter.insert(insert_place,new_number)
            print(f"The length of list1 is : {len(list1)}")
            print(f"The length of list2 is : {len(list2)}")
        else:
            print("Both lists are with the same length.")
        print(f"list1: {list1}")
        print(f"list2: {list2}")




