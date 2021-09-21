#!/usr/bin/env python3
from assets.__main__ import *
from assets.colors import red, white, reset
					
if __name__=="__main__":
	parser = argparse.ArgumentParser(description=f"{white}Git{red}OSINT{white}: {red}Github OSINT tool developed by {white}rly0nheart{red}. https://github.com/{white}rlyonheart{reset}")
	parser.add_argument("username", metavar="USERNAME", help="github username")
	args = parser.parse_args()
	username = args.username
	Search().main(username)


