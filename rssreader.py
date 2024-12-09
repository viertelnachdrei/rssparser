import feedparser

inputOk = False
while inputOk == False:
    inputUrl = input('Type in an URL of a RSS Feed: ').strip() # get url from user
    myFeed = feedparser.parse(inputUrl) # parse url
    if len(myFeed.entries) >= 1: # if parsed feed has one or more entries, the url seems valid enough ...
        inputOk = True
    else: # ... else user has to input a new url
        print('Input invalid, please try again.')
print(f'\nRSS Feed: {myFeed.feed.title}') # print title of the RSS Feed

inputYN = 'y'
myRange = 0
while inputYN == 'y': # while reader wants to read, print the next five items of the feed
    for i in range(myRange, myRange+5): # get title, date, description and link of every item of feed and print it nicely
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

    myRange += 5
