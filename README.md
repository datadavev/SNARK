# SNARK

Simply Normalizing ARKs

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



## Development

SNARK uses [poetry](). To setup a development environment:

```bash
git clone https://github.com/datadavev/SNARK.git
cd SNARK
poetry install
```