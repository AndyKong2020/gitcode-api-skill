# List All Namespaces Of Authorized Users
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-namespaces](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-namespaces)
Category: Users
- Method: `GET`
- Path: `/api/v5/user/namespaces`
- Operation ID: `get_api_v5_user_namespaces`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| mode | query | false | string | Participation Mode: project (namespaces of all participating repositories), intrant (the joined namespace), all (includes both of the above), default (intrant) |
| page | query | false | integer | Current page number |
| perPage | query | false | integer | Number of items per page |
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
  "items": {
    "properties": {
      "html_url": {
        "title": "access address namespace",
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "name": {
        "title": "namespace name",
        "type": "string"
      },
      "path": {
        "title": "namespace path",
        "type": "string"
      },
      "type": {
        "title": "namespace type, user: User; group: Organization",
        "type": "string"
      }
    },
    "required": [
      "id",
      "path",
      "name",
      "html_url",
      "type"
    ],
    "type": "object"
  },
  "type": "array"
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
  "operationId": "get_api_v5_user_namespaces",
  "parameters": [
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Participation Mode: project (namespaces of all participating repositories), intrant (the joined namespace), all (includes both of the above), default (intrant)",
      "in": "query",
      "name": "mode",
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
        "type": "integer"
      }
    },
    {
      "description": "Number of items per page",
      "in": "query",
      "name": "perPage",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/user/namespaces",
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
    "name": "List All Namespaces Of Authorized Users",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "namespaces"
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
            "content": "Participation Mode: project (namespaces of all participating repositories), intrant (the joined namespace), all (includes both of the above), default (intrant)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "mode",
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
          "key": "perPage",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "schema": {
            "items": {
              "properties": {
                "html_url": {
                  "title": "access address namespace",
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "name": {
                  "title": "namespace name",
                  "type": "string"
                },
                "path": {
                  "title": "namespace path",
                  "type": "string"
                },
                "type": {
                  "title": "namespace type, user: User; group: Organization",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "path",
                "name",
                "html_url",
                "type"
              ],
              "type": "object"
            },
            "type": "array"
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
  "tags": [
    "Users"
  ]
}
```
