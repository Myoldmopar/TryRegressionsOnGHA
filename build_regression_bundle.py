from os import makedirs

makedirs('regressions', exist_ok=True)
with open('regressions/index.html', 'w') as f:
    f.write('<html><h4>Hello, world</h4></html>')

