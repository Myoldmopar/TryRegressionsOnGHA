with open('build/summary.md') as md:
    md_contents = md.read()

with open('build/summary.js', 'w') as js:
    js_contents = f"""
await github.rest.issues.createComment({{
  issue_number: context.issue.number,
  owner: context.repo.owner,
  repo: context.repo.repo,
  body: "{md_contents}"
}})        
"""
    js.write(js_contents)
