extends Node2D

onready var CREATE_PLAYER_FRAMES = preload("res://assets/NewPlayer.tres")

func _ready():
	pass
	
	
func set_player(player, hide_equipment=false):
	if player == null:
		$Player.frames = null
		$Hair1.frames = null
		$Hair2.frames = null
		$Hair3.frames = null
		$Hair4.frames = null
		$Shield.frames = null
		$Armor.frames = null
		$Charm.frames = null
		$Helm.frames = null
		$Boots.frames = null
		$Gauntlets.frames = null
		$Ring.frames = null
		$Sword.frames = null
		$Spear.frames = null
		$Axe.frames = null
		$Dagger.frames = null
		$Club.frames = null
	elif player is String and player == "Create Player":
		$Player.frames = CREATE_PLAYER_FRAMES
		$Player.play("default")
		$Player.play("Idle")
		
		$Hair1.frames = null
		$Hair2.frames = null
		$Hair3.frames = null
		$Hair4.frames = null
		$Shield.frames = null
		$Armor.frames = null
		$Charm.frames = null
		$Helm.frames = null
		$Boots.frames = null
		$Gauntlets.frames = null
		$Ring.frames = null
		$Sword.frames = null
		$Spear.frames = null
		$Axe.frames = null
		$Dagger.frames = null
		$Club.frames = null
		
		$Player.material.set("shader_param/dark_eye", Color8(0, 0, 0))
	else:
		$Player.frames = player.get_node("SpriteLayers").get_node("Player").frames
		$Player.visible = player.get_node("SpriteLayers").get_node("Player").visible
		$Player.play("default")
		$Player.play("Idle")
		
		$Hair1.frames = player.get_node("SpriteLayers").get_node("Hair1").frames
		$Hair1.visible = player.get_node("SpriteLayers").get_node("Hair1").visible
		$Hair1.play("default")
		$Hair1.play("Idle")
		
		$Hair2.frames = player.get_node("SpriteLayers").get_node("Hair2").frames
		$Hair2.visible = player.get_node("SpriteLayers").get_node("Hair2").visible
		$Hair2.play("default")
		$Hair2.play("Idle")
		
		$Hair3.frames = player.get_node("SpriteLayers").get_node("Hair3").frames
		$Hair3.visible = player.get_node("SpriteLayers").get_node("Hair3").visible
		$Hair3.play("default")
		$Hair3.play("Idle")
		
		$Hair4.frames = player.get_node("SpriteLayers").get_node("Hair4").frames
		$Hair4.visible = player.get_node("SpriteLayers").get_node("Hair4").visible
		$Hair4.play("default")
		$Hair4.play("Idle")
		
		$Shield.frames = player.get_node("SpriteLayers").get_node("Shield").frames
		$Shield.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Shield").visible
		$Shield.play("default")
		$Shield.play("Idle")
		
		$Armor.frames = player.get_node("SpriteLayers").get_node("Armor").frames
		$Armor.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Armor").visible
		$Armor.play("default")
		$Armor.play("Idle")
		
		$Charm.frames = player.get_node("SpriteLayers").get_node("Charm").frames
		$Charm.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Charm").visible
		$Charm.play("default")
		$Charm.play("Idle")
		
		$Helm.frames = player.get_node("SpriteLayers").get_node("Helm").frames
		$Helm.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Helm").visible
		$Helm.play("default")
		$Helm.play("Idle")
		
		$Boots.frames = player.get_node("SpriteLayers").get_node("Boots").frames
		$Boots.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Boots").visible
		$Boots.play("default")
		$Boots.play("Idle")
		
		$Gauntlets.frames = player.get_node("SpriteLayers").get_node("Gauntlets").frames
		$Gauntlets.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Gauntlets").visible
		$Gauntlets.play("default")
		$Gauntlets.play("Idle")
		
		$Ring.frames = player.get_node("SpriteLayers").get_node("Ring").frames
		$Ring.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Ring").visible
		$Ring.play("default")
		$Ring.play("Idle")
		
		$Sword.frames = player.get_node("SpriteLayers").get_node("Sword").frames
		$Sword.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Sword").visible
		$Sword.play("default")
		$Sword.play("Idle")
		
		$Spear.frames = player.get_node("SpriteLayers").get_node("Spear").frames
		$Spear.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Spear").visible
		$Spear.play("default")
		$Spear.play("Idle")
		
		$Axe.frames = player.get_node("SpriteLayers").get_node("Axe").frames
		$Axe.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Axe").visible
		$Axe.play("default")
		$Axe.play("Idle")
		
		$Dagger.frames = player.get_node("SpriteLayers").get_node("Dagger").frames
		$Dagger.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Dagger").visible
		$Dagger.play("default")
		$Dagger.play("Idle")
		
		$Club.frames = player.get_node("SpriteLayers").get_node("Club").frames
		$Club.visible = false if hide_equipment else player.get_node("SpriteLayers").get_node("Club").visible
		$Club.play("default")
		$Club.play("Idle")
		
		$Player.material.set("shader_param/eye", player.colors["eye"])
		$Player.material.set("shader_param/dark_eye", player.colors["dark_eye"])
		$Player.material.set("shader_param/skin", player.colors["skin"])
		$Player.material.set("shader_param/dark_skin", player.colors["dark_skin"])
		$Player.material.set("shader_param/shirt", player.colors["shirt"])
		$Player.material.set("shader_param/pants", player.colors["pants"])
		$Player.material.set("shader_param/dark_pants", player.colors["dark_pants"])
		$Player.material.set("shader_param/shoe", player.colors["shoe"])
		$Player.material.set("shader_param/dark_shoe", player.colors["dark_shoe"])
		
		$Hair1.material.set("shader_param/hair", player.colors["hair"])
		$Hair2.material.set("shader_param/hair", player.colors["hair"])
		$Hair3.material.set("shader_param/hair", player.colors["hair"])
		$Hair4.material.set("shader_param/hair", player.colors["hair"])
		
		$Shield.material.set("shader_param/light_shield", player.colors["light_shield"])
		$Shield.material.set("shader_param/shield", player.colors["shield"])
		$Shield.material.set("shader_param/dark_shield", player.colors["dark_shield"])
		$Shield.material.set("shader_param/shield_flair", player.colors["shield_flair"])
		
		$Armor.material.set("shader_param/light_armor", player.colors["light_armor"])
		$Armor.material.set("shader_param/armor", player.colors["armor"])
		$Armor.material.set("shader_param/dark_armor", player.colors["dark_armor"])
		$Armor.material.set("shader_param/armor_flair", player.colors["armor_flair"])
		
		$Charm.material.set("shader_param/charm", player.colors["charm"])
		$Charm.material.set("shader_param/charm_flair", player.colors["charm_flair"])
		
		$Helm.material.set("shader_param/light_helm", player.colors["light_helm"])
		$Helm.material.set("shader_param/helm", player.colors["helm"])
		$Helm.material.set("shader_param/dark_helm", player.colors["dark_helm"])
		$Helm.material.set("shader_param/helm_flair", player.colors["helm_flair"])
		
		$Boots.material.set("shader_param/light_boot", player.colors["light_boot"])
		$Boots.material.set("shader_param/boot", player.colors["boot"])
		$Boots.material.set("shader_param/dark_boot", player.colors["dark_boot"])
		$Boots.material.set("shader_param/boot_flair", player.colors["boot_flair"])
		
		$Gauntlets.material.set("shader_param/light_gauntlet", player.colors["light_gauntlet"])
		$Gauntlets.material.set("shader_param/gauntlet", player.colors["gauntlet"])
		$Gauntlets.material.set("shader_param/dark_gauntlet", player.colors["dark_gauntlet"])
		$Gauntlets.material.set("shader_param/gauntlet_flair", player.colors["gauntlet_flair"])
		
		$Ring.material.set("shader_param/ring", player.colors["ring"])
		
		$Sword.material.set("shader_param/weapon_follow", player.colors["weapon_follow"])
		$Sword.material.set("shader_param/dark_weapon_follow", player.colors["dark_weapon_follow"])
		$Sword.material.set("shader_param/light_weapon", player.colors["light_weapon"])
		$Sword.material.set("shader_param/weapon", player.colors["weapon"])
		$Sword.material.set("shader_param/dark_weapon", player.colors["dark_weapon"])
		$Sword.material.set("shader_param/weapon_flair", player.colors["weapon_flair"])
		
		$Spear.material.set("shader_param/weapon_follow", player.colors["weapon_follow"])
		$Spear.material.set("shader_param/dark_weapon_follow", player.colors["dark_weapon_follow"])
		$Spear.material.set("shader_param/light_weapon", player.colors["light_weapon"])
		$Spear.material.set("shader_param/weapon", player.colors["weapon"])
		$Spear.material.set("shader_param/dark_weapon", player.colors["dark_weapon"])
		$Spear.material.set("shader_param/weapon_flair", player.colors["weapon_flair"])
		
		$Axe.material.set("shader_param/weapon_follow", player.colors["weapon_follow"])
		$Axe.material.set("shader_param/dark_weapon_follow", player.colors["dark_weapon_follow"])
		$Axe.material.set("shader_param/light_weapon", player.colors["light_weapon"])
		$Axe.material.set("shader_param/weapon", player.colors["weapon"])
		$Axe.material.set("shader_param/dark_weapon", player.colors["dark_weapon"])
		$Axe.material.set("shader_param/weapon_flair", player.colors["weapon_flair"])
		
		$Dagger.material.set("shader_param/weapon_follow", player.colors["weapon_follow"])
		$Dagger.material.set("shader_param/dark_weapon_follow", player.colors["dark_weapon_follow"])
		$Dagger.material.set("shader_param/light_weapon", player.colors["light_weapon"])
		$Dagger.material.set("shader_param/weapon", player.colors["weapon"])
		$Dagger.material.set("shader_param/dark_weapon", player.colors["dark_weapon"])
		$Dagger.material.set("shader_param/weapon_flair", player.colors["weapon_flair"])
		
		$Club.material.set("shader_param/weapon_follow", player.colors["weapon_follow"])
		$Club.material.set("shader_param/dark_weapon_follow", player.colors["dark_weapon_follow"])
		$Club.material.set("shader_param/light_weapon", player.colors["light_weapon"])
		$Club.material.set("shader_param/weapon", player.colors["weapon"])
		$Club.material.set("shader_param/dark_weapon", player.colors["dark_weapon"])
		$Club.material.set("shader_param/weapon_flair", player.colors["weapon_flair"])
