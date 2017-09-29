def PrintGoogleBooksData(books, response):
    if books:
        response.write("  # | Pages | Title\n")

        # Sort by largest page count
        def SortByPageCount(book):
            pageCount = book["volumeInfo"].get("pageCount", 0)
            return pageCount
        books.sort(key=SortByPageCount, reverse=True)

    i = 0
    for book in books:
        accessInfo = book["accessInfo"]

        # Skip books not available in epub (bug in Google Books API?)
        if not accessInfo["epub"]["isAvailable"]:
            continue

        volumeInfo = book["volumeInfo"]

        # Skip ebooks not in requested language (bug in Google Books API?)
        if volumeInfo["language"] <> BOOK_LG:
            continue

        title = volumeInfo["title"]
        subtitle = volumeInfo.get("subtitle", None)
        if subtitle is not None:
            title += " / " + subtitle
        pageCount = volumeInfo.get("pageCount", None)
        if pageCount is None:
            pageCount = ""
        else:
            pageCount = "{:,}".format(pageCount)

        i += 1
        response.write(u"{:3d} | {:>5} | {:.65}\n".format(i, pageCount, title))