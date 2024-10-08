# release-to-jira

A GitHub action to automatically create releases on JIRA.

Creates a release on Jira from Github. Uses its auto-generated description in GH release notes to find related JIRA issues and updates their "Fix versions" field on the JIRA server. If a release matching the tag (plus optional prefix) doesn't exist on JIRA, it will be automatically created.

This flow assumes auto-generated release notes will include JIRA issue keys. This can be achieved by including JIRA issue key in PR titles.

## Inputs

|Input|Description|Example|
|---|---|---|
|`jira_server`|JIRA server URL.|`https://company.atlassian.net`|
|`jira_project`|JIRA project key.|`PRJ`|
|`jira_user`|JIRA user with project admin permission.|`apiuser@company.com`|
|`jira_token`|JIRA token. Managed [here](https://id.atlassian.com/manage-profile/security/api-tokens).|`abcdef12345678`|
|`jira_release_prefix`|Optional string to add to the beginning of the github ref (tag) when naming the release in Jira|Convert `'0.1.0'` into `'Foo 0.1.0'`|


## Usage

Run when a new tag is created:

```yaml
on:
  push:
    tags:        
      - '*'
jobs:
  jira-release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: Medsien/release-to-jira@main
        with:
          jira_server: 'https://company.atlassian.net'
          jira_project: 'PRJ'
          jira_user: 'user@company.com'
          jira_token: '${{ secrets.JIRA_TOKEN }}'
          jira_release_prefix: 'Foo '
```
