wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 30

while(True):
    print("1) Wizard\n2) Elf\n3) Human")
    character = input("Choose your character:")
    if character == "1":
        character = wizard
        my_hp = wizard_hp
        my_dmg = wizard_damage
        break
    if character == "2":
        character = elf
        my_hp = elf_hp
        my_dmg = elf_damage
        break
    if character == "3":
        character = human
        my_hp = human_hp
        my_dmg = human_damage
        break
    else:
        print("Unknown Character")

print("You have chosen the character: ", character)
print("Health", my_hp)
print("Damage", my_dmg)

# task 4
while(True):
    # character attacks dragon
    dragon_hp = dragon_hp - my_dmg
    print("The", character, "damaged the Dragon!")
    print("The dragon hitpoints are now:" + str(dragon_hp))
    # dragon dies
    if dragon_hp == 0:
        print("The dragon has lost the battle")
        break
    # dragon attacks character
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the character")
    print("The character hitpoints are now:" + str(my_hp))
    # character dies
    if my_hp == 0:
        print("The", character, "has lost the battle")
        break
    # end task 4
