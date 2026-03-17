# Get the list of projects associated with Enterprise milestones
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-groups-projects](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-groups-projects)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/enterprises/{enterprise}/groups/projects`
- Operation ID: `get_api_v8_enterprise_{enterprise_id}_groups_projects`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | Enterprise ID |
| access_token | query | true | string | User authorization code |
| group_name | query | false | string | Organization Name |
## Request Body
No request body.
## Responses
### `200`
Successful Response
Headers:
```json
{
  "total_count": {
    "description": "Total quantity",
    "example": "",
    "required": false,
    "schema": {
      "type": "string"
    }
  },
  "total_page": {
    "description": "Total pages",
    "example": "",
    "required": false,
    "schema": {
      "type": "string"
    }
  }
}
```
#### `application/json`
Schema:
```json
{
  "items": {
    "properties": {
      "created_at": {
        "title": "creation time",
        "type": "string"
      },
      "full_name": {
        "title": "namespace path",
        "type": "string"
      },
      "human_name": {
        "title": "namespace name",
        "type": "string"
      },
      "id": {
        "title": "id",
        "type": "integer"
      },
      "name": {
        "title": "Project Name",
        "type": "string"
      },
      "path": {
        "title": "Project Path",
        "type": "string"
      },
      "updated_at": {
        "title": "Update time",
        "type": "string"
      }
    },
    "required": [
      "id",
      "full_name",
      "human_name",
      "path",
      "name",
      "created_at",
      "updated_at"
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
  "operationId": "get_api_v8_enterprise_{enterprise_id}_groups_projects",
  "parameters": [
    {
      "description": "Enterprise ID",
      "in": "path",
      "name": "enterprise",
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
      "description": "Organization Name",
      "in": "query",
      "name": "group_name",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v8/enterprises/{enterprise}/groups/projects",
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
    "name": "Get the list of projects associated with Enterprise milestones",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "groups",
        "projects"
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
            "content": "Organization Name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "group_name",
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
                "created_at": {
                  "title": "creation time",
                  "type": "string"
                },
                "full_name": {
                  "title": "namespace path",
                  "type": "string"
                },
                "human_name": {
                  "title": "namespace name",
                  "type": "string"
                },
                "id": {
                  "title": "id",
                  "type": "integer"
                },
                "name": {
                  "title": "Project Name",
                  "type": "string"
                },
                "path": {
                  "title": "Project Path",
                  "type": "string"
                },
                "updated_at": {
                  "title": "Update time",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "full_name",
                "human_name",
                "path",
                "name",
                "created_at",
                "updated_at"
              ],
              "type": "object"
            },
            "type": "array"
          }
        }
      },
      "description": "Successful Response",
      "headers": {
        "total_count": {
          "description": "Total quantity",
          "example": "",
          "required": false,
          "schema": {
            "type": "string"
          }
        },
        "total_page": {
          "description": "Total pages",
          "example": "",
          "required": false,
          "schema": {
            "type": "string"
          }
        }
      }
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
