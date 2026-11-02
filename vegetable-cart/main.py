vegetables = {
    "potato":5,
    "tomato":8,
    "onion":7,
    "carrot":6,
    "cucumber":9,
    "pepper":12,
    "zucchini":8,
    "eggplant":10,
    "cabbage":6,
    "lettuce":5,
    "cauliflower":11,
    "pumpkin":7
}
card ,total = [],0
print("--------------------")
print("\tOur Menu")
print("--------------------")
for key,value in vegetables.items():
	print(f"{key:12}: {value:02} DH")
print("--------------------")
print("Choose your Cart then press (q) to Quit")
while True:
	foods = input("choose your vegetable: ").lower()
	if foods == "q":
		break
	elif foods  not in vegetables:
		print("Please choose a valid vegetable")
	else :
		card.append(foods)
print("-------------------")
print("List of Vegetables:")
print("-------------------")
for veg in card:
	print(f"{veg:12}: {vegetables[veg]} DH")
	total = total + vegetables[veg]
print()
print("-------------------")
print("       Total       ")
print("-------------------")
print(f"your total is : {total}")

