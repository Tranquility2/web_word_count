from pyscript import document, fetch, window
from js import console

from app import word_count, create_table, table_to_html

async def on_change(event):
    # For each file the user has selected to upload...
    for file in input.files:
        console.log(f"Processing {file.name}...")
        console.log(f"File size: {file.size} bytes")
        console.log(f"File type: {file.type}")
        console.log(f"Reading file content...")
        # Read the file content as a string.
        content = await file.text()
        # Count the words in the file content.
        results = word_count(content)
        # Create a table with the top 10 words.
        table = create_table(results, count=10)
        # Convert the table to an HTML table.
        html_table = table_to_html(table)
        # update the document with the table.
        document.getElementById("output").innerHTML = html_table


# Grab a reference to the file upload input element and add
# the on_change handler (defined above) to process the files.
input = document.querySelector("input[type=file]")
input.onchange = on_change