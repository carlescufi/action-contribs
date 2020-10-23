#!/usr/bin/env python3

import os
import sys

def main():
    token = os.environ.get('GITHUB_TOKEN', None)
    if not token:
        sys.exit('Github token not set in environment, please set the'
                 'GITHUB_TOKEN environment variable and retry.')

    #gh = Github(token)
    #args = parse_args(sys.argv[1:], gh)

    print('Output from Python')
    print(f'token: {token}')
    sys.exit(0)

if __name__ == '__main__':
    main()
