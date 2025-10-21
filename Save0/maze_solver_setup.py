
unlocks = {
	Unlocks.Speed:3,
	Unlocks.Expand:4,
	Unlocks.Plant:1,
	Unlocks.Carrots:1,
	Unlocks.Trees:1,
	Unlocks.Pumpkins:1,
	Unlocks.Cactus:1,
	Unlocks.Dinosaurs:1,
	Unlocks.Fertilizer:4,
	Unlocks.Watering:3,
	Unlocks.Mazes:1

}

# Speed x3
# Expand x4
# Plant
# Carrots
# Trees
# Pumpkin
# Cactus
# Dinosaurs
# Fertilizer x4
# Mazes


items = {}
globals = {}
#a negative seed value means a random seed
seed = -1
speedup = 1
simulate("maze_solver", unlocks, items, globals, seed, speedup)


