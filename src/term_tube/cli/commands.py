# TODO: : Ask for input and display a loading bar
#
import time
import typer
from rich.prompt import Prompt
from rich.progress import track

""" Ask for the song name you want to search """

app = typer.Typer()


@app.command()
def ask_prompt():
    name = Prompt.ask("Enter the song name you want to search  :raccoon:")
    print(f"You have searched for {name}!")


@app.command()
def loading_bar():
    total = 0
    for value in track(range(100), description="Processing ..."):
        time.sleep(0.01)
        total += 1
    print(f"Processed {total} things.")


if __name__ == "__main__":
    app()
