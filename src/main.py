import os
import json
from pprint import pprint

from jira_api import add_release_to_issue, get_or_create_release
from notes_parser import extract_changes, extract_issue_id

release_name_prefix = os.environ["RELEASE_NAME_PREFIX"]

# Read all the content from the release
with open("notes.json", "r") as f:
    content = json.load(f)

release = get_or_create_release(content, release_name_prefix)
print("JIRA Release:")
pprint(release)

changes = extract_changes(content)
print("Release Issues:")
pprint(changes)

for change in changes:
    issue_id = extract_issue_id(change["title"])
    if not issue_id:
        print("No issue id:", change["title"])
        continue
    print("Updating", issue_id)
    add_release_to_issue(release['name'], issue_id)
