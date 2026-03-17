# Modify Project Protection Tag
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-protected-tags](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-protected-tags)
Category: Tag
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/protected_tags`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_protected_tags`
- Tags: `Tag`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "create_access_level": {
      "description": "Allowed access level to be created (0: no one allowed; 30: developers, maintainers, administrators; 40: maintainers, administrators)",
      "type": "integer"
    },
    "name": {
      "description": "Label name",
      "type": "string"
    }
  },
  "required": [
    "name",
    "create_access_level"
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
    "create_access_level": {
      "type": "integer"
    },
    "create_access_level_desc": {
      "type": "string"
    },
    "name": {
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
      "create_access_level": 30,
      "create_access_level_desc": "developers, maintainers, administrators",
      "name": "your_tag_name"
    }
  }
}
```
## JSON Request Example
```json
{
  "create_access_level": 0,
  "name": "string"
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
    "create_access_level": 0,
    "name": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_protected_tags",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/protected_tags",
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
    "name": "Modify Project Protection Tag",
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
        "protected_tags"
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
            "create_access_level": {
              "description": "Allowed access level to be created (0: no one allowed; 30: developers, maintainers, administrators; 40: maintainers, administrators)",
              "type": "integer"
            },
            "name": {
              "description": "Label name",
              "type": "string"
            }
          },
          "required": [
            "name",
            "create_access_level"
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
                "create_access_level": 30,
                "create_access_level_desc": "developers, maintainers, administrators",
                "name": "your_tag_name"
              }
            }
          },
          "schema": {
            "properties": {
              "create_access_level": {
                "type": "integer"
              },
              "create_access_level_desc": {
                "type": "string"
              },
              "name": {
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
    "Tag"
  ]
}
```
