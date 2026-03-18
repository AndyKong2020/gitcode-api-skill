# Get Project Pull Request List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Optional. Pull Request status: all, open, closed, locked, merged. Default: all |
| base | query | false | string | Optional. The name of the target branch for the Pull Request submission. |
| since | query | false | string | Optional. The start updated time, with the time format required to be ISO 8601, e.g., `2024-11-20T13:00:21+08:00`. |
| direction | query | false | string | Optional. Ascending or descending. Default: desc (asc or desc) |
| sort | query | false | string | Optional. Sort field: created, updated Default: created |
| milestone_number | query | false | integer | Optional. Milestone sequence number (id) |
| labels | query | false | string | A list of tag names separated by commas |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| author | query | false | string | Optional. Username of the PR creator |
| assignee | query | false | string | Optional. PR负责人用户名 |
| reviewer | query | false | string | Optional. PR reviewer username |
| merged_after | query | false | string | Returns merged merge requests after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00` |
| merged_before | query | false | string | Returns merged merge requests before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00` |
| only_count | query | false | boolean | If true, returns only the count of merge requests; the default is false. |
| created_after | query | false | string | Returns merge requests created after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00` |
| created_before | query | false | string | Returns merge requests created before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00` |
| updated_before | query | false | string | Returns merge requests updated before the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00` |
| updated_after | query | false | string | Returns merge requests updated after the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00` |
## Request Body
No request body.
## Responses
### `200`
Successful Response
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "items": {
    "properties": {
      "added_lines": {
        "type": "integer"
      },
      "assignees": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "assignees_number": {
        "type": "integer"
      },
      "base": {
        "properties": {
          "label": {
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "internal": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "full_path",
              "full_name",
              "human_name",
              "name",
              "path",
              "description",
              "owner",
              "assigner",
              "internal",
              "html_url"
            ],
            "type": "object"
          },
          "sha": {
            "type": "string"
          },
          "user": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "login",
              "name",
              "state",
              "avatar_url",
              "email",
              "name_cn",
              "html_url"
            ],
            "type": "object"
          }
        },
        "required": [
          "label",
          "ref",
          "sha",
          "user",
          "repo"
        ],
        "type": "object"
      },
      "body": {
        "type": "string"
      },
      "can_merge_check": {
        "type": "boolean"
      },
      "close_related_issue": {
        "type": "integer"
      },
      "closed_at": {
        "type": "string"
      },
      "closed_by": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "iam_id": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "nick_name": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "username": {
            "type": "string"
          },
          "web_url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "username",
          "iam_id",
          "nick_name",
          "state",
          "avatar_url",
          "email",
          "name_cn",
          "web_url"
        ],
        "type": "object"
      },
      "created_at": {
        "type": "string"
      },
      "diff_refs": {
        "properties": {
          "base_sha": {
            "type": "string"
          },
          "head_sha": {
            "type": "string"
          },
          "start_sha": {
            "type": "string"
          }
        },
        "required": [
          "base_sha",
          "head_sha",
          "start_sha"
        ],
        "type": "object"
      },
      "draft": {
        "type": "boolean"
      },
      "force_remove_source_branch": {
        "type": "boolean"
      },
      "head": {
        "properties": {
          "label": {
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "internal": {
                "type": "boolean"
              },
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "login",
                  "name",
                  "state",
                  "avatar_url",
                  "email",
                  "name_cn",
                  "html_url"
                ],
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "full_path",
              "full_name",
              "human_name",
              "name",
              "path",
              "description",
              "owner",
              "assigner",
              "internal",
              "html_url"
            ],
            "type": "object"
          },
          "sha": {
            "type": "string"
          },
          "user": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "login",
              "name",
              "state",
              "avatar_url",
              "email",
              "name_cn",
              "html_url"
            ],
            "type": "object"
          }
        },
        "required": [
          "label",
          "ref",
          "sha",
          "user",
          "repo"
        ],
        "type": "object"
      },
      "html_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "iid": {
        "type": "integer"
      },
      "labels": {
        "items": {
          "properties": {
            "color": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "repository_id": {
              "type": "integer"
            },
            "title": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "color",
            "name",
            "title",
            "repository_id"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "locked": {
        "type": "boolean"
      },
      "merge_request_type": {
        "type": "string"
      },
      "mergeable": {
        "type": "boolean"
      },
      "merged_at": {
        "type": "string"
      },
      "merged_by": {
        "description": "Merged Person",
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "login",
          "name",
          "avatar_url",
          "html_url"
        ],
        "type": "object"
      },
      "notes": {
        "type": "integer"
      },
      "number": {
        "type": "integer"
      },
      "pipeline_status": {
        "type": "string"
      },
      "pipeline_status_with_code_quality": {
        "type": "string"
      },
      "project_id": {
        "type": "integer"
      },
      "prune_branch": {
        "type": "boolean"
      },
      "removed_lines": {
        "type": "integer"
      },
      "review_mode": {
        "type": "string"
      },
      "source_branch": {
        "type": "string"
      },
      "source_git_url": {
        "type": "string"
      },
      "source_project_id": {
        "type": "integer"
      },
      "state": {
        "type": "string"
      },
      "target_branch": {
        "type": "string"
      },
      "testers": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "testers_number": {
        "type": "integer"
      },
      "title": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "user": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "object_id": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "user_id": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "user_id",
          "object_id",
          "login",
          "name",
          "state",
          "avatar_url",
          "email",
          "name_cn",
          "html_url"
        ],
        "type": "object"
      },
      "visibility_reason": {
        "description": "Visibility, public: Publicly visible, other: Visible to project members only",
        "type": "string"
      },
      "web_url": {
        "type": "string"
      }
    },
    "required": [
      "number",
      "html_url",
      "url",
      "close_related_issue",
      "prune_branch",
      "draft",
      "labels",
      "user",
      "assignees",
      "testers",
      "head",
      "base",
      "id",
      "iid",
      "project_id",
      "title",
      "state",
      "assignees_number",
      "testers_number",
      "created_at",
      "updated_at",
      "merged_at",
      "closed_at",
      "target_branch",
      "source_branch",
      "source_project_id",
      "force_remove_source_branch",
      "web_url",
      "merge_request_type",
      "review_mode",
      "added_lines",
      "removed_lines",
      "diff_refs",
      "notes",
      "pipeline_status",
      "pipeline_status_with_code_quality",
      "source_git_url",
      "can_merge_check",
      "mergeable",
      "locked",
      "closed_by",
      "body",
      "visibility_reason"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "all": 1,
  "closed": 0,
  "locked": 0,
  "merged": 0,
  "opened": 1
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "method": "get",
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "example": "",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. Pull Request status: all, open, closed, locked, merged. Default: all",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. The name of the target branch for the Pull Request submission.",
      "in": "query",
      "name": "base",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. The start updated time, with the time format required to be ISO 8601, e.g., `2024-11-20T13:00:21+08:00`.",
      "in": "query",
      "name": "since",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. Ascending or descending. Default: desc (asc or desc)",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. Sort field: created, updated Default: created",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. Milestone sequence number (id)",
      "in": "query",
      "name": "milestone_number",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "A list of tag names separated by commas",
      "in": "query",
      "name": "labels",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Current page number: defaults to 1",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Optional. Username of the PR creator",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. PR负责人用户名",
      "in": "query",
      "name": "assignee",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Optional. PR reviewer username",
      "in": "query",
      "name": "reviewer",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns merged merge requests after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "merged_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns merged merge requests before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "merged_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "If true, returns only the count of merge requests; the default is false.",
      "in": "query",
      "name": "only_count",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    },
    {
      "description": "Returns merge requests created after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "created_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns merge requests created before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns merge requests updated before the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "updated_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns merge requests updated after the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00`",
      "in": "query",
      "name": "updated_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "GET",
    "name": "Get Project Pull Request List",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo",
        "pulls"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Pull Request status: all, open, closed, locked, merged. Default: all",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. The name of the target branch for the Pull Request submission.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "base",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. The start updated time, with the time format required to be ISO 8601, e.g., `2024-11-20T13:00:21+08:00`.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Ascending or descending. Default: desc (asc or desc)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Sort field: created, updated Default: created",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Milestone sequence number (id)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "milestone_number",
          "value": ""
        },
        {
          "description": {
            "content": "A list of tag names separated by commas",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "labels",
          "value": ""
        },
        {
          "description": {
            "content": "Current page number: defaults to 1",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Username of the PR creator",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. PR负责人用户名",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "assignee",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. PR reviewer username",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "reviewer",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merged merge requests after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "merged_after",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merged merge requests before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "merged_before",
          "value": ""
        },
        {
          "description": {
            "content": "If true, returns only the count of merge requests; the default is false.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "only_count",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merge requests created after the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_after",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merge requests created before the specified time, with the time format required to be in ISO 8601, for example: `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merge requests updated before the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_before",
          "value": ""
        },
        {
          "description": {
            "content": "Returns merge requests updated after the specified time, with the time format required to be in ISO 8601, e.g., `2024-11-20T13:00:21+08:00`",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_after",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (organization or individual's address path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Repository path (path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "all": 1,
            "closed": 0,
            "locked": 0,
            "merged": 0,
            "opened": 1
          },
          "schema": {
            "items": {
              "properties": {
                "added_lines": {
                  "type": "integer"
                },
                "assignees": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "assignees_number": {
                  "type": "integer"
                },
                "base": {
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "html_url": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "login": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "human_name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "internal": {
                          "type": "boolean"
                        },
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "html_url": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "login": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "full_path",
                        "full_name",
                        "human_name",
                        "name",
                        "path",
                        "description",
                        "owner",
                        "assigner",
                        "internal",
                        "html_url"
                      ],
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "user": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "email": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "login",
                        "name",
                        "state",
                        "avatar_url",
                        "email",
                        "name_cn",
                        "html_url"
                      ],
                      "type": "object"
                    }
                  },
                  "required": [
                    "label",
                    "ref",
                    "sha",
                    "user",
                    "repo"
                  ],
                  "type": "object"
                },
                "body": {
                  "type": "string"
                },
                "can_merge_check": {
                  "type": "boolean"
                },
                "close_related_issue": {
                  "type": "integer"
                },
                "closed_at": {
                  "type": "string"
                },
                "closed_by": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    },
                    "iam_id": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "nick_name": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    },
                    "username": {
                      "type": "string"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "name",
                    "username",
                    "iam_id",
                    "nick_name",
                    "state",
                    "avatar_url",
                    "email",
                    "name_cn",
                    "web_url"
                  ],
                  "type": "object"
                },
                "created_at": {
                  "type": "string"
                },
                "diff_refs": {
                  "properties": {
                    "base_sha": {
                      "type": "string"
                    },
                    "head_sha": {
                      "type": "string"
                    },
                    "start_sha": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "base_sha",
                    "head_sha",
                    "start_sha"
                  ],
                  "type": "object"
                },
                "draft": {
                  "type": "boolean"
                },
                "force_remove_source_branch": {
                  "type": "boolean"
                },
                "head": {
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "html_url": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "login": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "human_name": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "internal": {
                          "type": "boolean"
                        },
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "avatar_url": {
                              "type": "string"
                            },
                            "email": {
                              "type": "string"
                            },
                            "html_url": {
                              "type": "string"
                            },
                            "id": {
                              "type": "string"
                            },
                            "login": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "required": [
                            "id",
                            "login",
                            "name",
                            "state",
                            "avatar_url",
                            "email",
                            "name_cn",
                            "html_url"
                          ],
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "full_path",
                        "full_name",
                        "human_name",
                        "name",
                        "path",
                        "description",
                        "owner",
                        "assigner",
                        "internal",
                        "html_url"
                      ],
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "user": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
                        },
                        "email": {
                          "type": "string"
                        },
                        "html_url": {
                          "type": "string"
                        },
                        "id": {
                          "type": "string"
                        },
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "login",
                        "name",
                        "state",
                        "avatar_url",
                        "email",
                        "name_cn",
                        "html_url"
                      ],
                      "type": "object"
                    }
                  },
                  "required": [
                    "label",
                    "ref",
                    "sha",
                    "user",
                    "repo"
                  ],
                  "type": "object"
                },
                "html_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "iid": {
                  "type": "integer"
                },
                "labels": {
                  "items": {
                    "properties": {
                      "color": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      },
                      "repository_id": {
                        "type": "integer"
                      },
                      "title": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "color",
                      "name",
                      "title",
                      "repository_id"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "locked": {
                  "type": "boolean"
                },
                "merge_request_type": {
                  "type": "string"
                },
                "mergeable": {
                  "type": "boolean"
                },
                "merged_at": {
                  "type": "string"
                },
                "merged_by": {
                  "description": "Merged Person",
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "login",
                    "name",
                    "avatar_url",
                    "html_url"
                  ],
                  "type": "object"
                },
                "notes": {
                  "type": "integer"
                },
                "number": {
                  "type": "integer"
                },
                "pipeline_status": {
                  "type": "string"
                },
                "pipeline_status_with_code_quality": {
                  "type": "string"
                },
                "project_id": {
                  "type": "integer"
                },
                "prune_branch": {
                  "type": "boolean"
                },
                "removed_lines": {
                  "type": "integer"
                },
                "review_mode": {
                  "type": "string"
                },
                "source_branch": {
                  "type": "string"
                },
                "source_git_url": {
                  "type": "string"
                },
                "source_project_id": {
                  "type": "integer"
                },
                "state": {
                  "type": "string"
                },
                "target_branch": {
                  "type": "string"
                },
                "testers": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "testers_number": {
                  "type": "integer"
                },
                "title": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    },
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "object_id": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    },
                    "user_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "user_id",
                    "object_id",
                    "login",
                    "name",
                    "state",
                    "avatar_url",
                    "email",
                    "name_cn",
                    "html_url"
                  ],
                  "type": "object"
                },
                "visibility_reason": {
                  "description": "Visibility, public: Publicly visible, other: Visible to project members only",
                  "type": "string"
                },
                "web_url": {
                  "type": "string"
                }
              },
              "required": [
                "number",
                "html_url",
                "url",
                "close_related_issue",
                "prune_branch",
                "draft",
                "labels",
                "user",
                "assignees",
                "testers",
                "head",
                "base",
                "id",
                "iid",
                "project_id",
                "title",
                "state",
                "assignees_number",
                "testers_number",
                "created_at",
                "updated_at",
                "merged_at",
                "closed_at",
                "target_branch",
                "source_branch",
                "source_project_id",
                "force_remove_source_branch",
                "web_url",
                "merge_request_type",
                "review_mode",
                "added_lines",
                "removed_lines",
                "diff_refs",
                "notes",
                "pipeline_status",
                "pipeline_status_with_code_quality",
                "source_git_url",
                "can_merge_check",
                "mergeable",
                "locked",
                "closed_by",
                "body",
                "visibility_reason"
              ],
              "type": "object"
            },
            "type": "array"
          }
        }
      },
      "description": "Successful Response",
      "headers": {}
    }
  },
  "security": [],
  "securitySchemes": {},
  "servers": [
    {
      "description": "正式环境",
      "url": "https://api.gitcode.com"
    }
  ],
  "tags": [
    "Pull Requests"
  ]
}
```
