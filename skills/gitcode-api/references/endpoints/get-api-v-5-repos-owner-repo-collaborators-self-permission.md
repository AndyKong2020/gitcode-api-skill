# Check the permission points of the current member repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators-self-permission](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators-self-permission)
Category: Member
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/collaborators/self-permission`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_collaborators_self-permission`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | false | string | User authorization code |
## Request Body
No request body.
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "resource_trees": {
      "description": "User Permission Matrix Tree",
      "items": {
        "properties": {
          "actions": {
            "description": "Permission Point",
            "items": {
              "properties": {
                "action": {
                  "description": "Permission Point",
                  "type": "string"
                },
                "cn_name": {
                  "description": "Permission Point Chinese Name",
                  "type": "string"
                },
                "name": {
                  "description": "Permission Point Name",
                  "type": "string"
                },
                "permission_id": {
                  "description": "Permission point ID",
                  "type": "integer"
                },
                "selected": {
                  "description": "Does it have",
                  "type": "boolean"
                }
              },
              "required": [
                "permission_id",
                "action",
                "name",
                "cn_name",
                "selected"
              ],
              "type": "object"
            },
            "type": "array"
          },
          "cn_name": {
            "description": "Resource Chinese Name",
            "type": "string"
          },
          "is_own": {
            "type": "integer"
          },
          "name": {
            "description": "Resource Name",
            "type": "string"
          },
          "order_num": {
            "description": "Sort Field",
            "type": "integer"
          },
          "path": {
            "description": "Permission Path",
            "type": "string"
          },
          "resource_id": {
            "description": "Resource ID",
            "type": "integer"
          },
          "scope": {
            "description": "Resource Identifier",
            "type": "string"
          }
        },
        "required": [
          "resource_id",
          "name",
          "cn_name",
          "scope",
          "actions",
          "path",
          "is_own",
          "order_num"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "role_info": {
      "description": "User Role",
      "properties": {
        "access_level": {
          "description": "Role Level",
          "type": "integer"
        },
        "cn_name": {
          "description": "Role Chinese Name",
          "type": "string"
        },
        "name": {
          "description": "Character Name",
          "type": "string"
        },
        "role_uuid": {
          "description": "Role ID",
          "type": "string"
        },
        "roles_type": {
          "description": "Role Type",
          "type": "integer"
        }
      },
      "required": [
        "role_uuid",
        "name",
        "cn_name",
        "roles_type",
        "access_level"
      ],
      "type": "object"
    }
  },
  "required": [
    "role_info",
    "resource_trees"
  ],
  "type": "object"
}
```
Example:
```json
{
  "resource_trees": [
    {
      "actions": [
        {
          "action": "fork",
          "cn_name": "fork",
          "name": "fork",
          "permission_id": 5,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 6,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 7,
          "selected": true
        },
        {
          "action": "setting",
          "cn_name": "Set",
          "name": "setting",
          "permission_id": 8,
          "selected": true
        },
        {
          "action": "archive",
          "cn_name": "Archive",
          "name": "archive",
          "permission_id": 9,
          "selected": true
        },
        {
          "action": "transfer",
          "cn_name": "Transfer",
          "name": "transfer",
          "permission_id": 10,
          "selected": true
        }
      ],
      "cn_name": "Project",
      "name": "repo",
      "resource_id": 2,
      "scope": "repo"
    },
    {
      "actions": [
        {
          "action": "push",
          "cn_name": "Push notification",
          "name": "push",
          "permission_id": 14,
          "selected": true
        },
        {
          "action": "download",
          "cn_name": "Download",
          "name": "download",
          "permission_id": 15,
          "selected": true
        }
      ],
      "cn_name": "```code\n```",
      "name": "code",
      "resource_id": 4,
      "scope": "code"
    },
    {
      "actions": [
        {
          "action": "push",
          "cn_name": "Push notification",
          "name": "push",
          "permission_id": 48,
          "selected": true
        },
        {
          "action": "download",
          "cn_name": "Download",
          "name": "download",
          "permission_id": 49,
          "selected": true
        }
      ],
      "cn_name": "Wiki",
      "name": "wiki",
      "resource_id": 14,
      "scope": "wiki"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Invitation",
          "name": "create",
          "permission_id": 16,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 17,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Remove",
          "name": "delete",
          "permission_id": 18,
          "selected": true
        }
      ],
      "cn_name": "member",
      "name": "member",
      "resource_id": 5,
      "scope": "member"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 19,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 20,
          "selected": true
        },
        {
          "action": "reopen",
          "cn_name": "Close/Open",
          "name": "reopen",
          "permission_id": 22,
          "selected": true
        },
        {
          "action": "pin",
          "cn_name": "Sticky",
          "name": "pin",
          "permission_id": 23,
          "selected": true
        },
        {
          "action": "lock",
          "cn_name": "Locking",
          "name": "lock",
          "permission_id": 24,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 11,
          "selected": true
        }
      ],
      "cn_name": "Issue",
      "name": "issue",
      "resource_id": 6,
      "scope": "issue"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 25,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 26,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 27,
          "selected": true
        }
      ],
      "cn_name": "Label",
      "name": "label",
      "resource_id": 7,
      "scope": "label"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 28,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 29,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 30,
          "selected": true
        }
      ],
      "cn_name": "Milestone",
      "name": "milestone",
      "resource_id": 8,
      "scope": "milestone"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 31,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 32,
          "selected": true
        }
      ],
      "cn_name": "Branch",
      "name": "branch",
      "resource_id": 9,
      "scope": "branch"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 33,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 34,
          "selected": true
        }
      ],
      "cn_name": "Tag",
      "name": "tag",
      "resource_id": 10,
      "scope": "tag"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 38,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 39,
          "selected": true
        },
        {
          "action": "review",
          "cn_name": "Review",
          "name": "review",
          "permission_id": 40,
          "selected": true
        },
        {
          "action": "approve",
          "cn_name": "Review",
          "name": "approve",
          "permission_id": 41,
          "selected": true
        },
        {
          "action": "merge",
          "cn_name": "Merge",
          "name": "merge",
          "permission_id": 42,
          "selected": true
        },
        {
          "action": "close",
          "cn_name": "close",
          "name": "close",
          "permission_id": 43,
          "selected": true
        },
        {
          "action": "reopen",
          "cn_name": "Reboot",
          "name": "reopen",
          "permission_id": 44,
          "selected": true
        },
        {
          "action": "test",
          "cn_name": "testing",
          "name": "test",
          "permission_id": 47,
          "selected": true
        }
      ],
      "cn_name": "PullRequest",
      "name": "pr",
      "resource_id": 12,
      "scope": "pr"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 45,
          "selected": true
        },
        {
          "action": "resolve",
          "cn_name": "Resolve",
          "name": "resolve",
          "permission_id": 46,
          "selected": true
        }
      ],
      "cn_name": "Comment",
      "name": "note",
      "resource_id": 13,
      "scope": "note"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Build Record",
          "name": "delete",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "run",
          "cn_name": "Run",
          "name": "run",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "rerun",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts!!! Run again",
          "name": "rerun",
          "permission_id": 0,
          "selected": true
        }
      ],
      "cn_name": "Production line",
      "is_own": 1,
      "name": "pipeline",
      "order_num": 10,
      "path": "/gitcode/repo/pipeline/*",
      "resource_id": 0,
      "scope": "pipeline"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "lock",
          "cn_name": "Locking",
          "name": "lock",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "pin",
          "cn_name": "Sticky",
          "name": "pin",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "close",
          "cn_name": "Close/Open",
          "name": "close",
          "permission_id": 0,
          "selected": true
        }
      ],
      "cn_name": "Discussion",
      "is_own": 1,
      "name": "discussion",
      "order_num": 15,
      "path": "/gitcode/repo/discussion/*",
      "resource_id": 0,
      "scope": "discussion"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "close",
          "cn_name": "Close/Open",
          "name": "close",
          "permission_id": 0,
          "selected": true
        }
      ],
      "cn_name": "Kanban",
      "is_own": 1,
      "name": "kanban",
      "order_num": 16,
      "path": "/gitcode/repo/kanban/*",
      "resource_id": 0,
      "scope": "kanban"
    },
    {
      "actions": [
        {
          "action": "create",
          "cn_name": "Create",
          "name": "create",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "update",
          "cn_name": "Update",
          "name": "update",
          "permission_id": 0,
          "selected": true
        },
        {
          "action": "delete",
          "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
          "name": "delete",
          "permission_id": 0,
          "selected": true
        }
      ],
      "cn_name": "Collection",
      "is_own": 1,
      "name": "collection",
      "order_num": 18,
      "path": "/gitcode/repo/collection/*",
      "resource_id": 0,
      "scope": "collection"
    }
  ],
  "role_info": {
    "access_level": 50,
    "cn_name": "Administrator",
    "name": "Owner",
    "role_uuid": "45a9-276d8e546f1b05f9f98ce1ffdc6",
    "roles_type": 1
  }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_collaborators_self-permission",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
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
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/collaborators/self-permission",
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
    "name": "Check the permission points of the current member repository",
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
        "collaborators",
        "self-permission"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (address path of the enterprise, organization, or individual)",
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
            "resource_trees": [
              {
                "actions": [
                  {
                    "action": "fork",
                    "cn_name": "fork",
                    "name": "fork",
                    "permission_id": 5,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 6,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 7,
                    "selected": true
                  },
                  {
                    "action": "setting",
                    "cn_name": "Set",
                    "name": "setting",
                    "permission_id": 8,
                    "selected": true
                  },
                  {
                    "action": "archive",
                    "cn_name": "Archive",
                    "name": "archive",
                    "permission_id": 9,
                    "selected": true
                  },
                  {
                    "action": "transfer",
                    "cn_name": "Transfer",
                    "name": "transfer",
                    "permission_id": 10,
                    "selected": true
                  }
                ],
                "cn_name": "Project",
                "name": "repo",
                "resource_id": 2,
                "scope": "repo"
              },
              {
                "actions": [
                  {
                    "action": "push",
                    "cn_name": "Push notification",
                    "name": "push",
                    "permission_id": 14,
                    "selected": true
                  },
                  {
                    "action": "download",
                    "cn_name": "Download",
                    "name": "download",
                    "permission_id": 15,
                    "selected": true
                  }
                ],
                "cn_name": "```code\n```",
                "name": "code",
                "resource_id": 4,
                "scope": "code"
              },
              {
                "actions": [
                  {
                    "action": "push",
                    "cn_name": "Push notification",
                    "name": "push",
                    "permission_id": 48,
                    "selected": true
                  },
                  {
                    "action": "download",
                    "cn_name": "Download",
                    "name": "download",
                    "permission_id": 49,
                    "selected": true
                  }
                ],
                "cn_name": "Wiki",
                "name": "wiki",
                "resource_id": 14,
                "scope": "wiki"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Invitation",
                    "name": "create",
                    "permission_id": 16,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 17,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Remove",
                    "name": "delete",
                    "permission_id": 18,
                    "selected": true
                  }
                ],
                "cn_name": "member",
                "name": "member",
                "resource_id": 5,
                "scope": "member"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 19,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 20,
                    "selected": true
                  },
                  {
                    "action": "reopen",
                    "cn_name": "Close/Open",
                    "name": "reopen",
                    "permission_id": 22,
                    "selected": true
                  },
                  {
                    "action": "pin",
                    "cn_name": "Sticky",
                    "name": "pin",
                    "permission_id": 23,
                    "selected": true
                  },
                  {
                    "action": "lock",
                    "cn_name": "Locking",
                    "name": "lock",
                    "permission_id": 24,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 11,
                    "selected": true
                  }
                ],
                "cn_name": "Issue",
                "name": "issue",
                "resource_id": 6,
                "scope": "issue"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 25,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 26,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 27,
                    "selected": true
                  }
                ],
                "cn_name": "Label",
                "name": "label",
                "resource_id": 7,
                "scope": "label"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 28,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 29,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 30,
                    "selected": true
                  }
                ],
                "cn_name": "Milestone",
                "name": "milestone",
                "resource_id": 8,
                "scope": "milestone"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 31,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 32,
                    "selected": true
                  }
                ],
                "cn_name": "Branch",
                "name": "branch",
                "resource_id": 9,
                "scope": "branch"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 33,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 34,
                    "selected": true
                  }
                ],
                "cn_name": "Tag",
                "name": "tag",
                "resource_id": 10,
                "scope": "tag"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 38,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 39,
                    "selected": true
                  },
                  {
                    "action": "review",
                    "cn_name": "Review",
                    "name": "review",
                    "permission_id": 40,
                    "selected": true
                  },
                  {
                    "action": "approve",
                    "cn_name": "Review",
                    "name": "approve",
                    "permission_id": 41,
                    "selected": true
                  },
                  {
                    "action": "merge",
                    "cn_name": "Merge",
                    "name": "merge",
                    "permission_id": 42,
                    "selected": true
                  },
                  {
                    "action": "close",
                    "cn_name": "close",
                    "name": "close",
                    "permission_id": 43,
                    "selected": true
                  },
                  {
                    "action": "reopen",
                    "cn_name": "Reboot",
                    "name": "reopen",
                    "permission_id": 44,
                    "selected": true
                  },
                  {
                    "action": "test",
                    "cn_name": "testing",
                    "name": "test",
                    "permission_id": 47,
                    "selected": true
                  }
                ],
                "cn_name": "PullRequest",
                "name": "pr",
                "resource_id": 12,
                "scope": "pr"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 45,
                    "selected": true
                  },
                  {
                    "action": "resolve",
                    "cn_name": "Resolve",
                    "name": "resolve",
                    "permission_id": 46,
                    "selected": true
                  }
                ],
                "cn_name": "Comment",
                "name": "note",
                "resource_id": 13,
                "scope": "note"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Build Record",
                    "name": "delete",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "run",
                    "cn_name": "Run",
                    "name": "run",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "rerun",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output any other content or prompts!!! Run again",
                    "name": "rerun",
                    "permission_id": 0,
                    "selected": true
                  }
                ],
                "cn_name": "Production line",
                "is_own": 1,
                "name": "pipeline",
                "order_num": 10,
                "path": "/gitcode/repo/pipeline/*",
                "resource_id": 0,
                "scope": "pipeline"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "lock",
                    "cn_name": "Locking",
                    "name": "lock",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "pin",
                    "cn_name": "Sticky",
                    "name": "pin",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "close",
                    "cn_name": "Close/Open",
                    "name": "close",
                    "permission_id": 0,
                    "selected": true
                  }
                ],
                "cn_name": "Discussion",
                "is_own": 1,
                "name": "discussion",
                "order_num": 15,
                "path": "/gitcode/repo/discussion/*",
                "resource_id": 0,
                "scope": "discussion"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "close",
                    "cn_name": "Close/Open",
                    "name": "close",
                    "permission_id": 0,
                    "selected": true
                  }
                ],
                "cn_name": "Kanban",
                "is_own": 1,
                "name": "kanban",
                "order_num": 16,
                "path": "/gitcode/repo/kanban/*",
                "resource_id": 0,
                "scope": "kanban"
              },
              {
                "actions": [
                  {
                    "action": "create",
                    "cn_name": "Create",
                    "name": "create",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "update",
                    "cn_name": "Update",
                    "name": "update",
                    "permission_id": 0,
                    "selected": true
                  },
                  {
                    "action": "delete",
                    "cn_name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Delete",
                    "name": "delete",
                    "permission_id": 0,
                    "selected": true
                  }
                ],
                "cn_name": "Collection",
                "is_own": 1,
                "name": "collection",
                "order_num": 18,
                "path": "/gitcode/repo/collection/*",
                "resource_id": 0,
                "scope": "collection"
              }
            ],
            "role_info": {
              "access_level": 50,
              "cn_name": "Administrator",
              "name": "Owner",
              "role_uuid": "45a9-276d8e546f1b05f9f98ce1ffdc6",
              "roles_type": 1
            }
          },
          "schema": {
            "properties": {
              "resource_trees": {
                "description": "User Permission Matrix Tree",
                "items": {
                  "properties": {
                    "actions": {
                      "description": "Permission Point",
                      "items": {
                        "properties": {
                          "action": {
                            "description": "Permission Point",
                            "type": "string"
                          },
                          "cn_name": {
                            "description": "Permission Point Chinese Name",
                            "type": "string"
                          },
                          "name": {
                            "description": "Permission Point Name",
                            "type": "string"
                          },
                          "permission_id": {
                            "description": "Permission point ID",
                            "type": "integer"
                          },
                          "selected": {
                            "description": "Does it have",
                            "type": "boolean"
                          }
                        },
                        "required": [
                          "permission_id",
                          "action",
                          "name",
                          "cn_name",
                          "selected"
                        ],
                        "type": "object"
                      },
                      "type": "array"
                    },
                    "cn_name": {
                      "description": "Resource Chinese Name",
                      "type": "string"
                    },
                    "is_own": {
                      "type": "integer"
                    },
                    "name": {
                      "description": "Resource Name",
                      "type": "string"
                    },
                    "order_num": {
                      "description": "Sort Field",
                      "type": "integer"
                    },
                    "path": {
                      "description": "Permission Path",
                      "type": "string"
                    },
                    "resource_id": {
                      "description": "Resource ID",
                      "type": "integer"
                    },
                    "scope": {
                      "description": "Resource Identifier",
                      "type": "string"
                    }
                  },
                  "required": [
                    "resource_id",
                    "name",
                    "cn_name",
                    "scope",
                    "actions",
                    "path",
                    "is_own",
                    "order_num"
                  ],
                  "type": "object"
                },
                "type": "array"
              },
              "role_info": {
                "description": "User Role",
                "properties": {
                  "access_level": {
                    "description": "Role Level",
                    "type": "integer"
                  },
                  "cn_name": {
                    "description": "Role Chinese Name",
                    "type": "string"
                  },
                  "name": {
                    "description": "Character Name",
                    "type": "string"
                  },
                  "role_uuid": {
                    "description": "Role ID",
                    "type": "string"
                  },
                  "roles_type": {
                    "description": "Role Type",
                    "type": "integer"
                  }
                },
                "required": [
                  "role_uuid",
                  "name",
                  "cn_name",
                  "roles_type",
                  "access_level"
                ],
                "type": "object"
              }
            },
            "required": [
              "role_info",
              "resource_trees"
            ],
            "type": "object"
          }
        }
      },
      "description": "",
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
  "tags": []
}
```
