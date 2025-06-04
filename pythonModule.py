# Minecraft Education Code Project
# Jody Ingram

from mcpi.minecraft import Minecraft  # Correct library for Minecraft Education
mc = Minecraft.create()

# Get the player's current position
x, y, z = mc.player.getTilePos()

# Place a diamond block in front of the player
mc.setBlock(x + 1, y, z, 57)  # "57" represents a diamond block in Minecraft

# Summon a bunch of chickens
chickens = 50
for count in range(chickens):
    mc.spawnEntity(x + 1, y, z, "CHICKEN")  # Spawns a chicken
    mc.postToChat(f"Summoned chicken {count + 1}")  # Sends a chat message
