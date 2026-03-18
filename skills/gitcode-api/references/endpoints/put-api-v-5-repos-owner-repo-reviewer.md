# Modify Project Code Review Settings
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-reviewer](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-reviewer)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/reviewer`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_reviewer`
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
    "assignees": {
      "description": "reviewer usernames, multiple usernames allowed, separated by half-width commas, e.g.: (username1,username2)",
      "type": "string"
    },
    "assignees_number": {
      "description": "Minimum number of reviewers",
      "type": "integer"
    },
    "testers": {
      "description": "Test user username, multiple can be provided, separated by half-width commas, e.g.: (username1,username2)",
      "type": "string"
    },
    "testers_number": {
      "description": "Minimum number of test participants",
      "type": "integer"
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
    "created_at": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "updated_at": {
      "type": "string"
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
      "created_at": "2024-01-24T14:33:44+08:00",
      "id": 7543745,
      "updated_at": "2024-04-07T21:23:08+08:00"
    }
  }
}
```
## JSON Request Example
```json
{
  "assignees": "string",
  "assignees_number": 0,
  "testers": "string",
  "testers_number": 0
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
    "assignees": "string",
    "assignees_number": 0,
    "testers": "string",
    "testers_number": 0
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_reviewer",
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
  "path": "/api/v5/repos/{owner}/{repo}/reviewer",
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
    "name": "Modify Project Code Review Settings",
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
        "reviewer"
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
            "assignees": {
              "description": "reviewer usernames, multiple usernames allowed, separated by half-width commas, e.g.: (username1,username2)",
              "type": "string"
            },
            "assignees_number": {
              "description": "Minimum number of reviewers",
              "type": "integer"
            },
            "testers": {
              "description": "Test user username, multiple can be provided, separated by half-width commas, e.g.: (username1,username2)",
              "type": "string"
            },
            "testers_number": {
              "description": "Minimum number of test participants",
              "type": "integer"
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
                "created_at": "2024-01-24T14:33:44+08:00",
                "id": 7543745,
                "updated_at": "2024-04-07T21:23:08+08:00"
              }
            }
          },
          "schema": {
            "properties": {
              "created_at": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "updated_at": {
                "type": "string"
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
