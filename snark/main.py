"""
Commandline interface for SNARK
"""
import sys
import click
import snark

SNARK_PORT = 20218

def runLocalSnark():
    import http.server
    import socketserver
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", SNARK_PORT), Handler) as httpd:
        print(f"Snarking at http://localhost:{SNARK_PORT}/")
        httpd.serve_forever()

def main():
    runLocalSnark()
    return 0


if __name__ == "__main__":
    sys.exit(main())
