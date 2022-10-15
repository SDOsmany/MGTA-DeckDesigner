# -*- coding: utf-8 -*-
"""MTGDataCleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ynmis_MTwjp7FLLg2ebvhO3Ho-L6ukJL
"""

#Loading data
import csv

#Open data and store in csv_reader
with open('modern_decks.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file)

  csv_reader = list(csv_reader)

#Now our data is stored in a list called csv_reader
#Get rid of empty lists on last 2 entries of csv_reader
csv_reader.pop()
csv_reader.pop()

#Remove any decks with winrate N/A, winrate 100%, or winrate == winrate (this showed up once)
csv_reader = [x for x in csv_reader if (x[4] != 'N/A' and x[4] != '100%' and x[4] != 'winrate')]

#We define a list of decks
decks = set()

for row in csv_reader:
  decks.add(row[5]) #the deck is the 5th item in this row

decks = list(decks)

#Now we make a dictionary, where (key, value) = (deck, deck attributes)
decks_dict = {}

for deck in decks:
  decks_dict[deck] = {'archetype': '', 'winrate': '', 'cards': []}

#Now we add archetype, winrate, and cards into each deck dictionary
for deck in decks:
  for row in csv_reader:
    if row[5] == deck: #if the deck in this row matches our current deck
      decks_dict[deck]['archetype'] = row[2] #set the archetype for this deck
      decks_dict[deck]['winrate'] = row[4] #set the archetype for this deck
      decks_dict[deck]['cards'].append(row[-1]) #add the card in this row to our current deck

#Now we remove some formatting text from the cards
for values in decks_dict.values():
  for i in range(len(values['cards'])):
    values['cards'][i] = values['cards'][i].replace('\n\xa0', 'x')
    
#Now we define our input list of decks and output list of winrates
decks = []
input = []
winrates = []

for deck, deck_dict in decks_dict.items():
  decks.append(deck)
  input.append(deck_dict['cards'])
  winrates.append(deck_dict['winrate'])



