# Get associated enterprises of the organization
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-org-org-enterprise](https://docs.gitcode.com/en/docs/apis/get-api-v-8-org-org-enterprise)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/org/{org}/enterprise`
- Operation ID: `get_api_v8_org_{org}_enterprise`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path |
| access_token | query | false | string | User authorization code |
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
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ],
  "type": "object"
}
```
Example:
```json
{
  "active": true,
  "role": "member",
  "url": "https://api.gitcode.com/api/v5/enterprises/litestabc/members/malongge5",
  "user": {
    "html_url": "https://gitcode.com/malongge5",
    "id": 953,
    "login": "malongge5",
    "url": "https://api.gitcode.com/api/v5/malongge5"
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
  "operationId": "get_api_v8_org_{org}_enterprise",
  "parameters": [
    {
      "description": "Organization's path",
      "example": "",
      "in": "path",
      "name": "org",
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
  "path": "/api/v8/org/{org}/enterprise",
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
    "name": "Get associated enterprises of the organization",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "org",
        ":org",
        "enterprise"
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
          "key": "org",
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
          "example": {
            "active": true,
            "role": "member",
            "url": "https://api.gitcode.com/api/v5/enterprises/litestabc/members/malongge5",
            "user": {
              "html_url": "https://gitcode.com/malongge5",
              "id": 953,
              "login": "malongge5",
              "url": "https://api.gitcode.com/api/v5/malongge5"
            }
          },
          "schema": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "name"
            ],
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
  "tags": []
}
```
