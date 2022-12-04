from character import Character
from tools import *

running = True


def print_char_sheet():
    print("=" * 50)
    print("Name:", char.name)
    print("Race:", char.race)
    print("Class:", char.character_class)
    print("Level:", char.level)
    if char.character_class == "Magus":
        print("Tradition:", char.tradition)
        print("Paths:", end=" ")
        for x in char.paths:
            if x != char.paths[-1]:
                print(x + ",", end=" ")
            elif x == char.paths[-1]:
                print(x)
    elif char.character_class == "Channeler":
        print("Order:", char.channeler_order)
    elif char.character_class == "Lycan":
        print("Tribe:", char.lycan_tribe)
    elif char.character_class == "Sanguinist":
        print("Hex:", char.sang_hex)
    elif char.character_class == "Vampire":
        print("Bloodline:", char.v_bloodline)
    print("----- General Attributes -----")
    print("Health:", char.health)
    print("Mana:", char.mana)
    print("PD:", char.pd)
    print("MD:", char.md)
    print("Aura Rating:", char.aura_rating)
    print("Appearance:", char.appearance)
    print("----- Physical Attributes -----")
    print("Strength:", char.strength)
    print("Dexterity:", char.dexterity)
    print("Stamina:", char.stamina)
    print("----- Mental Attributes -----")
    print("Intellect:", char.intellect)
    print("Willpower:", char.willpower)
    print("Charisma:", char.charisma)
    print("----- Magical Attributes -----")
    print("Focus:", char.focus)
    print("Talent:", char.talent)
    print("Skill:", char.skill)
    print("----- Skills -----")
    print("Athletics:", char.athletics)
    print("Artistic:", char.artistic)
    print("Scholarly:", char.scholarly)
    print("Social:", char.social)
    print("Survival:", char.survival)
    print("----- Knowledges -----")
    print("Arcane:", char.arcane_k)
    print("Divine:", char.divine_k)
    print("Elemental:", char.elemental_k)
    print("Mental:", char.mental_k)
    print("History:", char.history_k)
    print("Nature:", char.nature_k)
    print("Planar:", char.planar_k)
    print("----- Background -----")
    print("Contacts:", char.contacts)
    print("Sanctum:", char.sanctum)
    print("Wealth:", char.wealth)
    print("----- Traits & Flaws -----")
    print("Traits")
    for x in char.traits:
        print(x + ":", end=" ")
        print(traits_dict[x])
    print("Flaws")
    for x in char.flaws:
        print(x + ":", end=" ")
        print(flaws_dict[x])
    print("=" * 50)


while running:
    var = str(input("Do you wish to create a new character? Yes/No/Exit: "))
    if var in ["y", "Y", "Yes", "yes"]:
        bg_points = 5
        phys_points = 3
        mental_points = 3
        magic_points = 9
        csw_points = 5
        traits = []
        flaws = []
        paths = []
        race = ""
        level = 1
        character_class = ""
        tradition = ""
        primary_circle = ""
        channeler_order = ""
        lycan_tribe = ""
        sang_hex = ""
        v_bloodline = ""

        name = str(input("Please enter your character's name: \n"))

        selection = selector("Please enter your character's race: "  # Race Section
                             "\n1. Dwarf"
                             "\n2. Elf"
                             "\n3. Human"
                             "\n4. Gnome"
                             "\n5. Minotaur"
                             "\n6. Orc\n", 1, 6)
        if selection == 1:
            race = "Dwarf"
        elif selection == 2:
            race = "Elf"
            traits.append("Beautiful")
        elif selection == 3:
            race = "Human"
            traits.append("Skilled")
        elif selection == 4:
            race = "Gnome"
        elif selection == 5:
            race = "Minotaur"
        elif selection == 6:
            race = "Orc"

        selection = selector("Please enter your character's archetype/class: "  # Class Section
                             "\n1. Channeler"
                             "\n2. Magus"
                             "\n3. Sanguinist"
                             "\n4. Vampire"
                             "\n5. Lycan\n", 1, 5)
        if selection == 1:
            character_class = "Channeler"
        elif selection == 2:
            character_class = "Magus"
        elif selection == 3:
            character_class = "Sanguinist"
        elif selection == 4:
            character_class = "Vampire"
        elif selection == 5:
            character_class = "Lycan"

        selection = selector("Please enter your Tradition of Choice: "  # Tradition Section
                             "\n1. Ritualist "
                             "\n2. Enchanter "
                             "\n3. Folk "
                             "\n4. Witchcraft \n", 1, 4)
        if selection == 1:
            tradition = "Ritualist"
        elif selection == 2:
            tradition = "Enchanter"
        elif selection == 3:
            tradition = "Folk"
        elif selection == 4:
            tradition = "Witchcraft"

        if character_class == "Magus":   # Primary Circle Section
            selection = selector("Which of the magical Circles do you choose?: "
                                 "\n1. Arcane "
                                 "\n2. Divine "
                                 "\n3. Elemental"
                                 "\n4. Mental \n", 1, 4)
            if selection == 1:
                primary_circle = "Arcane"
            elif selection == 2:
                primary_circle = "Divine"
            elif selection == 3:
                primary_circle = "Elemental"
            elif selection == 4:
                primary_circle = "Mental"

        if character_class == "Magus":  # Path Section
            if primary_circle == "Arcane":
                selection = selector("Which of the arcane paths do you choose?: "
                                     "\n1. Aetherkinesis "
                                     "\n2. Animating "
                                     "\n3. Binding "
                                     "\n4. Summoning "
                                     "\n5. Transmutation \n", 1, 5)
                if selection == 1:
                    paths.append("Aetherkinesis")
                elif selection == 2:
                    paths.append("Animating")
                elif selection == 3:
                    paths.append("Binding")
                elif selection == 4:
                    paths.append("Summoning")
                elif selection == 5:
                    paths.append("Transmutation")
            elif primary_circle == "Divine":
                selection = selector("Which of the divine paths do you choose?: "
                                     "\n1. Consecration "
                                     "\n2. Creation "
                                     "\n3. Death "
                                     "\n4. Destruction "
                                     "\n5. Light"
                                     "\n6. Nature"
                                     "\n7. Restoration \n", 1, 7)
                if selection == 1:
                    paths.append("Consecration")
                elif selection == 2:
                    paths.append("Creation")
                elif selection == 3:
                    paths.append("Death")
                elif selection == 4:
                    paths.append("Destruction")
                elif selection == 5:
                    paths.append("Light")
                elif selection == 6:
                    paths.append("Nature")
                elif selection == 7:
                    paths.append("Restoration")
            elif primary_circle == "Elemental":
                selection = selector("Which of the elemental paths do you choose?: "
                                     "\n1. Aerokinesis "
                                     "\n2. Fulgurkinesis "
                                     "\n3. Geokinesis "
                                     "\n4. Hydrokinesis "
                                     "\n5. Pyrokinesis \n", 1, 5)
                if selection == 1:
                    paths.append("Aerokinesis")
                elif selection == 2:
                    paths.append("Fulgurkinesis")
                elif selection == 3:
                    paths.append("Geokinesis")
                elif selection == 4:
                    paths.append("Hydrokinesis")
                elif selection == 5:
                    paths.append("Pyrokinesis")
            elif primary_circle == "Mental":
                selection = selector("Which of the mental paths do you choose?: "
                                     "\n1. Clairvoyant "
                                     "\n2. Empath "
                                     "\n3. Familiar "
                                     "\n4. Projection "
                                     "\n5. Telekinesis \n", 1, 5)
                if selection == 1:
                    paths.append("Clairvoyant")
                elif selection == 2:
                    paths.append("Empath")
                elif selection == 3:
                    paths.append("Familiar")
                elif selection == 4:
                    paths.append("Projection")
                elif selection == 5:
                    paths.append("Telekinesis")

        if character_class == "Channeler":  # Channeler Order Selection
            selection = selector("Which of the three Channeler Orders do you choose?: "
                                 "\n1. Order of the Bow "
                                 "\n2. Order of the Shield"
                                 "\n3. Order of the Sword\n", 1, 3)
            if selection == 1:
                channeler_order = "Bow"
            elif selection == 2:
                channeler_order = "Shield"
            elif selection == 3:
                channeler_order = "Sword"

        if character_class == "Lycan":  # Lycan Tribe Selection
            selection = selector("Which of the three Lycan Tribes do you choose?: "
                                 "\n1. Clancaller"
                                 "\n2. Fearstalker"
                                 "\n3. Razorhide\n", 1, 3)
            if 1 <= selection <= 3:
                valid = True
                if selection == 1:
                    lycan_tribe = "Clancaller"
                elif selection == 2:
                    lycan_tribe = "Fearstalker"
                elif selection == 3:
                    lycan_tribe = "Razorhide"

        if character_class == "Sanguinist":  # Sanguinist Hex Selection
            selection = selector("Which of the three Sanguinist Hexes do you choose?: "
                                 "\n1. Hex of the Body"
                                 "\n2. Hex of the Mind"
                                 "\n3. Hex of the Spirit\n", 1, 3)
            if selection == 1:
                sang_hex = "Body"
            elif selection == 2:
                sang_hex = "Mind"
            elif selection == 3:
                sang_hex = "Spirit"

        if character_class == "Vampire":  # Vampire Bloodline Selection
            selection = selector("Which of the three Vampire Bloodlines do you choose?: "
                                 "\n1. Beast Speaker"
                                 "\n2. Mind Shaper"
                                 "\n3. Mist Walker\n", 1, 3)
            if selection == 1:
                v_bloodline = "Beast Speaker"
            elif selection == 2:
                v_bloodline = "Mind Shaper"
            elif selection == 3:
                v_bloodline = "Mist Walker"

        valid = False  # Traits Section
        while not valid:
            try:
                choice = str(input("Would you like to see the list of starting traits? Y/N\n"))
                if choice == "Y" or choice == "y":
                    print("Trait Name : Effect")
                    if race == "Elf":
                        print("-" * 25)
                        print("Supernatural Beauty : " + traits_dict["Supernatural Beauty"])
                    for key in starter_traits_dict:
                        print("-" * 25)
                        print(key + " : " + starter_traits_dict[key])
                selection = str(input("Please type the name of the trait you wish to start with at level 1: \n"))
            except TypeError as err:
                print(err)
                continue
            except ValueError as err:
                print(err)
                continue
            if selection != "":
                if selection not in traits_dict:
                    continue
                valid = True
                traits.append(selection)
                break
            else:
                print("Invalid Entry. Please try again.")
                continue

        bg_points = 5  # Background Section
        if "Skilled" in traits:
            bg_points += 2
        temp_val = bg_points
        athletics = 0
        artistic = 0
        scholarly = 0
        social = 0
        survival = 0
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                bg_spent = 0
                bg_points = temp_val
                print("\nYou have", bg_points, "Skill points available.")
                while True:
                    try:
                        bg_spent = int(input("How many points would you like to put into Athletics? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= bg_spent <= bg_points:
                        athletics += bg_spent
                        bg_points -= bg_spent
                        temp_val = bg_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                bg_spent = 0
                bg_points = temp_val
                print("\nYou have", bg_points, "Skill points available.")
                while True:
                    try:
                        bg_spent = int(input("How many points would you like to put into Artistic? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= bg_spent <= bg_points:
                        artistic += bg_spent
                        bg_points -= bg_spent
                        temp_val = bg_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                bg_spent = 0
                bg_points = temp_val
                print("\nYou have", bg_points, "Skill points available.")
                while True:
                    try:
                        bg_spent = int(input("How many points would you like to put into Scholarly? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= bg_spent <= bg_points:
                        scholarly += bg_spent
                        bg_points -= bg_spent
                        temp_val = bg_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                bg_spent = 0
                bg_points = temp_val
                print("\nYou have", bg_points, "Skill points available.")
                while True:
                    try:
                        bg_spent = int(input("How many points would you like to put into Social? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= bg_spent <= bg_points:
                        social += bg_spent
                        bg_points -= bg_spent
                        temp_val = bg_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                bg_spent = 0
                bg_points = temp_val
                print("\nYou have", bg_points, "Skill points available.")
                while True:
                    try:
                        bg_spent = int(input("How many points would you like to put into Survival? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= bg_spent <= bg_points:
                        survival += bg_spent
                        bg_points -= bg_spent
                        temp_val = bg_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

        temp_val = phys_points  # Physical Attributes Section
        strength = 1
        dexterity = 1
        stamina = 1
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                phys_spent = 0
                phys_points = temp_val
                print("\nYou have", phys_points, "Physical Attribute points available.")
                while True:
                    try:
                        phys_spent = int(input("How many points would you like to put into Strength? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= phys_spent <= phys_points:
                        strength += phys_spent
                        phys_points -= phys_spent
                        temp_val = phys_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                phys_spent = 0
                phys_points = temp_val
                print("\nYou have", phys_points, "Physical Attribute points available.")
                while True:
                    try:
                        phys_spent = int(input("How many points would you like to put into Dexterity? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= phys_spent <= phys_points:
                        dexterity += phys_spent
                        phys_points -= phys_spent
                        temp_val = phys_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                phys_spent = 0
                phys_points = temp_val
                print("\nYou have", phys_points, "Physical Attribute points available.")
                while True:
                    try:
                        phys_spent = int(input("How many points would you like to put into Stamina? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= phys_spent <= phys_points:
                        stamina += phys_spent
                        phys_points -= phys_spent
                        temp_val = phys_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

        temp_val = mental_points  # Mental Attributes Section
        intellect = 1
        willpower = 1
        charisma = 1
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                mental_spent = 0
                mental_points = temp_val
                print("\nYou have", mental_points, "Mental Attribute points available.")
                while True:
                    try:
                        mental_spent = int(input("How many points would you like to put into Intellect? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= mental_spent <= mental_points:
                        intellect += mental_spent
                        mental_points -= mental_spent
                        temp_val = mental_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                mental_spent = 0
                mental_points = temp_val
                print("\nYou have", mental_points, "Mental Attribute points available.")
                while True:
                    try:
                        mental_spent = int(input("How many points would you like to put into Willpower? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= mental_spent <= mental_points:
                        willpower += mental_spent
                        mental_points -= mental_spent
                        temp_val = mental_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                mental_spent = 0
                mental_points = temp_val
                print("\nYou have", mental_points, "Mental Attribute points available.")
                while True:
                    try:
                        mental_spent = int(input("How many points would you like to put into Charisma? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= mental_spent <= mental_points:
                        charisma += mental_spent
                        mental_points -= mental_spent
                        temp_val = mental_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

        temp_val = magic_points  # Magical Attributes Section
        focus = 1
        talent = 1
        skill = 1
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                magic_spent = 0
                magic_points = temp_val
                print("\nYou have", magic_points, "Magical Attribute points available.")
                while True:
                    try:
                        magic_spent = int(input("How many points would you like to put into Focus? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= magic_spent <= magic_points:
                        focus += magic_spent
                        magic_points -= magic_spent
                        temp_val = magic_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                magic_spent = 0
                magic_points = temp_val
                print("\nYou have", magic_points, "Magical Attribute points available.")
                while True:
                    try:
                        magic_spent = int(input("How many points would you like to put into Talent? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= magic_spent <= magic_points:
                        talent += magic_spent
                        magic_points -= magic_spent
                        temp_val = magic_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                magic_spent = 0
                magic_points = temp_val
                print("\nYou have", magic_points, "Magical Attribute points available.")
                while True:
                    try:
                        magic_spent = int(input("How many points would you like to put into Skill? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= magic_spent <= magic_points:
                        skill += magic_spent
                        magic_points -= magic_spent
                        temp_val = magic_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

        know_points = 3 + intellect
        arcane_k = 0
        divine_k = 0
        elemental_k = 0
        mental_k = 0
        history_k = 0
        nature_k = 0
        planar_k = 0
        temp_val = know_points

        # Knowledge Section
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                know_spent = 0
                know_points = temp_val
                print("\nYou have", know_points, "Knowledge points available.")
                while True:
                    try:
                        know_spent = int(input("How many points would you like to put into Arcane Knowledge? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= know_spent <= know_points:
                        arcane_k += know_spent
                        know_points -= know_spent
                        temp_val = know_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                know_spent = 0
                know_points = temp_val
                print("\nYou have", know_points, "Knowledge points available.")
                while True:
                    try:
                        know_spent = int(input("How many points would you like to put into Divine Knowledge? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= know_spent <= know_points:
                        divine_k += know_spent
                        know_points -= know_spent
                        temp_val = know_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                know_spent = 0
                know_points = temp_val
                print("\nYou have", know_points, "Knowledge points available.")
                while True:
                    try:
                        know_spent = int(input("How many points would you like to put into Elemental Knowledge? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= know_spent <= know_points:
                        elemental_k += know_spent
                        know_points -= know_spent
                        temp_val = know_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

                valid = False
                while not valid and temp_val > 0:
                    know_spent = 0
                    know_points = temp_val
                    print("\nYou have", know_points, "Knowledge points available.")
                    while True:
                        try:
                            know_spent = int(input("How many points would you like to put into Mental Knowledge? "))
                        except TypeError as err:
                            print(err)
                            continue
                        except ValueError as err:
                            print(err)
                            continue
                        if 0 <= know_spent <= know_points:
                            mental_k += know_spent
                            know_points -= know_spent
                            temp_val = know_points
                            valid = True
                            break
                        else:
                            print("Invalid Entry. Please try again.")
                            continue

                    valid = False
                    while not valid and temp_val > 0:
                        know_spent = 0
                        know_points = temp_val
                        print("\nYou have", know_points, "Knowledge points available.")
                        while True:
                            try:
                                know_spent = int(
                                    input("How many points would you like to put into History Knowledge? "))
                            except TypeError as err:
                                print(err)
                                continue
                            except ValueError as err:
                                print(err)
                                continue
                            if 0 <= know_spent <= know_points:
                                history_k += know_spent
                                know_points -= know_spent
                                temp_val = know_points
                                valid = True
                                break
                            else:
                                print("Invalid Entry. Please try again.")
                                continue

                        valid = False
                        while not valid and temp_val > 0:
                            know_spent = 0
                            know_points = temp_val
                            print("\nYou have", know_points, "Knowledge points available.")
                            while True:
                                try:
                                    know_spent = int(
                                        input("How many points would you like to put into Nature Knowledge? "))
                                except TypeError as err:
                                    print(err)
                                    continue
                                except ValueError as err:
                                    print(err)
                                    continue
                                if 0 <= know_spent <= know_points:
                                    nature_k += know_spent
                                    know_points -= know_spent
                                    temp_val = know_points
                                    valid = True
                                    break
                                else:
                                    print("Invalid Entry. Please try again.")
                                    continue

                            valid = False
                            while not valid and temp_val > 0:
                                know_spent = 0
                                know_points = temp_val
                                print("\nYou have", know_points, "Knowledge points available.")
                                while True:
                                    try:
                                        know_spent = int(
                                            input("How many points would you like to put into Planar Knowledge? "))
                                    except TypeError as err:
                                        print(err)
                                        continue
                                    except ValueError as err:
                                        print(err)
                                        continue
                                    if 0 <= know_spent <= know_points:
                                        planar_k += know_spent
                                        know_points -= know_spent
                                        temp_val = know_points
                                        valid = True
                                        break
                                    else:
                                        print("Invalid Entry. Please try again.")
                                        continue

        appearance = 1
        if "Beautiful" in traits:
            appearance += 2
        if "Supernatural Beauty" in traits:
            appearance += 2
        if "Transcendent Beauty" in traits:
            appearance += 2

        insanity = 0

        valid = False
        temp_val = csw_points  # Contacts/Sanctum/Wealth
        contacts = 0
        sanctum = 0
        wealth = 0
        while temp_val > 0:
            valid = False
            while not valid and temp_val > 0:
                csw_spent = 0
                csw_points = temp_val
                print("\nYou have", csw_points, "points available to spend on Contacts, Sanctum, and Wealth.")
                while True:
                    try:
                        csw_spent = int(input("How many points would you like to put into Contacts? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= csw_spent <= csw_points:
                        contacts += csw_spent
                        csw_points -= csw_spent
                        temp_val = csw_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                csw_spent = 0
                csw_points = temp_val
                print("\nYou have", csw_points, "points available to spend on Contacts, Sanctum, and Wealth.")
                while True:
                    try:
                        csw_spent = int(input("How many points would you like to put into Sanctum? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= csw_spent <= csw_points:
                        sanctum += csw_spent
                        csw_points -= csw_spent
                        temp_val = csw_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

            valid = False
            while not valid and temp_val > 0:
                csw_spent = 0
                csw_points = temp_val
                print("\nYou have", csw_points, "points available to spend on Contacts, Sanctum, and Wealth.")
                while True:
                    try:
                        csw_spent = int(input("How many points would you like to put into Wealth? "))
                    except TypeError as err:
                        print(err)
                        continue
                    except ValueError as err:
                        print(err)
                        continue
                    if 0 <= csw_spent <= csw_points:
                        wealth += csw_spent
                        csw_points -= csw_spent
                        temp_val = csw_points
                        valid = True
                        break
                    else:
                        print("Invalid Entry. Please try again.")
                        continue

        health = (5 + stamina) * level
        if "Defender, Lesser" in traits:
            health += (1 * level)
        if "Defender, Greater" in traits:
            health += (1 * level)
        mana = 7 + (2 * charisma) + level
        if "Mana Reserve" in traits:
            mana += 3
        if "Mana Reserve, Greater" in traits:
            mana += 3
        pd = 7 + dexterity + stamina
        md = 7 + willpower + charisma
        aura_rating = \
            (max(strength, dexterity, stamina)
             + max(intellect, willpower, charisma)
             + max(focus, talent, skill)
             + level)

        char = Character(name, race, character_class, level, athletics, artistic, scholarly, social, survival,
                         strength, dexterity, stamina, intellect, willpower, charisma, focus, talent, skill,
                         tradition, primary_circle, paths, health, mana, pd, md, aura_rating, appearance, insanity,
                         arcane_k, divine_k, elemental_k, mental_k, history_k, nature_k, planar_k, contacts,
                         sanctum, wealth, traits, channeler_order, v_bloodline, sang_hex, lycan_tribe, flaws)
        print_char_sheet()
        selection = selector("Do you wish to save your character?\n"
                             "1. Yes\n"
                             "2. No\n", 1, 2)
        if selection == 1:
            char.pickle_char()
        if selection == 2:
            pass
        running = True
        continue
    if var in ["n", "N", "No", "no"]:
        print("Select existing character to load: \n")
        char = unpickle_char()
        print_char_sheet()
        selection = selector("Do you wish to level-up your character?\n"
                             "1. Yes\n"
                             "2. No\n", 1, 2)
        know_points = 1
        if selection == 1:
            char.level += 1
            selection = selector("You have 1 Physical point to assign:\n"
                                 "1. Strength\n"
                                 "2. Dexterity\n"
                                 "3. Stamina\n", 1, 3)
            if selection == 1:
                char.strength += 1
            if selection == 2:
                char.dex += 1
            if selection == 3:
                char.stamina += 1
            selection = selector("You have 1 Mental point to assign:\n"
                                 "1. Intellect\n"
                                 "2. Willpower\n"
                                 "3. Charisma\n", 1, 3)
            if selection == 1:
                char.intellect += 1
                know_points += 1
            if selection == 2:
                char.willpower += 1
            if selection == 3:
                char.charisma += 1

            magic_points = 2
            while magic_points > 0:
                selection = selector(f"You have {magic_points} Magical point(s) to assign:\n"
                                     "1. Focus\n"
                                     "2. Talent\n"
                                     "3. Skill\n", 1, 3)
                if selection == 1:
                    char.focus += 1
                if selection == 2:
                    char.talent += 1
                if selection == 3:
                    char.skill += 1
                magic_points -= 1

            while know_points > 0:
                selection = selector(f"You have {know_points} Knowledge point(s) to assign:\n"
                                     "1. Arcane\n"
                                     "2. Divine\n"
                                     "3. Elemental\n"
                                     "4. History\n"
                                     "5. Mental\n"
                                     "6. Nature\n"
                                     "7. Planar\n", 1, 7)
                if selection == 1:
                    char.arcane_k += 1
                if selection == 2:
                    char.divine_k += 1
                if selection == 3:
                    char.elemental_k += 1
                if selection == 4:
                    char.history_k += 1
                if selection == 5:
                    char.mental_k += 1
                if selection == 6:
                    char.nature_k += 1
                if selection == 7:
                    char.planar_k += 1
                know_points -= 1

        if (char.level % 2) == 0:
            valid = False
            while not valid:
                try:
                    choice = str(input("Would you like to see the list of traits? Y/N\n"))
                    if choice == "Y" or choice == "y":
                        for key in traits_dict:
                            print("-" * 25)
                            print(key + " : " + traits_dict[key])
                    selection = str(input("Please type the name of the trait you wish to take: \n"))
                except TypeError as err:
                    print(err)
                    continue
                except ValueError as err:
                    print(err)
                    continue
                if selection != "":
                    if selection not in traits_dict:
                        continue
                    valid = True
                    char.traits.append(selection)
                    break
                else:
                    print("Invalid Entry. Please try again.")
                    continue

            char.level += 1
            health = (5 + char.stamina) * char.level
            if "Defender, Lesser" in char.traits:
                char.health += (1 * char.level)
            if "Defender, Greater" in char.traits:
                char.health += (1 * char.level)
            char.mana = 7 + (2 * char.charisma) + char.level
            if "Mana Reserve" in char.traits:
                char.mana += 3
            if "Mana Reserve, Greater" in char.traits:
                char.mana += 3
            char.pd = 7 + char.dexterity + char.stamina
            char.md = 7 + char.willpower + char.charisma
            char.aura_rating = \
                (max(char.strength, char.dexterity, char.stamina)
                 + max(char.intellect, char.willpower, char.charisma)
                 + max(char.focus, char.talent, char.skill)
                 + char.level)

            char.filename = f"{char.name}_lvl{char.level}_{char.character_class}.pkl"
            print_char_sheet()
            char.pickle_char()

        if selection == 2:
            pass
        running = True
        continue
    else:
        print("Exiting Program. Have a nice day!\n")
        running = False
