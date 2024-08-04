import click

from rich.console import Console
from rich.table import Table


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


def print_results(results: dict, count: int = 10) -> None:
    """Prints the top 10 results of the word count in a table using rich"""
    console = Console()
    table = Table(title="Top 10 Words")
    table.add_column("Word", style="bold cyan", no_wrap=True)
    table.add_column("Count", style="bold magenta")

    for word, count in sorted(results.items(), key=lambda x: x[1], reverse=True)[:count]:
        table.add_row(word, str(count))

    console.print(table)


if __name__ == "__main__":
    data: str = load_file(standalone_mode=False)
    results: dict = word_count(data)
    print_results(results, count=5)
