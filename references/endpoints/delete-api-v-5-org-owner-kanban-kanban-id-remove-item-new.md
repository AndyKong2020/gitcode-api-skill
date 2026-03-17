# Delete Issues or Pull Requests associated with the board
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-5-org-owner-kanban-kanban-id-remove-item-new](https://docs.gitcode.com/en/docs/apis/delete-api-v-5-org-owner-kanban-kanban-id-remove-item-new)
Category: Dashboard
- Method: `DELETE`
- Path: `/api/v5/org/{owner}/kanban/{kanban_id}/remove_item`
- Operation ID: `delete_api_v5_org_{owner}_kanban_{kanban_id}_remove_item_new`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Organization's path |
| kanban_id | path | true | string | kanban_id |
| access_token | query | false | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "items": {
    "properties": {
      "issue_iids": {
        "description": "Issue iid in the warehouse",
        "items": {
          "type": "integer"
        },
        "type": "array"
      },
      "pr_iids": {
        "description": "The iid of pull requests in the warehouse",
        "items": {
          "type": "integer"
        },
        "type": "array"
      },
      "repo": {
        "description": "Path of the warehouse",
        "type": "string"
      }
    },
    "required": [
      "repo",
      "issue_iids",
      "pr_iids"
    ],
    "type": "object"
  },
  "type": "array"
}
```
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {},
  "type": "object"
}
```
## JSON Request Example
```json
[
  {
    "issue_iids": [
      0
    ],
    "pr_iids": [
      0
    ],
    "repo": "string"
  }
]
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
  "jsonRequestBodyExample": [
    {
      "issue_iids": [
        0
      ],
      "pr_iids": [
        0
      ],
      "repo": "string"
    }
  ],
  "method": "delete",
  "operationId": "delete_api_v5_org_{owner}_kanban_{kanban_id}_remove_item_new",
  "parameters": [
    {
      "description": "Organization's path",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "kanban_id",
      "in": "path",
      "name": "kanban_id",
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
  "path": "/api/v5/org/{owner}/kanban/{kanban_id}/remove_item",
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
    "method": "DELETE",
    "name": "Delete Issues or Pull Requests associated with the board",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "org",
        ":owner",
        "kanban",
        ":kanban_id",
        "remove_item"
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
            "content": "(Required) Organization's path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) kanban_id",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "kanban_id",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "items": {
            "properties": {
              "issue_iids": {
                "description": "Issue iid in the warehouse",
                "items": {
                  "type": "integer"
                },
                "type": "array"
              },
              "pr_iids": {
                "description": "The iid of pull requests in the warehouse",
                "items": {
                  "type": "integer"
                },
                "type": "array"
              },
              "repo": {
                "description": "Path of the warehouse",
                "type": "string"
              }
            },
            "required": [
              "repo",
              "issue_iids",
              "pr_iids"
            ],
            "type": "object"
          },
          "type": "array"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "properties": {},
            "type": "object"
          }
        }
      },
      "description": "",
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
  "tags": []
}
```
