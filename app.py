import click
import io

from rich.console import Console
from rich.table import Table
from rich import print as rprint


@click.command()
@click.option("--file", "-f", type=click.Path(exists=True), required=True, help="File to read")
def load_file(file: str) -> str:
    """Reads a file and returns its content"""
    with open(file, "r") as f:
        data = f.read()
    return data


def word_count(data: str) -> dict:
    """Word counting object, counts total words and top 10 occurring words"""
    words = data.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def create_table(results: dict, count: int = 10) -> Table:
    """Prints the top results of the word count in a table using rich"""

    table = Table(title=f"Top {count} Words")
    table.add_column("Word", style="bold cyan")
    table.add_column("Count", style="bold magenta")

    for word, count in sorted(results.items(), key=lambda x: x[1], reverse=True)[:count]:
        table.add_row(word, str(count))

    # console = Console(file=io.StringIO(), width=120)
    # console.print(table)
    # result = console.file.getvalue()
    #
    #     return result

    return table


def table_to_html(table: Table) -> str:
    """Converts a rich table to an HTML table"""
    console = Console(record=True)
    console.print(table)
    console.end_capture()

    return console.export_html(inline_styles=True)


if __name__ == "__main__":
    data: str = load_file(standalone_mode=False)
    results: dict = word_count(data)
    table = create_table(results, count=5)
    rprint(table)
