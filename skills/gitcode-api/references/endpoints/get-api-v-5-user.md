# Get Profile of Authorized User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user)
Category: Users
- Method: `GET`
- Path: `/api/v5/user`
- Operation ID: `get_api_v5_user`
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
  "properties": {
    "avatar_url": {
      "type": "string"
    },
    "bio": {
      "type": "string"
    },
    "blog": {
      "type": "string"
    },
    "company": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "followers": {
      "type": "integer"
    },
    "followers_url": {
      "type": "string"
    },
    "following": {
      "type": "integer"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "login": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "top_languages": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "type": {
      "type": "string"
    },
    "url": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "avatar_url": "https://cdn-img.gitcode.com/fa/be/2fa2be6d3ffd01599dbc0a3c71ee9ec4cadb82f63a7a8489187645064ad95e59.png?time=1694709764757",
      "bio": "a PM ",
      "blog": "https://gitcode.com",
      "company": "",
      "email": "xiongjiamu@163.com",
      "followers": 8,
      "followers_url": "https://api.gitcode.com/api/v5/users/gitcode-xxm/followers",
      "following": 35,
      "html_url": "https://gitcode.com/gitcode-xxm",
      "id": "64e5ed8f7e20aa73efcbc302",
      "login": "gitcode-xxm",
      "name": "xxm",
      "top_languages": [
        "Python",
        "Markdown",
        "C++",
        "C",
        "HTML"
      ],
      "type": "User",
      "url": "https://api.gitcode.com/api/v5/gitcode-xxm"
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
  "operationId": "get_api_v5_user",
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
  "path": "/api/v5/user",
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
    "name": "Get Profile of Authorized User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user"
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
                "avatar_url": "https://cdn-img.gitcode.com/fa/be/2fa2be6d3ffd01599dbc0a3c71ee9ec4cadb82f63a7a8489187645064ad95e59.png?time=1694709764757",
                "bio": "a PM ",
                "blog": "https://gitcode.com",
                "company": "",
                "email": "xiongjiamu@163.com",
                "followers": 8,
                "followers_url": "https://api.gitcode.com/api/v5/users/gitcode-xxm/followers",
                "following": 35,
                "html_url": "https://gitcode.com/gitcode-xxm",
                "id": "64e5ed8f7e20aa73efcbc302",
                "login": "gitcode-xxm",
                "name": "xxm",
                "top_languages": [
                  "Python",
                  "Markdown",
                  "C++",
                  "C",
                  "HTML"
                ],
                "type": "User",
                "url": "https://api.gitcode.com/api/v5/gitcode-xxm"
              }
            }
          },
          "schema": {
            "properties": {
              "avatar_url": {
                "type": "string"
              },
              "bio": {
                "type": "string"
              },
              "blog": {
                "type": "string"
              },
              "company": {
                "type": "string"
              },
              "email": {
                "type": "string"
              },
              "followers": {
                "type": "integer"
              },
              "followers_url": {
                "type": "string"
              },
              "following": {
                "type": "integer"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "top_languages": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "type": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
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
  "tags": [
    "Users"
  ]
}
```
