# SNARK

Simply Normalizing ARKs

Online at [datadavev.github.io/SNARK](https://datadavev.github.io/SNARK/).

## Installation

Snark can be installed locally using `pipx`, for example:

```bash
pipx install git+https://github.com/datadavev/SNARK.git
```

Snark will then be available from the command line:

```bash
$ snark "https://n2t.net/ark:/some/fake.ark"
ark:some/fake.ark
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

The `mkvirtualenv` step is optional, without it `poetry` will make something for you.