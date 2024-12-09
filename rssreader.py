import feedparser

print('Type in an URL of a RSS Feed:') # get url from user
inputUrl = input().strip()

myFeed = feedparser.parse(inputUrl) # parse url and print title of RSS feed
print(f'\nRSS Feed: {myFeed.feed.title}')

inputYN = 'y'
myRange = 0

while inputYN == 'y': # while reader wants to read, print the next five items of the feed
    myRange +=5
    for i in range(myRange-5, myRange): # get title, date, description and link of every item of feed and print it nicely
        myTitle = myFeed.entries[i].title
        myDate = myFeed.entries[i].published_parsed
        myDate = f"{myDate[2]:02}.{myDate[1]:02}.{myDate[0]} {myDate[3]:02}:{myDate[4]:02}" # format date
        myDescr = myFeed.entries[i].description
        myDescr = myDescr[myDescr.find(">")+1:].strip() # some items include pictures in <> tags, delete them
        myLink = myFeed.entries[i].link

        print(f"\n{myDate} {myTitle}")
        print(myDescr)
        print("Read more: ", myLink)

    print("\nDo you like to see more? Type y for yes, n for no:") # does the user want to read more?
    inputYN = input().strip()
