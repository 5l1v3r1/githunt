#!/usr/bin/env python3
from assets.__main__ import *
from resources.banner import banner
from assets.colors import red, white, reset

print(banner)					
if __name__=="__main__":
	parser = argparse.ArgumentParser(description=f"{white}Git{red}Hunt{white}: {red}Github user OSINT tool developed by {white}rly0nheart{red}. https://github.com/{white}rlyonheart{reset}")
	parser.add_argument("username", metavar="USERNAME", help="github username")
	parser.add_argument("-v", "--verbose", dest="verbose",help="verbosity", action="store_true")
	args = parser.parse_args()
	if args.verbose:
		logging.basicConfig(format=f"{white}%(message)s{reset}"
,level=logging.DEBUG)

	Search().main(args)


