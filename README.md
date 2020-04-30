# pwntools-templater

A small templating script to quickly generate pwntools scripts for binary exploitation CTF challenges.
I made this tool to assist in some CTF competitions, and I hope it will come in handy for you as well.

## Synopsis

```
usage: template.py [-h] [--local LOCAL] [--remote REMOTE]
                   [--env ENV [ENV ...]] [--elfs ELFS [ELFS ...]]
                   [--outfile [OUTFILE]]

optional arguments:
  -h, --help            show this help message and exit
  --local LOCAL, -l LOCAL
                        The local executable path.
  --remote REMOTE, -r REMOTE
                        The remote host and port to connect to. (host:port)
  --env ENV [ENV ...]   The environment to be passed to the local executable.
                        (supplied like "KEY=VALUE")
  --elfs ELFS [ELFS ...], -e ELFS [ELFS ...]
                        The ELF files to be accessed in the script. (via
                        pwntools' ELF())
  --outfile [OUTFILE]   The file to write the script to. ('-' by default)
```

## Installation
```
git clone https://github.com/house-of-spirit/pwntools-templater
```
