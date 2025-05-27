#!/usr/bin/env python3

"""
__main__ script for littledarwin package
"""

from littledarwin import LittleDarwin
import sys
import os


def entryPoint():
    ld = LittleDarwin()
    ld.main()


if __name__ == "__main__":
    sys.exit(entryPoint())
