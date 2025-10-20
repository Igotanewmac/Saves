

# unlock speed 1
while num_items(Items.Hay) < 20:
	if can_harvest():
		harvest()
unlock(Unlocks.Speed)

#unlock expand 1
while num_items(Items.Hay) < 30:
	if can_harvest():
		harvest()
unlock(Unlocks.Expand)

# unlock planting and bushes
while num_items(Items.Hay) < 50:
	if can_harvest():
		harvest()
unlock(Unlocks.Plant)


#unlock speed 2
while num_items(Items.Wood) < 20:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Speed)

#unlock expand 2
while num_items(Items.Wood) < 20:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Expand)


#unlock carrots
while num_items(Items.Wood) < 50:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Carrots)

#unlock speed 3
# 50 carrots , 50 wood
# make ingredients first
while num_items(Items.Hay) < 50:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Wood) < 100:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 50:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Speed)


# unlock Expand
# 20 carrots , 30 wood
# make ingredients first
while num_items(Items.Hay) < 20:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Wood) < 50:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 20:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Expand)




# unlock Trees
# 70 carrots , 50 wood
# make ingredients first
while num_items(Items.Hay) < 70:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Wood) < 120:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 70:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Trees)

# unlock expand
# 100 wood, 50 carrots
while num_items(Items.Hay) < 50:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Wood) < 150:
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if can_harvest():
		harvest()
		plant(Entities.Bush)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 50:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Expand)


# pumpkins
# 500 wood , 200 carrots
while num_items(Items.Wood) < 700:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
while num_items(Items.Hay) < 200:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 200:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
unlock(Unlocks.Pumpkins)

			
# unlock cactus
# 5k pumpkins
# pumpkins cost 1 carrot each
while num_items(Items.Wood) < 5000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
while num_items(Items.Hay) < 5000:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 5000:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Pumpkin) < 5000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			move(North)
		move(East)
unlock(Unlocks.Cactus)

# unlock Dinosaurs
# 2k cactus
# 2 pumpkins per cactus
while num_items(Items.Wood) < 4000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
		move(East)
while num_items(Items.Hay) < 4000:
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()
		plant(Entities.Grass)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Carrot) < 4000:
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()
		plant(Entities.Carrot)
	if get_pos_y() == get_world_size() -1:
		move(East)
	move(North)
while num_items(Items.Pumpkin) < 4000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
			move(North)
		move(East)
while num_items(Items.Cactus) < 2000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_entity_type() != Entities.Cactus:
				plant(Entities.Cactus)
			move(North)
		move(East)
unlock(Unlocks.Dinosaurs)



directions = [
	[1,4,4,4,4,4],
	[1,2,1,2,1,3],
	[1,3,1,3,1,3],
	[1,3,1,3,1,3],
	[1,3,1,3,1,3],
	[2,3,2,3,2,3]
	]

compass = { 1:North , 2:East , 3:South , 4:West }


while num_items(Items.Bone) < 2000000:

	# 64 cacti per apple
	while num_items(Items.Wood) < 5000:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
					plant(Entities.Tree)
				else:
					plant(Entities.Bush)
				move(North)
			move(East)
	while num_items(Items.Hay) < 5000:
		if get_entity_type() != Entities.Grass:
			plant(Entities.Grass)
		if can_harvest():
			harvest()
			plant(Entities.Grass)
		if get_pos_y() == get_world_size() -1:
			move(East)
		move(North)
	while num_items(Items.Carrot) < 5000:
		if get_ground_type() != Grounds.Soil:
			till()
		if get_entity_type() != Entities.Carrot:
			plant(Entities.Carrot)
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
		if get_pos_y() == get_world_size() -1:
			move(East)
		move(North)
	while num_items(Items.Pumpkin) < 5000:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)
				move(North)
			move(East)
	while num_items(Items.Cactus) < 2500:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_entity_type() != Entities.Cactus:
					plant(Entities.Cactus)
				move(North)
			move(East)



# 2M bones for leaderboard unlock
	while num_items(Items.Cactus) > 2400:
		clear()
		change_hat(Hats.Dinosaur_Hat)
		hasmoved = True
		while hasmoved == True:
			hasmoved = move( compass[ directions[get_pos_y()][get_pos_x()] ] )
		change_hat(Hats.Straw_Hat)


unlock(Unlocks.Fertilizer)
unlock(Unlocks.Fertilizer)

while num_items(Items.Wood) < 63000:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if can_harvest():
				harvest()
			if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
				plant(Entities.Tree)
				if num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			else:
				plant(Entities.Bush)
				if num_items(Items.Fertilizer) > 0:
					use_item(Items.Fertilizer)
			move(North)
		move(East)
unlock(Unlocks.Fertilizer)
unlock(Unlocks.Fertilizer)
unlock(Unlocks.Mazes)


def weirstuffroutine():
	while num_items(Items.Weird_Substance) < 1000:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
					plant(Entities.Tree)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				else:
					plant(Entities.Bush)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				move(North)
			move(East)



def plantroutine():
	for _ in range( get_world_size() ):
		if get_water() < 0.25:
			use_item(Items.Water)
		plant(Entities.Bush)
		move(North)
	for _ in range( get_world_size() ):
		while not can_harvest():
			pass
		use_item( Items.Weird_Substance , (2**(num_unlocked(Unlocks.Mazes) -1)) )
		harvest()
		move(North)


while num_items(Items.Gold) < 1000000:
	if num_items(Items.Weird_Substance) < 10:
		weirstuffroutine()
	plantroutine()

unlock(Unlocks.Leaderboard)


print("AFR End")
#while 1:
#	pass
	 