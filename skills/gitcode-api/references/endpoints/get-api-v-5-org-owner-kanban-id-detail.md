# Get single kanban details
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-id-detail](https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-owner-kanban-id-detail)
Category: Dashboard
- Method: `GET`
- Path: `/api/v5/org/{owner}/kanban/{kanban_id}/detail`
- Operation ID: `get_api_v5_org_{owner}_kanban_{id}_detail`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Organization's path |
| kanban_id | path | true | string | kanban_id |
| access_token | query | false | string | User authorization code |
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
    "description": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "status": {
      "type": "integer"
    },
    "visibility": {
      "type": "integer"
    }
  },
  "required": [
    "id",
    "name",
    "description",
    "status",
    "visibility"
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
  "operationId": "get_api_v5_org_{owner}_kanban_{id}_detail",
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
  "path": "/api/v5/org/{owner}/kanban/{kanban_id}/detail",
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
    "name": "Get single kanban details",
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
        "detail"
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "properties": {
              "description": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "status": {
                "type": "integer"
              },
              "visibility": {
                "type": "integer"
              }
            },
            "required": [
              "id",
              "name",
              "description",
              "status",
              "visibility"
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
