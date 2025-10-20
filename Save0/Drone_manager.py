
import Drone_hay
import Drone_tree
import Drone_carrot
import Drone_sunflower
import Drone_strangestuff
import Drone_gold2
import Drone_pumpkin
import Drone_cactus




itemstogather = {	Items.Power 			: 250000,
					Items.Hay				: 1000000000,
					Items.Wood				: 10000000000,
					Items.Carrot			: 1000000000,
					Items.Weird_Substance	: 1000000,
					Items.Gold				: 100000000,
					Items.Pumpkin			: 1000000,
					Items.Cactus 			: 1000000000
				}

clear()
change_hat(Hats.Top_Hat)
while 1:
	
	if num_items( Items.Power ) < itemstogather[Items.Power]:
		Drone_sunflower.runthis()
		continue
	
	if num_items( Items.Hay ) < itemstogather[Items.Hay]:
		Drone_hay.runthis()
		continue
	
	if num_items( Items.Wood ) < itemstogather[Items.Wood]:
		Drone_tree.runthis()
		continue
	
	if num_items( Items.Carrot ) < itemstogather[Items.Carrot]:
		Drone_carrot.runthis()
		continue
	
	if num_items( Items.Weird_Substance ) < itemstogather[Items.Weird_Substance]:
		Drone_strangestuff.runthis()
		continue
			
	if num_items( Items.Gold ) < itemstogather[Items.Gold]:
		Drone_gold2.runthis()
		continue

	if num_items( Items.Pumpkin ) < itemstogather[Items.Pumpkin]:
		Drone_pumpkin.runthis()
		continue
				
	if num_items( Items.Cactus ) < itemstogather[Items.Cactus]:
		Drone_cactus.runthis()
		continue
	
	for singleitem in itemstogather:
		itemstogather[singleitem] += 100000
		