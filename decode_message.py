import requests
from bs4 import BeautifulSoup

def render_grid_from_doc(url: str):
    # Step 1: Download the Google Doc HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Find the first <table> element
    table = soup.find("table")
    if not table:
        print("No table found.")
        return

    rows = table.find_all("tr")
    pixels = []

    # Step 3: Extract valid rows
    for row in rows:
        cells = row.find_all("td")
        if len(cells) != 3:
            continue  # Skip malformed rows

        x_text = cells[0].text.strip()
        char = cells[1].text.strip()
        y_text = cells[2].text.strip()

        if not (x_text.isdigit() and y_text.isdigit()):
            continue  # Skip header or bad rows

        x = int(x_text)
        y = int(y_text)
        pixels.append((x, y, char))

    # Debug print to verify parsing
    print("Pixels found:", len(pixels))
    print("First 5 pixels:", pixels[:5])

    if not pixels:
        print("No valid pixel data found. Check the table structure.")
        return

    # Step 4: Determine grid size
    max_x = max(x for x, y, _ in pixels)
    max_y = max(y for x, y, _ in pixels)

    # Step 5: Initialize grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Step 6: Populate grid
    for x, y, char in pixels:
        grid[y][x] = char

    # Step 7: Print the result
    for row in grid:
        print(''.join(row))

# Run it with your provided URL
url = "https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub"
render_grid_from_doc(url)
