from os import makedirs
from sys import argv, exit

makedirs('build/regressions', exist_ok=True)
with open('build/regressions/index.html', 'w') as f:
    f.write('<html><h4>Hello, world</h4></html>')

if argv[1] == 'macos-14':
    with open('build/summary.md', 'w') as md:
        contents = f"""
<details>
  <summary>Regressions in {argv[1]}</summary>

  - 8 ESO Diffs
  - 9 Table Small Diffs
  - 1 JSON Diffs
</details>"""
        md.write(contents)
    print("Regressions encountered!  They will be uploaded as an artifact on GitHub Actions")
    exit(1)

print("No regressions found, great!")
