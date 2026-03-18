# Get Single Repository WebHook
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-hooks-id](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-hooks-id)
Category: Webhooks
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/hooks/{id}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_hooks_{id}`
- Tags: `Webhooks`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| id | path | true | string | The ID of the Webhook |
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
      "type": "null"
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
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "created_at": "2024-09-26T16:13:27+08:00",
      "id": 9529,
      "issues_events": true,
      "merge_requests_events": true,
      "note_events": false,
      "password": "123445",
      "project_id": 282463,
      "push_events": false,
      "result": null,
      "result_code": 0,
      "tag_push_events": false,
      "url": "http://duxwsqdkyx.cu/pxddddd"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_hooks_{id}",
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
      "description": "The ID of the Webhook",
      "example": "",
      "in": "path",
      "name": "id",
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
  "path": "/api/v5/repos/{owner}/{repo}/hooks/{id}",
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
    "name": "Get Single Repository WebHook",
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
        "hooks",
        ":id"
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
            "content": "(Required) The ID of the Webhook",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "id",
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
                "created_at": "2024-09-26T16:13:27+08:00",
                "id": 9529,
                "issues_events": true,
                "merge_requests_events": true,
                "note_events": false,
                "password": "123445",
                "project_id": 282463,
                "push_events": false,
                "result": null,
                "result_code": 0,
                "tag_push_events": false,
                "url": "http://duxwsqdkyx.cu/pxddddd"
              }
            }
          },
          "schema": {
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
                "type": "null"
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
