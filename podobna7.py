import random

mylst_15=[]
for i in range(15):
    r_number=random.randint(-1000,-1)
    mylst_15.append(r_number)
print(f"Mylst_15 is: {mylst_15}")

#a) nai-golqmo chislo ot mylst_15
maxi=max(mylst_15)
print(f"The biggest number is: {maxi}")

#b)suma na chislata ot mylst_15
suma=sum(mylst_15)
print(f"The sum of the numbers is: {suma}")

#v) vtori spisyk mylst_dev3, koito da syhranqva chislata ot mylst_15, koito sa kratni na 3
mylst_dev3=[]
for i in mylst_15:
    if i%3==0:
        mylst_dev3.append(i)
print(f"The second list mylst_dev3 is : {mylst_dev3}")

#g) Sortirai mylst_dev3 vyv vyzhodqsht red
if len(mylst_dev3)==0:
    print(f"There are no numbers in mylst_dev3.")

if len(mylst_dev3)>0:
    print(f"Before the sort: {mylst_dev3}")

    mylst_dev3.sort()
    print(f"After the sort: {mylst_dev3}")
else:
    print("The list is empty you can't sort anything!")

#e) iztrivane na vcichki elementi ot mylst_dev3, koito sa s necheten indeks
if len(mylst_dev3)>0:
    for x in range(len(mylst_dev3)-1,-1,-1):
        if x%2!=0:
            del mylst_dev3[x]
    print(f"Mylst_dev3 after the deleted numbers: {mylst_dev3}")
else:
    print("The list is empty!")
