import pygame
from button import *
import projectile
from images import Images

class Item():
    image = Images.placeholders[10]

    amount = 0
    sellPrice = 0
    slot = None

    descriptors = []

    @classmethod
    def drop(cls, world, pos, num=1):
        for i in range(num):
            world.sprites.add(projectile.Projectile(pos, (32, 32), 0, 0, -1, True, cls.image, updateCallback=cls.update, name=cls.__name__))

        if not world.player.tutorial['inventory']:
            world.player.tutorial['inventory'] = True
            world.pausing = 14
            world.paused = 'tutorial:inventory'
            DialogButton("Lo! An item! Pick up\nthe " + ''.join([(" " if c.lower() != c else "") + c for c in cls.__name__])[1:] + "\nand press " + pygame.key.name(world.player.keybinds['p-open_inventory']) + " to equip\nit and find out what\nit does.", (310, 90), 2).add(world.buttons)
            CustomTextButton((325, 300), 2, "    Continue    ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(world.buttons)
            Button(Images.icon, Images.icon, (WH, 110), 5).add(world.buttons)

    @classmethod
    def update(cls, projectile, world, name):
        projectile.rect.top += 4
        while pygame.sprite.spritecollideany(projectile, world.solids):
            projectile.rect.top -= 1

        if projectile.rect.colliderect(world.player.rect):
            cls.amount += 1
            if cls not in world.player.inventory.values() and cls not in world.player.inventory['inventory']:
                world.player.inventory['inventory'].append(cls)
            projectile.kill()

    @classmethod
    def sell(cls, player):
        if pygame.key.get_pressed()[pygame.K_L_SHIFT]:
            player.inventory['coins'] += cls.amount*cls.sellPrice
            cls.amount = 0
        else:
            player.inventory['coins'] += cls.sellPrice
            cls.amount -= 1

        if cls.amount == 0:
            player.inventory.pop(cls)


class Equipable(Item):
    damageIncrease = 0
    damageReduction = 0
    knockBackResistance = 0
    blockChanceIncrease = 0.0

    @classmethod
    def drawCallback(cls, world):
        pass

    @classmethod
    def rollCallback(cls, world):
        pass

    @classmethod
    def damageCallback(cls, world, amount, damagetype):
        return amount

class MartialWeapon(Equipable):
    attackStyle = 0
    damageIncrease = 0
    image = Images.placeholders[0]
    slot = 'martialweapon'

    descriptors = Equipable.descriptors + ['damageIncrease']

class ShortSword(MartialWeapon):
    attackStyle = 1
    damageIncrease = 1
    image = Images.items[0]

class Janto(MartialWeapon):
    attackStyle = 2
    damageIncrease = 1
    image = Images.items[72]

class LongSword(MartialWeapon):
    attackStyle = 1
    damageIncrease = 2
    image = Images.items[1]

class Machette(MartialWeapon):
    attackStyle = 1
    damageIncrease = 2
    image = Images.items[85]

class Rapier(MartialWeapon):
    attackStyle = 3
    damageIncrease = 1
    image = Images.items[2]

class Falchion(MartialWeapon):
    attackStyle = 3
    damageIncrease = 2
    image = Images.items[3]

class Dagger(MartialWeapon):
    attackStyle = 2
    damageIncrease = 2
    image = Images.items[73]

class Stiletto(MartialWeapon):
    attackStyle = 2
    damageIncrease = 2
    image = Images.items[74]

class Saber(MartialWeapon):
    attackStyle = 3
    damageIncrease = 3
    image = Images.items[4]

class BroadSword(MartialWeapon):
    attackStyle = 1
    damageIncrease = 3
    image = Images.items[5]

class Sai(MartialWeapon):
    attackStyle = 2
    damageIncrease = 3
    image = Images.items[75]

class Karambit(MartialWeapon):
    attackStyle = 2
    damageIncrease = 3
    image = Images.items[80]

class Pike(MartialWeapon):
    attackStyle = 5
    damageIncrease = 5
    image = Images.items[76]

class GreatSword(MartialWeapon):
    attackStyle = 1
    damageIncrease = 4
    image = Images.items[6]

class GoldDagger(MartialWeapon):
    attackStyle = 2
    damageIncrease = 5
    image = Images.items[81]

class Claymore(MartialWeapon):
    attackStyle = 1
    damageIncrease = 6
    image = Images.items[7]

class Lance(MartialWeapon):
    attackStyle = 5
    damageIncrease = 2
    image = Images.items[8]

class Spear(MartialWeapon):
    attackStyle = 6
    damageIncrease = 2
    image = Images.items[9]

class HollowHeadedSpear(MartialWeapon):
    attackStyle = 6
    damageIncrease = 3
    image = Images.items[79]

class Corseque(MartialWeapon):
    attackStyle = 5
    damageIncrease = 3
    image = Images.items[10]

class Ahlspeiss(MartialWeapon):
    attackStyle = 5
    damageIncrease = 4
    image = Images.items[11]

class Ranseur(MartialWeapon):
    attackStyle = 5
    damageIncrease = 4
    image = Images.items[77]

class Trident(MartialWeapon):
    attackStyle = 5
    damageIncrease = 4
    image = Images.items[78]

class Hatchet(MartialWeapon):
    attackStyle = 4
    damageIncrease = 1
    image = Images.items[12]

class Handaxe(MartialWeapon):
    attackStyle = 4
    damageIncrease = 2
    image = Images.items[84]

class ThrowingAxe(MartialWeapon):
    attackStyle = 6
    damageIncrease = 3
    image = Images.items[13]

class Waraxe(MartialWeapon):
    attackStyle = 4
    damageIncrease = 3
    image = Images.items[87]

class Bardiche(MartialWeapon):
    attackStyle = 5
    damageIncrease = 4
    image = Images.items[14]

class Halberd(MartialWeapon):
    attackStyle = 5
    damageIncrease = 4
    image = Images.items[86]

class Battleaxe(MartialWeapon):
    attackStyle = 4
    damageIncrease = 5
    image = Images.items[15]


class MagicWeapon(Equipable):
    image = Images.placeholders[1]
    slot = 'magicweapon'


class Helm(Equipable):
    image = Images.placeholders[2]
    slot = 'helm'

    descriptors = Equipable.descriptors + ['damageReduction']

class MetalHelm(Helm):
    damageReduction = 1
    image = Images.items[44]

class SquireHelm(Helm):
    damageReduction = 1
    image = Images.items[55]

class Cabasset(Helm):
    damageReduction = 2
    image = Images.items[111]

class HornedHelm(Helm):
    damageIncrease = 1
    damageReduction = 2
    image = Images.items[47]
    descriptors = Helm.descriptors + ['damageIncrease']

class Salade(Helm):
    damageReduction = 3
    image = Images.items[109]

class Barbuta(Helm):
    damageReduction = 3
    image = Images.items[45]

class Burganet(Helm):
    damageReduction = 4
    image = Images.items[108]

class GreatHelm(Helm):
    damageReduction = 5
    image = Images.items[46]

class HornedGreatHelm(Helm):
    damageIncrease = 2
    damageReduction = 6
    image = Images.items[110]
    descriptors = Helm.descriptors + ['damageIncrease']


class Charm(Equipable):
    image = Images.placeholders[3]
    slot = 'charm'

class ArmadilloCharm(Charm):
    image = Images.items[145]
    roll = "take 0 nonmagic damage and deal 1"
    descriptors = Charm.descriptors + ['roll']

    @classmethod
    def drawCallback(cls, world):
        if world.player.rolling and world.player.curIndex > 0 and world.player.curIndex < 8:
            img = pygame.transform.scale(Images.armadillon_roll[world.player.curIndex % 3], (128, 128))
            if world.player.flip:
                img = pygame.transform.flip(img, True, False)
            world.map_overlay_layer.blit(img, (world.player.rect.left - (45 if world.player.flip else 35), world.player.rect.top - 42))

    @classmethod
    def rollCallback(cls, world):
        if world.player.curIndex > 0 and world.player.curIndex < 8 and world.tick % 5 == 0:
            world.player.attack(world, 1, '')

    @classmethod
    def damageCallback(cls, world, amount, damagetype):
        if world.player.rolling and world.player.curIndex > 0 and world.player.curIndex < 8 and damagetype == '':
            return 0
        return amount


class BreastPlate(Equipable):
    image = Images.placeholders[4]
    slot = 'breastplate'

    descriptors = Equipable.descriptors + ['damageReduction']

class ChainTunic(BreastPlate):
    image = Images.items[115]

class LeatherTunic(BreastPlate):
    damageReduction = 1
    image = Images.items[56]

class LeatherPauldron(BreastPlate):
    damageReduction = 1
    damageIncrease = 1
    image = Images.items[112]
    descriptors = BreastPlate.descriptors + ['damageIncrease']

class StuddedTunic(BreastPlate):
    damageReduction = 2
    image = Images.items[114]

class MetalTunic(BreastPlate):
    damageReduction = 3
    image = Images.items[57]

class MetalPauldron(BreastPlate):
    damageReduction = 2
    damageIncrease = 2
    image = Images.items[113]
    descriptors = BreastPlate.descriptors + ['damageIncrease']

class MetalBreastPlate(BreastPlate):
    damageReduction = 4
    image = Images.items[58]

class GoldBreastPlate(BreastPlate):
    damageReduction = 5
    image = Images.items[59]


class Ring(Equipable):
    image = Images.placeholders[5]
    slot = 'ring'


class Boots(Equipable):
    image = Images.placeholders[6]
    slot = 'boots'

    descriptors = Equipable.descriptors + ['damageReduction', 'knockBackResistance']

class LeatherBoots(Boots):
    image = Images.items[48]

class StuddedLeatherBoots(Boots):
    damageReduction = 1
    knockBackResistance = 1
    image = Images.items[51]

class MetalBoots(Boots):
    damageReduction = 2
    knockBackResistance = 2
    image = Images.items[49]

class GoldBoots(Boots):
    damageReduction = 4
    knockBackResistance = 4
    image = Images.items[50]


class Gauntlet(Equipable):
    image = Images.placeholders[7]
    slot = 'gauntlet'

    descriptors = Equipable.descriptors + ['blockChanceIncrease', 'damageIncrease']

class LeatherGloves(Gauntlet):
    blockChanceIncrease = -0.1
    image = Images.items[60]

class FullLeatherGloves(Gauntlet):
    image = Images.items[61]

class StuddedGloves(Gauntlet):
    damageIncrease = 1
    blockChanceIncrease = 0.1
    image = Images.items[62]

class MetalGauntlet(Gauntlet):
    damageIncrease = 2
    blockChanceIncrease = 0.2
    image = Images.items[63]


class Shield(Equipable):
    image = Images.placeholders[8]
    slot = 'shield'

    descriptors = Equipable.descriptors + ['blockChanceIncrease']

class MetalShield(Shield):
    blockChanceIncrease = 0.3
    image = Images.items[25]

class WoodenShield(Shield):
    blockChanceIncrease = 0.4
    image = Images.items[26]

class WoodenHalfShield(Shield):
    blockChanceIncrease = 0.5
    image = Images.items[104]

class Buckler(Shield):
    blockChanceIncrease = 0.6
    image = Images.items[24]

class Heater(Shield):
    blockChanceIncrease = 0.7
    image = Images.items[106]

class Kite(Shield):
    knockBackResistance = 1
    blockChanceIncrease = 0.6
    image = Images.items[105]
    descriptors = Shield.descriptors + ['knockBackResistance']

class GoldShield(Shield):
    damageReduction = 1
    knockBackResistance = 2
    blockChanceIncrease = 0.8
    image = Images.items[27]
    descriptors = Shield.descriptors + ['damageReduction', 'knockBackResistance']

class WarDoor(Shield):
    damageReduction = 2
    knockBackResistance = 4
    blockChanceIncrease = 0.9
    image = Images.items[107]
    descriptors = Shield.descriptors + ['damageReduction', 'knockBackResistance']


class Cloak(Equipable):
    image = Images.placeholders[9]
    slot = 'cloak'

class Hood(Cloak):
    image = Images.items[116]


class Consumable(Item):
    lifegain = 0

class Food(Consumable):
    descriptors = Consumable.descriptors + ['lifegain']

class Apple(Food):
    lifegain = 1
    image = Images.items[64]

class Cheese(Food):
    lifegain = 2
    image = Images.items[65]

class Egg(Food):
    lifegain = 2
    image = Images.items[66]

class Pie(Food):
    lifegain = 4
    image = Images.items[67]

class Bread(Food):
    lifegain = 3
    image = Images.items[129]

class Meat(Food):
    lifegain = 4
    image = Images.items[130]

class Grapes(Food):
    lifegain = 1
    image = Images.items[138]

class Bananas(Food):
    lifegain = 1
    image = Images.items[139]


class Potion(Consumable):
    pass

class Honey(Potion):
    lifegain = 4
    image = Images.items[137]

    descriptors = Potion.descriptors + ['lifegain']

class PinkVial(Potion):
    image = Images.items[28]

class PinkFlask(Potion):
    image = Images.items[29]

class BlueVial(Potion):
    image = Images.items[30]

class BlueFlask(Potion):
    image = Images.items[31]


class BlueScroll(Item):
    image = Images.items[36]

class PinkScroll(Item):
    image = Images.items[37]

class Scroll(Item):
    image = Images.items[38]

class Tablet(Item):
    image = Images.items[39]

class CopperKey(Item):
    image = Images.items[68]

class SilverKey(Item):
    image = Images.items[69]

class Candle(Item):
    image = Images.items[70]

class Chalice(Item):
    image = Images.items[71]

class SilverBar(Item):
    image = Images.items[124]

class GoldBar(Item):
    image = Images.items[125]

class Wood(Item): # 1 wood -> 4 twigs
    image = Images.items[126]

class Twigs(Item): # 2 twigs -> 1 bowstock
    image = Images.items[127]

class Wheat(Item):
    image = Images.items[128]

class Mushroom(Item):
    image = Images.items[131]

class Rock(Item):
    image = Images.items[132]

class Mud(Item):
    image = Images.items[133]

class BlueDye(Item):
    image = Images.items[134]

class Cloth(Item):
    image = Images.items[135]

class Leaf(Item):
    image = Images.items[140]

class Feather(Item):
    image = Images.items[142]

class PhoenixFeather(Item):
    image = Images.items[143]

class BowStock(Item):
    image = Images.items[147]

class Coins(Item):
    image = Images.items[144]

    @classmethod
    def sell(cls, player):
        return


class Ammunition(Item):
    damageIncrease = 0
    velocityIncrease = 0
    image = Images.placeholders[11]
    slot = 'ammo'

    descriptors = Item.descriptors + ['damageIncrease', 'velocityIncrease']

class Arrow(Ammunition):
    image = Images.items[146]

    @classmethod
    def projectileupdate(cls, projectile, world):
        if projectile.active:
            projectile.rect.top += abs(projectile.lifespan)//(20-cls.velocityIncrease)
            projectile.rect.left += cls.velocityIncrease * (projectile.x_velocity//abs(projectile.x_velocity))

            if projectile.lifespan < -120:
                projectile.colors = Images.arrow[6]
            elif projectile.lifespan < -100:
                projectile.colors = Images.arrow[5]
            elif projectile.lifespan < -80:
                projectile.colors = Images.arrow[4]
            elif projectile.lifespan < -60:
                projectile.colors = Images.arrow[3]
            elif projectile.lifespan < -40:
                projectile.colors = Images.arrow[2]
            elif projectile.lifespan < -20:
                projectile.colors = Images.arrow[1]
            else:
                projectile.colors = Images.arrow[0]
            
            if projectile.rect.colliderect(world.player.rect):
                projectile.attack(world, 1, '')
                projectile.kill()
        elif projectile.rect.colliderect(world.player.rect):
            cls.drop(world, world.player.rect.topleft)
            projectile.kill()

        if pygame.sprite.spritecollideany(projectile, world.solids):
            projectile.active = False

nonDropables = [Item, Equipable, MartialWeapon, MagicWeapon, Helm, Charm, BreastPlate, Ring, Boots, Gauntlet, Shield, Cloak, Coins, Ammunition, Consumable, Food, Potion]

items = [
    [
        ShortSword,
        ChainTunic,
        LeatherBoots,
        LeatherGloves,
        MetalShield,
        Hood,
    ],
    [
        Janto,
        Rapier,
        MetalHelm,
        SquireHelm,
        LeatherTunic,
        StuddedLeatherBoots,
        FullLeatherGloves,
        WoodenShield,

        Hatchet,
    ],
    [
        LongSword,
        Machette,
        Falchion,
        Dagger,
        Stiletto,
        Lance,
        Spear,
        Cabasset,
        LeatherPauldron,
        StuddedTunic,
        StuddedGloves,
        WoodenHalfShield,

        Handaxe,
    ],
    [
        Saber,
        BroadSword,
        Sai,
        Karambit,
        HollowHeadedSpear,
        Corseque,
        HornedHelm,
        Salade,
        Barbuta,
        MetalTunic,
        MetalBoots,
        Buckler,

        ThrowingAxe,
        Waraxe,
    ],
    [
        GreatSword,
        Ahlspeiss,
        Ranseur,
        Trident,
        Bardiche,
        Halberd,
        Burganet,
        MetalPauldron,
        MetalBreastPlate,
        MetalGauntlet,
        Heater,
        Kite,
    ],
    [
        Pike,
        GoldDagger,
        GreatHelm,
        GoldBreastPlate,
        GoldBoots,
        GoldShield,

        Battleaxe,
    ],
    [
        Claymore,
        HornedGreatHelm,
        WarDoor,
    ],
]

item_drops = {
    'chest': ((1, 1), [
        items[0],
        items[1][:-1],
        items[2][:-1],
        items[3][:-2],
        items[4],
    ]),
    'barrel': ((1, 3), [
        [Apple, Cheese, Egg, Pie, Bread, Meat],
    ]),
    'axe': ((1, 1), [
        items[1][-1:],
        items[2][-1:],
        items[3][-2:],
    ]),
    'wood': ((2, 4), [
        [Wood],
    ]),
    'boxes': ((1, 2), [
        [PinkVial, PinkFlask, BlueVial, BlueFlask, CopperKey, SilverBar, Cloth],
    ])
}