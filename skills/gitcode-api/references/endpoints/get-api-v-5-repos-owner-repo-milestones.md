# Get All Repository Milestones
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-milestones](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-milestones)
Category: Milestone
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/milestones`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_milestones`
- Tags: `Milestone`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Milestone state: open, closed, all. Default: open |
| sort | query | false | string | Sorting method: due_on |
| direction | query | false | string | Ascending (asc) or descending (desc). Default: asc |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_milestones",
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
    },
    {
      "description": "Milestone state: open, closed, all. Default: open",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sorting method: due_on",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Ascending (asc) or descending (desc). Default: asc",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/milestones",
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
    "name": "Get All Repository Milestones",
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
            "content": "(Required) User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "Milestone state: open, closed, all. Default: open",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "Sorting method: due_on",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Ascending (asc) or descending (desc). Default: asc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
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
            "items": {
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
    "Milestone"
  ]
}
```
