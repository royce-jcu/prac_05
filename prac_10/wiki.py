import wikipedia

while True:
    search_input = input("Enter a page title or search phrase (or leave blank to quit): ")

    if not search_input:
        break

    try:
        page = wikipedia.page(search_input)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print("Disambiguation Error: Please specify a more specific page title.")
    except wikipedia.PageError as e:
        print("Page Error: The page could not be found.")

print("Program ended.")