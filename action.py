#!/usr/bin/env python3

import argparse
from github import Github, GithubException
import os
import sys

def gh_tuple_split(s):
    sl = s.split('/')
    if len(sl) != 2:
        raise RuntimeError("Invalid org or dst format")

    return sl[0], sl[1]

def main():

    parser = argparse.ArgumentParser(
        description="GH Action script for contribution management",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', '--command', action='store',
                        choices=['external'],
                        required=True,
                        help='Command to execute.')

    parser.add_argument('-m', '--message', action='store',
                        required=False,
                        help='Message to post.')

    parser.add_argument('-l', '--labels', action='store',
                        required=False,
                        help='Comma-separated list of labels.')

    print(sys.argv)

    args = parser.parse_args()


    # Retrieve main env vars
    action = os.environ.get('GITHUB_ACTION', None)
    workflow = os.environ.get('GITHUB_WORKFLOW', None)
    repo = os.environ.get('GITHUB_REPOSITORY', None)

    print(f'Running action {action} from workflow {workflow} in {repo}')
    
    evt_name = os.environ.get('GITHUB_EVENT_NAME', None)
    evt_path = os.environ.get('GITHUB_EVENT_PATH', None)
    workspace = os.environ.get('GITHUB_WORKSPACE', None)

    print(f'Event {evt_name} in {evt_path} and workspace {workspace}')
 
    token = os.environ.get('GITHUB_TOKEN', None)
    if not token:
        sys.exit('Github token not set in environment, please set the '
                 'GITHUB_TOKEN environment variable and retry.')

    gh = Github(token)

    org, repo = gh_tuple_split(repo)

    org = gh.get_organization(org)
    #team = org.get_team_by_slug('ncs-code-owners')
    #for m in team.get_members():
    #    print(m.login)
    #repo = gh.get_repo('nrfconnect/sdk-nrf')
    #i = 0
    #for p in repo.get_pulls():
    #    print(f'{p.number}: {p.title}')
    #    i = i+1
    #    if i > 10:
    #        break
    sys.exit(0)

if __name__ == '__main__':
    main()
