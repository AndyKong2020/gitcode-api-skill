# Get Project Custom Roles
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-customized-roles](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-customized-roles)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/customized_roles`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_customized_roles`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
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
      "access_level": {
        "type": "integer"
      },
      "created_at": {
        "type": "string"
      },
      "member_count": {
        "type": "integer"
      },
      "role_chinese_name": {
        "type": "string"
      },
      "role_description": {
        "type": "string"
      },
      "role_id": {
        "type": "string"
      },
      "role_name": {
        "type": "string"
      },
      "role_type": {
        "type": "string"
      },
      "updated_at": {
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
      "access_level": 15,
      "created_at": "2024-04-17 08:00",
      "member_count": 1,
      "role_chinese_name": "test role",
      "role_description": "test role",
      "role_id": "e6cd76d6c82f46c78c71fd7f67eaf3bf",
      "role_name": "test role",
      "role_type": "project-customized",
      "updated_at": "2024-04-17 08:00"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_customized_roles",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/customized_roles",
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
    "name": "Get Project Custom Roles",
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
        "customized_roles"
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
                "access_level": 15,
                "created_at": "2024-04-17 08:00",
                "member_count": 1,
                "role_chinese_name": "test role",
                "role_description": "test role",
                "role_id": "e6cd76d6c82f46c78c71fd7f67eaf3bf",
                "role_name": "test role",
                "role_type": "project-customized",
                "updated_at": "2024-04-17 08:00"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "access_level": {
                  "type": "integer"
                },
                "created_at": {
                  "type": "string"
                },
                "member_count": {
                  "type": "integer"
                },
                "role_chinese_name": {
                  "type": "string"
                },
                "role_description": {
                  "type": "string"
                },
                "role_id": {
                  "type": "string"
                },
                "role_name": {
                  "type": "string"
                },
                "role_type": {
                  "type": "string"
                },
                "updated_at": {
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
    "Repositories"
  ]
}
```
