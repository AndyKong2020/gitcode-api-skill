# Delete Enterprise Member
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-8-enterprises-enterprise-members-usernames](https://docs.gitcode.com/en/docs/apis/delete-api-v-8-enterprises-enterprise-members-usernames)
Category: Enterprise
- Method: `DELETE`
- Path: `/api/v8/enterprises/{enterprise}/members/{username}`
- Operation ID: `delete_api_v8_enterprises_{enterprise}_members_{usernames}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | integer | Enterprise ID |
| username | path | true | string |  |
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
Example:
```json
{
  "active": true,
  "role": "admin",
  "url": "https://api.gitcode.com/api/v5/enterprises/go-tribe/members/dengmengmian",
  "user": {
    "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
    "html_url": "https://gitcode.com/dengmengmian",
    "id": "268",
    "login": "dengmengmian",
    "name": "Mavan",
    "url": "https://api.gitcode.com/api/v5/dengmengmian"
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
  "method": "delete",
  "operationId": "delete_api_v8_enterprises_{enterprise}_members_{usernames}",
  "parameters": [
    {
      "description": "Enterprise ID",
      "example": 0,
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "",
      "in": "path",
      "name": "username",
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
  "path": "/api/v8/enterprises/{enterprise}/members/{username}",
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
    "method": "DELETE",
    "name": "Delete Enterprise Member",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "members",
        ":username"
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
            "content": "(Required) Enterprise ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "username",
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
            "role": "admin",
            "url": "https://api.gitcode.com/api/v5/enterprises/go-tribe/members/dengmengmian",
            "user": {
              "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
              "html_url": "https://gitcode.com/dengmengmian",
              "id": "268",
              "login": "dengmengmian",
              "name": "Mavan",
              "url": "https://api.gitcode.com/api/v5/dengmengmian"
            }
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
    "Organizations"
  ]
}
```
