__author__ = 'Filip'

import itertools
from collections import Iterable

class Combatant:
    def __init__(self, name, hp, damage=0, armor=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.cost = 0
        self.outfit = []

    def attack(self, opponent):
        damage_dealt = max(1, self.damage - opponent.armor)
        opponent.hp -= damage_dealt
        return '  - The {selfname} deals {damage}-{armor} = {damage_dealt} damage; the {opponentname} goes down to {hp} hit points.'.format(
            selfname=self.name, damage=self.damage, armor=opponent.armor, damage_dealt=damage_dealt, opponentname=opponent.name, hp=opponent.hp)

    def equip(self, outfit):
        self.outfit = outfit
        for item in outfit:
            self.cost += item.cost
            self.damage += item.damage
            self.armor += item.armor


class Battle:
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss
        self._attacker_and_defender = (self.player, self.boss)
        self.log = []

    def step(self):
        self.log.append(self._attacker_and_defender[0].attack(self._attacker_and_defender[1]))
        self._attacker_and_defender = self._attacker_and_defender[::-1]

class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return self.name

def flatten(coll):
    for i in coll:
            if isinstance(i, Iterable) and not isinstance(i, basestring):
                for subc in flatten(i):
                    yield subc
            else:
                yield i

weapons = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0)
]

armor = [
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5)
]

rings = [
    Item('Damage + 1', 25, 1, 0),
    Item('Damage + 2', 50, 2, 0),
    Item('Damage + 3', 100, 3, 0),
    Item('Defense + 1', 20, 0, 1),
    Item('Defense + 2', 40, 0, 2),
    Item('Defense + 3', 80, 0, 3)
]

outfits = itertools.product(weapons, armor + [[]], [[]] + rings + list(itertools.combinations(rings, 2)))

victories = []
losses = []
for outfit in outfits:
    outfit = list(flatten(outfit))
    print outfit
    player = Combatant('player', 100)
    player.equip(outfit)
    boss = Combatant('boss', 109, 8, 2)

    battle = Battle(player, boss)
    while player.hp > 0 and boss.hp > 0:
        battle.step()
    if player.hp > 0:
        victories.append((player.cost, player.outfit))
    else:
        losses.append((player.cost, player.outfit, battle.log))

outfit = []
lowest_cost = 1000000000
for victory in victories:
    if victory[0] < lowest_cost:
        lowest_cost = victory[0]
        outfit = victory[1]

print lowest_cost
print outfit

log = []
highest_cost = 0
for loss in losses:
    if loss[0] > highest_cost:
        highest_cost = loss[0]
        outfit = loss[1]
        log = loss[2]

print highest_cost
print outfit
for line in log:
    print line


# player = Combatant('player', 8, 5, 5)
# boss = Combatant('boss', 12, 7, 2)
# battle = Battle(player, boss)
#
# while player.hp > 0 and boss.hp > 0:
#     battle.step()
