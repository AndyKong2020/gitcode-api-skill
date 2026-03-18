# Get a Company's Member
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprise-members-username](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprise-members-username)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/enterprises/{enterprise}/members/{username}`
- Operation ID: `get_api_v8_enterprises_{enterprise}_members_{username}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | integer | Enterprise ID |
| username | path | true | string | username (alias: login) |
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
  "properties": {
    "active": {
      "type": "boolean"
    },
    "enterprise_email": {
      "type": "string"
    },
    "role": {
      "type": "string"
    },
    "role_id": {
      "type": "string"
    },
    "role_name": {
      "type": "string"
    },
    "role_name_cn": {
      "type": "string"
    },
    "user": {
      "properties": {
        "avatar_url": {
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
        "object_id": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "user_id": {
          "type": "string"
        }
      },
      "required": [
        "avatar_url",
        "html_url",
        "id",
        "object_id",
        "login",
        "name",
        "url",
        "user_id"
      ],
      "type": "object"
    }
  },
  "required": [
    "user",
    "active",
    "role",
    "role_name",
    "role_id",
    "role_name_cn",
    "enterprise_email"
  ],
  "type": "object"
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
  "operationId": "get_api_v8_enterprises_{enterprise}_members_{username}",
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
    "name": "Get a Company's Member",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "properties": {
              "active": {
                "type": "boolean"
              },
              "enterprise_email": {
                "type": "string"
              },
              "role": {
                "type": "string"
              },
              "role_id": {
                "type": "string"
              },
              "role_name": {
                "type": "string"
              },
              "role_name_cn": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "avatar_url": {
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
                  "object_id": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  },
                  "user_id": {
                    "type": "string"
                  }
                },
                "required": [
                  "avatar_url",
                  "html_url",
                  "id",
                  "object_id",
                  "login",
                  "name",
                  "url",
                  "user_id"
                ],
                "type": "object"
              }
            },
            "required": [
              "user",
              "active",
              "role",
              "role_name",
              "role_id",
              "role_name_cn",
              "enterprise_email"
            ],
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
