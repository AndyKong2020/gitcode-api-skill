# Warehouse Archiving
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-org-repo-repo-status](https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-org-repo-repo-status)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/org/{org}/repo/{repo}/status`
- Operation ID: `put_api_v5_org_{org}_repo_{repo}_status`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization to which the repository belongs. |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "password": {
      "description": "User password",
      "type": "string"
    },
    "status": {
      "description": "Repository status, 0: started, 2: closed",
      "type": "integer"
    }
  },
  "required": [
    "status",
    "password"
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
    "code": {
      "type": "integer"
    },
    "msg": {
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
      "code": 1,
      "msg": "success"
    }
  }
}
```
## JSON Request Example
```json
{
  "password": "string",
  "status": 0
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
    "password": "string",
    "status": 0
  },
  "method": "put",
  "operationId": "put_api_v5_org_{org}_repo_{repo}_status",
  "parameters": [
    {
      "description": "Organization to which the repository belongs.",
      "example": "",
      "in": "path",
      "name": "org",
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
  "path": "/api/v5/org/{org}/repo/{repo}/status",
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
    "name": "Warehouse Archiving",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "org",
        ":org",
        "repo",
        ":repo",
        "status"
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
            "content": "(Required) Organization to which the repository belongs.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "org",
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
            "password": {
              "description": "User password",
              "type": "string"
            },
            "status": {
              "description": "Repository status, 0: started, 2: closed",
              "type": "integer"
            }
          },
          "required": [
            "status",
            "password"
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
                "code": 1,
                "msg": "success"
              }
            }
          },
          "schema": {
            "properties": {
              "code": {
                "type": "integer"
              },
              "msg": {
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
