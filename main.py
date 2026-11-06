print("Welcome to place the rabbit\n")
leaves=[["🍀","🍀","🍀"],["🍀","🍀","🍀"],["🍀","🍀","🍀"]]
print("",leaves[0]," \n",leaves[1],"\n",leaves[2])
#كان يمكن استخدام ال اف سترينج اسهل  
#print(f"{leaves[0]} \n{leaves[1]} \n{leaves[2]}")
print("Where shoud the rabbit go? 🐇")
str_rabbit=(input("Please choose a row and a column\n "))
if len(str_rabbit)==2:
  if int(str_rabbit[0])<= 3 and int(str_rabbit[1])<=3 and int(str_rabbit[0])>0 and int(str_rabbit[1])>0:
    # القائمة هون ما كان الها داعي ابدا كان يمكن تخزين الأرقام المدخلة بمتغيرات عادية بدل ما رحت وساويت قائمة كاملة منشانهن
    rabbit=[]
    rabbit.append(str_rabbit[0])
    rabbit.append(str_rabbit[1])
    value=leaves[int(rabbit[0])-1][int(rabbit[1])-1]
    #print(value)
    leaves[int(rabbit[0])-1].remove(value)
    leaves[int(rabbit[0])-1].insert(int(rabbit[1])-1,"🐇")
    #هون ما كان في داعي للحذف والادخال من جديد كان ممكن بكل بساطة اني اعمل تغير لقيمة العنصر المخزن بداخل القائمة بدون االحذف والادخال 
    print("\n Success .... \n")
    print("",leaves[0]," \n",leaves[1],"\n",leaves[2])
  else:
    print("Sorry! invalid choise.")
else:
  print("Please enter two digits")



  #     ANOTHER WAY




  
print("Welcome to place the rabbit\n")
field = [ ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"], ["🍀", "🍀", "🍀"] ]

print(f"{field[0]} \n{field[1]} \n{field[2]}")
print("\nWhere should the rabbit go? 🐇 ")

position = (input("Please choose a row and a column "))
row = int(position[0])
column = int(position[1])

field[row-1][column-1] = "🐇"

print("\n Success .... \n")

print(f"{field[0]} \n{field[1]} \n{field[2]}")

