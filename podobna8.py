while True:
    try:
        n=int(input("Enter a whole number between 15 and 35: "))
        if n<15 or n>35:
            raise ValueError("You have to enter a whole number between 15 and 35.")
    except ValueError as er:
        print(f"Mistake: {er}")
    else:
        list1=[]
        for i in range(n):
            number=int(input(f"Enter a number in list1[{i}] in diapason 30:300: "))
            while not 30<number<300:
                print("Enter a valid number!")
                number = int(input(f"Enter a number in list1[{i}] in diapason 30:300: "))
            list1.append(number)
        print(f"The first list is : {list1}")

        #broi na elementi ot list1, chiqto cifra na deseticite e kratna na 3
        count1=0
        for i in list1:
            digit=(i//10)%10
            if digit%3==0:
                count1+=1
        print(f"The count of the number where desetica %3 : {count1}")

        #Da se nameri indeksa na minimalniq element ot tozi spisak, koito ima
        # ostatyk 4 pri celochisleno delenie na 6
        min_value=None
        min_index=-1
        for i in range(len(list1)):
            if list1[i]%6==4:
                if min_value is None or list1[i]<min_value: # ako pyrvoto takova ili e po-malko ot minimuma
                    min_value=list1[i]
                    min_index=i
        if min_index!=0:
            print(f"The min value is where x%6==4 : {min_value} and the index is {min_index}")
        else:
            print("There are no elements about that.")

        #vtori list i da se vkluchat tezi elementi ot list1, koito sa dvucifreni i sa kratni na 2 ILI 3
        #da se izpolzva list comprehension
        list2=[i for i in list1 if 10<=i<=99 and (i%2==0 or i%3==0)]
        print(f"The second list is : {list2}")

        #srednoaritmeticno na elementi ot list2, chiito indeksi sa nechetni
        odd_index_numbers=[]
        for i in range(len(list2)):
            if i%2!=0:
                odd_index_numbers.append(list2[i])
        if len(odd_index_numbers)>0:
            average=sum(odd_index_numbers)/len(odd_index_numbers)
            print(f"The average of the odd index elements is : {average}")
        else:
            print("There are no odd index elements.")

        #iztrivane na minimalno chetno chislo ot lis2
        even_numbers=[]
        count2=len(list2)
        for x in range(count2):
            for i in range(len(list2)-1,-1,-1):
                if list2[i]%2==0:
                    even_numbers.append(list2[i])
        if len(even_numbers)>0:
            mini=min(even_numbers)
            print(f"Min even number is : {mini}")
            list2.remove(mini)
            print(f"The list after the deleted min even number is : {list2}")
        else:
            print("There are no even numbers.")






