# TODO: : User prompt for asking some basic information
#
from pathlib import Path

import typer
from rich.prompt import Prompt

app = typer.Typer()


# @app.command()
# def song_name():
#     song = Prompt.ask("Enter the song name :duck:")
#     print(f"Searching for {song},Hang tight for a moment")


@app.command()
def dir_name():
    directory = Prompt.ask("Enter the folder name :📁:")
    print(f"Searching for {directory},Hang tight for a moment")


if __name__ == "__main__":
    app()
