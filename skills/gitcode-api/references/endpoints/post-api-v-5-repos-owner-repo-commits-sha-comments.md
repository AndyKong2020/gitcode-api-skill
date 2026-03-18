# Create Commit Comment
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-commits-sha-comments](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-commits-sha-comments)
Category: Commit
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/commits/{sha}/comments`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_commits_{sha}_comments`
- Tags: `Commit`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| sha | path | true | string | commit ID |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "body": {
      "description": "comment content",
      "type": "string"
    }
  },
  "required": [
    "body"
  ],
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
    "body": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "id": {
      "type": "string"
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
      "body": "content",
      "created_at": "2024-03-28T11:19:33+08:00",
      "id": "12312sadsa",
      "updated_at": "2024-03-28T11:19:33+08:00"
    }
  }
}
```
## JSON Request Example
```json
{
  "body": "string"
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
    "body": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_commits_{sha}_comments",
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
      "description": "commit ID",
      "example": "",
      "in": "path",
      "name": "sha",
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
  "path": "/api/v5/repos/{owner}/{repo}/commits/{sha}/comments",
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
    "method": "POST",
    "name": "Create Commit Comment",
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
        "commits",
        ":sha",
        "comments"
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
        },
        {
          "description": {
            "content": "(Required) commit ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sha",
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
            "body": {
              "description": "comment content",
              "type": "string"
            }
          },
          "required": [
            "body"
          ],
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
                "body": "content",
                "created_at": "2024-03-28T11:19:33+08:00",
                "id": "12312sadsa",
                "updated_at": "2024-03-28T11:19:33+08:00"
              }
            }
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "id": {
                "type": "string"
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
    "Commit"
  ]
}
```
