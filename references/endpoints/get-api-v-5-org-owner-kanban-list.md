# Get the list of organization kanbans
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-list](https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-list)
Category: Dashboard
- Method: `GET`
- Path: `/api/v5/org/{owner}/kanban/list`
- Operation ID: `get_api_v5_org_{owner}_kanban_list`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Organization's path |
| access_token | query | true | string | User authorization code |
| status | query | false | integer | Status 0: Normal 1: Closed, default is not passed as all. |
| sort | query | false | string | Latest: newest,  Oldest: oldest |
| visibility | query | false | integer | Visibility 1: Public 2: Private |
| search | query | false | string | Search by name |
| page | query | false | string | Current page number |
| per_page | query | false | string | Number of items per page |
## Request Body
No request body.
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
  "properties": {
    "all_count": {
      "type": "integer"
    },
    "close_count": {
      "type": "integer"
    },
    "content": {
      "items": {
        "properties": {
          "description": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "iid": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "status": {
            "type": "integer"
          },
          "updated_at": {
            "type": "string"
          },
          "visibility": {
            "type": "integer"
          }
        },
        "required": [
          "id",
          "iid",
          "name",
          "description",
          "status",
          "visibility",
          "updated_at"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "open_count": {
      "type": "integer"
    }
  },
  "required": [
    "close_count",
    "open_count",
    "all_count",
    "content"
  ],
  "type": "object"
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
  "operationId": "get_api_v5_org_{owner}_kanban_list",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Status 0: Normal 1: Closed, default is not passed as all.",
      "in": "query",
      "name": "status",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Latest: newest,  Oldest: oldest",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Visibility 1: Public 2: Private",
      "in": "query",
      "name": "visibility",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Search by name",
      "in": "query",
      "name": "search",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Number of items per page",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/org/{owner}/kanban/list",
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
    "name": "Get the list of organization kanbans",
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
        "list"
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
            "content": "Status 0: Normal 1: Closed, default is not passed as all.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "status",
          "value": ""
        },
        {
          "description": {
            "content": "Latest: newest,  Oldest: oldest",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Visibility 1: Public 2: Private",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "visibility",
          "value": ""
        },
        {
          "description": {
            "content": "Search by name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "search",
          "value": ""
        },
        {
          "description": {
            "content": "Current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "Number of items per page",
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
            "content": "(Required) Organization's path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
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
          "schema": {
            "properties": {
              "all_count": {
                "type": "integer"
              },
              "close_count": {
                "type": "integer"
              },
              "content": {
                "items": {
                  "properties": {
                    "description": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "iid": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "status": {
                      "type": "integer"
                    },
                    "updated_at": {
                      "type": "string"
                    },
                    "visibility": {
                      "type": "integer"
                    }
                  },
                  "required": [
                    "id",
                    "iid",
                    "name",
                    "description",
                    "status",
                    "visibility",
                    "updated_at"
                  ],
                  "type": "object"
                },
                "type": "array"
              },
              "open_count": {
                "type": "integer"
              }
            },
            "required": [
              "close_count",
              "open_count",
              "all_count",
              "content"
            ],
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
