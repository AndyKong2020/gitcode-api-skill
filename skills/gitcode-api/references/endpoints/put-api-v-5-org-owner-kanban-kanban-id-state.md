# Modify the status of the kanban board
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-owner-kanban-kanban-id-state](https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-owner-kanban-kanban-id-state)
Category: Dashboard
- Method: `PUT`
- Path: `/api/v5/org/{owner}/kanban/{kanban_id}/state`
- Operation ID: `put_api_v5_org_{owner}_kanban_{kanban_id}_state`
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
  "properties": {
    "state": {
      "description": "Kanban Status, Closed: closed; Open: open",
      "type": "string"
    }
  },
  "required": [
    "state"
  ],
  "type": "object"
}
```
## Responses
### `200`
Headers:
```json
{}
```
## JSON Request Example
```json
{
  "state": "string"
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
    "state": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_org_{owner}_kanban_{kanban_id}_state",
  "parameters": [
    {
      "description": "Organization's path",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "kanban_id",
      "example": "",
      "in": "path",
      "name": "kanban_id",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/org/{owner}/kanban/{kanban_id}/state",
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
      }
    ],
    "method": "PUT",
    "name": "Modify the status of the kanban board",
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
        "state"
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
          "properties": {
            "state": {
              "description": "Kanban Status, Closed: closed; Open: open",
              "type": "string"
            }
          },
          "required": [
            "state"
          ],
          "type": "object"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {},
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
