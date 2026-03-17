# Update Protection Branch Rules
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-branches-wildcard-setting](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-branches-wildcard-setting)
Category: Branch
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/branches/{wildcard}/setting`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_branches_{wildcard}_setting`
- Tags: `Branch`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| wildcard | path | true | string | Protect branch name |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "merger": {
      "description": "Members who can merge Pull Request. develop: Repository administrator and developer; admin: Repository administrator; maintainer: Maintainer; multiple roles are separated by English semicolons. Empty string: No one is allowed to merge",
      "type": "string"
    },
    "pusher": {
      "description": "Please push code members. develop: repository administrator and developer; admin: repository administrator; maintainer: maintainer; multiple roles are separated by English semicolons. Empty string: no one is allowed to push",
      "type": "string"
    }
  },
  "required": [
    "pusher",
    "merger"
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
  "properties": {},
  "type": "object"
}
```
## JSON Request Example
```json
{
  "merger": "string",
  "pusher": "string"
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
    "merger": "string",
    "pusher": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_branches_{wildcard}_setting",
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
      "description": "Protect branch name",
      "example": "",
      "in": "path",
      "name": "wildcard",
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
  "path": "/api/v5/repos/{owner}/{repo}/branches/{wildcard}/setting",
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
    "name": "Update Protection Branch Rules",
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
        "branches",
        ":wildcard",
        "setting"
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
            "content": "(Required) Protect branch name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "wildcard",
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
            "merger": {
              "description": "Members who can merge Pull Request. develop: Repository administrator and developer; admin: Repository administrator; maintainer: Maintainer; multiple roles are separated by English semicolons. Empty string: No one is allowed to merge",
              "type": "string"
            },
            "pusher": {
              "description": "Please push code members. develop: repository administrator and developer; admin: repository administrator; maintainer: maintainer; multiple roles are separated by English semicolons. Empty string: no one is allowed to push",
              "type": "string"
            }
          },
          "required": [
            "pusher",
            "merger"
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
