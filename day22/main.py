__author__ = 'Filip'

bleed = 1

class EffectInEffectError(Exception):
    pass

class Spell(object):
    def __init__(self, name, log):
        self.name = name
        self.log = log

    def cast(self, player, boss, effects):
        raise NotImplementedError

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class MagicMissile(Spell):
    def __init__(self, log):
        super(MagicMissile, self).__init__('Magic Missile', log)

    def cast(self, player, boss, effects):
        self.log.append('Player casts Magic Missile, dealing 4 damage.')
        boss.hp -= 4
        return 53

class Drain(Spell):
    def __init__(self, log):
        super(Drain, self).__init__('Drain', log)

    def cast(self, player, boss, effects):
        self.log.append('Player casts Drain, dealing 2 damage, and healing 2 hit points.')
        boss.hp -= 2
        player.hp += 2
        return 73

class Shield(Spell):
    def __init__(self, log):
        super(Shield, self).__init__('Shield', log)

    def cast(self, player, boss, effects):
        self.log.append('Player casts Shield, increasing armor by 7.')
        if effects.contains_effect_class(ShieldEffect):
            raise EffectInEffectError
        ShieldEffect(player, boss, effects, self.log)
        return 113

class Poison(Spell):
    def __init__(self, log):
        super(Poison, self).__init__('Poison', log)

    def cast(self, player, boss, effects):
        self.log.append('Player casts Poison.')
        if effects.contains_effect_class(PoisonEffect):
            raise EffectInEffectError
        PoisonEffect(player, boss, effects, self.log)
        return 173

class Recharge(Spell):
    def __init__(self, log):
        super(Recharge, self).__init__('Recharge', log)

    def cast(self, player, boss, effects):
        self.log.append('Player casts Recharge.')
        if effects.contains_effect_class(RechargeEffect):
            raise EffectInEffectError
        RechargeEffect(player, boss, effects, log)
        return 229


class Effect(object):
    def __init__(self, name, player, boss, effects, duration, log):
        self.name = name
        self.player = player
        self.boss = boss
        self.effects = effects
        self.duration = duration
        self.stopped = False
        self.log = log
        effects.append(self)

    def apply(self):
        self.duration -= 1
        self._stop_if_ended()

    def _stop_if_ended(self):
        if self.duration == 0:
            self._stop()

    def _stop(self):
        self.stopped = True
        self.log.append( '{} wears off.'.format(self.name))

class ShieldEffect(Effect):
    def __init__(self, player, boss, effects, log):
        super(ShieldEffect, self).__init__('Shield', player, boss, effects, 6, log)
        self.player.armor += 7

    def apply(self):
        super(ShieldEffect, self).apply()
        self.log.append("Shield's timer is now {}.".format(self.duration))

    def _stop(self):
        super(ShieldEffect, self)._stop()
        self.player.armor -= 7


class PoisonEffect(Effect):
    def __init__(self, player, boss, effects, log):
        super(PoisonEffect, self).__init__('Poison', player, boss, effects, 6, log)

    def apply(self):
        super(PoisonEffect, self).apply()
        self.log.append('Poison deals 3 damage, its timer is now {}.'.format(self.duration))
        self.boss.hp -= 3

class RechargeEffect(Effect):
    def __init__(self, player, boss, effects, log):
        super(RechargeEffect, self).__init__('Recharge', player, boss, effects, 5, log)

    def apply(self):
        super(RechargeEffect, self).apply()
        self.log.append('Recharge procides 101 mana, its timer is now {}.'.format(self.duration))
        self.player.mana += 101

class Player:
    def __init__(self, spells, hp=50, mana=500):
        self.spells = spells
        self.hp = hp
        self.mana = mana
        self.armor = 0

    def cast(self, boss, effects):
        spell = self.spells.pop(0)
        cost = spell.cast(self, boss, effects)
        self.mana -= cost
        return cost

class Boss:
    def __init__(self, hp=55, damage=8):
        self.hp = hp
        self.damage = damage

class EffectList(list):
    def contains_effect_class(self, effectClass):
        for effect in self:
            if type(effect) is effectClass:
                return True
        return False

class Battle:
    def __init__(self, player, boss, log):
        self.log = log
        effects = EffectList()
        self.mana_spent = 0
        beginning_spells = list(player.spells)
        while True:
            self.log.append('-- Player turn --')
            self.log.append('- Player has {} hit points, {} armor, {} mana'.format(player.hp, player.armor, player.mana))
            self.log.append('- Boss has {} hit points'.format(boss.hp))
            player.hp -= bleed
            if player.hp <= 0:
                self.victory = False
                break
            for effect in effects:
                effect.apply()
            effects = EffectList([effect for effect in effects if not effect.stopped])

            if len(player.spells) == 0:
                #print 'Out of spells! Spells: {}'.format(beginning_spells)
                self.log.append('Out of spells!')
                self.log.append(str(beginning_spells))
                self.victory = False
                break
            try:
                self.mana_spent += player.cast(boss, effects)
            except EffectInEffectError:
                print 'Effect in effect! Spells: {}'.format(beginning_spells)
                self.victory = False
                break
            if player.mana < 0:
                self.victory = False
                break
            if boss.hp <= 0:
                self.victory = True
                break
            self.log.append('')

            self.log.append('-- Boss turn --')
            self.log.append('- Player has {} hit points, {} armor, {} mana'.format(player.hp, player.armor, player.mana))
            self.log.append('- Boss has {} hit points'.format(boss.hp))
            for effect in effects:
                effect.apply()
            effects = EffectList([effect for effect in effects if not effect.stopped])
            if boss.hp <= 0:
                self.victory = True
                break
            self.log.append('Boss attacks for {}-{} = {} damage!'.format(boss.damage, player.armor, boss.damage - player.armor))
            player.hp -= (boss.damage - player.armor)
            if player.hp <= 0:
                self.victory = False
                break
            self.log.append('')
        if self.victory:
            self.log.append('Player wins!')
        else:
            self.log.append('Player loses.')

# player = Player([Recharge(), Shield(), Drain(), Poison(), MagicMissile()], 10, 250)
# boss = Boss(14, 8)
#
# battle = Battle(player, boss)

spells = [MagicMissile, Drain, Shield, Poison, Recharge]
player_turn_durations = {MagicMissile: 0, Drain: 0, Shield: 4, Poison: 3, Recharge: 3}

spell_lists = []
MAX_LENGTH = 9

def add_spell_to_spell_list(input_spell_list):
    global spell_lists
    for spell in spells:
        if spell in input_spell_list:
            player_turns_since_last_cast = input_spell_list[::-1].index(spell) + 1
            spell_duration = player_turn_durations[spell]
            if player_turns_since_last_cast < spell_duration:
                continue
        new_spell_list = input_spell_list + [spell]
        if len(new_spell_list) < MAX_LENGTH:
            add_spell_to_spell_list(new_spell_list)
        else:
            spell_lists.append(new_spell_list)


add_spell_to_spell_list([])

# for spell_list in spell_lists:
#     print spell_list
# print len(spell_lists)

# spell_combinations = list(product(spells, repeat=6))



results = []
i = 1
total_nr = len(spell_lists)
for spell_combination in spell_lists:
    #print '{}/{}'.format(i, total_nr)
    i += 1

    log = []
    spells = [spell(log) for spell in spell_combination]
    player = Player(spells)
    boss = Boss()
    battle = Battle(player, boss, log)
    if battle.victory:
        results.append((battle.mana_spent, battle.log))

min_mana_spent = 100000000
min_log = []
for mana_spent, log in results:
    if mana_spent < min_mana_spent:
        min_mana_spent = mana_spent
        min_log = log

print min_mana_spent
for row in min_log:
    print row


