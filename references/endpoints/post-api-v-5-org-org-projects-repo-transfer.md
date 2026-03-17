# Transfer Warehouse
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-org-org-projects-repo-transfer](https://docs.gitcode.com/en/docs/apis/post-api-v-5-org-org-projects-repo-transfer)
Category: Repositories
- Method: `POST`
- Path: `/api/v5/org/{org}/projects/{repo}/transfer`
- Operation ID: `post_api_v5_org_{org}_projects_{repo}_transfer`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization to which the repository belongs. |
| repo | path | true | string | Repository path |
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
    "transfer_to": {
      "description": "The target organization to transfer to.",
      "type": "string"
    }
  },
  "required": [
    "transfer_to",
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
  "transfer_to": "string"
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
    "transfer_to": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_org_{org}_projects_{repo}_transfer",
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
      "description": "Repository path",
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
  "path": "/api/v5/org/{org}/projects/{repo}/transfer",
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
    "name": "Transfer Warehouse",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "org",
        ":org",
        "projects",
        ":repo",
        "transfer"
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
            "content": "(Required) Repository path",
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
            "transfer_to": {
              "description": "The target organization to transfer to.",
              "type": "string"
            }
          },
          "required": [
            "transfer_to",
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
