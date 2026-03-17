# Create Repository Milestone
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-milestones](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-milestones)
Category: Milestone
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/milestones`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_milestones`
- Tags: `Milestone`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | false | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "description": {
      "description": "Specific description of the milestone",
      "type": "string"
    },
    "due_on": {
      "description": "The deadline date for the milestone",
      "type": "string"
    },
    "title": {
      "description": "Milestone Title",
      "type": "string"
    }
  },
  "required": [
    "title",
    "due_on"
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
## JSON Request Example
```json
{
  "description": "string",
  "due_on": "string",
  "title": "string"
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
    "description": "string",
    "due_on": "string",
    "title": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_milestones",
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
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/milestones",
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
    "name": "Create Repository Milestone",
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
        "milestones"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "description": {
              "description": "Specific description of the milestone",
              "type": "string"
            },
            "due_on": {
              "description": "The deadline date for the milestone",
              "type": "string"
            },
            "title": {
              "description": "Milestone Title",
              "type": "string"
            }
          },
          "required": [
            "title",
            "due_on"
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
