extends Node2D

var inv_len = 0
var num_pages = 0
var page = 0
const PAGE_LEN = 6

func _ready():
	$MartialWeapon/Placeholder.frame = 1
	$MagicWeapon/Placeholder.frame = 2
	$Helm/Placeholder.frame = 3
	$Charm/Placeholder.frame = 4
	$Armor/Placeholder.frame = 5
	$Ring/Placeholder.frame = 6
	$Boots/Placeholder.frame = 7
	$Gauntlets/Placeholder.frame = 8
	$Shield/Placeholder.frame = 9
	$Item/Placeholder.frame = 11
	$Ammunition/Placeholder.frame = 12
	
	
func _process(_delta):
	$MartialWeapon.item = Base.player.inventory["martial weapon"]["name"] if Base.player.inventory["martial weapon"] != null else null
	$MagicWeapon.item = Base.player.inventory["magic weapon"]["name"] if Base.player.inventory["magic weapon"] != null else null
	$Helm.item = Base.player.inventory["helm"]["name"] if Base.player.inventory["helm"] != null else null
	$Charm.item = Base.player.inventory["charm"]["name"] if Base.player.inventory["charm"] != null else null
	$Armor.item = Base.player.inventory["armor"]["name"] if Base.player.inventory["armor"] != null else null
	$Ring.item = Base.player.inventory["ring"]["name"] if Base.player.inventory["ring"] != null else null
	$Boots.item = Base.player.inventory["boots"]["name"] if Base.player.inventory["boots"] != null else null
	$Gauntlets.item = Base.player.inventory["gauntlets"]["name"] if Base.player.inventory["gauntlets"] != null else null
	$Shield.item = Base.player.inventory["shield"]["name"] if Base.player.inventory["shield"] != null else null
	$Item.item = Base.player.inventory["item"]["name"] if Base.player.inventory["item"] != null else null
	$Ammunition.item = Base.player.inventory["ammunition"]["name"] if Base.player.inventory["ammunition"] != null else null
	$Coins.item = Base.player.inventory["coins"]["name"] if Base.player.inventory["coins"] != null else null
	$Inventory.text = str(len(Base.player.inventory["inventory"]))
	
	if Input.is_action_just_pressed("open_inventory"):
		if $InventoryMenu/Backpack.target == 0 and not Base.popup_active:
			Base.popup_active = true
			$InventoryMenu/Backpack.target = $InventoryMenu/Backpack.DEFAULTFRAME
		else:
			if $InventoryMenu/Backpack.target == $InventoryMenu/Backpack.DEFAULTFRAME:
				Base.popup_active = false
			$InventoryMenu/Backpack.target = 0
	
	if $InventoryMenu/Backpack/Contents.visible:
		inv_len = len(Base.player.inventory["inventory"])
		num_pages = inv_len / PAGE_LEN
			
		for item in $InventoryMenu/Backpack/Contents.get_children():
			if not item is Label:
				var index = int(item.get_name().substr(1)) + PAGE_LEN*page
				item.item = null if index >= inv_len else Base.player.inventory["inventory"][index]["name"]
				item.visible = item.item != null
		
		$InventoryMenu/Backpack.canFlipUp = page > 0
		$InventoryMenu/Backpack.canFlipDown = page + 1 < num_pages


func _on_Backpack_up_arrow_pressed():
	page -= 1


func _on_Backpack_down_arrow_pressed():
	page += 1


func _on_I0_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page)


func _on_I1_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page + 1)


func _on_I2_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page + 2)


func _on_I3_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page + 3)


func _on_I4_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page + 4)


func _on_I5_pressed():
	Base.player.inventory_clicked(PAGE_LEN*page + 5)


func _on_MartialWeapon_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("martial weapon")


func _on_MagicWeapon_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("magic weapon")


func _on_Helm_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("helm")


func _on_Charm_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("charm")


func _on_Armor_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("armor")


func _on_Ring_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("ring")


func _on_Boots_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("boots")


func _on_Gauntlets_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("gauntlets")


func _on_Shield_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("shield")


func _on_Item_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("item")


func _on_Ammunition_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("ammunition")


func _on_Coins_pressed():
	if $InventoryMenu/Backpack/Contents.visible:
		Base.player.inventory_slot_clicked("coins")
