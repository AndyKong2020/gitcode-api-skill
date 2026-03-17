# List All Members Of The Enterprise
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprise-members](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprise-members)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/enterprises/{enterprise}/members`
- Operation ID: `get_api_v8_enterprises_{enterprise}_members`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | integer | Enterprise ID |
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
      "active": {
        "type": "boolean"
      },
      "enterprise_email": {
        "type": "string"
      },
      "role": {
        "type": "string"
      },
      "role_id": {
        "type": "string"
      },
      "role_name": {
        "type": "string"
      },
      "role_name_cn": {
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
          "url": {
            "type": "string"
          },
          "user_id": {
            "type": "string"
          }
        },
        "required": [
          "avatar_url",
          "html_url",
          "id",
          "object_id",
          "login",
          "name",
          "url",
          "user_id"
        ],
        "type": "object"
      }
    },
    "required": [
      "user",
      "active",
      "role",
      "role_name",
      "role_id",
      "role_name_cn"
    ],
    "type": "object"
  },
  "type": "array"
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
  "operationId": "get_api_v8_enterprises_{enterprise}_members",
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
  "path": "/api/v8/enterprises/{enterprise}/members",
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
    "name": "List All Members Of The Enterprise",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
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
            "content": "(Required) Enterprise ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
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
          "schema": {
            "items": {
              "properties": {
                "active": {
                  "type": "boolean"
                },
                "enterprise_email": {
                  "type": "string"
                },
                "role": {
                  "type": "string"
                },
                "role_id": {
                  "type": "string"
                },
                "role_name": {
                  "type": "string"
                },
                "role_name_cn": {
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
                    "url": {
                      "type": "string"
                    },
                    "user_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "avatar_url",
                    "html_url",
                    "id",
                    "object_id",
                    "login",
                    "name",
                    "url",
                    "user_id"
                  ],
                  "type": "object"
                }
              },
              "required": [
                "user",
                "active",
                "role",
                "role_name",
                "role_id",
                "role_name_cn"
              ],
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
