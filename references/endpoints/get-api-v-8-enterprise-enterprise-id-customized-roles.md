# Get Custom Role of Enterprise
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-customized-roles](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-customized-roles)
Category: Issues
- Method: `GET`
- Path: `/api/v8/enterprise/{enterprise_id}/customized_roles`
- Operation ID: `get_api_v8_enterprise_{enterprise_id}_customized_roles`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise_id | path | true | string | Enterprise ID |
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
      "role_type": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      }
    },
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
  "operationId": "get_api_v8_enterprise_{enterprise_id}_customized_roles",
  "parameters": [
    {
      "description": "Enterprise ID",
      "in": "path",
      "name": "enterprise_id",
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
  "path": "/api/v8/enterprise/{enterprise_id}/customized_roles",
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
    "name": "Get Custom Role of Enterprise",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprise",
        ":enterprise_id",
        "customized_roles"
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
            "content": "(Required) Enterprise ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise_id",
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
                "role_type": {
                  "type": "string"
                },
                "updated_at": {
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
  "tags": []
}
```
