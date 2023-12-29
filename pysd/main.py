import sys
from argparse import Namespace
from pysd.view.elfview import ElfView

def main(args: Namespace):

   
    if not args.file.is_file():
        return -1

    ElfView.from_file(args.file)

    return 0