# src/mewicli/cli.py

from typing import Annotated, Optional

import typer
from rich.console import Console

from .main import MediaWiki

app = typer.Typer(help="A simple cli for MediaWiki api actions.")

error_console = Console(stderr=True)


def creds_or_raise_error(
    url: str | None,
    username: str | None,
    password: str | None,
) -> tuple[str, str, str]:
    error = False
    optenvvar = (
        (url, "url", "MEDIAWIKI_URL"),
        (username, "username", "MEDIAWIKI_USERNAME"),
        (password, "password", "MEDIAWIKI_PASSWORD"),
    )
    for opt, opt_name, envvar_name in optenvvar:
        if opt is None:
            error_console.print(
                f"Either option `{opt_name}` or environment variable"
                f" `{envvar_name}` must be set."
            )
            error = True
    if error:
        raise typer.Exit(code=2)
    return (url, username, password)  # type: ignore


@app.command()
def update(
    title: Annotated[
        str,
        typer.Argument(
            help="Name of the page to upload.",
        ),
    ],
    filename: Annotated[
        str,
        typer.Argument(
            help="Filename of wiki text to upload.",
        ),
    ],
    url: Annotated[
        Optional[str],  # noqa: UP007
        typer.Option(
            envvar="MEDIAWIKI_URL",
            help="URL of MediaWiki.",
        ),
    ] = None,
    username: Annotated[
        Optional[str],  # noqa: UP007
        typer.Option(
            envvar="MEDIAWIKI_USERNAME",
            help="Username of API user.",
        ),
    ] = None,
    password: Annotated[
        Optional[str],  # noqa: UP007
        typer.Option(
            envvar="MEDIAWIKI_PASSWORD",
            help="Password of API user.",
        ),
    ] = None,
):
    """
    Update the contents of MediaWiki page from file.
    """
    url, username, password = creds_or_raise_error(url, username, password)
    mediawiki = MediaWiki(url)
    mediawiki.login(username, password)
    print(f"title: {title}")
    print(f"filename: {filename}")
    print(f"url: {url}")
    print(f"username: {username}")
    print(f"password: {password}")


@app.callback()
def callback():
    pass


if __name__ == "__main__":
    app()
