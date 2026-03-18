# Get All Comments of an Enterprise's Certain Issue
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number-comments](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number-comments)
Category: Issues
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/issues/{number}/comments`
- Operation ID: `get_api_v5_enterprises_{enterprise}_issues_{number}_comments`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | Repository space address (organization or individual's address path) |
| number | path | true | integer | issue Global Unique ID |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | Number of items per page: Maximum 100, default 20. |
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
      "body": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "target": {
        "properties": {
          "issue": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "iid": {
                "type": "integer"
              },
              "title": {
                "type": "string"
              }
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "updated_at": {
        "type": "string"
      },
      "user": {
        "properties": {
          "id": {
            "type": "integer"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "body": "etst",
  "created_at": "2024-12-10T16:02:21+08:00",
  "id": 1535981,
  "target": {
    "issue": {
      "id": 471521,
      "iid": 1,
      "title": "bbbbb"
    }
  },
  "updated_at": "2024-12-10T16:02:21+08:00",
  "user": {
    "id": 287,
    "login": "csdn_fenglh",
    "name": "fenglh",
    "type": "User"
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
  "operationId": "get_api_v5_enterprises_{enterprise}_issues_{number}_comments",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "example": "",
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "issue Global Unique ID",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Number of items per page: Maximum 100, default 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/enterprises/{enterprise}/issues/{number}/comments",
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
    "name": "Get All Comments of an Enterprise's Certain Issue",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "enterprises",
        ":enterprise",
        "issues",
        ":number",
        "comments"
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
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "Number of items per page: Maximum 100, default 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (organization or individual's address path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) issue Global Unique ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
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
            "body": "etst",
            "created_at": "2024-12-10T16:02:21+08:00",
            "id": 1535981,
            "target": {
              "issue": {
                "id": 471521,
                "iid": 1,
                "title": "bbbbb"
              }
            },
            "updated_at": "2024-12-10T16:02:21+08:00",
            "user": {
              "id": 287,
              "login": "csdn_fenglh",
              "name": "fenglh",
              "type": "User"
            }
          },
          "schema": {
            "items": {
              "properties": {
                "body": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "target": {
                  "properties": {
                    "issue": {
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "iid": {
                          "type": "integer"
                        },
                        "title": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                },
                "updated_at": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "id": {
                      "type": "integer"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
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
    "Issues"
  ]
}
```
