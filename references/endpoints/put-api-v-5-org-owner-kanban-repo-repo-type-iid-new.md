# Update the board associated with an Issue or Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-owner-kanban-repo-repo-type-iid-new](https://docs.gitcode.com/en/docs/apis/put-api-v-5-org-owner-kanban-repo-repo-type-iid-new)
Category: Dashboard
- Method: `PUT`
- Path: `/api/v5/org/{owner}/kanban/repo/{repo}/{type}/{iid}`
- Operation ID: `put_api_v5_org_{owner}_kanban_repo_{repo}_{type}_{iid}_new`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Organization's path |
| repo | path | true | string | Path of the warehouse |
| type | path | true | string | Type, issue/merge_request |
| iid | path | true | string | issue or pull request iid |
| access_token | query | false | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "kanban_id": {
      "description": "kanban_id",
      "type": "string"
    }
  },
  "required": [
    "kanban_id"
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
{
  "kanban_id": "string"
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
    "kanban_id": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_org_{owner}_kanban_repo_{repo}_{type}_{iid}_new",
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
      "description": "Path of the warehouse",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Type, issue/merge_request",
      "in": "path",
      "name": "type",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "issue or pull request iid",
      "in": "path",
      "name": "iid",
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
  "path": "/api/v5/org/{owner}/kanban/repo/{repo}/{type}/{iid}",
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
    "name": "Update the board associated with an Issue or Pull Request",
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
        "repo",
        ":repo",
        ":type",
        ":iid"
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
            "content": "(Required) Path of the warehouse",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Type, issue/merge_request",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "type",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) issue or pull request iid",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "iid",
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
            "kanban_id": {
              "description": "kanban_id",
              "type": "string"
            }
          },
          "required": [
            "kanban_id"
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
