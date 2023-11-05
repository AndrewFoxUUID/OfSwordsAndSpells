extends Node2D

signal items_purchased
signal items_sold

var seller_inv = []
var left_start = 0
var right_start = 0

func _ready():
	$MenuBook.target = 3
	
	
func _process(_delta):
	for i in 4:
		$MenuBook/LeftPage.get_node("Item" + str(i+1)).item = seller_inv[left_start+i]["name"] if len(seller_inv) > left_start+i else null
		$MenuBook/LeftPage.get_node("Item" + str(i+1)).override_quantity = seller_inv[left_start+i]["quantity"] if len(seller_inv) > left_start+i else 0
		
		$MenuBook/RightPage.get_node("Item" + str(i+1)).item = Base.player.inventory["inventory"][right_start+i]["name"] if len(Base.player.inventory["inventory"]) > right_start+i else null
		$MenuBook/RightPage.get_node("Item" + str(i+1)).override_quantity = null
		
	$MenuBook/LeftPage/LeftArrow.visible = left_start > 0
	$MenuBook/LeftPage/RightArrow.visible = left_start + 3 < len(seller_inv) - 1
	$MenuBook/LeftPage/MinusButton.visible = $MenuBook/LeftPage/BuySlot.item != null
	$MenuBook/LeftPage/PlusButton.visible = $MenuBook/LeftPage/BuySlot.item != null
	
	$MenuBook/RightPage/LeftArrow.visible = right_start > 0
	$MenuBook/RightPage/RightArrow.visible = right_start + 3 < len(Base.player.inventory["inventory"]) - 1
	$MenuBook/RightPage/MinusButton.visible = $MenuBook/RightPage/SellSlot.item != null
	$MenuBook/RightPage/PlusButton.visible = $MenuBook/RightPage/SellSlot.item != null
	
	$MenuBook/LeftPage/Button.text = "Buy for " + (str(int(Constants.ITEM_DATA[$MenuBook/LeftPage/BuySlot.item]["buy"] * int($MenuBook/LeftPage/BuySlot/Quantity.text))) if $MenuBook/LeftPage/BuySlot.item != null else "0") + " Coins"
	$MenuBook/RightPage/Button.text = "Sell for " + (str(int(Constants.ITEM_DATA[$MenuBook/RightPage/SellSlot.item]["sell"] * int($MenuBook/RightPage/SellSlot/Quantity.text))) if $MenuBook/RightPage/SellSlot.item != null else "0") + " Coins"


func _on_LeftPage_LeftArrow_pressed():
	left_start -= 4
	if left_start < 0:
		left_start = 0


func _on_LeftPage_RightArrow_pressed():
	if len(seller_inv) > left_start + 4:
		left_start += 4


func _on_RightPage_LeftArrow_pressed():
	right_start -= 4
	if right_start < 0:
		right_start = 0


func _on_RightPage_RightArrow_pressed():
	if len(Base.player.inventory["inventory"]) > right_start + 4:
		right_start += 4


func _on_LeftPage_Item_pressed(i):
	$MenuBook/LeftPage/BuySlot.item = seller_inv[left_start+i]["name"]
	$MenuBook/LeftPage/BuySlot.override_quantity = 1


func _on_LeftPage_PlusButton_pressed():
	if $MenuBook/LeftPage/BuySlot.override_quantity < Base.player.get_num($MenuBook/LeftPage/BuySlot.item):
		$MenuBook/LeftPage/BuySlot.override_quantity += 1


func _on_LeftPage_MinusButton_pressed():
	if $MenuBook/LeftPage/BuySlot.override_quantity >= 1:
		$MenuBook/LeftPage/BuySlot.override_quantity -= 1


func _on_RightPage_PlusButton_pressed():
	if $MenuBook/RightPage/SellSlot.override_quantity < Base.player.get_num($MenuBook/RightPage/SellSlot.item):
		$MenuBook/RightPage/SellSlot.override_quantity += 1


func _on_RightPage_MinusButton_pressed():
	if $MenuBook/RightPage/SellSlot.override_quantity >= 1:
		$MenuBook/RightPage/SellSlot.override_quantity -= 1


func _on_BuySlot_pressed():
	$MenuBook/LeftPage/BuySlot.item = null


func _on_SellSlot_pressed():
	$MenuBook/RightPage/SellSlot.item = null


func _on_RightPage_Item_pressed(i):
	$MenuBook/RightPage/SellSlot.item = Base.player.inventory["inventory"][right_start+i]["name"]
	$MenuBook/RightPage/SellSlot.override_quantity = 1


func _on_LeftPage_Button_pressed():
	if $MenuBook/LeftPage/BuySlot.item != null and $MenuBook/LeftPage/BuySlot/Quantity.text != "0":
		emit_signal("items_purchased", $MenuBook/LeftPage/BuySlot.item, int($MenuBook/LeftPage/BuySlot/Quantity.text))
		$MenuBook/LeftPage/BuySlot.item = null


func _on_RightPage_Button_pressed():
	if $MenuBook/RightPage/SellSlot.item != null and $MenuBook/RightPage/SellSlot/Quantity.text != "0":
		emit_signal("items_sold", $MenuBook/RightPage/SellSlot.item, int($MenuBook/RightPage/SellSlot/Quantity.text))
		$MenuBook/RightPage/SellSlot.item = null


func _unhandled_key_input(event):
	if event.is_pressed():
		queue_free()


func _on_ShopMenu_tree_exited():
	Base.popup_active = false
