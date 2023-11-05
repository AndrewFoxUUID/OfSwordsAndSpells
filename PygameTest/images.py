import pygame, os
from constants import *

class Images():
    pygame.init()
    display = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)

    # -- USER INTERFACE --
    # Exclamation Point
    exclamation_point = [pygame.image.load("Assets/User Interface/Exclamation Point/" + str(i) + ".png").convert_alpha() for i in range(6)]

    # Game Icon
    icon = pygame.image.load("Assets/Icon/icon_base.png").convert_alpha()

    # Item Base
    itembase = [pygame.image.load("Assets/User Interface/Item Base/" + str(i) + ".png").convert_alpha() for i in range(13)]

    # Hearts
    base4 = pygame.image.load("Assets/User Interface/Hearts/base4.png").convert_alpha()
    base3 = pygame.image.load("Assets/User Interface/Hearts/base3.png").convert_alpha()
    base2 = pygame.image.load("Assets/User Interface/Hearts/base2.png").convert_alpha()
    base1 = pygame.image.load("Assets/User Interface/Hearts/base1.png").convert_alpha()
    heart4 = pygame.image.load("Assets/User Interface/Hearts/heart4.png").convert_alpha()
    heart3 = pygame.image.load("Assets/User Interface/Hearts/heart3.png").convert_alpha()
    heart2 = pygame.image.load("Assets/User Interface/Hearts/heart2.png").convert_alpha()
    heart1 = pygame.image.load("Assets/User Interface/Hearts/heart1.png").convert_alpha()
    shield = pygame.image.load("Assets/User Interface/Hearts/shield.png").convert_alpha()

    # Menu Books
    menubooks = [pygame.image.load("Assets/User Interface/Menu Books/menubook" + str(i) + ".png").convert_alpha() for i in range(7)]

    # Spell Icons
    spellicons = [pygame.image.load("Assets/User Interface/Spell Icons/skill_icons" + str(i) + ".png").convert_alpha() for i in range(1, 57)]

    # Spell Highlight
    spellhighlight = [pygame.image.load("Assets/User Interface/Spell Highlight/" + str(i) + ".png").convert_alpha() for i in range(11)]

    # Text Popup Base
    textpopupbase = [pygame.image.load("Assets/User Interface/Text Popup Base/textpopupbase-" + str(i) + ".png").convert_alpha() for i in range(8)]

    # Buttons
    checkbox_empty = pygame.image.load("Assets/User Interface/Buttons/checkbox_empty.png").convert_alpha()
    checkbox_filled = pygame.image.load("Assets/User Interface/Buttons/checkbox_filled.png").convert_alpha()

    # Items
    items = [pygame.image.load("Assets/Items/Item__" + ("0" if i < 100 else "") + ("0" if i < 10 else "") + str(i) + ".png").convert_alpha() for i in range(148)]
    placeholders = [pygame.image.load("Assets/Items/Placeholders/" + str(i) + ".png").convert_alpha() for i in range(12)]

    # -- Projectiles --
    arrow = [pygame.image.load("Assets/Main/Objects/Arrow/" + str(i) + ".png").convert_alpha() for i in range(7)]
    fireball_small = [pygame.image.load("Assets/Projectiles/Fireballs/1/1_" + str(i) + ".png").convert_alpha() for i in range(61)]
    fireball_medium = [pygame.image.load("Assets/Projectiles/Fireballs/3/1_" + str(i) + ".png").convert_alpha() for i in range(61)]
    fireball_large = [pygame.image.load("Assets/Projectiles/Fireballs/2/1_" + str(i) + ".png").convert_alpha() for i in range(61)]
    wind = [pygame.image.load("Assets/Projectiles/Wind/" + str(i) + ".png").convert_alpha() for i in range(4)]

    # -- Hero Knight -- (83, 50, 20), (34, 22, 10)
    human_attack1 = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Attack1/HeroKnight_Attack1_" + str(i) + ".png").convert_alpha() for i in range(6)]
    human_attack1_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_attack1]
    human_attack1_mask = human_attack1_masks[0][0]
    for mask in human_attack1_masks:
        human_attack1_mask.draw(mask[0], (0, 0))
        human_attack1_mask.draw(mask[1], (0, 0))
    human_attack2 = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Attack2/HeroKnight_Attack2_" + str(i) + ".png").convert_alpha() for i in range(6)]
    human_attack2_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_attack2]
    human_attack2_mask = human_attack2_masks[0][0]
    for mask in human_attack2_masks:
        human_attack2_mask.draw(mask[0], (0, 0))
        human_attack2_mask.draw(mask[1], (0, 0))
    human_attack3 = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Attack3/HeroKnight_Attack3_" + str(i) + ".png").convert_alpha() for i in range(8)]
    human_attack3_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_attack3]
    human_attack3_mask = human_attack3_masks[0][0]
    for mask in human_attack3_masks:
        human_attack3_mask.draw(mask[0], (0, 0))
        human_attack3_mask.draw(mask[1], (0, 0))
    human_block = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Block/HeroKnight_Block_" + str(i) + ".png").convert_alpha() for i in range(5)]
    human_block_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_block]
    human_block_mask = human_block_masks[0][0]
    for mask in human_block_masks:
        human_block_mask.draw(mask[0], (0, 0))
        human_block_mask.draw(mask[1], (0, 0))
    human_blockidle = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/BlockIdle/HeroKnight_Block Idle_" + str(i) + ".png").convert_alpha() for i in range(8)]
    human_blockidle_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_blockidle]
    human_blockidle_mask = human_blockidle_masks[0][0]
    for mask in human_blockidle_masks:
        human_blockidle_mask.draw(mask[0], (0, 0))
        human_blockidle_mask.draw(mask[1], (0, 0))
    human_blocknoeffect = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/BlockNoEffect/HeroKnight_BlockNoEffect_" + str(i) + ".png").convert_alpha() for i in range(5)]
    human_blocknoeffect_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_blocknoeffect]
    human_blocknoeffect_mask = human_blocknoeffect_masks[0][0]
    for mask in human_blocknoeffect_masks:
        human_blocknoeffect_mask.draw(mask[0], (0, 0))
        human_blocknoeffect_mask.draw(mask[1], (0, 0))
    human_cast = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Cast/HeroKnight_Cast_" + str(i) + ".png").convert_alpha() for i in range(3)]
    human_cast_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_cast]
    human_cast_mask = human_cast_masks[0][0]
    for mask in human_cast_masks:
        human_cast_mask.draw(mask[0], (0, 0))
        human_cast_mask.draw(mask[1], (0, 0))
    human_death = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/DeathNoBlood/HeroKnight_DeathNoBlood_" + str(i) + ".png").convert_alpha() for i in range(10)]
    human_death_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_death]
    human_death_mask = human_death_masks[0][0]
    for mask in human_death_masks:
        human_death_mask.draw(mask[0], (0, 0))
        human_death_mask.draw(mask[1], (0, 0))
    human_fall = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Fall/HeroKnight_Fall_" + str(i) + ".png").convert_alpha() for i in range(4)]
    human_fall_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_fall]
    human_fall_mask = human_fall_masks[0][0]
    for mask in human_fall_masks:
        human_fall_mask.draw(mask[0], (0, 0))
        human_fall_mask.draw(mask[1], (0, 0))
    human_hurt = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Hurt/HeroKnight_Hurt_" + str(i) + ".png").convert_alpha() for i in range(3)]
    human_hurt_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_hurt]
    human_hurt_mask = human_hurt_masks[0][0]
    for mask in human_hurt_masks:
        human_hurt_mask.draw(mask[0], (0, 0))
        human_hurt_mask.draw(mask[1], (0, 0))
    human_idle = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Idle/HeroKnight_Idle_" + str(i) + ".png").convert_alpha() for i in range(8)]
    human_idle_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_idle]
    human_idle_mask = human_idle_masks[0][0]
    for mask in human_idle_masks:
        human_idle_mask.draw(mask[0], (0, 0))
        human_idle_mask.draw(mask[1], (0, 0))
    human_jump = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Jump/HeroKnight_Jump_" + str(i) + ".png").convert_alpha() for i in range(3)]
    human_jump_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_jump]
    human_jump_mask = human_jump_masks[0][0]
    for mask in human_jump_masks:
        human_jump_mask.draw(mask[0], (0, 0))
        human_jump_mask.draw(mask[1], (0, 0))
    human_ledgegrab = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/LedgeGrab/HeroKnight_Grab Ledge_" + str(i) + ".png").convert_alpha() for i in range(4,5)]
    human_ledgegrab_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_ledgegrab]
    human_ledgegrab_mask = human_ledgegrab_masks[0][0]
    for mask in human_ledgegrab_masks:
        human_ledgegrab_mask.draw(mask[0], (0, 0))
        human_ledgegrab_mask.draw(mask[1], (0, 0))
    human_roll = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Roll/HeroKnight_Roll_" + str(i) + ".png").convert_alpha() for i in range(9)]
    human_roll_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_roll]
    human_roll_mask = human_roll_masks[0][0]
    for mask in human_roll_masks:
        human_roll_mask.draw(mask[0], (0, 0))
        human_roll_mask.draw(mask[1], (0, 0))
    human_run = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/Run/HeroKnight_Run_" + str(i) + ".png").convert_alpha() for i in range(10)]
    human_run_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_run]
    human_run_mask = human_run_masks[0][0]
    for mask in human_run_masks:
        human_run_mask.draw(mask[0], (0, 0))
        human_run_mask.draw(mask[1], (0, 0))
    human_wallslide = [pygame.image.load("Assets/Hero Knight/Sprites/HeroKnight/WallSlide/HeroKnight_Slide_" + str(i) + ".png").convert_alpha() for i in range(5)]
    human_wallslide_masks = [(pygame.mask.from_threshold(pygame.transform.scale(image, (200, 110)), (60, 40, 40), (60, 40, 40)), pygame.mask.from_threshold(pygame.transform.scale(pygame.transform.flip(image, True, False), (200, 110)), (60, 40, 40), (60, 40, 40))) for image in human_wallslide]
    human_wallslide_mask = human_wallslide_masks[0][0]
    for mask in human_wallslide_masks:
        human_wallslide_mask.draw(mask[0], (0, 0))
        human_wallslide_mask.draw(mask[1], (0, 0))

    human_blockflash = [pygame.image.load("Assets/Hero Knight/Sprites/Effects/BlockFlash/BlockFlash_" + str(i) + ".png").convert_alpha() for i in range(5)]
    human_slidedust = [pygame.image.load("Assets/Hero Knight/Sprites/Effects/SlideDust/SlideDust_" + str(i) + ".png").convert_alpha() for i in range(5)]

    # -- Map View Components --
    tiles = {}
    for file in os.listdir("Assets/Tiles/"):
        if len(file) > 4 and file[-4:] == '.png':
            tiles[file[:-4]] = pygame.image.load("Assets/Tiles/" + file).convert_alpha()
    overlays = {}
    for file in os.listdir("Assets/Tiles/Overlays/"):
        if len(file) > 4 and file[-4:] == '.png':
            overlays[file[:-4]] = pygame.image.load("Assets/Tiles/Overlays/" + file).convert_alpha()

    # -- Tile View Components --
    backgrounds = {'meadow': [], 'plains': [], 'swamp': [], 'savannah': [], 'desert': [], 'water': [], 'deep_water': [], 'snow': []}
    for dir in os.listdir("Assets/Backgrounds/"):
        for i in range(2, 5):
            if dir[0] == '.': continue
            try:
                backgrounds[dir].append(pygame.Surface((1200, 528), pygame.SRCALPHA))
                for j in range(5): backgrounds[dir][-1].blit(
                    pygame.transform.scale(pygame.image.load("Assets/Backgrounds/" + dir + "/" + str(i) + ".png").convert_alpha(), (240, 528)),
                    (240*j, 0)
                )
            except FileNotFoundError:
                continue

    chest = [pygame.image.load("Assets/Main/Objects/Obj-Chest-" + str(i) + ".png").convert_alpha() for i in range(5)]
    objects = {
        'axe': pygame.image.load("Assets/Main/Objects/Obj-Axe-Wood.png").convert_alpha(),
        'barrel': pygame.image.load("Assets/Main/Objects/Obj-Barrel.png").convert_alpha(),
        'boxes': pygame.image.load("Assets/Main/Objects/Obj-Boxes.png").convert_alpha(),
        'cage': pygame.image.load("Assets/Main/Objects/Obj-Cage.png").convert_alpha(),
        'fence': pygame.image.load("Assets/Main/Objects/Obj-Fence.png").convert_alpha(),
        'wood': pygame.image.load("Assets/Main/Objects/Obj-Wood.png").convert_alpha()
    }
    shop = pygame.image.load("Assets/Main/Misc/House-02.png").convert_alpha()
    interactables = {}
    for file in os.listdir("Assets/Objects/"):
        name = file.split(".")[0]
        if name != '':
            img = pygame.image.load("Assets/Objects/" + file)
            interactables[name] = pygame.transform.scale(img, (img.get_width()*4, img.get_height()*4))

    # -- Enemies --
    # Armadillo
    armadillo_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillo/idle" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(8)]
    armadillo_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillo_idle]
    armadillo_run = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillo/run" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    armadillo_run_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillo_run]
    armadillo_rollup = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillo/rollup" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(8)]
    armadillo_rollup_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillo_rollup]
    armadillo_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillo/hurt" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(3)]
    armadillo_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillo_hurt]
    armadillo_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillo/die" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(3)]
    armadillo_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillo_die]
    # Dummy
    dummy_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Dummy/idle" + str(i) + ".png").convert_alpha(), (70, 76)) for i in range(1)]
    dummy_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in dummy_idle]
    dummy_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Dummy/hurt" + str(i) + ".png").convert_alpha(), (70, 76)) for i in range(3)]
    dummy_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in dummy_hurt]
    dummy_throw = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Dummy/throw" + str(i) + ".png").convert_alpha(), (70, 76)) for i in range(4)]
    dummy_throw_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in dummy_throw]
    # Hedgehog
    hedgehog_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Hedgehog/idle" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    hedgehog_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in hedgehog_idle]
    hedgehog_walk = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Hedgehog/walk" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    hedgehog_walk_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in hedgehog_walk]
    hedgehog_attack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Hedgehog/attack" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    hedgehog_attack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in hedgehog_attack]
    hedgehog_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Hedgehog/die" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(3)]
    hedgehog_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in hedgehog_die]
    # TwigBlight
    twigblight_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/TwigBlight/idle" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    twigblight_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in twigblight_idle]
    twigblight_run = [pygame.transform.scale(pygame.image.load("Assets/Enemies/TwigBlight/run" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(8)]
    twigblight_run_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in twigblight_run]
    twigblight_attack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/TwigBlight/attack" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(6)]
    twigblight_attack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in twigblight_attack]
    twigblight_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/TwigBlight/hurt" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(5)]
    twigblight_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in twigblight_hurt]
    twigblight_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/TwigBlight/die" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(5)]
    twigblight_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in twigblight_die]
    # Bat
    bat_fly = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Bat/fly" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    bat_fly_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in bat_fly]
    bat_attack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Bat/attack" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(7)]
    bat_attack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in bat_attack]
    bat_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Bat/hurt" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(5)]
    bat_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in bat_hurt]
    bat_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Bat/die" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(8)]
    bat_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in bat_die]
    # Slime
    slime_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/idle" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    slime_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_idle]
    slime_slide = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/slide" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    slime_slide_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_slide]
    slime_jump = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/jump" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(8)]
    slime_jump_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_jump]
    slime_attack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/attack" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    slime_attack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_attack]
    slime_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/hurt" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(3)]
    slime_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_hurt]
    slime_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Slime/die" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    slime_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in slime_die]
    # Ghoul
    ghoul_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Ghoul/idle" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    ghoul_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in ghoul_idle]
    ghoul_walk = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Ghoul/walk" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(8)]
    ghoul_walk_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in ghoul_walk]
    ghoul_attack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Ghoul/attack" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(6)]
    ghoul_attack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in ghoul_attack]
    ghoul_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Ghoul/hurt" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(4)]
    ghoul_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in ghoul_hurt]
    ghoul_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Ghoul/die" + str(i) + ".png").convert_alpha(), (64, 64)) for i in range(6)]
    ghoul_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in ghoul_die]

    # -- Bosses --
    # Armadillon
    armadillon_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/idle" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(8)]
    armadillon_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_idle]
    armadillon_run = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/run" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(4)]
    armadillon_run_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_run]
    armadillon_rollup = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/rollup" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(5)]
    armadillon_rollup_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_rollup]
    armadillon_roll = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/roll" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(3)]
    armadillon_roll_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_roll]
    armadillon_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/hurt" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(3)]
    armadillon_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_hurt]
    armadillon_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Armadillon/die" + str(i) + ".png").convert_alpha(), (128, 128)) for i in range(3)]
    armadillon_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in armadillon_die]
    # Lich
    lich_idle = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/idle" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(8)]
    lich_idle_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_idle]
    lich_run = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/run" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(8)]
    lich_run_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_run]
    lich_jump = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/jump" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(2)]
    lich_jump_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_jump]
    lich_fall = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/fall" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(2)]
    lich_fall_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_fall]
    lich_upattack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/upattack" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(8)]
    lich_upattack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_upattack]
    lich_downattack = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/downattack" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(8)]
    lich_downattack_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_downattack]
    lich_hurt = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/hurt" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(3)]
    lich_hurt_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_hurt]
    lich_die = [pygame.transform.scale(pygame.image.load("Assets/Enemies/Lich/die" + str(i) + ".png").convert_alpha(), (500, 500)) for i in range(7)]
    lich_die_masks = [(pygame.mask.from_surface(image, 254), pygame.mask.from_surface(pygame.transform.flip(image, True, False), 254)) for image in lich_die]
