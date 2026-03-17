# View Warehouse Members' Permissions
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators-username-permission](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-collaborators-username-permission)
Category: Member
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/collaborators/{username}/permission`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_collaborators_{username}_permission`
- Tags: `Member`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
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
    "access_level": {
      "type": "integer"
    },
    "email": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "join_way": {
      "type": "string"
    },
    "login": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "nick_name": {
      "type": "string"
    },
    "object_id": {
      "type": "string"
    },
    "permission": {
      "type": "string"
    },
    "permissions": {
      "properties": {
        "admin": {
          "type": "boolean"
        }
      },
      "required": [
        "admin"
      ],
      "type": "object"
    },
    "role_name": {
      "type": "string"
    },
    "role_name_cn": {
      "type": "string"
    },
    "source_name": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "username": {
      "type": "string"
    },
    "web_url": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "username",
    "nick_name",
    "state",
    "email",
    "web_url",
    "access_level",
    "type",
    "join_way",
    "source_name",
    "role_name",
    "role_name_cn",
    "permissions",
    "object_id",
    "permission",
    "login"
  ],
  "type": "object"
}
```
Example:
```json
{
  "id": 268,
  "login": "dengmengmian",
  "permission": "admin"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_collaborators_{username}_permission",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
  "path": "/api/v5/repos/{owner}/{repo}/collaborators/{username}/permission",
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
    "name": "View Warehouse Members' Permissions",
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
        "collaborators",
        ":username",
        "permission"
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
            "content": "(Required) Repository space address (address path of the enterprise, organization, or individual)",
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
          "example": {
            "id": 268,
            "login": "dengmengmian",
            "permission": "admin"
          },
          "schema": {
            "properties": {
              "access_level": {
                "type": "integer"
              },
              "email": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "join_way": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "nick_name": {
                "type": "string"
              },
              "object_id": {
                "type": "string"
              },
              "permission": {
                "type": "string"
              },
              "permissions": {
                "properties": {
                  "admin": {
                    "type": "boolean"
                  }
                },
                "required": [
                  "admin"
                ],
                "type": "object"
              },
              "role_name": {
                "type": "string"
              },
              "role_name_cn": {
                "type": "string"
              },
              "source_name": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "type": {
                "type": "string"
              },
              "username": {
                "type": "string"
              },
              "web_url": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "name",
              "username",
              "nick_name",
              "state",
              "email",
              "web_url",
              "access_level",
              "type",
              "join_way",
              "source_name",
              "role_name",
              "role_name_cn",
              "permissions",
              "object_id",
              "permission",
              "login"
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
    "Member"
  ]
}
```
