COUNTRY = "US"
BOOK_LG = "en"
BOOK_FIELDS = (
    "items("
    "id"
    ",accessInfo(epub/isAvailable)"
    ",volumeInfo(title,subtitle,language,pageCount)"
    ")"
)

def GetGoogleBooksData(author):
    books = []
    errors = None
    pageBookIdx = 0
    pageBookCnt = 40 # Default: 10, Max: 40

    while True:

        # Request paginated data from Google Books API
        url = (
            "https://www.googleapis.com/books/v1/volumes?"
            "q={}"
            "&startIndex={}"
            "&maxResults={}"
            "&country={}"
            "&langRestrict={}"
            "&download=epub"
            "&printType=books"
            "&showPreorders=false"
            "&fields={}"
        ).format(
            urllib.quote_plus('inauthor:"%s"' % (author)),
            pageBookIdx,
            pageBookCnt,
            COUNTRY,
            BOOK_LG,
            urllib.quote_plus(BOOK_FIELDS)
        )

        reqPageData = None
        try:
            response = urllib2.urlopen(url)
            reqPageData = json.load(response)
        except urllib2.HTTPError, err:
            errors = err.read()
            print "HTTPError = ", str(err.code)
        except:
            print "Error when handling\n", url

        if reqPageData is None:
            break

        pageBookItems = reqPageData.get("items", None)
        if pageBookItems is None:
            break

        books += pageBookItems
        itemCnt = len(pageBookItems)
        if itemCnt < pageBookCnt:
            # Do not issue another HTTP request
            break

        pageBookIdx += pageBookCnt
        # Loop and request next page data

    return books, errors