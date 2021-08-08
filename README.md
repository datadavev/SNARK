# SNARK

Simply Normalizing [ARK](https://datatracker.ietf.org/doc/html/draft-kunze-ark-27)s

Online at [datadavev.github.io/SNARK](https://datadavev.github.io/SNARK/).

**Note: 2021-08-08 Not yet released.** The normalization rules are not verfiied and are subject to change.

## Installation

Snark can be installed locally using `pipx`, for example:

```bash
pipx install git+https://github.com/datadavev/SNARK.git
```

Snark will then be available from the command line:

```bash
$ snark "https://example.org/ark:12345/x54xz321/s3/f8.05v.tiff"
ark:12345/x54xz321/s3/f8.05v.tiff
```

Snark has a local web UI as well:
```bash
$ snark -W
Snarking at http://localhost:20218/
```

## Development

SNARK uses [poetry](https://python-poetry.org/). To setup a development environment:

```bash
git clone https://github.com/datadavev/SNARK.git
cd SNARK
mkvirtualenv SNARK
poetry install
```

The `mkvirtualenv` step is optional. Without it, `poetry` will make something for you.
