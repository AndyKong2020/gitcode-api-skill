# Get Organization Custom Role
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-org-customized-roles](https://docs.gitcode.com/en/docs/apis/get-api-v-5-org-org-customized-roles)
Category: Organizations
- Method: `GET`
- Path: `/api/v5/orgs/{org}/customized_roles`
- Operation ID: `get_api_v5_org_{org}_customized_roles`
- Tags: `Organizations`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
## Responses
### `200`
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
      "access_level": {
        "type": "integer"
      },
      "created_at": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "id": {
        "type": "string"
      },
      "member_count": {
        "type": "integer"
      },
      "mgnt_mode": {
        "type": "integer"
      },
      "name": {
        "type": "string"
      },
      "name_cn": {
        "type": "string"
      },
      "product_id": {
        "type": "string"
      },
      "role_from": {
        "type": "string"
      },
      "role_type": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      }
    },
    "required": [
      "id",
      "name",
      "name_cn",
      "product_id",
      "access_level",
      "created_at",
      "role_type",
      "updated_at",
      "description",
      "member_count",
      "role_from",
      "mgnt_mode"
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
  "operationId": "get_api_v5_org_{org}_customized_roles",
  "parameters": [
    {
      "description": "Organization's path (path/login)",
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
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/orgs/{org}/customized_roles",
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
    "name": "Get Organization Custom Role",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
        "customized_roles"
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
            "content": "(Required) Organization's path (path/login)",
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
          "schema": {
            "items": {
              "properties": {
                "access_level": {
                  "type": "integer"
                },
                "created_at": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "id": {
                  "type": "string"
                },
                "member_count": {
                  "type": "integer"
                },
                "mgnt_mode": {
                  "type": "integer"
                },
                "name": {
                  "type": "string"
                },
                "name_cn": {
                  "type": "string"
                },
                "product_id": {
                  "type": "string"
                },
                "role_from": {
                  "type": "string"
                },
                "role_type": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "name_cn",
                "product_id",
                "access_level",
                "created_at",
                "role_type",
                "updated_at",
                "description",
                "member_count",
                "role_from",
                "mgnt_mode"
              ],
              "type": "object"
            },
            "type": "array"
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
    "Organizations"
  ]
}
```
