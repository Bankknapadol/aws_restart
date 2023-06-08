myFruitlist = ["apple","banana","cherry"]
print(myFruitlist)
print(type(myFruitlist))

print(myFruitlist[0])
print(myFruitlist[1])
print(myFruitlist[2])

myFruitlist[2] = "orange"
print(myFruitlist)
#แก้ data ข้างในได้

myFinalAnswerTuple = ("mango","pineapple","orange")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])
#แก้ data ข้างในไม่ได้

myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple",
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
#Dictionary มองตัวด้านหน้าเป็น key เพื่อเข้าถึง value ด้านหลัง