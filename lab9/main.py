from lxml import etree

def parse_library(filename):
    tree = etree.parse(filename)
    root = tree.getroot()

    books = []
    for author in root.findall("author"):
        author_name = author.get("name")
        for book in author.findall("book"):
            data = {
                "title": book.findtext("title"),
                "author": author_name,
                "year": int(book.findtext("year")),
                "genre": book.findtext("genre"),
                "price": float(book.findtext("price"))
            }
            books.append(data)
            print(f"{data['title']} | {data['author']} | {data['year']} | {data['genre']} | ${data['price']:.2f}")

    avg_price = sum(book["price"] for book in books) / len(books)
    print(f"\nСредняя цена книг: ${avg_price:.2f}")

    # Фильтрация по жанру
    genre_filter = "Приключения"
    filtered = [b for b in books if b["genre"] == genre_filter]
    print(f"\nКниги в жанре '{genre_filter}':")
    for b in filtered:
        print(f"- {b['title']} ({b['year']})")

parse_library("library.xml")
