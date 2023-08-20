# src/mewicli/main.py

from __future__ import annotations  # for Python 3.7-3.9

import os
from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def download(
    url: Annotated[str, typer.Option(help="URL of MediaWiki site.")] = "",
    username: Annotated[str, typer.Option(help="username of API user.")] = "",
    password: Annotated[str, typer.Option(help="password of API user.")] = "",
    filename: Annotated[
        str, typer.Option(help="Filename to wiki text to.")
    ] = "",
    pagename: Annotated[
        str, typer.Option(help="Name of the page to download.")
    ] = "",
):
    """
    Download a wiki page from a MediaWiki.
    """
    MEDIAWIKI_URL = url or os.environ.get(
        "MEDIAWIKI_URL", "http://localhost/w/api.php"
    )
    MEDIAWIKI_USERNAME = username or os.environ.get(
        "MEDIAWIKI_USERNAME", "ingrid"
    )
    MEDIAWIKI_PASSWORD = password or os.environ.get(
        "MEDIAWIKI_PASSWORD", "henk123"
    )
    MEDIAWIKI_FILENAME = filename or os.environ.get(
        "MEDIAWIKI_FILENAME", "README.wiki"
    )
    MEDIAWIKI_PAGENAME = pagename or os.environ.get(
        "MEDIAWIKI_PAGENAME", "does_not_exist"
    )
    print(f"url: {MEDIAWIKI_URL}")
    print(f"username: {MEDIAWIKI_USERNAME}")
    print(f"password: {MEDIAWIKI_PASSWORD}")
    print(f"filename: {MEDIAWIKI_FILENAME}")
    print(f"pagename: {MEDIAWIKI_PAGENAME}")


@app.command()
def upload(
    url: Annotated[str, typer.Option(help="URL of MediaWiki site.")] = "",
    username: Annotated[str, typer.Option(help="username of API user.")] = "",
    password: Annotated[str, typer.Option(help="password of API user.")] = "",
    filename: Annotated[
        str,
        typer.Option(help="Filename of wiki text to upload."),
    ] = "",
    pagename: Annotated[
        str, typer.Option(help="Name of the page to upload.")
    ] = "",
):
    """
    Upload a wiki page from a MediaWiki.
    """
    MEDIAWIKI_URL = url or os.environ.get(
        "MEDIAWIKI_URL", "http://localhost/w/api.php"
    )
    MEDIAWIKI_USERNAME = username or os.environ.get(
        "MEDIAWIKI_USERNAME", "ingrid"
    )
    MEDIAWIKI_PASSWORD = password or os.environ.get(
        "MEDIAWIKI_PASSWORD", "henk123"
    )
    MEDIAWIKI_FILENAME = filename or os.environ.get(
        "MEDIAWIKI_FILENAME", "README.wiki"
    )
    MEDIAWIKI_PAGENAME = pagename or os.environ.get(
        "MEDIAWIKI_PAGENAME", "does_not_exist"
    )
    print(f"url: {MEDIAWIKI_URL}")
    print(f"username: {MEDIAWIKI_USERNAME}")
    print(f"password: {MEDIAWIKI_PASSWORD}")
    print(f"filename: {MEDIAWIKI_FILENAME}")
    print(f"pagename: {MEDIAWIKI_PAGENAME}")


if __name__ == "__main__":
    app()
