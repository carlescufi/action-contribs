#!/usr/bin/env python3

import argparse
from github import Github, GithubException
import json
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

    if not ("pull_request" in evt_name):
        sys.exit(f'Invalid event {evt_name}')

    with open(evt_path, 'r') as f:
        evt = json.load(f)

    pr = evt['pull_request']
    user = pr['user']
    login = user['login']

    print(f'user: {login} PR: {pr["title"]}')

    gh = Github(token)
    tk_usr = gh.get_user()

    org, repo = gh_tuple_split(repo)

    print(f'token user: {tk_usr.login} org: {org} repo: {repo}')

    gh_org = gh.get_organization(org)
    gh_usr = gh.get_user(login)
    member = gh_org.has_in_members(gh_usr)
    nstr = '' if member else 'NOT '

    print(f'User {login} is {nstr}a member of org {org}')

    if member:
        sys.exit(0)

    # Post a comment if not already there


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
