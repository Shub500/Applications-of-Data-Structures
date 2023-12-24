text = """You may write me down in history
With your bitter, twisted lies,
You may tread me in the very dirt
But still, like dust, I'll rise.
Does my sassiness upset you?
Why are you beset with gloom?
'Cause I walk like I've got oil wells
Pumping in my living room.
Just like moons and like suns,
With the certainty of tides,
Just like hopes springing high,
Still I'll rise.
Did you want to see me broken?
Bowed head and lowered eyes?
Shoulders falling down like teardrops.
Weakened by my soulful cries.
Does my haughtiness offend you?
Don't you take it awful hard
'Cause I laugh like I've got gold mines
Diggin' in my own back yard.
You may shoot me with your words,
You may cut me with your eyes,
You may kill me with your hatefulness,
But still, like air, I'll rise.
Does my sexiness upset you?
Does it come as a surprise
That I dance like I've got diamonds
At the meeting of my thighs?
Out of the huts of history's shame
I rise
Up from a past that's rooted in pain
I rise
I'm a black ocean, leaping and wide,
Welling and swelling I bear in the tide.
Leaving behind nights of terror and fear
I rise
Into a daybreak that's wondrously clear
I rise
Bringing the gifts that my ancestors gave,
I am the dream and the hope of the slave.
I rise
I rise
I rise."""


import Levenshtein
import statistics

targetWords = ["eye", "eyes", "ear", "ears", "nose", "noses", "hand", "hands", "tongue", "tongues", "tooth", "teeth", "death", "deaths", "water", "waters", "sun", "suns"
               "wind", "winds", "night", "nights", "two", "twos", "three", "threes", "four", "fours", "I", "you", "who", "why",
               "name", "names", "flower",  "flowers", "year", "years", "God", "universe", "smile", "smiles", "open", "close",
               "time", "star", "stars", "moon", "moons", "fire"]

list = text.split(" ")
sims = []
for i in range(len(list)):
    for j in range(len(targetWords)):
        if list[i].__contains__(targetWords[j]):
            sims.append(list[i])

sims = [*set(sims)]
print(sims)

hits = ["nights", "why", "I", "eyes", "you", "suns", "moons"]
p = ["noites", "por que", "eu", "olhos", "tu", "sois", "lua"]
m = ["ratri", "ka", "mi", "dole", "tu", "surya", "chandra"]

total = 0
list = []
for i in range(len(p)):
    list.append(Levenshtein.ratio(p[i], m[i]))
    total = total + Levenshtein.ratio(p[i], m[i])

avgSim = total/len(hits)

print(avgSim)
print(statistics.stdev(list))