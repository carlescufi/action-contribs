#!/usr/bin/env python3

from github import Github, GithubException
import os
import sys

def main():

    # Retrieve main env vars
    action = os.environ.get('GITHUB_ACTION', None)
    workflow = os.environ.get('GITHUB_WORKFLOW', None)
    repo = os.environ.get('GITHUB_REPOSITORY', None)

    print(f'Running action f{action} from workflow f{workflow} in repository '
           'f{repo}')
    
    evt_name = os.environ.get('GITHUB_EVENT_NAME', None)
    evt_path = os.environ.get('GITHUB_EVENT_PATH', None)
    workspace = os.environ.get('GITHUB_WORKSPACE', None)

    print(f'Event f{evt_name} in f{evt_path} and workspace f{workspace}')
 
    token = os.environ.get('GITHUB_TOKEN', None)
    if not token:
        sys.exit('Github token not set in environment, please set the '
                 'GITHUB_TOKEN environment variable and retry.')

    gh = Github(token)
    org = gh.get_organization('nrfconnect')
    #team = org.get_team_by_slug('ncs-code-owners')
    #for m in team.get_members():
    #    print(m.login)
    repo = gh.get_repo('nrfconnect/sdk-nrf')
    i = 0
    for p in repo.get_pulls():
        print(f'{p.number}: {p.title}')
        i = i+1
        if i > 10:
            break

    print(sys.argv)
    #args = parse_args(sys.argv[1:], gh)

    sys.exit(0)

if __name__ == '__main__':
    main()
