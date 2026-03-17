# Get A Public Key
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-keys-id](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-keys-id)
Category: Users
- Method: `GET`
- Path: `/api/v5/user/keys/{id}`
- Operation ID: `get_api_v5_user_keys_{id}`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| id | path | true | string | public key ID |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
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
  "items": {
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
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "created_at": "2024-07-23T10:29:42.119+00:00",
      "id": 308357,
      "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCwT9UXXtGfLa16tbxV+0RQ6m+BaAG2wJvqApr+juVNEmnM0lKNt1tyxY/V9SsCRf38UprPLTp71+btRpFIH9TLrGhkvT3tJOouYDXVUpSaigi7OO+6eLc+Cn0TZSLj4RmwVe/w93kmsCUzgqkeHk14K3S+2oCCm1rbpBAvpPhSKHhAH9LcTBecDoZ+NA2dsEDyfsloVH5cMJQO9n2W1QYduMuuaVHHpehSdDohN7cDI799Rwofaqqyz6ZJrc6eBjSVi1W+JPDTT6NW0+eFBYXo3KWybffixH4cAWdbS1Ms5Pe9Xh+G4WqFuhFh9zCoXlRUUrArLo5pYfpy5gv4iUVmniM0Pb0/Y5x8RJyGaPdS/2c68s8LQsm/9Ees8aeE5TcT5isDEvh+wy7jp1xi5nONk9QvOy7EdYYeHQtkw/0rklsz7UvAIjjHObNNYpY6RLQRT+dqN/lAb7stT047FSxqcNMCX/cybapLygs1y2ClcgU42p16RfgCH0NKA5emRhM= xiaogang@csdn.net",
      "title": "xiaogang@csdn.net\r\n",
      "url": "https://api.gitcode.com/v5/user/keys/308357"
    }
  }
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
  "method": "get",
  "operationId": "get_api_v5_user_keys_{id}",
  "parameters": [
    {
      "description": "public key ID",
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
  "path": "/api/v5/user/keys/{id}",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "GET",
    "name": "Get A Public Key",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "keys",
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
            "content": "(Required) public key ID",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "created_at": "2024-07-23T10:29:42.119+00:00",
                "id": 308357,
                "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCwT9UXXtGfLa16tbxV+0RQ6m+BaAG2wJvqApr+juVNEmnM0lKNt1tyxY/V9SsCRf38UprPLTp71+btRpFIH9TLrGhkvT3tJOouYDXVUpSaigi7OO+6eLc+Cn0TZSLj4RmwVe/w93kmsCUzgqkeHk14K3S+2oCCm1rbpBAvpPhSKHhAH9LcTBecDoZ+NA2dsEDyfsloVH5cMJQO9n2W1QYduMuuaVHHpehSdDohN7cDI799Rwofaqqyz6ZJrc6eBjSVi1W+JPDTT6NW0+eFBYXo3KWybffixH4cAWdbS1Ms5Pe9Xh+G4WqFuhFh9zCoXlRUUrArLo5pYfpy5gv4iUVmniM0Pb0/Y5x8RJyGaPdS/2c68s8LQsm/9Ees8aeE5TcT5isDEvh+wy7jp1xi5nONk9QvOy7EdYYeHQtkw/0rklsz7UvAIjjHObNNYpY6RLQRT+dqN/lAb7stT047FSxqcNMCX/cybapLygs1y2ClcgU42p16RfgCH0NKA5emRhM= xiaogang@csdn.net",
                "title": "xiaogang@csdn.net\r\n",
                "url": "https://api.gitcode.com/v5/user/keys/308357"
              }
            }
          },
          "schema": {
            "items": {
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
            },
            "type": "array"
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
