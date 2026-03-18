# Update Warehouse Settings
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-repo-settings](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-repo-settings)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/repo_settings`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_repo_settings`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "branch_name_regex": {
      "description": "Branch name regular expression",
      "type": "string"
    },
    "disable_fork": {
      "description": "Prohibit derivative projects (Disallow Fork projects)",
      "type": "boolean"
    },
    "forbidden_committer_create_branch": {
      "description": "Prohibit the submitter from creating branches.",
      "type": "boolean"
    },
    "forbidden_developer_create_branch": {
      "description": "Prohibit developers from creating branches",
      "type": "boolean"
    },
    "forbidden_developer_create_branch_user_ids": {
      "description": "Whitelist user IDs of developers prohibited from creating branches",
      "type": "string"
    },
    "forbidden_developer_create_tag": {
      "description": "Prohibit developers from creating tags",
      "type": "boolean"
    },
    "generate_pre_merge_ref": {
      "description": "The Pre-Merge reference for generating the Merge Request",
      "type": "boolean"
    },
    "include_lfs_objects": {
      "description": "The compressed package download includes LFS objects.",
      "type": "boolean"
    },
    "open_gpg_verified": {
      "description": "Expose GPG public key for verification",
      "type": "boolean"
    },
    "rebase_disable_trigger_webhook": {
      "description": "MR rebase does not trigger Webhook events",
      "type": "boolean"
    },
    "tag_name_regex": {
      "description": "Regular expression for the label name",
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
""
```
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
## JSON Request Example
```json
{
  "branch_name_regex": "string",
  "disable_fork": true,
  "forbidden_committer_create_branch": true,
  "forbidden_developer_create_branch": true,
  "forbidden_developer_create_branch_user_ids": "string",
  "forbidden_developer_create_tag": true,
  "generate_pre_merge_ref": true,
  "include_lfs_objects": true,
  "open_gpg_verified": true,
  "rebase_disable_trigger_webhook": true,
  "tag_name_regex": "string"
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
  "jsonRequestBodyExample": {
    "branch_name_regex": "string",
    "disable_fork": true,
    "forbidden_committer_create_branch": true,
    "forbidden_developer_create_branch": true,
    "forbidden_developer_create_branch_user_ids": "string",
    "forbidden_developer_create_tag": true,
    "generate_pre_merge_ref": true,
    "include_lfs_objects": true,
    "open_gpg_verified": true,
    "rebase_disable_trigger_webhook": true,
    "tag_name_regex": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_repo_settings",
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
    "body": {
      "mode": "raw",
      "options": {
        "raw": {
          "language": "json"
        }
      },
      "raw": ""
    },
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "PUT",
    "name": "Update Warehouse Settings",
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "branch_name_regex": {
              "description": "Branch name regular expression",
              "type": "string"
            },
            "disable_fork": {
              "description": "Prohibit derivative projects (Disallow Fork projects)",
              "type": "boolean"
            },
            "forbidden_committer_create_branch": {
              "description": "Prohibit the submitter from creating branches.",
              "type": "boolean"
            },
            "forbidden_developer_create_branch": {
              "description": "Prohibit developers from creating branches",
              "type": "boolean"
            },
            "forbidden_developer_create_branch_user_ids": {
              "description": "Whitelist user IDs of developers prohibited from creating branches",
              "type": "string"
            },
            "forbidden_developer_create_tag": {
              "description": "Prohibit developers from creating tags",
              "type": "boolean"
            },
            "generate_pre_merge_ref": {
              "description": "The Pre-Merge reference for generating the Merge Request",
              "type": "boolean"
            },
            "include_lfs_objects": {
              "description": "The compressed package download includes LFS objects.",
              "type": "boolean"
            },
            "open_gpg_verified": {
              "description": "Expose GPG public key for verification",
              "type": "boolean"
            },
            "rebase_disable_trigger_webhook": {
              "description": "MR rebase does not trigger Webhook events",
              "type": "boolean"
            },
            "tag_name_regex": {
              "description": "Regular expression for the label name",
              "type": "string"
            }
          },
          "type": "object"
        }
      }
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
