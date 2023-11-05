extends Node

const ITEM_DATA = {
	"Short Sword": {
		"frame": 1,
		"rarity": 0,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 2,
		"buy": 3,
		"sell": 2
	},
	"Long Sword": {
		"frame": 2,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(219, 187, 61),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Rapier": {
		"frame": 3,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Falchion": {
		"frame": 4,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(216, 152, 77),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Saber": {
		"frame": 5,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(216, 152, 77),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(216, 152, 77),
		"flair_color": Color8(121, 84, 64),
		"damage": 3,
		"buy": 5,
		"sell": 4
	},
	"Broadsword": {
		"frame": 6,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(219, 187, 61),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(127, 188, 73),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Greatsword": {
		"frame": 7,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(219, 187, 61),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(219, 187, 61),
		"flair_color": Color8(219, 187, 61),
		"damage": 4,
		"buy": 7,
		"sell": 6
	},
	"Claymore": {
		"frame": 8,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(74, 132, 154),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(219, 187, 61),
		"flair_color": Color8(125, 203, 225),
		"damage": 6,
		"buy": 12,
		"sell": 10
	},
	"Spear": {
		"frame": 9,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(121, 84, 64),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Javelin": {
		"frame": 10,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "throwing ranged",
		"player_style": "javelin",
		"light_color": Color8(144, 56, 62),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Glaive": {
		"frame": 11,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(121, 84, 64),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Lance": {
		"frame": 12,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Hatchet": {
		"frame": 13,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "throwing ranged",
		"player_style": "throwing axe",
		"damage": 2,
		"buy": 4,
		"sell": 3
	},
	"Hand Axe": {
		"frame": 14,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "axe",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Battle Axe": {
		"frame": 15,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "axe",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Cleaver": {
		"frame": 16,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "axe",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 5,
		"buy": 7,
		"sell": 6
	},
	"Long Bow": {
		"frame": 17,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 3,
		"buy": 8,
		"sell": 6
	},
	"Fanged Bow": {
		"frame": 18,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 4,
		"buy": 9,
		"sell": 7
	},
	"Short Bow": {
		"frame": 19,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 2,
		"buy": 6,
		"sell": 5
	},
	"Great Bow": {
		"frame": 20,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 5,
		"buy": 12,
		"sell": 9
	},
	"Staff": {
		"frame": 21,
		"rarity": 1,
		"slot": "magic weapon",
		"magic": true,
		"buy": 5,
		"sell": 4
	},
	"Staff of Vines": {
		"frame": 22,
		"rarity": 2,
		"slot": "magic weapon",
		"magic": true,
		"buy": 8,
		"sell": 6
	},
	"Staff of the Moon": {
		"frame": 23,
		"rarity": 2,
		"slot": "magic weapon",
		"magic": true,
		"buy": 9,
		"sell": 7
	},
	"Staff of Power": {
		"frame": 24,
		"rarity": 3,
		"slot": "magic weapon",
		"magic": true,
		"buy": 13,
		"sell": 10
	},
	"Reinforced Buckler": {
		"frame": 25,
		"rarity": 2,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 30,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(96, 59, 51),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Plate Shield": {
		"frame": 26,
		"rarity": 2,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 40,
		"light_color": Color8(207, 218, 249),
		"color": Color8(207, 218, 249),
		"dark_color": Color8(207, 218, 249),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Wooden Buckler": {
		"frame": 27,
		"rarity": 1,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 20,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(208, 163, 111),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 4,
		"sell": 3
	},
	"Gilded Shield": {
		"frame": 28,
		"rarity": 3,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 65,
		"light_color": Color8(249, 243, 95),
		"color": Color8(249, 243, 95),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 13,
		"sell": 11
	},
	"Vial of Regeneration": {
		"frame": 29,
		"rarity": 1,
		"consumable": true,
		"buy": 1,
		"sell": 1
	},
	"Flask of Regeneration": {
		"frame": 30,
		"rarity": 2,
		"consumable": true,
		"buy": 2,
		"sell": 1
	},
	"Vial of Cleansing": {
		"frame": 31,
		"rarity": 1,
		"consumable": true,
		"buy": 1,
		"sell": 1
	},
	"Flask of Cleansing": {
		"frame": 32,
		"rarity": 1,
		"consumable": true,
		"buy": 2,
		"sell": 1
	},
	"Charm of Cleansing": {
		"frame": 33,
		"rarity": 2,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(207, 218, 249),
		"magic": true,
		"buy": 20,
		"sell": 15
	},
	"Charm of Stars": {
		"frame": 34,
		"rarity": 2,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(249, 243, 95),
		"magic": true,
		"buy": 8,
		"sell": 6
	},
	"Charm of Fangs": {
		"frame": 35,
		"rarity": 2,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(255, 255, 255),
		"magic": true,
		"buy": 8,
		"sell": 6
	},
	"Charm of Skulls": {
		"frame": 36,
		"rarity": 2,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(255, 255, 255),
		"magic": true,
		"buy": 8,
		"sell": 6
	},
	"Scroll of Cleansing": {
		"frame": 37,
		"rarity": 1,
		"consumable": true,
		"buy": 3,
		"sell": 1
	},
	"Scroll of Regeneration": {
		"frame": 38,
		"rarity": 1,
		"consumable": true,
		"buy": 3,
		"sell": 1
	},
	"Lifeless Scroll": {
		"frame": 39,
		"rarity": 1,
		"buy": 1,
		"sell": 0.5
	},
	"Lifeless Tablet": {
		"frame": 40,
		"rarity": 1,
		"buy": 1,
		"sell": 0.5
	},
	"Ring of Invisibility": {
		"frame": 41,
		"rarity": 2,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(249, 243, 95),
		"magic": true,
		"buy": 15,
		"sell": 12
	},
	"Ring of Cleansing": {
		"frame": 42,
		"rarity": 3,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(112, 154, 248),
		"magic": true,
		"buy": 18,
		"sell": 14
	},
	"Ring of Regeneration": {
		"frame": 43,
		"rarity": 3,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(203, 128, 183),
		"magic": true,
		"buy": 18,
		"sell": 14
	},
	"Ring of Poison": {
		"frame": 44,
		"rarity": 2,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(169, 227, 103),
		"magic": true,
		"buy": 8,
		"sell": 6
	},
	"Plate Helm": {
		"frame": 45,
		"rarity": 1,
		"slot": "helm",
		"player_style": "helm",
		"armor": 2,
		"light_color": Color8(14, 14, 16),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(158, 173, 182),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 5,
		"sell": 4
	},
	"Barbuta": {
		"frame": 46,
		"rarity": 2,
		"slot": "helm",
		"player_style": "helm",
		"armor": 4,
		"light_color": Color8(231, 197, 159),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(158, 173, 182),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Greathelm": {
		"frame": 47,
		"rarity": 3,
		"slot": "helm",
		"player_style": "helm",
		"armor": 6,
		"light_color": Color8(231, 197, 159),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(0, 0, 0),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 13,
		"sell": 11
	},
	"Horned Helm": {
		"frame": 48,
		"rarity": 2,
		"slot": "helm",
		"player_style": "helm",
		"armor": 2,
		"martial_damage_increase": 1,
		"light_color": Color8(14, 14, 16),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(158, 173, 182),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Old Boots": {
		"frame": 49,
		"rarity": 0,
		"slot": "boots",
		"player_style": "boots",
		"armor": 1,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(135, 88, 64),
		"dark_color": Color8(120, 73, 49),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 1,
		"sell": 0.5
	},
	"Plate Boots": {
		"frame": 50,
		"rarity": 2,
		"slot": "boots",
		"player_style": "boots",
		"armor": 2,
		"speed_increase": 10,
		"light_color": Color8(207, 218, 249),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(143, 158, 167),
		"flair_color": Color8(192, 203, 234),
		"martial": true,
		"buy": 4,
		"sell": 3
	},
	"Gilded Boots": {
		"frame": 51,
		"rarity": 3,
		"slot": "boots",
		"player_style": "boots",
		"armor": 6,
		"speed_increase": 50,
		"light_color": Color8(209, 119, 58),
		"color": Color8(249, 243, 95),
		"dark_color": Color8(234, 228, 80),
		"flair_color": Color8(194, 104, 43),
		"martial": true,
		"buy": 12,
		"sell": 10
	},
	"Leather Boots": {
		"frame": 52,
		"rarity": 1,
		"slot": "boots",
		"player_style": "boots",
		"armor": 1,
		"speed_increase": 5,
		"light_color": Color8(96, 59, 51),
		"color": Color8(135, 88, 64),
		"dark_color": Color8(120, 73, 49),
		"flair_color": Color8(81, 44, 36),
		"martial": true,
		"buy": 2,
		"sell": 1
	},
	"Old Hat": {
		"frame": 53,
		"rarity": 1,
		"slot": "helm",
		"player_style": "hat",
		"magic": true,
		"buy": 4,
		"sell": 3
	},
	"Witch Hat": {
		"frame": 54,
		"rarity": 2,
		"slot": "helm",
		"player_style": "hat",
		"magic": true,
		"buy": 8,
		"sell": 5
	},
	"Stylish Headband": {
		"frame": 55,
		"rarity": 2,
		"slot": "helm",
		"player_style": "headband",
		"martial": true,
		"magic": true,
		"buy": 10,
		"sell": 5
	},
	"Squire Helm": {
		"frame": 56,
		"rarity": 1,
		"slot": "helm",
		"player_style": "hood+hat",
		"armor": 2,
		"martial": true,
		"buy": 5,
		"sell": 4
	},
	"Leather Tunic": {
		"frame": 57,
		"rarity": 1,
		"slot": "armor",
		"player_style": "armor",
		"armor": 2,
		"light_color": Color8(216, 152, 77),
		"color": Color8(209, 119, 58),
		"dark_color": Color8(135, 88, 64),
		"flair_color": Color8(196, 132, 57),
		"martial": true,
		"buy": 4,
		"sell": 3
	},
	"Plate Tunic": {
		"frame": 58,
		"rarity": 2,
		"slot": "armor",
		"player_style": "armor",
		"armor": 4,
		"light_color": Color8(120, 122, 151),
		"color": Color8(140, 142, 171),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(100, 102, 131),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Plate Armor": {
		"frame": 59,
		"rarity": 2,
		"slot": "armor",
		"player_style": "armor",
		"armor": 5,
		"light_color": Color8(120, 122, 151),
		"color": Color8(140, 142, 171),
		"dark_color": Color8(107, 104, 93),
		"flair_color": Color8(100, 102, 131),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Gilded Armor": {
		"frame": 60,
		"rarity": 3,
		"slot": "armor",
		"player_style": "armor",
		"armor": 8,
		"light_color": Color8(216, 152, 77),
		"color": Color8(219, 187, 61),
		"dark_color": Color8(144, 56, 62),
		"flair_color": Color8(184, 148, 62),
		"martial": true,
		"buy": 15,
		"sell": 13
	},
	"Old Gloves": {
		"frame": 61,
		"rarity": 0,
		"slot": "gauntlets",
		"player_style": "gauntlets",
		"block_chance_increase": 5,
		"critical_chance_increase": 5,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(135, 88, 64),
		"dark_color": Color8(120, 73, 49),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 1,
		"sell": 0.5
	},
	"Leather Gloves": {
		"frame": 62,
		"rarity": 1,
		"slot": "gauntlets",
		"player_style": "gauntlets",
		"block_chance_increase": 10,
		"critical_chance_increase": 5,
		"light_color": Color8(96, 59, 51),
		"color": Color8(135, 88, 64),
		"dark_color": Color8(120, 73, 49),
		"flair_color": Color8(81, 44, 36),
		"martial": true,
		"buy": 3,
		"sell": 2
	},
	"Inset Gauntlets": {
		"frame": 63,
		"rarity": 2,
		"slot": "gauntlets",
		"player_style": "gauntlets",
		"block_chance_increase": 15,
		"critical_chance_increase": 10,
		"light_color": Color8(96, 59, 51),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(143, 158, 167),
		"flair_color": Color8(81, 44, 36),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Plate Gauntlets": {
		"frame": 64,
		"rarity": 2,
		"slot": "gauntlets",
		"player_style": "gauntlets",
		"block_chance_increase": 20,
		"critical_chance_increase": 15,
		"light_color": Color8(131, 126, 134),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(143, 158, 167),
		"flair_color": Color8(116, 111, 119),
		"martial": true,
		"buy": 8,
		"sell": 7
	},
	"Apple": {
		"frame": 65,
		"rarity": 1,
		"life_gain": 1,
		"consumable": true,
		"buy": 0.5,
		"sell": 0.25
	},
	"Cheese": {
		"frame": 66,
		"rarity": 1,
		"life_gain": 1,
		"consumable": true,
		"buy": 0.5,
		"sell": 0.25
	},
	"Omelette": {
		"frame": 67,
		"rarity": 1,
		"life_gain": 2,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Pie": {
		"frame": 68,
		"rarity": 1,
		"life_gain": 2,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Old Key": {
		"frame": 69,
		"rarity": 1,
		"buy": 1,
		"sell": 1
	},
	"Key": {
		"frame": 70,
		"rarity": 1,
		"buy": 1,
		"sell": 1
	},
	"Candle": {
		"frame": 71,
		"rarity": 1,
		"buy": 0.5,
		"sell": 0.25
	},
	"Gilded Chalice": {
		"frame": 72,
		"rarity": 2,
		"buy": 7,
		"sell": 6
	},
	"Janto": {
		"frame": 73,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(121, 84, 64),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 2,
		"buy": 5,
		"sell": 4
	},
	"Dagger": {
		"frame": 74,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 5,
		"sell": 4
	},
	"Stiletto": {
		"frame": 75,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(77, 74, 78),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 6,
		"sell": 5
	},
	"Sai": {
		"frame": 76,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 4,
		"buy": 7,
		"sell": 6
	},
	"Pike": {
		"frame": 77,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(121, 84, 64),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 7,
		"sell": 6
	},
	"Ranseur": {
		"frame": 78,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(77, 74, 78),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(77, 74, 78),
		"damage": 4,
		"buy": 7,
		"sell": 6
	},
	"Trident": {
		"frame": 79,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "piercing melee",
		"player_style": "spear",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 5,
		"buy": 8,
		"sell": 7
	},
	"Hollow Point Spear": {
		"frame": 80,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "throwing ranged",
		"player_style": "javelin",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 8,
		"sell": 6
	},
	"Hollow Point Dagger": {
		"frame": 81,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 5,
		"buy": 8,
		"sell": 7
	},
	"Gilded Dagger": {
		"frame": 82,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(179, 184, 212),
		"color": Color8(216, 152, 77),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 6,
		"buy": 12,
		"sell": 10
	},
	"Goblin Blade": {
		"frame": 83,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "backhanded melee",
		"player_style": "dagger",
		"light_color": Color8(219, 187, 61),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(219, 187, 61),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 7,
		"buy": 15,
		"sell": 10
	},
	"Antivenom Injection": {
		"frame": 84,
		"rarity": 2,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Climbing Hooks": {
		"frame": 85,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "claws",
		"damage": 3,
		"buy": 10,
		"sell": 5
	},
	"Machette": {
		"frame": 86,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "sword",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Halberd": {
		"frame": 87,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "axe",
		"light_color": Color8(107, 104, 93),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Waraxe": {
		"frame": 88,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "axe",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(121, 84, 64),
		"flair_color": Color8(179, 184, 212),
		"damage": 6,
		"buy": 9,
		"sell": 7
	},
	"Club": {
		"frame": 89,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(79, 55, 42),
		"dark_color": Color8(79, 55, 42),
		"flair_color": Color8(79, 55, 42),
		"damage": 2,
		"buy": 3,
		"sell": 2
	},
	"Mace": {
		"frame": 90,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(0, 0, 0, 0),
		"dark_color": Color8(79, 55, 42),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Hammer": {
		"frame": 91,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(79, 55, 42),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 2,
		"buy": 3,
		"sell": 2
	},
	"Sledgehammer": {
		"frame": 92,
		"rarity": 1,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(79, 55, 42),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 3,
		"buy": 4,
		"sell": 3
	},
	"Bone Short Bow": {
		"frame": 93,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 4,
		"buy": 7,
		"sell": 5
	},
	"Bone Long Bow": {
		"frame": 94,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 5,
		"buy": 8,
		"sell": 6
	},
	"Gilded Bow": {
		"frame": 95,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 6,
		"buy": 18,
		"sell": 15
	},
	"Fanged Dark Bow": {
		"frame": 96,
		"rarity": 3,
		"slot": "martial weapon",
		"martial": true,
		"style": "shooting ranged",
		"player_style": "bow",
		"damage": 7,
		"buy": 19,
		"sell": 16
	},
	"Plate Maul": {
		"frame": 97,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(179, 184, 212),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 5,
		"sell": 4
	},
	"Plate Hammer": {
		"frame": 98,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(179, 184, 212),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(179, 184, 212),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Plate Mace": {
		"frame": 99,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(179, 184, 212),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 5,
		"sell": 4
	},
	"Plate Sledgehammer": {
		"frame": 100,
		"rarity": 2,
		"slot": "martial weapon",
		"martial": true,
		"style": "slashing melee",
		"player_style": "club",
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(179, 184, 212),
		"flair_color": Color8(0, 0, 0, 0),
		"damage": 4,
		"buy": 6,
		"sell": 5
	},
	"Staff of Sight": {
		"frame": 101,
		"rarity": 2,
		"slot": "magic weapon",
		"magic": true,
		"buy": 7,
		"sell": 6
	},
	"Gilded Staff": {
		"frame": 102,
		"rarity": 2,
		"slot": "magic weapon",
		"magic": true,
		"buy": 11,
		"sell": 10
	},
	"Staff of Purity": {
		"frame": 103,
		"rarity": 2,
		"slot": "magic weapon",
		"magic": true,
		"buy": 7,
		"sell": 6
	},
	"Staff of Wings": {
		"frame": 104,
		"rarity": 3,
		"slot": "magic weapon",
		"magic": true,
		"buy": 14,
		"sell": 12
	},
	"Crescent Shield": {
		"frame": 105,
		"rarity": 2,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 45,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(96, 59, 51),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Kite": {
		"frame": 106,
		"rarity": 2,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 50,
		"light_color": Color8(158, 173, 182),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Heater": {
		"frame": 107,
		"rarity": 2,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 45,
		"light_color": Color8(158, 173, 182),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(131, 126, 134),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"War Door": {
		"frame": 108,
		"rarity": 3,
		"slot": "shield",
		"player_style": "shield",
		"block_chance": 80,
		"light_color": Color8(158, 59, 55),
		"color": Color8(158, 59, 55),
		"dark_color": Color8(158, 59, 55),
		"flair_color": Color8(249, 243, 95),
		"martial": true,
		"buy": 13,
		"sell": 12
	},
	"Burganet": {
		"frame": 109,
		"rarity": 2,
		"slot": "helm",
		"player_style": "helm",
		"armor": 4,
		"light_color": Color8(158, 173, 182),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(14, 14, 16),
		"flair_color": Color8(158, 59, 55),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Salade": {
		"frame": 110,
		"rarity": 2,
		"slot": "helm",
		"player_style": "helm",
		"armor": 5,
		"light_color": Color8(14, 14, 16),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(14, 14, 16),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Horned Greathelm": {
		"frame": 111,
		"rarity": 3,
		"slot": "helm",
		"player_style": "helm",
		"armor": 6,
		"damage_increase": 2,
		"light_color": Color8(249, 243, 95),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(14, 14, 16),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"buy": 16,
		"sell": 14
	},
	"Cabasset": {
		"frame": 112,
		"rarity": 2,
		"slot": "helm",
		"player_style": "hat",
		"armor": 4,
		"hair_style": 2,
		"hair_color": Color8(65, 42, 59),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Leather Pauldron": {
		"frame": 113,
		"rarity": 1,
		"slot": "armor",
		"player_style": "armor",
		"block_chance_increase": 10,
		"critical_chance_increase": 20, 
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(0, 0, 0, 0),
		"dark_color": Color8(135, 88, 64),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 5,
		"sell": 4
	},
	"Plate Pauldron": {
		"frame": 114,
		"rarity": 2,
		"slot": "armor",
		"player_style": "armor",
		"armor": 1,
		"block_chance_increase": 20,
		"critical_chance_increase": 30,
		"light_color": Color8(0, 0, 0, 0),
		"color": Color8(0, 0, 0, 0),
		"dark_color": Color8(179, 184, 212),
		"flair_color": Color8(0, 0, 0, 0),
		"martial": true,
		"buy": 7,
		"sell": 6
	},
	"Old Plate Tunic": {
		"frame": 115,
		"rarity": 2,
		"slot": "armor",
		"player_style": "armor",
		"armor": 5,
		"light_color": Color8(146, 101, 77),
		"color": Color8(179, 184, 212),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(121, 84, 64),
		"martial": true,
		"buy": 6,
		"sell": 5
	},
	"Chain Tunic": {
		"frame": 116,
		"rarity": 0,
		"slot": "armor",
		"player_style": "armor",
		"armor": 1,
		"light_color": Color8(63, 63, 112),
		"color": Color8(94, 110, 218),
		"dark_color": Color8(0, 0, 0, 0),
		"flair_color": Color8(33, 36, 58),
		"martial": true,
		"buy": 1,
		"sell": 0.5
	},
	"Hood": {
		"frame": 117,
		"rarity": 1,
		"slot": "helm",
		"player_style": "hood",
		"magic": true,
		"buy": 1,
		"sell": 1
	},
	"Cleansing Balm": {
		"frame": 118,
		"rarity": 2,
		"consumable": true,
		"buy": 4,
		"sell": 3
	},
	"Skull Helm": {
		"frame": 119,
		"rarity": 2,
		"slot": "helm",
		"player_style": "helm",
		"armor": 2,
		"light_color": Color8(158, 173, 182),
		"color": Color8(158, 173, 182),
		"dark_color": Color8(131, 126, 134),
		"flair_color": Color8(131, 126, 134),
		"martial": true,
		"magic": true,
		"buy": 9,
		"sell": 7
	},
	"Gilded Crown": {
		"frame": 120,
		"rarity": 3,
		"slot": "helm",
		"player_style": "headband",
		"martial": true,
		"buy": 12,
		"sell": 10
	},
	"Charm of Vines": {
		"frame": 121,
		"rarity": 1,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(81, 146, 113),
		"magic": true,
		"buy": 6,
		"sell": 5
	},
	"Charm of Light": {
		"frame": 122,
		"rarity": 1,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(207, 218, 249),
		"magic": true,
		"buy": 6,
		"sell": 5
	},
	"Ring of Life": {
		"frame": 123,
		"rarity": 1,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(169, 227, 103),
		"magic": true,
		"buy": 6,
		"sell": 5
	},
	"Ring of Truesight": {
		"frame": 124,
		"rarity": 3,
		"slot": "ring",
		"player_style": "ring",
		"color": Color8(125, 203, 225),
		"magic": true,
		"buy": 18,
		"sell": 16
	},
	"Plate Bar": {
		"frame": 125,
		"rarity": 1,
		"buy": 2,
		"sell": 1
	},
	"Gild Bar": {
		"frame": 126,
		"rarity": 2,
		"buy": 6,
		"sell": 5
	},
	"Log": {
		"frame": 127,
		"rarity": 1,
		"buy": 1,
		"sell": 1
	},
	"Twigs": {
		"frame": 128,
		"rarity": 1,
		"buy": 0.5,
		"sell": 0.25
	},
	"Wheat": {
		"frame": 129,
		"rarity": 1,
		"buy": 0.5,
		"sell": 0.25
	},
	"Bread": {
		"frame": 130,
		"rarity": 1,
		"life_gain": 2,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Drumstick": {
		"frame": 131,
		"rarity": 1,
		"life_gain": 3,
		"consumable": true,
		"buy": 2,
		"sell": 1
	},
	"Mushroom": {
		"frame": 132,
		"rarity": 1,
		"buy": 2,
		"sell": 1
	},
	"Rock": {
		"frame": 133,
		"rarity": 1,
		"buy": 0.5,
		"sell": 0.25
	},
	"Mud": {
		"frame": 134,
		"rarity": 1,
		"buy": 0.25,
		"sell": 0.125
	},
	"Dye": {
		"frame": 135,
		"rarity": 1,
		"buy": 2,
		"sell": 1
	},
	"Paper": {
		"frame": 136,
		"rarity": 1,
		"buy": 1,
		"sell": 0.5
	},
	"Milk": {
		"frame": 137,
		"rarity": 1,
		"life_gain": 2,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Honey": {
		"frame": 138,
		"rarity": 1,
		"life_gain": 3,
		"consumable": true,
		"buy": 2,
		"sell": 1
	},
	"Grapes": {
		"frame": 139,
		"rarity": 1,
		"life_gain": 1,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Bananas": {
		"frame": 140,
		"rarity": 1,
		"life_gain": 1,
		"consumable": true,
		"buy": 1,
		"sell": 0.5
	},
	"Leaf": {
		"frame": 141,
		"rarity": 1,
		"buy": 0.25,
		"sell": 0.125
	},
	"Pipe Weed": {
		"frame": 142,
		"rarity": 1,
		"buy": 2,
		"sell": 1
	},
	"Feather": {
		"frame": 143,
		"rarity": 1,
		"buy": 0.5,
		"sell": 0.25
	},
	"Pheonix Feather": {
		"frame": 144,
		"rarity": 2,
		"buy": 8,
		"sell": 7
	},
	"Coins": {
		"frame": 145,
		"rarity": 0,
		"buy": 1,
		"sell": 1
	},
	"Armadillo Charm": {
		"frame": 146,
		"rarity": 3,
		"slot": "charm",
		"player_style": "charm",
		"color": Color8(231, 197, 159),
		"flair_color": Color8(187, 128, 81),
		"magic": true,
		"buy": 19,
		"sell": 15
	},
	"Arrow": {
		"frame": 147,
		"rarity": 1,
		"slot": "ammunition",
		"martial": true,
		"buy": 1,
		"sell": 1
	},
	"Bow Shaft": {
		"frame": 148,
		"rarity": 1,
		"buy": 2,
		"sell": 1
	}
}

const SPELL_DATA = {
	"Firebolt": {
		"level": 1,
		"cost": "rrr",
		"icon": 13
	},
	"Swiftness": {
		"level": 1,
		"cost": "sss",
		"icon": 29
	},
	"Revitalize": {
		"level": 1,
		"cost": "lll",
		"icon": 35
	},
	"Drain": {
		"level": 1,
		"cost": "ddd",
		"icon": 11
	},
	"Smite": {
		"level": 1,
		"cost": "fff",
		"icon": 1
	},
	"Plane Step": {
		"level": 1,
		"cost": "RRSSLLDDFFTT",
		"icon": 54
	},
	"World Walk": {
		"level": 2,
		"cost": "RRSSLLDDFFTT",
		"icon": 55
	}
}

var TILE_DATA = [
	# TODO 0 beach
	["desert", "dds", {}, {}],
	# TODO 1 bog
	["swamp", "lll", {}, {}],
	# TODO 2 bog lake
	["swamp", "lls", {}, {}],
	# TODO 3 caldera
	["barren", "fff", {}, {}],
	# TODO 4 city
	["grassland", "lrf", {}, {}],
	# TODO 5 cold deep water
	["deep water", "ddddd", {}, {}],
	# TODO 6 cold water
	["water", "dddd", {}, {}],
	# TODO 7 crater
	["barren", "fff", {}, {}],
	# TODO 8 dead desert
	["barren", "nnn", {}, {}],
	# TODO 9 deep water
	["deep water", "ssss", {}, {}],
	# TODO 10 desert
	["desert", "ddd", {}, {}],
	# TODO 11 desert city
	["desert", "ddf", {}, {}],
	# TODO 12 desert mountain
	["desert", "dddr", {}, {}],
	# TODO 13 desert plateau
	["desert", "dddrr", {}, {}],
	# TODO 14 desert town
	["desert", "ddf", {}, {}],
	# TODO 15 desert village
	["desert", "ddf", {}, {}],
	# TODO 16 erupting caldera
	["barren", "rrrr", {}, {}],
	# TODO 17 erupting mountain
	["barren", "rrrr", {}, {}],
	# TODO 18 erupting volcano
	["barren", "rrrr", {}, {}],
	# TODO 19 flooded plains
	["plains", "lrs", {}, {}],
	# TODO 20 forest
	["grassland", "llr", {}, {}],
	# TODO 21 forest hills
	["grassland", "lrf", {}, {}],
	# TODO 22 frozen deep water
	["deep water", "ssssss", {}, {}],
	# TODO 23 frozen water
	["water", "sssss", {}, {}],
	# TODO 24 glacier
	["deep water", "sssssss", {}, {}],
	# TODO 25 growing meadow
	["grassland", "llr", {}, {"armadillo": 100}],
	# TODO 26 growing savannah
	["savannah", "llrr", {}, {}],
	# 27 hills
	["grassland", "lrf", {"largerock": 50}, {"armadillo": 100}],
	# TODO 28 hilly rocky forest
	["grassland", "llrf", {}, {}],
	# TODO 29 icy deep water
	["deep water", "sssss", {}, {}],
	# TODO 30 icy water
	["water", "ssss", {}, {}],
	# TODO 31 jungle
	["grassland", "lllr", {}, {}],
	# TODO 32 jungle swamp
	["swamp", "llll", {}, {}],
	# TODO 33 lake
	["grassland", "lss", {}, {"armadillo": 100}],
	# TODO 34 lava
	["barren", "fffff", {}, {}],
	# TODO 35 lava caldera
	["barren", "ffffff", {}, {}],
	# TODO 36 lava mountain
	["barren", "ffffff", {}, {}],
	# TODO 37 lava volcano
	["barren", "ffffff", {}, {}],
	# TODO 38 left cold water village
	["water", "sssf", {}, {}],
	# TODO 39 left water village
	["water", "ssf", {}, {}],
	# TODO 40 lightly wooded growing savannah
	["savannah", "llrf", {}, {}],
	# TODO 41 lightly wooded savannah
	["savannah", "lrf", {}, {}],
	# TODO 42 magma
	["barren", "ffff", {}, {}],
	# TODO 43 marsh
	["grassland", "lll", {}, {}],
	# 44 meadow
	["grassland", "llr", {"meadowtree": 100}, {"armadillo": 100}],
	# TODO 45 monument
	["grassland", "llrf", {"meadowtree": 80, "largerock": 20}, {"armadillo": 100}],
	# TODO 46 mountain
	["barren", "fff", {}, {}],
	# TODO 47 overgrown bog
	["swamp", "llll", {}, {}],
	# TODO 48 overgrown forest
	["grassland", "lllr", {}, {}],
	# TODO 49 overgrown savannah
	["savannah", "lllrf", {}, {}],
	# TODO 50 overgrown swamp
	["swamp", "llll", {}, {}],
	# TODO 51 plains
	["plains", "llr", {}, {}],
	# TODO 52 right cold water village
	["water", "sssf", {}, {}],
	# TODO 53 right water village
	["water", "ssf", {}, {}],
	# TODO 54 rocky desert
	["desert", "ddf", {}, {}],
	# TODO 55 rocky forest
	["grassland", "llrf", {}, {}],
	# 56 rocky hills
	["grassland", "lrf", {"meadowtree": 20, "largerock": 80}, {"armadillo": 100}],
	# TODO 57 rocky savannah
	["savannah", "ffr", {}, {}],
	# TODO 58 rocky wooded savannah
	["savannah", "ffllr", {}, {}],
	# TODO 59 rolling bog
	["swamp", "lll", {}, {}],
	# TODO 60 rolling desert
	["desert", "ddd", {}, {}],
	# TODO 61 rolling meadow
	["grassland", "llr", {}, {"armadillo": 100}],
	# TODO 62 rolling savannah
	["savannah", "rrf", {}, {}],
	# TODO 63 running caldera
	["barren", "ffff", {}, {}],
	# TODO 64 running mountain
	["barren", "ffff", {}, {}],
	# TODO 65 running volcano
	["barren", "ffff", {}, {}],
	# TODO 66 savannah
	["savannah", "rrf", {}, {}],
	# TODO 67 shrubby savannah
	["savannah", "lrf", {}, {}],
	# TODO 68 snow
	["grassland", "sss", {}, {}],
	# TODO 69 snowy castle
	["grassland", "ssf", {}, {}],
	# TODO 70 snowy city
	["grassland", "ssf", {}, {}],
	# TODO 71 snowy forest
	["grassland", "ssl", {}, {}],
	# TODO 72 snowy hilly rocky forest
	["grassland", "sfl", {}, {}],
	# TODO 73 snowy meadow
	["grassland", "ssl", {}, {}],
	# TODO 74 snowy monument
	["grassland", "ssf", {}, {}],
	# TODO 75 snowy mountain
	["barren", "sff", {}, {}],
	# TODO 76 snowy rocky hills
	["grassland", "ssf", {}, {}],
	# TODO 77 snowy town
	["grassland", "ssf", {}, {}],
	# TODO 78 snowy village
	["grassland", "ssf", {}, {}],
	# TODO 79 snowy wooded meadow
	["grassland", "ssl", {}, {}],
	# TODO 80 snow covered forest
	["grassland", "ssl", {}, {}],
	# TODO 81 snow covered hills
	["grassland", "ssf", {}, {}],
	# TODO 82 snow covered rocky wooded hills
	["grassland", "sfl", {}, {}],
	# TODO 83 snow covered wooded meadow
	["grassland", "ssl", {}, {}],
	# 84 stony hills
	["grassland", "lff", {"meadowtree": 20, "largerock": 80}, {"armadillo": 100}],
	# TODO 85 swamp
	["swamp", "lll", {}, {}],
	# TODO 86 town
	["grassland", "lrf", {}, {}],
	# 87 village
	["grassland", "lrf", {"tavern": 10, "chest": 5, "lantern": 15, "lightpost": 10, "marketstall": 10, "boxes": 10, "backgroundshorthouse": 15, "backgroundtallhouse": 15, "meadowtree": 10}, {"armadillo": 100}],
	# TODO 88 water
	["water", "sss", {}, {}],
	# TODO 89 wetland
	["grassland", "slr", {}, {"armadillo": 100}],
	# TODO 90 wet bog
	["swamp", "sll", {}, {}],
	# TODO 91 wooded bog
	["swamp", "llll", {}, {}],
	# TODO 92 wooded growing savannah
	["savannah", "llfr", {}, {}],
	# TODO 93 wooded hills
	["grassland", "llf", {}, {}],
	# TODO 94 wooded meadow
	["grassland", "llr", {}, {}],
	# TODO 95 wooded savannah
	["savannah", "llrf", {}, {}]
]

var CHEST_LOOT_TABLE = []
func _ready():
	for item in ITEM_DATA:
		if "slot" in ITEM_DATA[item]:
			match ITEM_DATA[item]["slot"]:
				"martial weapon":
					if ITEM_DATA[item]["style"] != "shooting ranged":
						for i in 1 + 2*(3-ITEM_DATA[item]["rarity"]):
							CHEST_LOOT_TABLE.append(item)
				"helm":
					continue
				"armor":
					continue
				"boots":
					continue
				"shield":
					continue
				"gauntlets":
					if "martial" in ITEM_DATA[item] and not ("magic" in ITEM_DATA[item]):
						for i in 2 + 4*(3-ITEM_DATA[item]["rarity"]):
							CHEST_LOOT_TABLE.append(item)
