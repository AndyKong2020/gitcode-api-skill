# Mark Notifications as Read in a Repository
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-notifications](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-notifications)
Category: Users
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/notifications`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_notifications`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string |  |
| repo | path | true | string |  |
| access_token | query | true | string | User authorization code |
| ids | query | false | string | Specify a group of notification IDs, separated by commas. |
## Request Body
No request body.
## Responses
### `200`
Headers:
```json
{}
```
#### `*/*`
Schema:
```json
{
  "title": "",
  "type": "undefined"
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
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_notifications",
  "parameters": [
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "",
      "in": "path",
      "name": "repo",
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
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Specify a group of notification IDs, separated by commas.",
      "in": "query",
      "name": "ids",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/notifications",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "*/*"
      }
    ],
    "method": "PUT",
    "name": "Mark Notifications as Read in a Repository",
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
        "notifications"
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
            "content": "Specify a group of notification IDs, separated by commas.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "ids",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "*/*": {
          "schema": {
            "title": "",
            "type": "undefined"
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
