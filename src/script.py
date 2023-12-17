import sys
import os

if len(sys.argv) >= 2:
    lowercase=sys.argv[1].lower()
    uppercase=sys.argv[1].upper()
    capitalized=f'{uppercase[:1]}{lowercase[1:]}'
    dashnormalized=''.join(x if x.isalnum() else '-' for x in lowercase)

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'lowercase={lowercase}', file=fh)
        print(f'uppercase={uppercase}', file=fh)
        print(f'capitalized={capitalized}', file=fh)
        print(f'dashnormalized={dashnormalized}', file=fh)
