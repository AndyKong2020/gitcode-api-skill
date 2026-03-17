# Create New Protection Branch Rule
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-branches-setting-new](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-branches-setting-new)
Category: Branch
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/branches/setting/new`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_branches_setting_new`
- Tags: `Branch`
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
    "merger": {
      "description": "Members who can merge Pull Request. develop: Repository administrator and developer; admin: Repository administrator; maintainer: Maintainer; multiple roles are separated by English semicolons. Empty string: No one is allowed to merge",
      "type": "string"
    },
    "pusher": {
      "description": "Please push code members. develop: repository administrator and developer; admin: repository administrator; maintainer: maintainer; multiple roles are separated by English semicolons. Empty string: no one is allowed to push",
      "type": "string"
    },
    "wildcard": {
      "description": "Branch/Wildcard",
      "type": "string"
    }
  },
  "required": [
    "wildcard",
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
  "pusher": "string",
  "wildcard": "string"
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
    "pusher": "string",
    "wildcard": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_branches_setting_new",
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
  "path": "/api/v5/repos/{owner}/{repo}/branches/setting/new",
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
    "name": "Create New Protection Branch Rule",
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
        "setting",
        "new"
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
            "merger": {
              "description": "Members who can merge Pull Request. develop: Repository administrator and developer; admin: Repository administrator; maintainer: Maintainer; multiple roles are separated by English semicolons. Empty string: No one is allowed to merge",
              "type": "string"
            },
            "pusher": {
              "description": "Please push code members. develop: repository administrator and developer; admin: repository administrator; maintainer: maintainer; multiple roles are separated by English semicolons. Empty string: no one is allowed to push",
              "type": "string"
            },
            "wildcard": {
              "description": "Branch/Wildcard",
              "type": "string"
            }
          },
          "required": [
            "wildcard",
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
    "Branch"
  ]
}
```
