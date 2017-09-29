class ListEbooksByAuthor(webapp2.RequestHandler):
    def get(self, author):
        author = urllib.unquote_plus(author)
        self.response.headers["Content-Type"] = "text/plain; charset=utf-8"

        caption = ' "%s" ebooks available on Google Books\n' % (author)
        border = "".ljust(len(caption),"=") + "\n"
        self.response.write(border)
        self.response.write(caption)
        self.response.write(border)

        start = timer()
        books, errors = GetGoogleBooksData(author)
        end = timer()

        if errors is None:
            PrintGoogleBooksData(books, self.response)
        else:
            self.response.write("### Error ###\n%s" % (errors))

        self.response.write(border)
        self.response.write(" Executed in %.1f s\n" % (end - start))
        self.response.write(border)