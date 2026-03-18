# Search Users
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-users](https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-users)
Category: Search
- Method: `GET`
- Path: `/api/v5/search/users`
- Operation ID: `get_api_v5_search_users`
- Tags: `Search`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number, maximum is 100. |
| per_page | query | false | integer | The number of items per page, with a maximum of 50. |
| q | query | true | string | Search keyword |
| sort | query | false | string | sort_field: The sorting field,可以选择 joined_at (registration time), with the default being the best match. |
| order | query | false | string | Sort order (default: desc) |
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
      "created_at": {
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
      "avatar_url": "https://cdn-img.gitcode.com/bb/bf/b1b0bff5bafab700603248485bc4a236061f84433741855a9ce8b0c42c8.png",
      "created_at": "2024-11-15T00:00:00+08:00",
      "html_url": "https://gitcode.com/wu_com",
      "id": "25235036",
      "login": "wu_com",
      "name": "wu_com"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "avatar_url": "https://cdn-img.gitcode.com/ad/ec/a8670853d9137e2c34efbc14904985a7cc5998929bfebca9ceb8626e170.png",
      "created_at": "2024-11-15T00:00:00+08:00",
      "html_url": "https://gitcode.com/wu5567488",
      "id": "25153392",
      "login": "wu5567488",
      "name": "wu5567488"
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
  "operationId": "get_api_v5_search_users",
  "parameters": [
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
      "description": "Current page number, maximum is 100.",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 50.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Search keyword",
      "in": "query",
      "name": "q",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "sort_field: The sorting field,可以选择 joined_at (registration time), with the default being the best match.",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order (default: desc)",
      "in": "query",
      "name": "order",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/search/users",
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
    "name": "Search Users",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "search",
        "users"
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
            "content": "Current page number, maximum is 100.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 50.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Search keyword",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "q",
          "value": ""
        },
        {
          "description": {
            "content": "sort_field: The sorting field,可以选择 joined_at (registration time), with the default being the best match.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order (default: desc)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "order",
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
                "avatar_url": "https://cdn-img.gitcode.com/bb/bf/b1b0bff5bafab700603248485bc4a236061f84433741855a9ce8b0c42c8.png",
                "created_at": "2024-11-15T00:00:00+08:00",
                "html_url": "https://gitcode.com/wu_com",
                "id": "25235036",
                "login": "wu_com",
                "name": "wu_com"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "avatar_url": "https://cdn-img.gitcode.com/ad/ec/a8670853d9137e2c34efbc14904985a7cc5998929bfebca9ceb8626e170.png",
                "created_at": "2024-11-15T00:00:00+08:00",
                "html_url": "https://gitcode.com/wu5567488",
                "id": "25153392",
                "login": "wu5567488",
                "name": "wu5567488"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "avatar_url": {
                  "type": "string"
                },
                "created_at": {
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
    "Search"
  ]
}
```
