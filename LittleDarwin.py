#!/usr/bin/env python3
import sys
import time
import datetime
from littledarwin.Schemata import parseCmdArgs
from optparse import OptionParser


def main(args):
    s_time = time.time()
    optionParser = OptionParser()
    options, filterType, filterList, higherOrder = parseCmdArgs(
        optionParser, args
    )
    if (options.reset):
        from littledarwin.Schemata import Schemata
        schemata = Schemata()
        schemata.cleanup_littleDarwin()
    else:
        from littledarwin.Schemata import Schemata
        schemata = Schemata()
        try:
            if options.isSchemataActive:
                schemata.main()
            elif options.isCoverageActive:
                from littledarwin.LittleDarwin import LittleDarwin
                littleDarwin = LittleDarwin()
                littleDarwin.main()
            else:
                from littledarwin.original import LittleDarwin as LittleDarwin_original
                LittleDarwin_original.main()
        finally:
            schemata.cleanup_littleDarwin()

    print("elapsed: " + str(datetime.timedelta(seconds=int(time.time() - s_time))))
    return 0


if __name__ == "__main__":
    main(sys.argv)
