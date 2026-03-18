# Get a User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username](https://docs.gitcode.com/en/docs/apis/get-api-v-5-users-username)
Category: Users
- Method: `GET`
- Path: `/api/v5/users/{username}`
- Operation ID: `get_api_v5_users_{username}`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| username | path | true | string | username (String, required) - The username of the user. |
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
      "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
      "bio": "Nacos is an open-source service governance middleware by Alibaba, integrating dynamic service discovery, configuration management, and service metadata management functionalities. It is widely used in microservice architectures to simplify the service governance process.",
      "blog": "https://www.dengmengmian.com",
      "company": "developer",
      "email": "my@dengmengmian.com",
      "followers": 0,
      "followers_url": "https://api.gitcode.com/api/v5/users/dengmengmian/followers",
      "following": 6,
      "html_url": "https://gitcode.com/dengmengmian",
      "id": "650d67fbae6d795139b49b41",
      "login": "dengmengmian",
      "name": "Mavan",
      "top_languages": [
        "Python",
        "Shell"
      ],
      "type": "User",
      "url": "https://api.gitcode.com/api/v5/dengmengmian"
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
  "operationId": "get_api_v5_users_{username}",
  "parameters": [
    {
      "description": "username (String, required) - The username of the user.",
      "example": "",
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
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/users/{username}",
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
    "name": "Get a User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "users",
        ":username"
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
            "content": "(Required) username (String, required) - The username of the user.",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
                "bio": "Nacos is an open-source service governance middleware by Alibaba, integrating dynamic service discovery, configuration management, and service metadata management functionalities. It is widely used in microservice architectures to simplify the service governance process.",
                "blog": "https://www.dengmengmian.com",
                "company": "developer",
                "email": "my@dengmengmian.com",
                "followers": 0,
                "followers_url": "https://api.gitcode.com/api/v5/users/dengmengmian/followers",
                "following": 6,
                "html_url": "https://gitcode.com/dengmengmian",
                "id": "650d67fbae6d795139b49b41",
                "login": "dengmengmian",
                "name": "Mavan",
                "top_languages": [
                  "Python",
                  "Shell"
                ],
                "type": "User",
                "url": "https://api.gitcode.com/api/v5/dengmengmian"
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
