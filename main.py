# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from translate import Translator
from inltk.inltk import tokenize
from inltk.inltk import setup
import spacy
import numpy as np
from spacy.vocab import Vocab
#nlp = spacy.load('en_core_web_sm')
from nltk.util import ngrams
import Levenshtein
import statistics


setup("mr")

targetWords = ["eye", "eyes", "ear", "ears" "nose", "noses", "hand", "hands" "tongue", "tongues" "tooth", "teeth", "death", "deaths", "water", "waters", "sun", "suns"
               "wind", "winds", "night", "nights", "two", "twos", "three", "threes", "four", "fours", "I", "you", "who",
               "name", "names"]

# change this to another list... // add in between from the book sanskrit to portoguese and delete non-workers from this istt
# maybe you calculauate what percentage of the poem contains target words 

targetWordsMarathi = ["डोळा", "डोळे", "कान", "कान" "नाक", "नाक", "हात", "हात" "जीभ", "जीभ" "दात", "दात", "मृत्यू ", "मृत्यू", "पाणी", "पाणी", "सूर्य", "सूर्य"
                "वारा", "वारा", "रात्र", "रात्र", "दोन", "दोन", "तीन", "तीन", "चार", "चार", "मी", "तू", "कोण ",
                "नाव", "नावे"]
targetWordsPorto = ["olho", "olhos", "orelha", "orelhas" "nariz", "nariz", "mão", "mãos" "língua", "língua" "dente", "dentes", "morte ", "mortes", "água", "águas", "sol", "sóis"
                "vento", "ventos", "noite", "noites", "dois", "dois", "três", "três", "quatro", "quatro", "eu", "você", "quem ",
                "nome", "nomes"]


marathiPoem = """तुम्ही मला इतिहासात लिहू शकता

तुझ्या कडू, वळणदार खोट्याने,

तुम्ही मला अगदी घाणीत तुडवू शकता

पण तरीही, धुळीप्रमाणे, मी उठेन.

माझी उदासीनता तुम्हाला अस्वस्थ करते का?

उदास का आहेस?

कारण मी तेलाच्या विहिरी असल्यासारखे चालतो

माझ्या लिव्हिंग रूममध्ये पंपिंग.

जसे चंद्र आणि सूर्यासारखे,

भरतीच्या निश्चिततेसह,

जसे आशा उंच उगवतात,

तरीही मी उठेन.

तुला मला तुटलेले बघायचे होते का?

डोके टेकवले आणि डोळे खाली केले?

अश्रूंच्या थेंबांसारखे खाली पडणारे खांदे.

माझ्या आत्मीय रडण्याने अशक्त झालो.

माझा अभिमान तुला त्रास देतो का?

तुम्ही ते कठोरपणे घेऊ नका

कारण मला सोन्याच्या खाणी मिळाल्यासारखे हसते

माझ्या स्वतःच्या मागच्या अंगणात खोदत आहे.

तू मला तुझ्या शब्दांनी गोळ्या घालू शकतोस,

तू मला तुझ्या डोळ्यांनी कापू शकतेस,

तू मला तुझ्या द्वेषाने मारून टाकशील.

पण तरीही, हवेप्रमाणे, मी उठेन.

माझी कामुकता तुम्हाला अस्वस्थ करते का?

तो एक आश्चर्य म्हणून येतो का

की मला हिरे मिळाल्यासारखे मी नाचतो

माझ्या मांड्यांच्या बैठकीत?

इतिहासाच्या लाजिरवाण्या झोपडीतून

मी उठतो

भूतकाळापासून जे वेदनांमध्ये रुजलेले आहे

मी उठतो

मी एक काळा महासागर आहे, उडी मारणारा आणि रुंद आहे,

विहिरी आणि सूज मी भरती मध्ये सहन.

दहशत आणि भीतीच्या रात्री मागे सोडून

मी उठतो

एका दिवसात जे आश्चर्यकारकपणे स्पष्ट आहे

मी उठतो

माझ्या पूर्वजांनी दिलेल्या भेटवस्तू आणणे,

मी दासाचे स्वप्न आणि आशा आहे.

मी उठतो

मी उठतो

मी उठतो."""
portoguesePoem = """Você pode me descrever na história
Com suas azedas, retorcidas mentiras,
Você pode pisar em mim enquanto estou na lama
Mas ainda assim, como poeira, eu me levanto.
 
A minha audácia te incomoda?
Por que você está cercado de melancolia?
Porque eu caminho como se tivesse petróleo
Jorrando na minha sala de estar?
 
Assim como luas e sóis,
Com a certeza das marés,
Assim como esperanças voando para o alto
Ainda me levanto.
 
Você quer me ver quebrada?
Com a cabeça curvada, os olhos baixos?
Os ombros caindo como lágrimas
Enfraquecidos pelos lamentos da minha alma.
 
Será que minha altivez te ofende?
Você não deveria levar isso tão a sério
Porque vou rir como se tivesse minas de ouro
Enterradas no meu próprio quintal.
 
Você pode me atirar com suas palavras,
Você pode me cortar com seus olhos,
Você pode me matar com seu ódio,
Mas ainda assim, como o ar, eu me levanto.
 
Será que minha sensualidade te ofende?
Será que isso vem como uma surpresa
Que eu danço como se tivesse diamantes
Entre as minhas coxas?
 
Para fora das cabanas da vergonha da história
Eu me levanto
De um passado enraizado na dor
Eu me levanto
Sou um oceano negro, amplo e pulsante,
Satisfeito e inchada eu me agarro às marés
Deixando para trás noites de terror e de medo
Eu me levanto
Rumo ao nascer de um dia maravilhosamente belo
Eu me levanto
Trazendo os presentes que meus antepassados me deram,
Eu sou o sonho e a esperança dos escravos.
Eu me levanto
Eu me levanto
Eu me levanto."""
output = tokenize(marathiPoem, "mr")
portoguesePoem = portoguesePoem.split(" ")
extractedMarathi = []
for i in range(len(output)):
    for j in range(len(targetWordsMarathi)):
        if output[i].__contains__(targetWordsMarathi[j]):
            extractedMarathi.append(output[i])

#for i in range(len(extractedMarathi)):
    #if extractedMarathi[i].__contains__("▁"):
       # extractedMarathi[i] = extractedMarathi[i][1:]


comparePorto = []
for i in range(len(portoguesePoem)):
    for j in range(len(targetWordsPorto)):
        if portoguesePoem[i].__contains__(targetWordsPorto[j]):
            comparePorto.append(portoguesePoem[i])

i = 0
while (i < (len(comparePorto))):
    comparePorto[i] = comparePorto[i].lower()
    if comparePorto[i].__contains__("\n"):
        elements = comparePorto[i].split(",\n")
        comparePorto.append(elements[0])
        comparePorto.append(elements[1])
        comparePorto.remove(comparePorto[i])
        i = i - 1
    i = i + 1

extractedMarathi = [*set(extractedMarathi)] # duplicates deleting
comparePorto = [*set(comparePorto)] # duplicates deleting

print(extractedMarathi)
print(comparePorto)


#['तून', '▁भेटवस्तू', '▁डोळे', '▁मी', '▁रात्री', '▁तू', '▁सूर्य']
#['meus', 'você', 'olhos', 'noites', 'seu', 'seus', 'meu', 'eu']

c1 = Levenshtein.ratio("surya", "sóis")
c2 = Levenshtein.ratio("dole", "olhos")
c3 = Levenshtein.ratio("mi", "eu")
c4 = Levenshtein.ratio("ratri", "noites")
c5 = Levenshtein.ratio("tu", "tu")
avgSim = (c1+c2+c3+c4+c5)/5
print(avgSim)

print(statistics.stdev([c1, c2, c3, c4, c5]))


# compare all the tests but
# 1) get the words in order and tuple them
# 2) then do the tests for all of them and get average
# do a std to get a normal distribution as well and compare that with the website calc and do a t-test

















