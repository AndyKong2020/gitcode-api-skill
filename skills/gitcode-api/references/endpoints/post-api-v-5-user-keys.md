# Add a Public Key
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-user-keys](https://docs.gitcode.com/en/docs/apis/post-api-v-5-user-keys)
Category: Users
- Method: `POST`
- Path: `/api/v5/user/keys`
- Operation ID: `post_api_v5_user_keys`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "key": {
      "description": "Public key content",
      "type": "string"
    },
    "title": {
      "description": "public key name",
      "type": "string"
    }
  },
  "required": [
    "key",
    "title"
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
    "created_at": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "key": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "url": {
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
      "created_at": "2024-11-14T03:34:40.318+00:00",
      "id": 311915,
      "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIa6IyTGuI8V5wrhANDFyezQqL73dY9ctLGHgpOggp7E Gitee",
      "title": "555555",
      "url": "https://api.gitcode.com/v5/user/keys/311915"
    }
  }
}
```
## JSON Request Example
```json
{
  "key": "string",
  "title": "string"
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
    "key": "string",
    "title": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_user_keys",
  "parameters": [
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
  "path": "/api/v5/user/keys",
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
    "name": "Add a Public Key",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "keys"
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
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "key": {
              "description": "Public key content",
              "type": "string"
            },
            "title": {
              "description": "public key name",
              "type": "string"
            }
          },
          "required": [
            "key",
            "title"
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
                "created_at": "2024-11-14T03:34:40.318+00:00",
                "id": 311915,
                "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIa6IyTGuI8V5wrhANDFyezQqL73dY9ctLGHgpOggp7E Gitee",
                "title": "555555",
                "url": "https://api.gitcode.com/v5/user/keys/311915"
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
              "key": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "url": {
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
    "Users"
  ]
}
```
