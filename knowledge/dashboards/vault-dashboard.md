---
title: "Vault Dashboard"
type: dashboard
status: active
topic: [vault, dataview]
source: []
created: 2026-04-19
updated: 2026-04-27
confidence: medium
review_after:
tags: [dashboard, dataview]
---

# Vault Dashboard

## Entry Points

- [[AGENTS]]
- [[PROJECT]]
- [[memory/l1-triggers|L1 Triggers]]
- [[tasks/active/2026-04-18-vault-bootstrap|Vault Bootstrap]]
- [[tasks/handoff/2026-04-18-vault-bootstrap-handoff|Vault Bootstrap Handoff]]

## Active Tasks

```dataview
TABLE status, updated, topic
FROM "tasks/active"
SORT updated DESC
```

## Recent Task Records

```dataview
TABLE status, updated, topic
FROM "tasks"
WHERE type = "task"
SORT updated DESC
LIMIT 10
```

## Decisions

```dataview
TABLE status, updated, topic, confidence
FROM "knowledge/decisions"
SORT updated DESC
```

## Knowledge

```dataview
TABLE status, updated, topic, confidence
FROM "knowledge"
WHERE type != "dashboard"
SORT updated DESC
LIMIT 20
```

## Sources

```dataview
TABLE status, updated, topic, confidence, review_after
FROM "sources"
SORT updated DESC
```

## Inbox

```dataview
TABLE status, updated, topic, confidence
FROM "inbox"
SORT updated DESC
```

## Memory

```dataview
TABLE status, updated, topic
FROM "memory"
SORT updated DESC
```

## Templates

```dataview
LIST
FROM "templates"
SORT file.name ASC
```

## Review After

```dataview
TABLE review_after, status, topic
FROM ""
WHERE review_after
SORT review_after ASC
```
