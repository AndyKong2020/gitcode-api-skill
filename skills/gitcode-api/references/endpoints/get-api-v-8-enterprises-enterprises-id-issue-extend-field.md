# Get the list of custom fields for enterprise Issue
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprises-id-issue-extend-field](https://docs.gitcode.com/en/docs/apis/get-api-v-8-enterprises-enterprises-id-issue-extend-field)
Category: Enterprise
- Method: `GET`
- Path: `/api/v8/enterprises/{enterprise_id}/issue_extend_field`
- Operation ID: `get_api_v8_enterprises_{enterprises_id}_issue_extend_field`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise_id | path | true | string | Enterprise ID |
| access_token | query | true | string | User authorization code |
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
    "required": false,
    "schema": {
      "type": "string"
    }
  },
  "total_page": {
    "description": "Total pages",
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
      "created_time": {
        "description": "creation time",
        "type": "string"
      },
      "description": {
        "description": "Field Description",
        "type": "string"
      },
      "field_type": {
        "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
        "type": "string"
      },
      "field_visibility": {
        "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
        "type": "integer"
      },
      "id": {
        "description": "id",
        "type": "integer"
      },
      "name": {
        "description": "Field Name",
        "type": "string"
      },
      "options": {
        "description": "Option details, only option type is returned",
        "items": {
          "properties": {
            "created_time": {
              "type": "string"
            },
            "extend_field_id": {
              "type": "integer"
            },
            "field_value": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "sort_num": {
              "type": "integer"
            },
            "updated_time": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "extend_field_id",
            "sort_num",
            "field_value",
            "created_time",
            "updated_time"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "types": {
        "description": "The list of issue types associated with this field",
        "items": {
          "properties": {
            "desc": {
              "type": "string"
            },
            "enabled": {
              "type": "boolean"
            },
            "id": {
              "type": "integer"
            },
            "kind": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "sort_num": {
              "type": "integer"
            }
          },
          "required": [
            "id",
            "name",
            "desc",
            "enabled",
            "sort_num",
            "kind"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "updated_time": {
        "description": "Update time",
        "type": "string"
      }
    },
    "required": [
      "id",
      "name",
      "description",
      "field_type",
      "field_visibility",
      "created_time",
      "updated_time",
      "options",
      "types"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
[
  {
    "created_time": "2025-12-18T14:50:25+08:00",
    "description": "",
    "field_type": "select_multi",
    "field_visibility": 0,
    "id": 48,
    "name": "Multiple Choice Dropdown",
    "options": [
      {
        "created_time": "2025-12-18T14:50:34+08:00",
        "extend_field_id": 48,
        "field_value": "1",
        "id": 51,
        "sort_num": 9999,
        "updated_time": "2025-12-18T14:50:34+08:00"
      },
      {
        "created_time": "2025-12-18T14:50:36+08:00",
        "extend_field_id": 48,
        "field_value": "2",
        "id": 52,
        "sort_num": 9999,
        "updated_time": "2025-12-18T14:50:36+08:00"
      },
      {
        "created_time": "2025-12-18T14:50:38+08:00",
        "extend_field_id": 48,
        "field_value": "3",
        "id": 53,
        "sort_num": 9999,
        "updated_time": "2025-12-18T14:50:38+08:00"
      },
      {
        "created_time": "2025-12-18T14:50:41+08:00",
        "extend_field_id": 48,
        "field_value": "4",
        "id": 54,
        "sort_num": 9999,
        "updated_time": "2025-12-18T14:50:41+08:00"
      }
    ],
    "types": [
      {
        "desc": "",
        "enabled": true,
        "id": 425,
        "kind": 0,
        "name": "requirement",
        "sort_num": 1
      }
    ],
    "updated_time": "2025-12-18T14:50:25+08:00"
  },
  {
    "created_time": "2025-12-18T10:58:24+08:00",
    "description": "",
    "field_type": "select_single",
    "field_visibility": 1,
    "id": 47,
    "name": "test3",
    "options": [
      {
        "created_time": "2025-12-18T10:58:58+08:00",
        "extend_field_id": 47,
        "field_value": "1",
        "id": 49,
        "sort_num": 9999,
        "updated_time": "2025-12-18T10:58:58+08:00"
      },
      {
        "created_time": "2025-12-18T10:59:02+08:00",
        "extend_field_id": 47,
        "field_value": "2",
        "id": 50,
        "sort_num": 9999,
        "updated_time": "2025-12-18T10:59:02+08:00"
      }
    ],
    "types": [
      {
        "desc": "",
        "enabled": true,
        "id": 425,
        "kind": 0,
        "name": "requirement",
        "sort_num": 1
      }
    ],
    "updated_time": "2025-12-18T10:58:24+08:00"
  },
  {
    "created_time": "2025-12-18T10:57:54+08:00",
    "description": "1",
    "field_type": "text_single",
    "field_visibility": 1,
    "id": 46,
    "name": "test2",
    "types": [],
    "updated_time": "2025-12-18T10:57:54+08:00"
  },
  {
    "created_time": "2025-12-18T10:46:51+08:00",
    "description": "",
    "field_type": "text_single",
    "field_visibility": 0,
    "id": 45,
    "name": "test1",
    "types": [
      {
        "desc": "",
        "enabled": true,
        "id": 425,
        "kind": 0,
        "name": "requirement",
        "sort_num": 1
      }
    ],
    "updated_time": "2026-01-07T09:22:17+08:00"
  }
]
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
  "operationId": "get_api_v8_enterprises_{enterprises_id}_issue_extend_field",
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
  "path": "/api/v8/enterprises/{enterprise_id}/issue_extend_field",
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
    "name": "Get the list of custom fields for enterprise Issue",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise_id",
        "issue_extend_field"
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
          "example": [
            {
              "created_time": "2025-12-18T14:50:25+08:00",
              "description": "",
              "field_type": "select_multi",
              "field_visibility": 0,
              "id": 48,
              "name": "Multiple Choice Dropdown",
              "options": [
                {
                  "created_time": "2025-12-18T14:50:34+08:00",
                  "extend_field_id": 48,
                  "field_value": "1",
                  "id": 51,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T14:50:34+08:00"
                },
                {
                  "created_time": "2025-12-18T14:50:36+08:00",
                  "extend_field_id": 48,
                  "field_value": "2",
                  "id": 52,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T14:50:36+08:00"
                },
                {
                  "created_time": "2025-12-18T14:50:38+08:00",
                  "extend_field_id": 48,
                  "field_value": "3",
                  "id": 53,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T14:50:38+08:00"
                },
                {
                  "created_time": "2025-12-18T14:50:41+08:00",
                  "extend_field_id": 48,
                  "field_value": "4",
                  "id": 54,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T14:50:41+08:00"
                }
              ],
              "types": [
                {
                  "desc": "",
                  "enabled": true,
                  "id": 425,
                  "kind": 0,
                  "name": "requirement",
                  "sort_num": 1
                }
              ],
              "updated_time": "2025-12-18T14:50:25+08:00"
            },
            {
              "created_time": "2025-12-18T10:58:24+08:00",
              "description": "",
              "field_type": "select_single",
              "field_visibility": 1,
              "id": 47,
              "name": "test3",
              "options": [
                {
                  "created_time": "2025-12-18T10:58:58+08:00",
                  "extend_field_id": 47,
                  "field_value": "1",
                  "id": 49,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T10:58:58+08:00"
                },
                {
                  "created_time": "2025-12-18T10:59:02+08:00",
                  "extend_field_id": 47,
                  "field_value": "2",
                  "id": 50,
                  "sort_num": 9999,
                  "updated_time": "2025-12-18T10:59:02+08:00"
                }
              ],
              "types": [
                {
                  "desc": "",
                  "enabled": true,
                  "id": 425,
                  "kind": 0,
                  "name": "requirement",
                  "sort_num": 1
                }
              ],
              "updated_time": "2025-12-18T10:58:24+08:00"
            },
            {
              "created_time": "2025-12-18T10:57:54+08:00",
              "description": "1",
              "field_type": "text_single",
              "field_visibility": 1,
              "id": 46,
              "name": "test2",
              "types": [],
              "updated_time": "2025-12-18T10:57:54+08:00"
            },
            {
              "created_time": "2025-12-18T10:46:51+08:00",
              "description": "",
              "field_type": "text_single",
              "field_visibility": 0,
              "id": 45,
              "name": "test1",
              "types": [
                {
                  "desc": "",
                  "enabled": true,
                  "id": 425,
                  "kind": 0,
                  "name": "requirement",
                  "sort_num": 1
                }
              ],
              "updated_time": "2026-01-07T09:22:17+08:00"
            }
          ],
          "schema": {
            "items": {
              "properties": {
                "created_time": {
                  "description": "creation time",
                  "type": "string"
                },
                "description": {
                  "description": "Field Description",
                  "type": "string"
                },
                "field_type": {
                  "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
                  "type": "string"
                },
                "field_visibility": {
                  "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
                  "type": "integer"
                },
                "id": {
                  "description": "id",
                  "type": "integer"
                },
                "name": {
                  "description": "Field Name",
                  "type": "string"
                },
                "options": {
                  "description": "Option details, only option type is returned",
                  "items": {
                    "properties": {
                      "created_time": {
                        "type": "string"
                      },
                      "extend_field_id": {
                        "type": "integer"
                      },
                      "field_value": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "sort_num": {
                        "type": "integer"
                      },
                      "updated_time": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "extend_field_id",
                      "sort_num",
                      "field_value",
                      "created_time",
                      "updated_time"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "types": {
                  "description": "The list of issue types associated with this field",
                  "items": {
                    "properties": {
                      "desc": {
                        "type": "string"
                      },
                      "enabled": {
                        "type": "boolean"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "kind": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      },
                      "sort_num": {
                        "type": "integer"
                      }
                    },
                    "required": [
                      "id",
                      "name",
                      "desc",
                      "enabled",
                      "sort_num",
                      "kind"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "updated_time": {
                  "description": "Update time",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "name",
                "description",
                "field_type",
                "field_visibility",
                "created_time",
                "updated_time",
                "options",
                "types"
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
          "required": false,
          "schema": {
            "type": "string"
          }
        },
        "total_page": {
          "description": "Total pages",
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
