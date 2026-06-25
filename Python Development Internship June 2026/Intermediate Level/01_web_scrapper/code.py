"""Web Scraper: Extract data from websites using libraries like
Beautiful Soup or Scrapy.

This example fetches quotes from http://quotes.toscrape.com and prints the
quote text, author, and tags for each quote on the page.
"""

import csv
import requests
from bs4 import BeautifulSoup

# Base URL for the example target website that contains quotes.
BASE_URL = "http://quotes.toscrape.com"


def fetch_page(url: str) -> str:
    """Fetch the HTML content of a page.

    Sends an HTTP GET request to the provided URL and returns the page HTML as
    a string. Raises an exception if the request fails.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_quotes(html: str) -> list[dict[str, str | list[str]]]:
    """Parse quote data from HTML content.

    Uses BeautifulSoup to locate each quote block on the page and extract the
    quote text, author name, and list of tags.
    """
    soup = BeautifulSoup(html, "html.parser")
    quotes = []

    for quote_block in soup.select("div.quote"):
        text = quote_block.select_one("span.text").get_text(strip=True)
        author = quote_block.select_one("small.author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote_block.select("div.tags a.tag")]

        quotes.append({
            "text": text,
            "author": author,
            "tags": tags,
        })

    return quotes


def print_quotes(quotes: list[dict[str, str | list[str]]]) -> None:
    """Print parsed quote data to the console."""
    for index, quote in enumerate(quotes, start=1):
        print(f"Quote {index}:")
        print(f"  Text: {quote['text']}")
        print(f"  Author: {quote['author']}")
        print(f"  Tags: {', '.join(quote['tags']) or 'None'}")
        print()


def save_quotes_to_csv(quotes: list[dict[str, str | list[str]]], filename: str) -> None:
    """Write the scraped quote data into a CSV file."""
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["text", "author", "tags"])
        writer.writeheader()

        for quote in quotes:
            writer.writerow({
                "text": quote["text"],
                "author": quote["author"],
                "tags": ", ".join(quote["tags"]),
            })


def main() -> None:
    """Main entrypoint for the script.

    Fetches the page, parses the quotes, prints them, and stores the data in a
    CSV file.
    """
    html = fetch_page(f"{BASE_URL}/page/1/")
    quotes = parse_quotes(html)

    if not quotes:
        print("No quotes found on the page.")
        return

    # Print the quotes to the terminal so users can see the results immediately.
    print_quotes(quotes)

    # Save the parsed quote data to a CSV file.
    save_quotes_to_csv(quotes, "quotes.csv")
    print("Saved scraped quotes to quotes.csv")


if __name__ == "__main__":
    main()

