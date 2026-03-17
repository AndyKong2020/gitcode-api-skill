# Set Project Push Rules
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-push-config](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-push-config)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/push_config`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_push_config`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "commit_message_regex": {
      "description": "Submit information validation",
      "type": "string"
    },
    "deny_force_push": {
      "description": "No强制推送 (including administrators)",
      "type": "boolean"
    },
    "max_file_size": {
      "description": "Submission file limit (in MB)",
      "type": "integer"
    },
    "reject_not_signed_by_gpg": {
      "description": "Only signed submissions with authentication are allowed.",
      "type": "boolean"
    },
    "skip_rule_for_owner": {
      "description": "The submission of the project administrator is not restricted by the above rules.",
      "type": "boolean"
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
    "deny_force_push": {
      "type": "integer"
    },
    "max_file_size": {
      "type": "integer"
    },
    "reject_not_signed_by_gpg": {
      "type": "integer"
    },
    "skip_rule_for_owner": {
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
      "deny_force_push": true,
      "max_file_size": 10,
      "reject_not_signed_by_gpg": false,
      "skip_rule_for_owner": false
    }
  }
}
```
## JSON Request Example
```json
{
  "commit_message_regex": "string",
  "deny_force_push": true,
  "max_file_size": 0,
  "reject_not_signed_by_gpg": true,
  "skip_rule_for_owner": true
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
    "commit_message_regex": "string",
    "deny_force_push": true,
    "max_file_size": 0,
    "reject_not_signed_by_gpg": true,
    "skip_rule_for_owner": true
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_push_config",
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
  "path": "/api/v5/repos/{owner}/{repo}/push_config",
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
    "name": "Set Project Push Rules",
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
        "push_config"
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "commit_message_regex": {
              "description": "Submit information validation",
              "type": "string"
            },
            "deny_force_push": {
              "description": "No强制推送 (including administrators)",
              "type": "boolean"
            },
            "max_file_size": {
              "description": "Submission file limit (in MB)",
              "type": "integer"
            },
            "reject_not_signed_by_gpg": {
              "description": "Only signed submissions with authentication are allowed.",
              "type": "boolean"
            },
            "skip_rule_for_owner": {
              "description": "The submission of the project administrator is not restricted by the above rules.",
              "type": "boolean"
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
                "deny_force_push": true,
                "max_file_size": 10,
                "reject_not_signed_by_gpg": false,
                "skip_rule_for_owner": false
              }
            }
          },
          "schema": {
            "properties": {
              "deny_force_push": {
                "type": "integer"
              },
              "max_file_size": {
                "type": "integer"
              },
              "reject_not_signed_by_gpg": {
                "type": "integer"
              },
              "skip_rule_for_owner": {
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
