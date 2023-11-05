import pygame

from position_utilities import Coord

class Projectile(pygame.sprite.Sprite):
    def __init__(self, topleft: Coord, dimensions: tuple, x_velocity: int, y_velocity: int, lifespan: int, piercing: bool, colors: list, imageSet: list=[], updateCallback=None, name=None):
        super().__init__()
        if len(imageSet) > 0:
            if x_velocity >= 0:
                topleft.x += (len(imageSet[0][0]) - dimensions[0])
            topleft.y += len(imageSet[0])//2 - dimensions[1]//2
        self.rect = pygame.Rect(topleft.x, topleft.y, *dimensions)
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.lifespan = lifespan
        self.piercing = piercing
        self.colors = colors
        self.imageSet = imageSet
        self.curIndex = 0
        self.updateCallback = updateCallback
        self.name = name
        self.active = True

    def update(self, world):
        if self.lifespan == 0 or (not self.piercing and pygame.sprite.spritecollideany(self, world.solids)):
            self.kill()
            return
        if world.tick % 5 == 0:
            self.lifespan -= 1
            self.curIndex += 1
            if (self.imageSet == [] and type(self.colors) == list and self.curIndex >= len(self.colors)) or (self.imageSet != [] and self.curIndex >= len(self.imageSet)):
                self.curIndex = 0

        if self.active:
            self.rect.left += self.x_velocity
            if self.rect.right < 0 or self.rect.left > TW:
                self.kill()
            self.rect.top += self.y_velocity
            if self.rect.bottom < 0 or self.rect.top > 1440:
                self.kill()

        if self.updateCallback is not None:
            if self.name is None:
                self.updateCallback(self, world)
            else:
                self.updateCallback(self, world, self.name)

    def attack(self, world, damage, damagetype=''):
        fullImage = pygame.sprite.Sprite()
        fullImage.image = pygame.transform.scale(world.player.curImageSet[world.player.curIndex], (200, 110))
        fullImage.rect = pygame.Rect(world.player.rect.left-76, world.player.rect.bottom-106, 200, 110)

        player_mask = pygame.mask.from_surface(pygame.transform.flip(fullImage.image, world.player.flip, False), 254)
        enemy_mask = pygame.mask.from_surface(pygame.transform.flip(
            pygame.transform.scale(
                self.imageSet[self.curIndex],
                (self.imageSet[self.curIndex].get_width()*2, self.imageSet[self.curIndex].get_height()*2)
            ),
            self.x_velocity < 0,
            False
        ), 254)
        if player_mask.overlap(enemy_mask, (self.rect.left - fullImage.rect.left, self.rect.top - fullImage.rect.top)):
            return world.player.damage(world, damage, damagetype)
        return False

    def draw(self, world):
        if world.player.debug:
            pygame.draw.rect(world.map_overlay_layer, PURPLE, self.rect, 1)
        if type(self.colors) == list:
            if self.imageSet == []:
                img = pygame.transform.scale(self.colors[self.curIndex], (self.rect.width, self.rect.height))
                if self.x_velocity < 0:
                    img = pygame.transform.flip(img, True, False)
                world.map_overlay_layer.blit(img, (self.rect.left, self.rect.top))
            else:
                for r, row in enumerate(self.imageSet[self.curIndex]):
                    if self.x_velocity < 0:
                        row = row[::-1]
                    for c, item in enumerate(row):
                        if item != 0:
                            pygame.draw.rect(world.map_overlay_layer, self.colors[item], (self.rect.left + c, self.rect.y + r, 1, 1))
        else:
            img = pygame.transform.scale(self.colors, (self.rect.width, self.rect.height))
            if self.x_velocity < 0:
                img = pygame.transform.flip(img, True, False)
            world.map_overlay_layer.blit(img, (self.rect.left, self.rect.top))

def wind_callback(projectile, world):
    if projectile.rect.colliderect(world.player.rect):
        projectile.attack(world, 1, '')