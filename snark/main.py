"""
Commandline interface for SNARK
"""
import sys
import click
import snark
import http.server
import socketserver
import pathlib

SNARK_PORT = 20218
SNARK_HOME = pathlib.Path(globals().get("__file__", "./_")).absolute().parent.parent

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SNARK_HOME, **kwargs)

def runLocalSnark():
    with socketserver.TCPServer(("", SNARK_PORT), Handler) as httpd:
        print(f"Snarking at http://localhost:{SNARK_PORT}/")
        httpd.serve_forever()

@click.command()
@click.option("-W", "--web", is_flag=True)
@click.argument("src", required=False)
def main(web, src=None):
    if web:
        runLocalSnark()
        return 0
    if src is not None:
        res,infl = snark.normalizeARK(src)
        if infl != snark.Inflection.NONE:
            print(f"Inflection: {infl.name}")
        print(res[-1])
    return 0


if __name__ == "__main__":
    sys.exit(main())
