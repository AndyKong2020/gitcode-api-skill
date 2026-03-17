# Get Protection Branch Rules List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-protect-branches](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-protect-branches)
Category: Branch
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/protect_branches`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_protect_branches`
- Tags: `Branch`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
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
      "committer_can_merge": {
        "type": "integer"
      },
      "committer_can_push": {
        "type": "integer"
      },
      "developers_can_merge": {
        "type": "integer"
      },
      "developers_can_push": {
        "type": "integer"
      },
      "maintainer_can_merge": {
        "type": "integer"
      },
      "maintainer_can_push": {
        "type": "integer"
      },
      "master_can_merge": {
        "type": "integer"
      },
      "master_can_push": {
        "type": "integer"
      },
      "merge_users": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "merged": {
        "type": "integer"
      },
      "name": {
        "type": "string"
      },
      "no_one_can_merge": {
        "type": "integer"
      },
      "no_one_can_push": {
        "type": "integer"
      },
      "owner_can_merge": {
        "type": "integer"
      },
      "owner_can_push": {
        "type": "integer"
      },
      "push_users": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "updated_at": {
        "type": "string"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "committer_can_merge": false,
      "committer_can_push": false,
      "developers_can_merge": false,
      "developers_can_push": false,
      "maintainer_can_merge": true,
      "maintainer_can_push": true,
      "master_can_merge": true,
      "master_can_push": true,
      "merge_users": [],
      "merged": false,
      "name": "main",
      "no_one_can_merge": false,
      "no_one_can_push": false,
      "owner_can_merge": true,
      "owner_can_push": true,
      "push_users": [],
      "updated_at": "2024-09-18T10:15:48.471+08:00"
    }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_protect_branches",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/protect_branches",
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
    "name": "Get Protection Branch Rules List",
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
        "protect_branches"
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "committer_can_merge": false,
                "committer_can_push": false,
                "developers_can_merge": false,
                "developers_can_push": false,
                "maintainer_can_merge": true,
                "maintainer_can_push": true,
                "master_can_merge": true,
                "master_can_push": true,
                "merge_users": [],
                "merged": false,
                "name": "main",
                "no_one_can_merge": false,
                "no_one_can_push": false,
                "owner_can_merge": true,
                "owner_can_push": true,
                "push_users": [],
                "updated_at": "2024-09-18T10:15:48.471+08:00"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "committer_can_merge": {
                  "type": "integer"
                },
                "committer_can_push": {
                  "type": "integer"
                },
                "developers_can_merge": {
                  "type": "integer"
                },
                "developers_can_push": {
                  "type": "integer"
                },
                "maintainer_can_merge": {
                  "type": "integer"
                },
                "maintainer_can_push": {
                  "type": "integer"
                },
                "master_can_merge": {
                  "type": "integer"
                },
                "master_can_push": {
                  "type": "integer"
                },
                "merge_users": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "merged": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "no_one_can_merge": {
                  "type": "integer"
                },
                "no_one_can_push": {
                  "type": "integer"
                },
                "owner_can_merge": {
                  "type": "integer"
                },
                "owner_can_push": {
                  "type": "integer"
                },
                "push_users": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "updated_at": {
                  "type": "string"
                }
              },
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
    "Branch"
  ]
}
```
