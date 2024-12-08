import feedparser

print('Bitte eine URL zum RSS-Feed eingeben:')
inputUrl = input().strip()


myFeed = feedparser.parse(inputUrl)
print('\n\nRSS Feed "' + myFeed.feed.title + '"')

inputYN = 'j'
myRange = 0
while inputYN == 'j':
    myRange +=5
    for i in range(myRange-5, myRange):
        myTitle = myFeed.entries[i].title
        myDate = myFeed.entries[i].published
        myDescr = myFeed.entries[i].description
        myLink = myFeed.entries[i].link
        print('\n', myTitle, " (", myDate, ")")
        print(myDescr)
        print(myLink)
    print("Möchten Sie mehr sehen? j für Ja oder n für Nein eingeben:")
    inputYN = input().strip()
