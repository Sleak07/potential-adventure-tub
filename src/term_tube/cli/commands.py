# TODO: : Ask for input and display a loading bar
#

import typer
import time
from rich.prompt import Prompt
from rich.progress import Progress, SpinnerColumn, TextColumn


app = typer.Typer()


""" Ask for the song name you want to search """


@app.command()
def ask_prompt():
    name = Prompt.ask("Enter the song name you want to search  :raccoon:")
    print(f"You have searched for {name}!")


""" Ask for the entry or exit from app """


@app.command()
def choice_exit():
    depart = typer.confirm("Are you sure you want to exit it?", abort=True)
    print(f"{depart}, Exiting the app")


"""  Get the progress of app """


@app.command()
def progress_bar():
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        progress.add_task(description="Preparing...", total=None)
        time.sleep(5)
    print("Done!")


if __name__ == "__main__":
    app()
