# List WebHooks Of The Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-hooks](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-hooks)
Category: Webhooks
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/hooks`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_hooks`
- Tags: `Webhooks`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
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
      "created_at": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "issues_events": {
        "type": "integer"
      },
      "merge_requests_events": {
        "type": "integer"
      },
      "note_events": {
        "type": "integer"
      },
      "password": {
        "type": "string"
      },
      "project_id": {
        "type": "integer"
      },
      "push_events": {
        "type": "integer"
      },
      "result": {
        "type": "string"
      },
      "result_code": {
        "type": "integer"
      },
      "tag_push_events": {
        "type": "integer"
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
      "created_at": "2024-09-18T17:51:44+08:00",
      "id": 9523,
      "issues_events": true,
      "merge_requests_events": true,
      "note_events": false,
      "password": "123445",
      "project_id": 282463,
      "push_events": false,
      "result": "not found",
      "result_code": 503,
      "tag_push_events": false,
      "url": "http://duxwsqdkyx.cu/pxssss"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_hooks",
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
  "path": "/api/v5/repos/{owner}/{repo}/hooks",
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
    "name": "List WebHooks Of The Repository",
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
        "hooks"
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
                "created_at": "2024-09-18T17:51:44+08:00",
                "id": 9523,
                "issues_events": true,
                "merge_requests_events": true,
                "note_events": false,
                "password": "123445",
                "project_id": 282463,
                "push_events": false,
                "result": "not found",
                "result_code": 503,
                "tag_push_events": false,
                "url": "http://duxwsqdkyx.cu/pxssss"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "created_at": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "issues_events": {
                  "type": "integer"
                },
                "merge_requests_events": {
                  "type": "integer"
                },
                "note_events": {
                  "type": "integer"
                },
                "password": {
                  "type": "string"
                },
                "project_id": {
                  "type": "integer"
                },
                "push_events": {
                  "type": "integer"
                },
                "result": {
                  "type": "string"
                },
                "result_code": {
                  "type": "integer"
                },
                "tag_push_events": {
                  "type": "integer"
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
    "Webhooks"
  ]
}
```
