import glob
import os
import sys
import threading
import yaml
from github import Github


file_list = glob.glob('./*/*')
g = Github(os.environ['TOKEN'])


class th(threading.Thread):

    def __init__(self, file):
        threading.Thread.__init__(self)
        self._file = file

    def run(self):
        l = self._file.split('/')
        owner_name = l[1]
        repo_name = os.path.splitext(os.path.basename(l[2]))[0]
        obj = self.yaml_load(f)
        org = g.get_organization(owner_name)
        repo = g.get_repo(owner_name + '/' + repo_name)
        self.delete_teams(repo, obj)
        for k, v in obj.items():
            for i in v:
                team = org.get_team_by_slug(i)
                team.update_team_repository(repo, k)
        print(f'Finished setting of {repo}')

    def yaml_load(self, path):
        try:
            with open(path) as file:
                obj = yaml.safe_load(file)
        except Exception as e:
            print(e, file=sys.stderr)
            sys.exit(1)
        return obj

    def delete_teams(self, repo, obj):
        teams = repo.get_teams()
        l = []
        for _, v in obj.items():
            l.append(v)
        l = sum(l, [])
        for team in teams:
            if team.name not in l:
                team.remove_from_repos(repo)

for f in file_list:
    t = th(f)
    t.start()
