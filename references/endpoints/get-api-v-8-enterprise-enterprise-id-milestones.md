# Get Enterprise Milestone List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-milestones](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprise-enterprise-id-milestones)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/enterprises/{enterprise}/milestones`
- Operation ID: `get_api_v8_enterprise_{enterprise_id}_milestones`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | Enterprise ID |
| access_token | query | true | string | User authorization code |
| name | query | false | string | Name |
| state | query | false | string | Status |
| order_by | query | false | string | Sort field. Optional: updated_at |
| sort | query | false | string | Sort order. Descending: desc; Ascending: asc |
| page | query | false | string | Current page number: defaults to 1 |
| per_page | query | false | string | The number of items per page, with a maximum of 100. The default is 20. |
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
      "description": {
        "title": "description",
        "type": "string"
      },
      "due_date": {
        "title": "Deadline",
        "type": "string"
      },
      "id": {
        "title": "id",
        "type": "integer"
      },
      "projects": {
        "items": {
          "properties": {
            "archived": {
              "type": "boolean"
            },
            "created_at": {
              "type": "string"
            },
            "description": {
              "type": "string"
            },
            "id": {
              "title": "Project ID",
              "type": "integer"
            },
            "name": {
              "title": "Project Name",
              "type": "string"
            },
            "name_with_namespace": {
              "type": "string"
            },
            "path": {
              "title": "Project Path",
              "type": "string"
            },
            "path_with_namespace": {
              "type": "string"
            },
            "updated_at": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "description",
            "name",
            "name_with_namespace",
            "path",
            "path_with_namespace",
            "created_at",
            "updated_at",
            "archived"
          ],
          "type": "object"
        },
        "title": "List of Associated Projects",
        "type": "array"
      },
      "start_date": {
        "title": "Start Time",
        "type": "string"
      },
      "state": {
        "title": "Status",
        "type": "string"
      },
      "title": {
        "title": "Title",
        "type": "string"
      },
      "updated_at": {
        "title": "Update time",
        "type": "string"
      }
    },
    "required": [
      "id",
      "title",
      "state",
      "created_at",
      "updated_at",
      "description",
      "projects"
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
  "operationId": "get_api_v8_enterprise_{enterprise_id}_milestones",
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
      "description": "Name",
      "in": "query",
      "name": "name",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Status",
      "example": "",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort field. Optional: updated_at",
      "in": "query",
      "name": "order_by",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order. Descending: desc; Ascending: asc",
      "in": "query",
      "name": "sort",
      "required": false,
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
        "type": "string"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v8/enterprises/{enterprise}/milestones",
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
    "name": "Get Enterprise Milestone List",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "milestones"
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
            "content": "Name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "name",
          "value": ""
        },
        {
          "description": {
            "content": "Status",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "Sort field. Optional: updated_at",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "order_by",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order. Descending: desc; Ascending: asc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
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
                "description": {
                  "title": "description",
                  "type": "string"
                },
                "due_date": {
                  "title": "Deadline",
                  "type": "string"
                },
                "id": {
                  "title": "id",
                  "type": "integer"
                },
                "projects": {
                  "items": {
                    "properties": {
                      "archived": {
                        "type": "boolean"
                      },
                      "created_at": {
                        "type": "string"
                      },
                      "description": {
                        "type": "string"
                      },
                      "id": {
                        "title": "Project ID",
                        "type": "integer"
                      },
                      "name": {
                        "title": "Project Name",
                        "type": "string"
                      },
                      "name_with_namespace": {
                        "type": "string"
                      },
                      "path": {
                        "title": "Project Path",
                        "type": "string"
                      },
                      "path_with_namespace": {
                        "type": "string"
                      },
                      "updated_at": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "description",
                      "name",
                      "name_with_namespace",
                      "path",
                      "path_with_namespace",
                      "created_at",
                      "updated_at",
                      "archived"
                    ],
                    "type": "object"
                  },
                  "title": "List of Associated Projects",
                  "type": "array"
                },
                "start_date": {
                  "title": "Start Time",
                  "type": "string"
                },
                "state": {
                  "title": "Status",
                  "type": "string"
                },
                "title": {
                  "title": "Title",
                  "type": "string"
                },
                "updated_at": {
                  "title": "Update time",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "title",
                "state",
                "created_at",
                "updated_at",
                "description",
                "projects"
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
