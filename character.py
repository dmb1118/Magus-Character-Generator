import os.path
import pickle


class Character:

    def __init__(self, name, race, character_class, level, athletics, artistic, scholarly, social, survival, strength,
                 dexterity, stamina, intellect, willpower, charisma, focus, talent, skill, tradition, primary_circle,
                 paths, health, mana, pd, md, aura_rating, appearance, insanity, arcane_k, divine_k, elemental_k,
                 mental_k, history_k, nature_k, planar_k, contacts, sanctum, wealth, traits, channeler_order,
                 v_bloodline, sang_hex, lycan_tribe, flaws):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.athletics = athletics
        self.artistic = artistic
        self.scholarly = scholarly
        self.social = social
        self.survival = survival
        self.strength = strength
        self.dexterity = dexterity
        self.stamina = stamina
        self.intellect = intellect
        self.willpower = willpower
        self.charisma = charisma
        self.focus = focus
        self.talent = talent
        self.skill = skill
        self.tradition = tradition
        self.primary_circle = primary_circle
        self.paths = paths
        self.health = health
        self.mana = mana
        self.pd = pd
        self.md = md
        self.aura_rating = aura_rating
        self.appearance = appearance
        self.insanity = insanity
        self.arcane_k = arcane_k
        self.divine_k = divine_k
        self.elemental_k = elemental_k
        self.mental_k = mental_k
        self.history_k = history_k
        self.nature_k = nature_k
        self.planar_k = planar_k
        self.contacts = contacts
        self.sanctum = sanctum
        self.wealth = wealth
        self.traits = traits
        self.channeler_order = channeler_order
        self.v_bloodline = v_bloodline
        self.sang_hex = sang_hex
        self.lycan_tribe = lycan_tribe
        self.flaws = flaws
        self.filename = f"{self.name}_lvl{self.level}_{self.character_class}.pkl"

    def pickle_char(self):
        with open(os.getcwd() + "/pickles/" + self.filename, 'wb') as outp:  # Overwrites any existing file.
            pickle.dump(self, outp, pickle.HIGHEST_PROTOCOL)
