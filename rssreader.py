import feedparser

print('Type in an URL of a RSS Feed:')
inputUrl = input().strip()


myFeed = feedparser.parse(inputUrl)
print('\n\nRSS Feed "' + myFeed.feed.title + '"')

inputYN = 'y'
myRange = 0
while inputYN == 'y':
    myRange +=5
    for i in range(myRange-5, myRange):
        myTitle = myFeed.entries[i].title
        myDate = myFeed.entries[i].published
        myDescr = myFeed.entries[i].description
        myLink = myFeed.entries[i].link
        print('\n', myTitle, " (", myDate, ")")
        print(myDescr)
        print(myLink)
    print("Do you like to see more? Type y for yes, n for no:")
    inputYN = input().strip()
