from os import makedirs
from sys import argv, exit

makedirs('build/regressions', exist_ok=True)
with open('build/regressions/index.html', 'w') as f:
    f.write('<html><h4>Hello, world</h4></html>')

if argv[1] == 'macos-14':
    print("Regressions encountered!  They will be uploaded as an artifact on GitHub Actions")
    exit(1)
