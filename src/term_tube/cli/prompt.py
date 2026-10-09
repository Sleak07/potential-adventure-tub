# TODO: : User prompt for asking the name of the song
#
import typer
from rich.prompt import Prompt

app = typer.Typer()


@app.command()
def song_name():
    song = Prompt.ask("Enter the song name :duck:")
    print(f"Searching for {song},Hang tight for a moment")


if __name__ == "__main__":
    app()
