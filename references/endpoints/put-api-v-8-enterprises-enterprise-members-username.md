# Modify Enterprise Member Permissions
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-8-enterprises-enterprise-members-username](https://docs.gitcode.com/en/docs/apis/put-api-v-8-enterprises-enterprise-members-username)
Category: Enterprise
- Method: `PUT`
- Path: `/api/v8/enterprises/{enterprise}/members/{username}`
- Operation ID: `put_api_v8_enterprises_{enterprise}_members_{username}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | integer | Enterprise ID |
| username | path | true | string | username (alias: login) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "role": {
      "description": "Enterprise Role (viewer: viewer, tester: tester, developer: developer, maintainer: maintainer, admin: administrator, customized: customized role)",
      "type": "string"
    },
    "role_id": {
      "description": "Role ID, if role is passed as customized, the role ID needs to be passed",
      "type": "string"
    }
  },
  "required": [
    "role"
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
    "active": {
      "type": "integer"
    },
    "role": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "user": {
      "properties": {
        "html_url": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "login": {
          "type": "string"
        },
        "name": {
          "description": "Name",
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "required": [
        "name"
      ],
      "type": "object"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "active": true,
  "role": "member",
  "url": "https://api.gitcode.com/api/v5/enterprises/litestabc/members/malongge5",
  "user": {
    "html_url": "https://gitcode.com/malongge5",
    "id": 953,
    "login": "malongge5",
    "url": "https://api.gitcode.com/api/v5/malongge5"
  }
}
```
## JSON Request Example
```json
{
  "role": "string",
  "role_id": "string"
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
    "role": "string",
    "role_id": "string"
  },
  "method": "put",
  "operationId": "put_api_v8_enterprises_{enterprise}_members_{username}",
  "parameters": [
    {
      "description": "Enterprise ID",
      "example": 0,
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "username (alias: login)",
      "example": "",
      "in": "path",
      "name": "username",
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
  "path": "/api/v8/enterprises/{enterprise}/members/{username}",
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
    "name": "Modify Enterprise Member Permissions",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "members",
        ":username"
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
            "content": "(Required) Enterprise ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) username (alias: login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "username",
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
            "role": {
              "description": "Enterprise Role (viewer: viewer, tester: tester, developer: developer, maintainer: maintainer, admin: administrator, customized: customized role)",
              "type": "string"
            },
            "role_id": {
              "description": "Role ID, if role is passed as customized, the role ID needs to be passed",
              "type": "string"
            }
          },
          "required": [
            "role"
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
            "active": true,
            "role": "member",
            "url": "https://api.gitcode.com/api/v5/enterprises/litestabc/members/malongge5",
            "user": {
              "html_url": "https://gitcode.com/malongge5",
              "id": 953,
              "login": "malongge5",
              "url": "https://api.gitcode.com/api/v5/malongge5"
            }
          },
          "schema": {
            "properties": {
              "active": {
                "type": "integer"
              },
              "role": {
                "type": "string"
              },
              "url": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "html_url": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "description": "Name",
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "required": [
                  "name"
                ],
                "type": "object"
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
    "Organizations"
  ]
}
```
