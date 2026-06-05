-- Active tasks
SELECT path, title, updated
FROM notes
WHERE path LIKE 'tasks/active/%'
ORDER BY updated DESC;

-- Decisions
SELECT path, title, updated, confidence
FROM notes
WHERE path LIKE 'knowledge/decisions/%'
ORDER BY updated DESC;

-- Review targets
SELECT path, title, review_after
FROM notes
WHERE review_after IS NOT NULL
  AND review_after != ''
ORDER BY review_after ASC;

-- Keyword search
SELECT n.path, n.title
FROM notes_fts f
JOIN notes n ON n.path = f.path
WHERE notes_fts MATCH 'Dataview';

