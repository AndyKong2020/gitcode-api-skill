# Get Authorized User's Member Profile in an Organization
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-memberships-orgs-org](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-memberships-orgs-org)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/user/memberships/orgs/{org}`
- Operation ID: `get_api_v5_user_memberships_orgs_{org}`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | The path of the enterprise (path/login) |
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
    "avatar_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "organization": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "login": {
          "type": "string"
        },
        "name": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "path": {
      "type": "string"
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
    "summary": "Successful Example",
    "value": {
      "active": true,
      "avatar_url": "https://cdn-img.gitcode.com/bb/eb/b3b4e25b54add3c80961d3ba2e3724d03998eae467c99ab898ea39e48cb1b4f6.png?time1717675394237",
      "id": 1783195,
      "name": "gotribe",
      "organization": {
        "id": 1783195,
        "login": "Go-Tribe",
        "name": "gotribe"
      },
      "path": "Go-Tribe",
      "role": "admin",
      "url": "https://gitcode.com/Go-Tribe",
      "user": {
        "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
        "html_url": "https://gitcode.com/dengmengmian",
        "id": "650d67fbae6d795139b49b41",
        "login": "dengmengmian",
        "name": "Mavan"
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
  "operationId": "get_api_v5_user_memberships_orgs_{org}",
  "parameters": [
    {
      "description": "The path of the enterprise (path/login)",
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
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/user/memberships/orgs/{org}",
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
    "name": "Get Authorized User's Member Profile in an Organization",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "memberships",
        "orgs",
        ":org"
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "active": true,
                "avatar_url": "https://cdn-img.gitcode.com/bb/eb/b3b4e25b54add3c80961d3ba2e3724d03998eae467c99ab898ea39e48cb1b4f6.png?time1717675394237",
                "id": 1783195,
                "name": "gotribe",
                "organization": {
                  "id": 1783195,
                  "login": "Go-Tribe",
                  "name": "gotribe"
                },
                "path": "Go-Tribe",
                "role": "admin",
                "url": "https://gitcode.com/Go-Tribe",
                "user": {
                  "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
                  "html_url": "https://gitcode.com/dengmengmian",
                  "id": "650d67fbae6d795139b49b41",
                  "login": "dengmengmian",
                  "name": "Mavan"
                }
              }
            }
          },
          "schema": {
            "properties": {
              "active": {
                "type": "integer"
              },
              "avatar_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "organization": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "path": {
                "type": "string"
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
