# List All Members of An Organization
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-members](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-members)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}/members`
- Operation ID: `get_api_v5_orgs_{org}_members`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | The path of the enterprise (path/login) |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| role | query | false | string | Filter members by role (all/admin/member) |
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
      "avatar_url": {
        "type": "string"
      },
      "followers_url": {
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
      "member_role": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "object_id": {
        "type": "string"
      },
      "type": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "user_id": {
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
    "description": "",
    "summary": "Successful Example",
    "value": {
      "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
      "followers_url": "https://api.gitcode.com/api/v5users/dengmengmian/followers",
      "html_url": "https://gitcode.com/dengmengmian",
      "id": "268",
      "login": "dengmengmian",
      "member_role": "admin",
      "name": "Mavan",
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
  "operationId": "get_api_v5_orgs_{org}_members",
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
    },
    {
      "description": "Current page number: defaults to 1",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Filter members by role (all/admin/member)",
      "in": "query",
      "name": "role",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/orgs/{org}/members",
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
    "name": "List All Members of An Organization",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
        "members"
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
            "content": "Current page number: defaults to 1",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Filter members by role (all/admin/member)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "role",
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
              "description": "",
              "summary": "Successful Example",
              "value": {
                "avatar_url": "https://cdn-img.gitcode.com/ec/fb/430ecf07b9ee91bbbbf341d92a36783d06e69086f82ce8cf5a6406f79f1c9cf4.png",
                "followers_url": "https://api.gitcode.com/api/v5users/dengmengmian/followers",
                "html_url": "https://gitcode.com/dengmengmian",
                "id": "268",
                "login": "dengmengmian",
                "member_role": "admin",
                "name": "Mavan",
                "type": "User",
                "url": "https://api.gitcode.com/api/v5/dengmengmian"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "avatar_url": {
                  "type": "string"
                },
                "followers_url": {
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
                "member_role": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "object_id": {
                  "type": "string"
                },
                "type": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "user_id": {
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
    "Organizations"
  ]
}
```
