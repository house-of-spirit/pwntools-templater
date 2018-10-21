#!/usr/bin/env python3
import sys
import argparse
import os

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    sys.stderr.write("Python 3.6+ is required for this program to run. (fstrings)\n")
    exit(1)

def generate_template(args):
    # DO NOT JUDGE

    env = ('{' + ', '.join(':'.join(["'" + y + "'" for y in x.split('=')]) for x in args.env) + '}') if args.env else 'os.environ'
    exec_path = args.local if args.local else ''
    remote_host, remote_port = args.remote.split(':') if args.remote else ('', '0000')
    elfs = ''.join([f'ELF_{i} = ELF("{elf}")'+'\n' for i, elf in enumerate(args.elfs)]) if args.elfs else ''

    return \
    f"""\
from pwn import *
import sys
import os

if sys.version_info[0] == 2:
    input = raw_input

def handle():
    env = {env}
    
    if args.LOCAL:
        return process('{exec_path}', env=env)
    elif args.GDB:
        return gdb.debug('{exec_path}', env=env)
    elif args.REMOTE:
        return remote('{remote_host}', {remote_port})
    print('Please supply an option via command line arguments.')
    exit(1)

{elfs}

def main():
    l = handle()
    if args.GDB:
        input()

    '''
    Your code here
    '''
    """
        




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--local', '-l', help="The local executable path.")
    parser.add_argument('--remote', '-r', help="The remote host and port to connect to. (host:port)")
    parser.add_argument('--env', nargs='+', help="The environment to be passed to the local executable. (supplied like \"KEY=VALUE\")")
    parser.add_argument('--elfs', '-e', nargs='+', help="The ELF files to be accessed in the script. (via pwntools' ELF())")

    parser.add_argument('--outfile', nargs='?', help="The file to write the script to. ('-' by default)", default='-')
    args = parser.parse_args()
    
    if args.outfile == '-':
        out = sys.stdout
    else:
        if os.path.exists(args.outfile):
            print("*****Writing script terminated: File already exists*****", file=sys.stderr)
            print("Writing to stdout instead....", file=sys.stderr)
            print("-"*80, file=sys.stderr)
            out = sys.stdout
        else:
            out = open(args.outfile, 'w')


    print(generate_template(args), file=out)

if __name__ == "__main__":
    main()
