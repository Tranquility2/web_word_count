from pyscript import document, fetch, window
from js import console

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
    for file in input.files:
        # console.log(f"Processing {file.name}...")
        # console.log(f"File size: {file.size} bytes")
        # console.log(f"File type: {file.type}")
        console.log(f"Reading file content...")
        # Read the file content as a string.
        content = await file.text()
        await process_data(content)


# Grab a reference to the file upload input element and add
# the on_change handler (defined above) to process the files.
input = document.querySelector("input[type=file]")
input.onchange = on_change