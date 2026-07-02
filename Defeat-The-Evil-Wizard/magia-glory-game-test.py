class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.secret_ability_used = False

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name} - HP: {self.health}/{self.max_health}, ATK: {self.attack_power}")


# ------------------ WARRIOR ------------------
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 140, 25)

    def special_ability(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Strike for {damage} damage!")

    def shield_block(self):
        self.health += 10
        print(f"{self.name} uses Shield Block (+10 HP)")

    def secret_ability(self, opponent):
        if self.health > 20:
            print("Last Stand not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Last Stand already used!")
            return

        damage = self.attack_power * 3
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} uses LAST STAND for {damage} damage!")


# ------------------ MAGE ------------------
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100, 35)

    def special_ability(self, opponent):
        damage = 50
        opponent.health -= damage
        print(f"{self.name} casts Fireball for {damage} damage!")

    def ice_shield(self):
        self.health += 15
        print(f"{self.name} uses Ice Shield (+15 HP)")

    def secret_ability(self, opponent):
        if self.health > 30:
            print("Arcane Blast not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Arcane Blast already used!")
            return

        damage = 100
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} uses ARCANE BLAST for {damage} damage!")


# ------------------ EVIL WIZARD ------------------
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, 200, 15)

    def special_ability(self, opponent):
        damage = 90
        opponent.health -= damage
        print(f"{self.name} uses Oblivion for {damage} damage!")

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 HP")

    def secret_ability(self, opponent):
        if self.health > 50:
            print("Dark Portal not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Dark Portal already used!")
            return

        damage = 120
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} opens DARK PORTAL for {damage} damage!")


# ------------------ ARCHER ------------------
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 120, 20)

    def special_ability(self, opponent):
        damage = 40
        opponent.health -= damage
        print(f"{self.name} uses Precision Shot for {damage} damage!")

    def evade(self):
        self.health += 10
        print(f"{self.name} evades (+10 HP)")

    def secret_ability(self, opponent):
        if self.health > 40:
            print("Rapid Fire not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Rapid Fire already used!")
            return

        damage = 80
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} uses RAPID FIRE for {damage} damage!")


# ------------------ PALADIN ------------------
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, 160, 30)

    def special_ability(self, opponent):
        damage = 60
        opponent.health -= damage
        print(f"{self.name} uses Holy Light for {damage} damage!")

    def divine_shield(self):
        self.health += 20
        print(f"{self.name} uses Divine Shield (+20 HP)")

    def secret_ability(self, opponent):
        if self.health > 30:
            print("Disintegrate not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Disintegrate already used!")
            return

        damage = 100
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} uses DISINTEGRATE for {damage} damage!")


# ------------------ CHOSEN ONE ------------------
class Chosen_one(Character):
    def __init__(self, name):
        super().__init__(name, 200, 40)

    def special_ability(self, opponent):
        damage = 80
        opponent.health -= damage
        print(f"{self.name} uses Divine Wrath for {damage} damage!")

    def celestial_shield(self):
        self.health += 25
        print(f"{self.name} uses Celestial Shield (+25 HP)")

    def secret_ability(self, opponent):
        if self.health > 50:
            print("Judgment Day not unlocked yet!")
            return
        if self.secret_ability_used:
            print("Judgment Day already used!")
            return

        damage = 150
        opponent.health -= damage
        self.secret_ability_used = True

        print(f"{self.name} uses JUDGMENT DAY for {damage} damage!")


# ------------------ TESTS ------------------
def test_game():
    warrior = Warrior("TestWarrior")
    enemy = EvilWizard("TestEnemy")

    warrior.attack(enemy)
    assert enemy.health == 175

    warrior.special_ability(enemy)
    assert enemy.health == 125

    warrior.shield_block()
    assert warrior.health == 150

    warrior.health = 20
    warrior.secret_ability(enemy)
    assert enemy.health == 50   # FIXED EXPECTATION


# ------------------ SIMPLE GAME LOOP ------------------
def battle(player, opponent):
    print(f"\n{player.name} vs {opponent.name}\n")

    while player.health > 0 and opponent.health > 0:
        player.display_stats()
        opponent.display_stats()

        print("\n1 Attack | 2 Special | 3 Secret | 4 Heal")
        action = input("> ")

        if action == "1":
            player.attack(opponent)
        elif action == "2":
            player.special_ability(opponent)
        elif action == "3":
            player.secret_ability(opponent)
        elif action == "4":
            if hasattr(player, "shield_block"):
                player.shield_block()
            elif hasattr(player, "ice_shield"):
                player.ice_shield()
            elif hasattr(player, "evade"):
                player.evade()
            elif hasattr(player, "divine_shield"):
                player.divine_shield()
            elif hasattr(player, "celestial_shield"):
                player.celestial_shield()
        else:
            print("Invalid move")

        if opponent.health > 0:
            opponent.attack(player)

    print("\nYou Win!" if player.health > 0 else "\nYou Lose!")


def create_character():
    name = input("Name: ")

    print("1 Warrior 2 Mage 3 Archer 4 Paladin 5 Chosen One")
    choice = input("> ")

    return {
        "1": Warrior(name),
        "2": Mage(name),
        "3": Archer(name),
        "4": Paladin(name),
        "5": Chosen_one(name)
    }.get(choice, Warrior(name))


def main():
    print("MAGIA GLORY GAME")
    player = create_character()
    enemy = EvilWizard("Kel'Thuzad")

    battle(player, enemy)


if __name__ == "__main__":
    test_game()
    main()
