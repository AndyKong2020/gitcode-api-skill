# Get Repository Settings
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-repo-settings](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-repo-settings)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/repo_settings`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_repo_settings`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
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
  "properties": {
    "disable_fork": {
      "type": "integer"
    },
    "forbidden_committer_create_branch": {
      "type": "integer"
    },
    "forbidden_developer_create_branch": {
      "type": "integer"
    },
    "forbidden_developer_create_tag": {
      "type": "integer"
    },
    "forbidden_gitlab_access": {
      "type": "integer"
    },
    "generate_pre_merge_ref": {
      "type": "integer"
    },
    "include_lfs_objects": {
      "type": "integer"
    },
    "rebase_disable_trigger_webhook": {
      "type": "integer"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "disable_fork": true,
      "forbidden_committer_create_branch": false,
      "forbidden_developer_create_branch": false,
      "forbidden_developer_create_tag": false,
      "forbidden_gitlab_access": true,
      "generate_pre_merge_ref": false,
      "include_lfs_objects": false,
      "rebase_disable_trigger_webhook": false
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_repo_settings",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
  "path": "/api/v5/repos/{owner}/{repo}/repo_settings",
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
    "name": "Get Repository Settings",
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
        "repo_settings"
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "disable_fork": true,
                "forbidden_committer_create_branch": false,
                "forbidden_developer_create_branch": false,
                "forbidden_developer_create_tag": false,
                "forbidden_gitlab_access": true,
                "generate_pre_merge_ref": false,
                "include_lfs_objects": false,
                "rebase_disable_trigger_webhook": false
              }
            }
          },
          "schema": {
            "properties": {
              "disable_fork": {
                "type": "integer"
              },
              "forbidden_committer_create_branch": {
                "type": "integer"
              },
              "forbidden_developer_create_branch": {
                "type": "integer"
              },
              "forbidden_developer_create_tag": {
                "type": "integer"
              },
              "forbidden_gitlab_access": {
                "type": "integer"
              },
              "generate_pre_merge_ref": {
                "type": "integer"
              },
              "include_lfs_objects": {
                "type": "integer"
              },
              "rebase_disable_trigger_webhook": {
                "type": "integer"
              }
            },
            "type": "object"
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
    "Repositories"
  ]
}
```
