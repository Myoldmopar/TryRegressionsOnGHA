with open('build/summary.md') as md:
    md_contents = md.read()

with open('build/summary.js', 'w') as js:
    js_contents = f"""
module.exports = ({{github, context}}) => {{    
    github.rest.issues.createComment({{
        issue_number: context.issue.number,
        owner: context.repo.owner,
        repo: context.repo.repo,
        body: `{md_contents}`
    }})
}}
"""
    js.write(js_contents)


# body: "### :warning: Regressions detected on ${{ matrix.os }} for commit ${{ github.sha }}\n\n ${{ env.R_STUFF }}\n\n - [View Results](https://github.com/NREL/EnergyPlus/actions/runs/${{ github.run_id }})\n - [Download Regressions](${{ steps.upload_regressions.outputs.artifact-url }})"