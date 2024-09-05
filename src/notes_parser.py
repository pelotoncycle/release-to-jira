import os
import re
import json

PROJECT = os.environ["INPUT_JIRA_PROJECT"]
ISSUE_PATTERN = rf"{PROJECT}-[0-9]+"
CHANGES_SECTION = "What's Changed"


def _get_section(md_content, section_title):
    return md_content.split(f"## {section_title}\r\n", 1)[1].split("\r\n\r\n", 1)[0]


def _parse_changelist(content):
    items = []
    for line in content.split("\n"):
        line = line[2:]
        try:
            pr_title, line = line.split(" by @", 1)
            author, pr_link = line.split(" in ", 1)
            items.append(
                {
                    "title": pr_title,
                    "author": author,
                    "link": pr_link,
                }
            )
        except Exception as ex:
            print('skipped', line, ex)
    return items


def extract_changes(content):
    try:
        notes = content['body']
        if CHANGES_SECTION not in notes:
            return []
    except KeyError:
        return []

    return _parse_changelist(_get_section(notes, CHANGES_SECTION))


def extract_issue_id(change):
    matches = re.findall(ISSUE_PATTERN, change)
    if not matches:
        return None
    return matches[0]
