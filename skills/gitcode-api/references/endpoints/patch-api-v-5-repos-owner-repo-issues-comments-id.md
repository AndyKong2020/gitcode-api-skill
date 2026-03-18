# Update Issue Comment
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-issues-comments-id](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-issues-comments-id)
Category: Issues
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/{repo}/issues/comments/{id}`
- Operation ID: `patch_api_v5_repos_{owner}_{repo}_issues_comments_{id}`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| id | path | true | string | Comment ID |
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
  "properties": {},
  "type": "object"
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
  "method": "patch",
  "operationId": "patch_api_v5_repos_{owner}_{repo}_issues_comments_{id}",
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
      "description": "Comment ID",
      "example": "",
      "in": "path",
      "name": "id",
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
  "path": "/api/v5/repos/{owner}/{repo}/issues/comments/{id}",
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
    "method": "PATCH",
    "name": "Update Issue Comment",
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
        "issues",
        "comments",
        ":id"
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
            "content": "(Required) Comment ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "id",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
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
          "schema": {
            "properties": {},
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
  "tags": [
    "Issues"
  ]
}
```
