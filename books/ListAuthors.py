AUTHORS = [
    "Miguel de Cervantes",
    "Charles Dickens",
    "Antoine de Saint-Exupéry",
    "J. K. Rowling",
    "J. R. R. Tolkien",
    "Agatha Christie",
    "Lewis Carroll",
    "C. S. Lewis",
    "Dan Brown",
    "Arthur Conan Doyle",
    "Jules Verne",
    "Stephen King",
    "Stieg Larsson",
    "George Orwell",
    "Ian Fleming",
    "James Patterson",
    "Anne Rice",
    "Terry Pratchett",
    "George R. R. Martin",
    "Edgar Rice Burroughs",
    "Michael Connelly",
    "Jo Nesbo"
]

HTML_CONTENT_BEG = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Ebooks By Demo</title>
  <style>body{font-family: sans-serif}</style>
</head>
<body>
  <h1>Welcome</h1>
  <h2>List available ebooks written by</h2>
  <ul>'''
HTML_CONTENT_LI_FMT = '''
    <li><a href="./%s">%s</a></li>'''
HTML_CONTENT_END = '''
  </ul>
</body>
</html>'''

class ListAuthors(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write(HTML_CONTENT_BEG)
        for author in sorted(AUTHORS):
            li = (HTML_CONTENT_LI_FMT) % (
                urllib.quote_plus(author),
                author
            )
            self.response.write(li)
        self.response.write(HTML_CONTENT_END)