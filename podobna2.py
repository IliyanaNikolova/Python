import random
while True:
    try:
        m=int(input("Enter a whole number between 20 and 30: "))
        if m<20 or m>30:
            raise ValueError("The number has to be between 20 and 30.")
    except ValueError as er:
        print(f"Mistake: {er}")
    else:
        p=random.randint(-4000,-1000)
        q=random.randint(2000, 5000)
        print(f"The diapason is: {p};{q}")

        main_list=[]
        for i in range(m):
            number=int(input(f"Enter a number in main_list[{i}] in the interval {p};{q}: "))
            while not p<number<q:
                print(f"Number is not in the diapason and not valid.")
                number = int(input(f"Enter a number in main_list[{i}] in the interval {p};{q}: "))
            main_list.append(number)
        print(f"main_list: {main_list}")

        #a) suma na polozitelnite chisla ot main_list, chiqto cifra na stoticite
        #e nechetna ILI e ravna na 2
        sum1=0
        pozitive_numbers=[i for i in main_list if i>0]
        for x in pozitive_numbers:
            digit=(x//100)%10
            if digit %2 !=0 or digit==2:
                sum1+=x
        print(f"The sum of pozitive numbers with stotica nechetna or =2: {sum1}")

        #b) srednoarit na elementite ot main-list, chiqto stoinost e dvucifrena i otricatelna
        negative_two_digit_number=[]
        for i in main_list:
            if i<0 and 10<=abs(i)<=99:
                negative_two_digit_number.append(i)
        if len(negative_two_digit_number)>0:
            average=sum(negative_two_digit_number)/len(negative_two_digit_number)
            print(f"Average of negative two digit numbers is: {average}")
        else:
            print("No negative two digit numbers found")

        #v) 2ri spisyk w koito sa tricifreni ILI sa kratni na 7 ot main_list
        filtered_list=[]
        for i in main_list:
            if 100<=abs(i)<=999 or i%7==0:
                filtered_list.append(i)
        print(f"filtered_list: {filtered_list}")

        #g) broi elementi s nechetna stoinost, koito sa na cheten indeks ot filtered_list
        count1=0
        for i in range(len(filtered_list)):
            if i%2==0:
                if filtered_list[i]%2!=0:
                    count1+=1
        print(f"The count of the odd elements on even index is: {count1}")

        #d) iztrivane na elementi ot filtered_list, koito sa tricifreni I sa otricatelni
        count2=len(filtered_list)
        for x in range(count2):
            for i in range(len(filtered_list)-1,-1,-1):
                if filtered_list[i]<0 and 100<=abs(filtered_list[i])<=999:
                    del filtered_list[i]
        print(f"After the deleted element filtered_list looks: {filtered_list}")

        #e) izravnqvane na spisycite
        len_main_list=len(main_list)
        len_filtered_list=len(filtered_list)

        if len_main_list!=len_filtered_list:
            if len_main_list<len_filtered_list:
                shorter=main_list
                longer=filtered_list
                print(f"the shorter list is {shorter}")
            else:
                shorter=filtered_list
                longer=main_list
                print(f"the shorter list is {shorter}")

            diffrence=len(longer)-len(shorter)
            print(f"We add {diffrence} more elements to the shorter list")
            for i in range(diffrence):
                new_number=random.randint(p+1, q-1)
                shorter.insert(0, new_number) #dobavqme v nachaloto
                print(f"Added element {new_number} to the beggining of the {shorter}")
                print(f"main_list: {len(main_list)}")
                print(f"filtered_list: {len(filtered_list)}")
        else:
            print(f"Both  lists are with the same length")
        print(f"main_list: {main_list}")
        print(f"filtered_list: {filtered_list}")



