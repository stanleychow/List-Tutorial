songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[-1])
print(songs[1:])
songs[-1] = "Sanctuary"
songs.extend(["Excursions", "Only Child", "RENTAL"])
songs.pop(-1)

animals=["Fox", "Lion", "Cheetah"]
animals.append("Dolpin")
print(animals[2])
animals.pop(0)
for animal in animals:
    print animal