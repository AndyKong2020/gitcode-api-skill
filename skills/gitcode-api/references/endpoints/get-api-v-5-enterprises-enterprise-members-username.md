# Get a Company's Member
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-members-username](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-members-username)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/members/{username}`
- Operation ID: `get_api_v5_enterprises_{enterprise}_members_{username}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | The path of the enterprise (path/login) |
| username | path | true | string | username (alias: login) |
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
    "active": {
      "type": "integer"
    },
    "enterprise": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "role": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "user": {
      "properties": {
        "avatar_url": {
          "type": "string"
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
        "object_id": {
          "type": "string"
        },
        "user_id": {
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "description": "",
    "summary": "Successful Example",
    "value": {
      "active": true,
      "enterprise": {
        "id": 0,
        "url": "https://gitcode.com/dengmengmian"
      },
      "role": "admin",
      "url": "https://gitcode.com/dengmengmian",
      "user": {
        "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
        "html_url": "https://gitcode.com/dengmengmian",
        "id": "268",
        "login": "dengmengmian",
        "name": "dengmengmian"
      }
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
  "operationId": "get_api_v5_enterprises_{enterprise}_members_{username}",
  "parameters": [
    {
      "description": "The path of the enterprise (path/login)",
      "example": "",
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "username (alias: login)",
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
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/enterprises/{enterprise}/members/{username}",
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
    "name": "Get a Company's Member",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
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
            "content": "(Required) The path of the enterprise (path/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) username (alias: login)",
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
              "description": "",
              "summary": "Successful Example",
              "value": {
                "active": true,
                "enterprise": {
                  "id": 0,
                  "url": "https://gitcode.com/dengmengmian"
                },
                "role": "admin",
                "url": "https://gitcode.com/dengmengmian",
                "user": {
                  "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
                  "html_url": "https://gitcode.com/dengmengmian",
                  "id": "268",
                  "login": "dengmengmian",
                  "name": "dengmengmian"
                }
              }
            }
          },
          "schema": {
            "properties": {
              "active": {
                "type": "integer"
              },
              "enterprise": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "role": {
                "type": "string"
              },
              "url": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "avatar_url": {
                    "type": "string"
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
                  "object_id": {
                    "type": "string"
                  },
                  "user_id": {
                    "type": "string"
                  }
                },
                "type": "object"
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
    "Organizations"
  ]
}
```
