# Invite enterprise members
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-8-enterprises-enterprise-memberships-username](https://docs.gitcode.com/en/docs/apis/post-api-v-8-enterprises-enterprise-memberships-username)
Category: Enterprise
- Method: `POST`
- Path: `/api/v8/enterprises/{enterprise}/memberships/{username}`
- Operation ID: `post_api_v8_enterprises_{enterprise}_memberships_{username}`
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
    "permission": {
      "description": "Member Permissions: pull, push, admin, customized. Default: push",
      "type": "string"
    },
    "role_id": {
      "description": "Role ID, if \"permission\" is set to \"customized\", the role ID must be provided.",
      "type": "string"
    }
  },
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
    "followers_url": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "login": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "permissions": {
      "properties": {
        "admin": {
          "type": "integer"
        },
        "customized": {
          "type": "integer"
        },
        "pull": {
          "type": "integer"
        },
        "push": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "type": {
      "type": "string"
    },
    "url": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "followers_url": "https://api.gitcode.com/api/v5/users/xiaogang2/followers",
  "html_url": "https://gitcode.com/xiaogang2",
  "id": "65ffca965079ba0d1c00f6f2",
  "login": "xiaogang2",
  "name": "Xiao Gang 2",
  "permissions": {
    "admin": false,
    "customized": true,
    "pull": true,
    "push": true
  },
  "type": "User",
  "url": "https://api.gitcode.com/api/v5/xiaogang2"
}
```
## JSON Request Example
```json
{
  "permission": "string",
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
    "permission": "string",
    "role_id": "string"
  },
  "method": "post",
  "operationId": "post_api_v8_enterprises_{enterprise}_memberships_{username}",
  "parameters": [
    {
      "description": "Enterprise ID",
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
  "path": "/api/v8/enterprises/{enterprise}/memberships/{username}",
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
    "name": "Invite enterprise members",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "memberships",
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
            "permission": {
              "description": "Member Permissions: pull, push, admin, customized. Default: push",
              "type": "string"
            },
            "role_id": {
              "description": "Role ID, if \"permission\" is set to \"customized\", the role ID must be provided.",
              "type": "string"
            }
          },
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
            "followers_url": "https://api.gitcode.com/api/v5/users/xiaogang2/followers",
            "html_url": "https://gitcode.com/xiaogang2",
            "id": "65ffca965079ba0d1c00f6f2",
            "login": "xiaogang2",
            "name": "Xiao Gang 2",
            "permissions": {
              "admin": false,
              "customized": true,
              "pull": true,
              "push": true
            },
            "type": "User",
            "url": "https://api.gitcode.com/api/v5/xiaogang2"
          },
          "schema": {
            "properties": {
              "followers_url": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "permissions": {
                "properties": {
                  "admin": {
                    "type": "integer"
                  },
                  "customized": {
                    "type": "integer"
                  },
                  "pull": {
                    "type": "integer"
                  },
                  "push": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "type": {
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
    "Organizations"
  ]
}
```
