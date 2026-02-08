from pyke import DataDragon

# Let's create a DataDragon instance, we can pass a version if we want
# But by default the latest version will be used
# If you wish to pass a version use the following format:
# "15.21.1" (or "lolpatch_7.20" for older versions)
ddragon = DataDragon()

# print(ddragon.champion.get_all("en_GB"))
# print(ddragon.champion_full.get_all("en_GB"))
# print(ddragon.challenges.get_all("en_GB"))
print(ddragon.itemmodifiers.get_all("en_GB"))
