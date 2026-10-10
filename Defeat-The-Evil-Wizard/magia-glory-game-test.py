import random


# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.block_next_attack = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        print(f"{self.name} attacks!")
        opponent.take_damage(damage)

    def take_damage(self, damage):
        if self.block_next_attack:
            print(f"{self.name} blocks or evades the attack!")
            self.block_next_attack = False
            return

        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage!")

    def heal(self):
        amount = min(25, self.max_health - self.health)
        self.health += amount
        print(f"{self.name} heals {amount} HP!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - "
            f"Health: {self.health}/{self.max_health}, "
            f"Attack Power: {self.attack_power}"
        )


# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_ability(self, opponent):
        print("1. Power Strike")
        print("2. Shield Block")
        choice = input("Choose an ability: ")

        if choice == "1":
            print(f"{self.name} uses Power Strike!")
            opponent.take_damage(self.attack_power * 2)
        elif choice == "2":
            print(f"{self.name} uses Shield Block!")
            self.block_next_attack = True
        else:
            print("Invalid ability.")
            return False

        return True


# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_ability(self, opponent):
        print("1. Fireball")
        print("2. Arcane Recovery")
        choice = input("Choose an ability: ")

        if choice == "1":
            print(f"{self.name} casts Fireball!")
            opponent.take_damage(50)
        elif choice == "2":
            amount = min(40, self.max_health - self.health)
            self.health += amount
            print(f"{self.name} uses Arcane Recovery and heals {amount} HP!")
        else:
            print("Invalid ability.")
            return False

        return True


# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def special_ability(self, opponent):
        print("1. Quick Shot")
        print("2. Evade")
        choice = input("Choose an ability: ")

        if choice == "1":
            print(f"{self.name} uses Quick Shot!")
            self.attack(opponent)

            if opponent.health > 0:
                self.attack(opponent)
        elif choice == "2":
            print(f"{self.name} prepares to evade!")
            self.block_next_attack = True
        else:
            print("Invalid ability.")
            return False

        return True


# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=30)

    def special_ability(self, opponent):
        print("1. Holy Strike")
        print("2. Divine Shield")
        choice = input("Choose an ability: ")

        if choice == "1":
            print(f"{self.name} uses Holy Strike!")
            opponent.take_damage(self.attack_power + 20)
        elif choice == "2":
            print(f"{self.name} uses Divine Shield!")
            self.block_next_attack = True
        else:
            print("Invalid ability.")
            return False

        return True


# Evil Wizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        amount = min(5, self.max_health - self.health)
        self.health += amount
        print(f"{self.name} regenerates {amount} health!")


# Basic tests
def test_game():
    warrior = Warrior("TestWarrior")
    enemy = EvilWizard("TestEnemy")

    # Warrior damage should be between 20 and 30.
    starting_health = enemy.health
    warrior.attack(enemy)
    damage = starting_health - enemy.health
    assert 20 <= damage <= 30

    # Healing restores health without exceeding the maximum.
    warrior.health = 100
    warrior.heal()
    assert warrior.health == 125

    warrior.health = 135
    warrior.heal()
    assert warrior.health == 140

    # A shield blocks one attack, then wears off.
    warrior.block_next_attack = True
    enemy.attack(warrior)
    assert warrior.health == 140
    assert warrior.block_next_attack is False

    # Wizard regeneration is capped at maximum health.
    enemy.health = 140
    enemy.regenerate()
    assert enemy.health == 145

    enemy.health = 148
    enemy.regenerate()
    assert enemy.health == 150

    print("All tests passed!\n")


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            if not player.special_ability(wizard):
                continue
        elif choice == "3":
            player.heal()
        elif choice == "4":
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")
            continue

        # The wizard regenerates and attacks if still alive.
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

    if wizard.health <= 0:
        print(f"\nVictory! {player.name} defeated {wizard.name}!")
    else:
        print(f"\nDefeat! {player.name} has been defeated!")


def main():
    print("MAGIA GLORY GAME")
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    test_game()
    main()
