# pdoc-test

## Build Setup

### Travis

Define the following environment variables:

- `PYPI_REPO`: URL to the repository, does not have to be a protected variable, e.g. `https://eu.artifactory.swg-devops.com/artifactory/api/pypi/sys-zaas-devops-taskforce-team-test-dev-pypi-virtual`
- `PYPI_USERNAME`: Username, should be protected, e.g. your IBM intranet URL
- `PYPI_PASSWORD`: Password, must be protected, e.g. your artifactory API token

### Git Workflow

Pushing to git will trigger a new build but not a new deployment. In order to deploy first update the version number using the [bumpversion](https://pypi.org/project/bump2version/) workflow, e.g. 

```bash
bumpversion patch
```

Then execute a tagged commit:

```bash
git push --tags
```

