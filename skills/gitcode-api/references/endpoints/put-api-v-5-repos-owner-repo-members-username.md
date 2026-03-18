# Update Project Member Roles
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-members-username](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-members-username)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/members/{username}`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_members_{username}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| username | path | true | string | Project member username |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "permission": {
      "description": "Member permissions: pull code, push code, admin. Default: push, customized role.",
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
  "followers_url": "https://api-test.gitcode.com/api/v5/users/xiaogang2/followers",
  "html_url": "https://test.gitcode.net/xiaogang2",
  "id": "65ffca965079ba0d1c00f6f2",
  "login": "xiaogang2",
  "name": "Xiao Gang 2",
  "permissions": {
    "admin": false,
    "customized": true,
    "pull": false,
    "push": false
  },
  "type": "User",
  "url": "https://api-test.gitcode.com/api/v5/xiaogang2"
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
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_members_{username}",
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
      "description": "Project member username",
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
  "path": "/api/v5/repos/{owner}/{repo}/members/{username}",
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
    "name": "Update Project Member Roles",
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
            "content": "(Required) Project member username",
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
              "description": "Member permissions: pull code, push code, admin. Default: push, customized role.",
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
            "followers_url": "https://api-test.gitcode.com/api/v5/users/xiaogang2/followers",
            "html_url": "https://test.gitcode.net/xiaogang2",
            "id": "65ffca965079ba0d1c00f6f2",
            "login": "xiaogang2",
            "name": "Xiao Gang 2",
            "permissions": {
              "admin": false,
              "customized": true,
              "pull": false,
              "push": false
            },
            "type": "User",
            "url": "https://api-test.gitcode.com/api/v5/xiaogang2"
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
    "Repositories"
  ]
}
```
