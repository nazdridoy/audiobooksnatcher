from gazpacho import get, Soup
from pick import pick
from halo import Halo
from urllib.parse import quote
import re

def search_book(source):
    if source == "toky":
        SEARCH_URL = "https://tokybook.com/?s="
        TITLE_PATTERN = r'<h2 class="entry-title"[^>]*><a href="([^"]+)"[^>]*>([^<]+)</a></h2>'
    elif source == "freeaudiobooks":
        SEARCH_URL = "https://freeaudiobooks.top/?s="
        TITLE_PATTERN = r'<h1 class="main-title title underline-effect large"><a href="([^"]+)"[^>]*>([^<]+)</a></h1>'
    else:
        raise ValueError("Invalid source specified")

    spinner = Halo(text="Searching...", spinner="dots")
    query = input("Search query: ")
    spinner.start()

    html = get(SEARCH_URL + quote(query))
    
    # print(f"Debug: HTML content length: {len(html)}")
    # print(f"Debug: First 1000 characters of HTML:\n{html[:1000]}")

    if "Nothing Found" in html:
        print("No results found!")
        spinner.stop()
        return search_book(source)

    matches = re.findall(TITLE_PATTERN, html, re.DOTALL)
    # print(f"Debug: Number of matches found: {len(matches)}")

    if not matches:
        print("No results found or unable to parse the page.")
        spinner.stop()
        return search_book(source)

    urls, titles = zip(*matches)
    titles = [title.strip() for title in titles]

    # print(f"Debug: Number of titles found: {len(titles)}")
    # print(f"Debug: Number of urls found: {len(urls)}")

    spinner.stop()
    _, idx = pick(titles, "Search results:")
    return urls[idx]
