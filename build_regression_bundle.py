from os import makedirs

makedirs('build/regressions', exist_ok=True)
with open('build/regressions/index.html', 'w') as f:
    f.write('<html><h4>Hello, world</h4></html>')

