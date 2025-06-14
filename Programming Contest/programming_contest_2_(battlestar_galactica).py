# PROGRAMMING CONTEST 2 - CSE110

# -------------------- App 1: Set Operations --------------------
select = int(input("Set Operation (1=Union, 2=Intersection, 3=Complement, 4=Difference, 5=Cross Product): "))
x = []
if select == 3:
    A = input("A: ").strip("[] ").split(", ")
    U = input("Universal Set, U: ").strip("[] ").split(", ")
    if any(i not in U for i in A):
        print("Error: First Set Containing Elements that are not a Part of the Universal Set.")
    else:
        for i in U:
            if i not in A:
                x.append(i)
        print("A’ :", x)
else:
    user1 = input("A: ").strip("[] ").split(", ")
    user2 = input("B: ").strip("[] ").split(", ")
    if user1 == ['']:
        user1 = []
    if user2 == ['']:
        user2 = []
    if select == 1:
        user = user1 + user2
        for i in user:
            if i not in x:
                x.append(i)
        x.sort()
        print("A U B:", x)
    elif select == 2:
        for i in user1:
            if i in user2 and i not in x:
                x.append(i)
        x.sort()
        print("A ∩ B:", x)
    elif select == 4:
        for i in user1:
            if i not in user2:
                x.append(i)
        x.sort()
        print("A – B:", x)
    elif select == 5:
        if not user2:
            for i in user1:
                x.append([i, None])
        else:
            for i in user1:
                for j in user2:
                    x.append([i, j])
        print("A X B:", x)

# -------------------- App 2: Minecraft Crafting Table --------------------
craft = {
    "redstone torch": {"torch": 1, "redstone": 1},
    "iron sword": {"iron ingot": 2, "stick": 1},
    "torch": {"stick": 1, "coal": 1},
    "stick": {"planks": 1},
    "boat": {"planks": 5},
    "planks": {"oak log": 1},
    "bed": {"wool": 3, "planks": 3},
    "beacon": {"nether star": 1, "glass": 5, "obsidian": 3},
    "furnace": {"cobblestone": 8},
    "blast furnace": {"furnace": 1, "iron ingot": 5, "smooth stone": 3}
}

from collections import defaultdict

def get_recipe(item, result):
    if item not in craft:
        result[item] += 1
    else:
        for i in craft[item]:
            for _ in range(craft[item][i]):
                get_recipe(i, result)

item = input().lower()
if item in craft:
    final = defaultdict(int)
    get_recipe(item, final)
    print(dict(final))
else:
    print("Recipe not found")

# -------------------- App 3: Attack on Titan --------------------
titan_eaters = {
    "Eren Yeager": ["Grisha Yeager", "Lara Tybur"],
    "Grisha Yeager": ["Eren Kruger", "Frieda Reiss"],
    "Porco": ["Marcel"],
    "Marcel": ["Ymir"],
    "Falco": ["Porco"],
    "Armin": ["Pieck"],
    "Levi Ackerman": ["Zeke Yeager"],
    "Mikasa Ackerman": ["Levi", "Annie"],
    "Commander Erwin": ["Berethold"]
}
original_titans = {
    "Founder": "Frieda Reiss", "Attack": "Eren Kruger", "Armored": "Reiner",
    "Colossal": "Berethold", "Female": "Annie", "Jaw": "Ymir", "Cart": "Pieck",
    "Warhammer": "Lara Tybur", "Beast": "Zeke Yeager"
}

final_output = {"Reiner": ["Armored"]}
rev_dict = {v: k for k, v in original_titans.items()}

def find_titan_power(person):
    result = []
    stack = [person]
    while stack:
        current = stack.pop()
        if current in titan_eaters:
            stack += titan_eaters[current]
        elif current in rev_dict:
            result.append(rev_dict[current])
    return result

for i in titan_eaters:
    final_output[i] = find_titan_power(i)

print(final_output)

# -------------------- App 4: Dark Bootstrap Paradox --------------------
events = ("Michael gets lost in the woods. Ulrich goes to find Michael. Both travel to the past but not in the same timeline. "
          "Ulrich gets put into the prison. Michael is Jonas's father. Michael committed suicide by hanging himself. Jonas travels back in time to save his father. "
          "He finds his dad and tells him about his death. His dad now understood what he had to do. Michael committed suicide by hanging himself. "
          "The entire family of Tannahaus was killed in a car accident. This drove him crazy. Tannahaus built a time machine. He also wrote a book on time travel. "
          "Claudia finds the book on time travel. Future Claudia gave the present Claudia and time machine. The present Claudia travels back in time and gave the time travelling book to Tannahaus. "
          "Tannahaus took ideas from the book he was supposed to write in future. Tannahaus built a time machine. A cult like faction keeps on abducting kids from Winden and experiments on them. "
          "None of the abducted kids are ever found again. Charlotte gave birth to Elizabeth. The apocalypse takes place and Charlotte dies. However, Elizabeth somehow survives and gets sent to the past. "
          "Elizabeth meets a guy and they have a daughter named Charlotte. After growing up Charlotte gets married. Charlotte gave birth to Elizabeth. Thus the cycle continues. "
          "After the apocalypse, only a handful of people survived. Elizabeth was one of them. She became the leader of a savage group. Jonas and Martha love each other. "
          "Martha is killed by Adam. Adam is from the future. Jonas travels through time to stop Adam, only to find out that he is the one who eventually becomes Adam. "
          "Adam is the only one capable of breaking the endless cycle. For Jonas to become Adam, it is necessary for Martha to die. Without her dying, Jonas would not become Adam and the cycle would never be broken. "
          "So, Adam goes back in time. Martha is killed by Adam. After Martha's death Jonas travels into another world.")

list_of_events = events.split(". ")
paradox_origin = []
loop = {}
event = ""
paradox = 0
for i in list_of_events:
    if list_of_events.count(i) == 2 and i not in paradox_origin:
        paradox_origin.append(i)
        index = list_of_events.index(i)
        event += i + ". "
        for j in list_of_events[index+1:]:
            if j != i:
                event += j + ". "
            else:
                event += j + ". "
                break
        paradox += 1
        loop[paradox] = event
        event = ""
print(f"{paradox} Paradoxes\n")
for i in loop:
    print(loop[i])
    print()

# -------------------- App 5: Snakes and Ladders --------------------
p1 = 0
p2 = 0
snakes = {15: 5, 19: 12, 25: 16, 27: 21}
Ladders = {9: 14, 13: 18, 17: 26}
start1 = False
start2 = False
while True:
    player1 = int(input("P1: "))
    if player1 == 1:
        start1 = True
    if start1:
        p1 += player1
        if p1 == 30:
            print("P1 Wins!")
            break
        if p1 in snakes:
            p1 = snakes[p1]
            print("P1 got eaten by snake!")
        if p1 in Ladders:
            p1 = Ladders[p1]
            print("P1 got a ladder!")
        if p1 > 29:
            p1 -= player1

    player2 = int(input("P2: "))
    if player2 == 1:
        start2 = True
    if start2:
        p2 += player2
        if p2 == 30:
            print("P2 Wins!")
            break
        if p2 in snakes:
            p2 = snakes[p2]
            print("P2 got eaten by snake!")
        if p2 in Ladders:
            p2 = Ladders[p2]
            print("P2 got a ladder!")
        if p2 > 29:
            p2 -= player2
    print("P1 in box", p1, "and P2 in box", p2)

# -------------------- App 6: Mathematical Series Builder --------------------
op = input("Which Series to Build? (1=Common Difference, 2= Power, 3= Fibonacci, 4= Reversal): ")
n = 0
if 1 <= int(op) <= 4:
    n = int(input("Value of n: "))
    s = 0
    series = ""

if n < 0:
    print("Invalid Input")
else:
    if op == "1":
        a = int(input("Value of a: "))
        d = int(input("Value of d: "))
        for i in range(n):
            term = a + i * d
            series += f"{term}" + (", " if i < n - 1 else "")
            s += term
    elif op == "2":
        x = int(input("Value of x: "))
        for i in range(1, n + 1):
            series += f"{i}^{x}" + (", " if i < n else "")
            s += i ** x
    elif op == "3":
        a, b = 0, 1
        series += f"{a}, "
        s += a
        for i in range(n - 1):
            series += f"{b}" + (", " if i < n - 2 else "")
            s += b
            a, b = b, a + b
    elif op == "4":
        for i in range(1, n + 1):
            val = i if i % 2 else -i
            series += f"{val}" + (", " if i < n else "")
            s += val
    print("Series:", series)
    print("Sum of the series:", s)

# -------------------- App 7: Spotify Playlist Modifier --------------------
playlists = {}

def create_playlist(name):
    playlists[name] = []
    print(f"New Playlist Created: {name}")

def add_songs(playlist, song):
    playlists[playlist].append(song)
    print(f"Song {song} added to {playlist}")

def delete_songs(playlist, song):
    if song in playlists[playlist]:
        playlists[playlist].remove(song)
        print(f"{song} removed from {playlist}")
    else:
        print(f"No song named {song} in {playlist}")

def search_songs(playlist, song):
    if song in playlists[playlist]:
        print(f"{song} found at position {playlists[playlist].index(song)+1} in {playlist}")
    else:
        print(f"{song} not found in {playlist}")

def sort_songs(playlist):
    playlists[playlist].sort()
    print(f"{playlist} playlist sorted alphabetically")

def blend_playlists(p1, p2, new_name):
    playlists[new_name] = playlists[p1] + playlists[p2]
    print(f"{p1} and {p2} blended into {new_name}")

def delete_playlist(name):
    if name in playlists:
        del playlists[name]
        print(f"Playlist: {name} deleted")
    else:
        print(f"No playlist named {name} found")

def show_playlist(name):
    if name in playlists:
        print(f"{name}: {playlists[name]}")
    else:
        print(f"No playlist named {name} found")

def show_all_playlists():
    print(playlists)

# Example Test Usage:
create_playlist("Chill Hour")
add_songs("Chill Hour", "Hello")
add_songs("Chill Hour", "Beautiful Mistakes")
add_songs("Chill Hour", "Echoes in Your Attic")
show_playlist("Chill Hour")
search_songs("Chill Hour", "Beautiful Mistakes")
delete_songs("Chill Hour", "Beautiful Mistakes")
search_songs("Chill Hour", "Beautiful Mistakes")
delete_songs("Chill Hour", "In The End")
sort_songs("Chill Hour")
create_playlist("Come vibe with me")
add_songs("Come vibe with me", "Apocalypse")
show_all_playlists()
blend_playlists("Chill Hour", "Come vibe with me", "Colab")
show_playlist("Colab")
delete_playlist("Chill Hour")
show_playlist("Chill Hour")
