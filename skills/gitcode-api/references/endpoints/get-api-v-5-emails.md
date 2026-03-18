# Get All Email Addresses of Authorized User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-emails](https://docs.gitcode.com/en/docs/apis/get-api-v-5-emails)
Category: Users
- Method: `GET`
- Path: `/api/v5/emails`
- Operation ID: `get_api_v5_emails`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
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
  "items": {
    "properties": {
      "email": {
        "type": "string"
      },
      "state": {
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
      "email": "my@dengmengmian.com",
      "state": "confirmed"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "email": "xxxx@qq.com",
      "state": "confirmed"
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
  "operationId": "get_api_v5_emails",
  "parameters": [
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
  "path": "/api/v5/emails",
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
    "name": "Get All Email Addresses of Authorized User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "emails"
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
      "variable": []
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
                "email": "my@dengmengmian.com",
                "state": "confirmed"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "email": "xxxx@qq.com",
                "state": "confirmed"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "email": {
                  "type": "string"
                },
                "state": {
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
    "Users"
  ]
}
```
