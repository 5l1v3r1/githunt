import logging
import argparse
import random
import requests
from resources.headers import user_agents
from assets.colors import green,red,white,reset

logging.basicConfig(format=f"%(asctime)s {white}%(message)s{reset}"
,datefmt=f"{white}%I{green}:{white}%M{green}:{white}%S%p",level=logging.DEBUG)

class Search:
	def __init__ (self):
		self.base = "https://api.github.com/users/"
		self.headers = {"User-Agent": f"{random.choice(user_agents)}"}
				
	def main(self,username):
		base = self.base+username
		while True:
			try:
				data = requests.get(base, headers=self.headers).json()
				print(f"""{white}
{data['name']}
┌─── Profile photo: {green}{data['avatar_url']}{white}
├── Account type: {green}{data['type']}{white}
├── Username: {green}{data['login']}{white}
├── User id: {green}{data['id']}{white}
├── Node ID: {green}{data['node_id']}{white}
├── Location: {green}{data['location']}{white}
├── Followers: {green}{data['followers']}{white}
├── Following: {green}{data['following']}{white}
├── Blog: {green}{data['blog']}{white}
├── Bio: {green}{data['bio']}{white}
├── Public gists: {green}{data['public_gists']}{white}
├── Public repositories: {green}{data['public_repos']}{white}
├── Is site admin: {red}{data['site_admin']}{white}
├── Is hireable: {green}{data['hireable']}{white}
├── Organization: {green}{data['company']}{white}
├── Twitter handle: {green}@{data['twitter_username']}{white}
├── Joined on: {green}{data['created_at']}{white}
└──╼ Last updated on: {green}{data['updated_at']}{reset}
""")
			
				break
			except Exception as e:
				logging.info(f"ERROR: {red}{e}{reset}")
				logging.info(f"Retrying...{reset}")
				
			except KeyboardInterrupt:
				exit()
