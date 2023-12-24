text = """To go into solitude, a man needs to retire as much from his chamber as from society. I am not solitary whilst I read and write, though nobody is with me. But if a man would be alone, let him look at the stars. The rays that come from those heavenly worlds, will separate between him and what he touches. One might think the atmosphere was made transparent with this design, to give man, in the heavenly bodies, the perpetual presence of the sublime. Seen in the streets of cities, how great they are! If the stars should appear one night in a thousand years, how would men believe and adore; and preserve for many generations the remembrance of the city of God which had been shown! But every night come out these envoys of beauty, and light the universe with their admonishing smile.
The stars awaken a certain reverence, because though always present, they are inaccessible; but all natural objects make a kindred impression, when the mind is open to their influence. Nature never wears a mean appearance. Neither does the wisest man extort her secret, and lose his curiosity by finding out all her perfection. Nature never became a toy to a wise spirit. The flowers, the animals, the mountains, reflected the wisdom of his best hour, as much as they had delighted the simplicity of his childhood.
"""
targetWords = ["eye", "eyes", "ear", "ears", "nose", "noses", "hand", "hands", "tongue", "tongues", "tooth", "teeth", "death", "deaths", "water", "waters", "sun", "suns"
               "wind", "winds", "night", "nights", "two", "twos", "three", "threes", "four", "fours", "I", "you", "who", "why",
               "name", "names", "flower",  "flowers", "year", "years", "God", "universe", "smile", "smiles", "open", "close",
               "time", "star", "stars", "moon", "moons", "fire"]


print(len(targetWords))
import Levenshtein
import statistics

list = text.split(" ")
sims = []
for i in range(len(list)):
    for j in range(len(targetWords)):
        if list[i].__contains__(targetWords[j]):
            sims.append(list[i])

sims = [*set(sims)]
print(sims)

o = ['stars', 'God', 'smile', 'I', 'night', 'years,', 'open', 'flowers,', 'universe']

p = ["estrelas", "Deus", "sorrir", "eu", "noite", "anos", "abrir", "flores", "universo"]
m = ["tare", "deva", "smita", "mi", "ratri", "varse", "khuli", "fule", "visva"]

total = 0
list = []
for i in range(len(p)):
    list.append(Levenshtein.ratio(p[i], m[i]))
    total = total + Levenshtein.ratio(p[i], m[i])

avgSim = total/len(o)

print(avgSim)
print(statistics.stdev(list))

