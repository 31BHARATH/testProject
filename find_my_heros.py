hero_name = input("Enter the hero name: ")

pan_indian_heros = [
    "Prabhas",
    "Mahesh Babu",
    "Pawan Kalyan"
]

heros1 = []
heros2 = []

for hero in pan_indian_heros:
    hero1 = hero.lower()
    hero2 = hero.upper()
    
    heros1.append(hero1)
    heros2.append(hero2)
    
pan_indian_heros = pan_indian_heros + heros1 + heros2

if hero_name in pan_indian_heros:
    print(f"{hero_name} is in pan india list")
else:
    print(f"{hero_name} is not in pan india list")