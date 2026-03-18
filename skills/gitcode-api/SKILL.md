---
name: gitcode-api
description: Use the official GitCode REST API documentation to inspect endpoints, plan GitCode automations, and perform GitCode operations across repositories, issues, pull requests, orgs, members, webhooks, releases, enterprise features, OAuth, and AI Hub.
---

# GitCode API

Use this skill when the user wants to interact with GitCode through the official API, build GitCode integrations, or script GitCode operations instead of using the web UI.

## Workflow

1. Identify the target resource and action.
2. Search [`references/endpoint-catalog.json`](references/endpoint-catalog.json) with `rg` to find the exact endpoint by title, method, path, or category.
3. Open the matching file under [`references/endpoints/`](references/endpoints) for the exact request/response schema and examples.
4. Before mutating files, confirm whether the target path already exists. For repository contents, use `GET /api/v5/repos/{owner}/{repo}/contents/{path}` first; create missing files with `POST .../contents/{path}` and update existing files with `PUT .../contents/{path}`.
5. Execute the API call with [`scripts/gitcode_api.py`](scripts/gitcode_api.py) unless the user explicitly wants raw curl or code only.
6. Report the exact method, path, auth mode, request payload, and the API result. Do not hide non-2xx responses.

## Authentication

GitCode API docs state that authentication can be passed in any of these forms:
- `Authorization: Bearer <token>`
- `PRIVATE-TOKEN: <token>`
- `access_token=<token>` query parameter

Default to the `Authorization` header when you control the client. If the endpoint documentation or the user's existing integration uses another mode, match that mode.

`scripts/gitcode_api.py` reads the token from `GITCODE_TOKEN` by default, or from `--token`.

## Conventions

- Base URL: `https://api.gitcode.com`
- Most REST endpoints are under `/api/v5`
- The docs home page states rate limits of `50/min` and `4000/hour`
- Prefer exact values from endpoint reference files over assumptions
- Enterprise-only fields and endpoints are marked in the endpoint docs; do not assume availability on non-enterprise instances
- Creating a repository with `auto_init=true` creates an initial commit and a default `README.md`
- Some endpoints use `application/x-www-form-urlencoded`; use `scripts/gitcode_api.py --form KEY=VALUE` for those requests
- Protected-branch workflows appear to distinguish between creating a rule and updating an existing rule; do not assume `PUT /branches/{wildcard}/setting` creates the rule if none exists
- Real API responses may differ slightly from docs examples; check [`references/tested-behaviors.md`](references/tested-behaviors.md) for verified behavior notes

## References

- [`references/auth-and-conventions.md`](references/auth-and-conventions.md): auth methods, status codes, and shared API rules from the docs introduction
- [`references/category-index.md`](references/category-index.md): sidebar categories and page list
- [`references/endpoint-catalog.json`](references/endpoint-catalog.json): machine-readable index of all API docs pages
- [`references/tested-behaviors.md`](references/tested-behaviors.md): behavior verified against the live GitCode API during smoke testing
- [`references/endpoints/`](references/endpoints): one Markdown file per API docs page

## Common commands

Search endpoints:

```bash
rg -n "Create Issue|/api/v5/repos/\{owner\}/issues|Issues" references/endpoint-catalog.json
```

Dry-run a request:

```bash
python scripts/gitcode_api.py request POST /api/v5/repos/{owner}/issues           --path owner=my-org           --json '{"repo":"my-repo","title":"Bug","body":"Details"}'           --dry-run
```

Execute the same request with bearer auth from `GITCODE_TOKEN`:

```bash
python scripts/gitcode_api.py request POST /api/v5/repos/{owner}/issues           --path owner=my-org           --json '{"repo":"my-repo","title":"Bug","body":"Details"}'
```
