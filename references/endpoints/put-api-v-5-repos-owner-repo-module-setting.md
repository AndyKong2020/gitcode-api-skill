# Set Project Module
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-module-setting](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-module-setting)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/module/setting`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_module_setting`
- Tags: `Repositories`
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
    "has_analysis": {
      "description": "Whether to set up analytics",
      "type": "boolean"
    },
    "has_discussion": {
      "description": "Whether to set the discussion",
      "type": "boolean"
    },
    "has_fork": {
      "description": "Whether to set fork",
      "type": "boolean"
    },
    "has_issue": {
      "description": "Whether to set the issue",
      "type": "boolean"
    },
    "has_merge_request": {
      "description": "Whether to set the merge request",
      "type": "boolean"
    },
    "has_security": {
      "description": "Whether to set up security configuration",
      "type": "boolean"
    },
    "has_wiki": {
      "description": "Whether to set the wiki",
      "type": "boolean"
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
    "code": {
      "type": "integer"
    },
    "msg": {
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
      "code": 1,
      "msg": "success"
    }
  }
}
```
## JSON Request Example
```json
{
  "has_analysis": true,
  "has_discussion": true,
  "has_fork": true,
  "has_issue": true,
  "has_merge_request": true,
  "has_security": true,
  "has_wiki": true
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
    "has_analysis": true,
    "has_discussion": true,
    "has_fork": true,
    "has_issue": true,
    "has_merge_request": true,
    "has_security": true,
    "has_wiki": true
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_module_setting",
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
  "path": "/api/v5/repos/{owner}/{repo}/module/setting",
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
    "name": "Set Project Module",
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
        "module",
        "setting"
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
            "has_analysis": {
              "description": "Whether to set up analytics",
              "type": "boolean"
            },
            "has_discussion": {
              "description": "Whether to set the discussion",
              "type": "boolean"
            },
            "has_fork": {
              "description": "Whether to set fork",
              "type": "boolean"
            },
            "has_issue": {
              "description": "Whether to set the issue",
              "type": "boolean"
            },
            "has_merge_request": {
              "description": "Whether to set the merge request",
              "type": "boolean"
            },
            "has_security": {
              "description": "Whether to set up security configuration",
              "type": "boolean"
            },
            "has_wiki": {
              "description": "Whether to set the wiki",
              "type": "boolean"
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
                "code": 1,
                "msg": "success"
              }
            }
          },
          "schema": {
            "properties": {
              "code": {
                "type": "integer"
              },
              "msg": {
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
