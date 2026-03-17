# Add Project Members or Update Project Members Permissions
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-collaborators-username](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-collaborators-username)
Category: Member
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/collaborators/{username}`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_collaborators_{username}`
- Tags: `Member`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| username | path | true | string | username (alias: login) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "permission": {
      "description": "Member permissions: pull code, push code, repository maintainer (admin), custom role by entering the role name. Default: push",
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
    "avatar_url": {
      "type": "null"
    },
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
      "type": "string"
    },
    "permissions": {
      "properties": {
        "admin": {
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
    "remark": {
      "type": "string"
    },
    "type": {
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
      "avatar_url": null,
      "html_url": "https://gitcode.com/centking",
      "id": 7543745,
      "login": "centking",
      "name": "score占比",
      "permissions": {
        "admin": false,
        "pull": true,
        "push": true
      },
      "remark": "",
      "type": "User"
    }
  }
}
```
## JSON Request Example
```json
{
  "permission": "string"
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
    "permission": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_collaborators_{username}",
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
  "path": "/api/v5/repos/{owner}/{repo}/collaborators/{username}",
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
    "name": "Add Project Members or Update Project Members Permissions",
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
              "description": "Member permissions: pull code, push code, repository maintainer (admin), custom role by entering the role name. Default: push",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "avatar_url": null,
                "html_url": "https://gitcode.com/centking",
                "id": 7543745,
                "login": "centking",
                "name": "score占比",
                "permissions": {
                  "admin": false,
                  "pull": true,
                  "push": true
                },
                "remark": "",
                "type": "User"
              }
            }
          },
          "schema": {
            "properties": {
              "avatar_url": {
                "type": "null"
              },
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
                "type": "string"
              },
              "permissions": {
                "properties": {
                  "admin": {
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
              "remark": {
                "type": "string"
              },
              "type": {
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
    "Member"
  ]
}
```
