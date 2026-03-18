# Submit Pull Request Comments
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-comments](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-comments)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls_{number}_comments`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
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
    },
    "path": {
      "description": "Relative path of the file",
      "type": "string"
    },
    "position": {
      "description": "Number of code lines",
      "type": "integer"
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
    "id": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "body": "22222",
  "id": "97219c08d421e55cfa841deca16a30f5d7269e10"
}
```
## JSON Request Example
```json
{
  "body": "string",
  "path": "string",
  "position": 0
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
    "body": "string",
    "path": "string",
    "position": 0
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls_{number}_comments",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/comments",
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
    "name": "Submit Pull Request Comments",
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
        "pulls",
        ":number",
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
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
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
            },
            "path": {
              "description": "Relative path of the file",
              "type": "string"
            },
            "position": {
              "description": "Number of code lines",
              "type": "integer"
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
          "example": {
            "body": "22222",
            "id": "97219c08d421e55cfa841deca16a30f5d7269e10"
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "id": {
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
    "Pull Requests"
  ]
}
```
