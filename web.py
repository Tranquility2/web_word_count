from pyscript import document, fetch, window
from js import console

import asyncio

from app import word_count, create_table, table_to_html

async def process_data(data: str):
    console.log(f"Processing file content...")
    results = await word_count(data)
    table = await create_table(results, count=10)
    html_table = await table_to_html(table)
    # update the document with the table.
    document.getElementById("output").innerHTML = html_table

async def on_change(event):
    # For each file the user has selected to upload...
    for file in event.target.files:
        # console.log(f"Processing {file.name}...")
        # console.log(f"File size: {file.size} bytes")
        # console.log(f"File type: {file.type}")
        console.log(f"Reading file content...")
        # Read the file content as a string.
        content = await file.text()
        await process_data(content)

async def main():
    # Get the input element.
    input = document.querySelector("input[type=file]")
    # When the user selects a file to upload, call the on_change function.
    input.onchange = on_change

asyncio.get_event_loop().run_until_complete(main())
