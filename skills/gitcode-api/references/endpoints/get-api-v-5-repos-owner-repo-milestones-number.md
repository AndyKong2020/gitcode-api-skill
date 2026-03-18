# Get Single Repository Milestone
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-milestones-number](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-milestones-number)
Category: Milestone
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/milestones/{number}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_milestones_{number}`
- Tags: `Milestone`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | Milestone Sequence Number (number) |
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
    "closed_issues": {
      "type": "integer"
    },
    "created_at": {
      "type": "string"
    },
    "description": {
      "type": "string"
    },
    "due_on": {
      "type": "string"
    },
    "number": {
      "type": "integer"
    },
    "open_issues": {
      "type": "integer"
    },
    "repository_id": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    },
    "url": {
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
      "closed_issues": 0,
      "created_at": "2024-10-08T10:58:16+08:00",
      "description": "Hello China",
      "due_on": "2024-11-08",
      "number": 4914,
      "open_issues": 0,
      "repository_id": 4066481,
      "state": "active",
      "title": "Hello China",
      "updated_at": "2024-10-08T10:58:16+08:00",
      "url": "https://gitcode.com/dengmengmian/oneapi/milestones/1"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_milestones_{number}",
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
      "description": "Milestone Sequence Number (number)",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
  "path": "/api/v5/repos/{owner}/{repo}/milestones/{number}",
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
    "name": "Get Single Repository Milestone",
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
        "milestones",
        ":number"
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
            "content": "(Required) Milestone Sequence Number (number)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
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
                "closed_issues": 0,
                "created_at": "2024-10-08T10:58:16+08:00",
                "description": "Hello China",
                "due_on": "2024-11-08",
                "number": 4914,
                "open_issues": 0,
                "repository_id": 4066481,
                "state": "active",
                "title": "Hello China",
                "updated_at": "2024-10-08T10:58:16+08:00",
                "url": "https://gitcode.com/dengmengmian/oneapi/milestones/1"
              }
            }
          },
          "schema": {
            "properties": {
              "closed_issues": {
                "type": "integer"
              },
              "created_at": {
                "type": "string"
              },
              "description": {
                "type": "string"
              },
              "due_on": {
                "type": "string"
              },
              "number": {
                "type": "integer"
              },
              "open_issues": {
                "type": "integer"
              },
              "repository_id": {
                "type": "integer"
              },
              "state": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
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
    "Milestone"
  ]
}
```
