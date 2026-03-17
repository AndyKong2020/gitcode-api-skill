# Get a Specific Issue of an Enterprise
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number)
Category: Issues
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/issues/{number}`
- Operation ID: `get_api_v5_enterprises_{enterprise}_issues_{number}`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | Repository space address (organization or individual's address path) |
| number | path | true | integer | issue Global Unique ID |
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
    "body": {
      "type": "string"
    },
    "comments": {
      "type": "integer"
    },
    "created_at": {
      "type": "string"
    },
    "custom_fields": {
      "description": "Custom field information",
      "items": {
        "properties": {
          "field_name": {
            "description": "Custom Field Name",
            "type": "string"
          },
          "field_type": {
            "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
            "type": "string"
          },
          "field_values": {
            "description": "Custom field value",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "field_visibility": {
            "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "finished_at": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "issue_priority_detail": {
      "description": "Issue Priority",
      "properties": {
        "id": {
          "type": "string"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "title"
      ],
      "type": "object"
    },
    "issue_state": {
      "type": "string"
    },
    "issue_state_detail": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "serial": {
          "type": "integer"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "serial",
        "id"
      ],
      "type": "object"
    },
    "issue_type": {
      "type": "string"
    },
    "issue_type_detail": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "is_system": {
          "type": "boolean"
        },
        "title": {
          "type": "string"
        }
      },
      "required": [
        "title",
        "id",
        "is_system"
      ],
      "type": "object"
    },
    "labels": {
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "number": {
      "type": "string"
    },
    "priority": {
      "type": "integer"
    },
    "repository": {
      "properties": {
        "assigner": {
          "properties": {},
          "type": "object"
        },
        "created_at": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "full_name": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "paas": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "full_name",
        "path",
        "name",
        "description",
        "created_at",
        "updated_at",
        "assigner",
        "paas"
      ],
      "type": "object"
    },
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
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
      "required": [
        "avatar_url",
        "html_url",
        "id",
        "login",
        "name"
      ],
      "type": "object"
    },
    "visibility_reason": {
      "description": "Visibility, public: publicly visible, confidential: confidential, visible to project members, other: visible to project members due to other reasons",
      "type": "string"
    }
  },
  "required": [
    "id",
    "html_url",
    "number",
    "state",
    "title",
    "body",
    "user",
    "repository",
    "created_at",
    "updated_at",
    "finished_at",
    "labels",
    "issue_state",
    "comments",
    "priority",
    "issue_type",
    "issue_state_detail",
    "issue_type_detail"
  ],
  "type": "object"
}
```
Example:
```json
{
  "body": "sdfsdf",
  "created_at": "2024-12-10T16:02:12+08:00",
  "finished_at": "",
  "html_url": "https://test.gitcode.net/owner-test/wonderful1/issues/1",
  "id": 471521,
  "issue_state": "to-do items",
  "issue_state_detail": {
    "serial": 0,
    "title": "to-do items"
  },
  "labels": [],
  "number": "1",
  "priority": 0,
  "repository": {
    "assigner": {},
    "created_at": "2024-10-16T15:51:35+08:00",
    "description": "my test code repository",
    "full_name": "owner-test/wonderful1",
    "id": 686738,
    "name": "wonderful1",
    "paas": "",
    "path": "wonderful1",
    "updated_at": "2024-10-16T15:51:35+08:00"
  },
  "state": "open",
  "title": "bbbbb",
  "updated_at": "2024-12-10T16:02:21+08:00",
  "user": {
    "html_url": "https://test.gitcode.net/csdn_fenglh",
    "id": "654c61e5560ed95fd216cf31",
    "login": "csdn_fenglh",
    "name": "fenglh"
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
  "operationId": "get_api_v5_enterprises_{enterprise}_issues_{number}",
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
    }
  ],
  "path": "/api/v5/enterprises/{enterprise}/issues/{number}",
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
    "name": "Get a Specific Issue of an Enterprise",
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
        ":number"
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
            "body": "sdfsdf",
            "created_at": "2024-12-10T16:02:12+08:00",
            "finished_at": "",
            "html_url": "https://test.gitcode.net/owner-test/wonderful1/issues/1",
            "id": 471521,
            "issue_state": "to-do items",
            "issue_state_detail": {
              "serial": 0,
              "title": "to-do items"
            },
            "labels": [],
            "number": "1",
            "priority": 0,
            "repository": {
              "assigner": {},
              "created_at": "2024-10-16T15:51:35+08:00",
              "description": "my test code repository",
              "full_name": "owner-test/wonderful1",
              "id": 686738,
              "name": "wonderful1",
              "paas": "",
              "path": "wonderful1",
              "updated_at": "2024-10-16T15:51:35+08:00"
            },
            "state": "open",
            "title": "bbbbb",
            "updated_at": "2024-12-10T16:02:21+08:00",
            "user": {
              "html_url": "https://test.gitcode.net/csdn_fenglh",
              "id": "654c61e5560ed95fd216cf31",
              "login": "csdn_fenglh",
              "name": "fenglh"
            }
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "comments": {
                "type": "integer"
              },
              "created_at": {
                "type": "string"
              },
              "custom_fields": {
                "description": "Custom field information",
                "items": {
                  "properties": {
                    "field_name": {
                      "description": "Custom Field Name",
                      "type": "string"
                    },
                    "field_type": {
                      "description": "Field type. text_single: single line text, text_multi: multi-line text, integer: integer, decimal: decimal, date: date, select_single: single select dropdown, select_multi: multi-select dropdown, member_single: single select member, member_multi: multi-select member",
                      "type": "string"
                    },
                    "field_values": {
                      "description": "Custom field value",
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
                    },
                    "field_visibility": {
                      "description": "Visibility. 0: Visible to administrators only, 1: Visible to everyone",
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "finished_at": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "issue_priority_detail": {
                "description": "Issue Priority",
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "title"
                ],
                "type": "object"
              },
              "issue_state": {
                "type": "string"
              },
              "issue_state_detail": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "serial": {
                    "type": "integer"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "title",
                  "serial",
                  "id"
                ],
                "type": "object"
              },
              "issue_type": {
                "type": "string"
              },
              "issue_type_detail": {
                "properties": {
                  "id": {
                    "type": "integer"
                  },
                  "is_system": {
                    "type": "boolean"
                  },
                  "title": {
                    "type": "string"
                  }
                },
                "required": [
                  "title",
                  "id",
                  "is_system"
                ],
                "type": "object"
              },
              "labels": {
                "items": {
                  "type": "string"
                },
                "type": "array"
              },
              "number": {
                "type": "string"
              },
              "priority": {
                "type": "integer"
              },
              "repository": {
                "properties": {
                  "assigner": {
                    "properties": {},
                    "type": "object"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "description": {
                    "type": "string"
                  },
                  "full_name": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "name": {
                    "type": "string"
                  },
                  "paas": {
                    "type": "string"
                  },
                  "path": {
                    "type": "string"
                  },
                  "updated_at": {
                    "type": "string"
                  }
                },
                "required": [
                  "id",
                  "full_name",
                  "path",
                  "name",
                  "description",
                  "created_at",
                  "updated_at",
                  "assigner",
                  "paas"
                ],
                "type": "object"
              },
              "state": {
                "type": "string"
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
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
                "required": [
                  "avatar_url",
                  "html_url",
                  "id",
                  "login",
                  "name"
                ],
                "type": "object"
              },
              "visibility_reason": {
                "description": "Visibility, public: publicly visible, confidential: confidential, visible to project members, other: visible to project members due to other reasons",
                "type": "string"
              }
            },
            "required": [
              "id",
              "html_url",
              "number",
              "state",
              "title",
              "body",
              "user",
              "repository",
              "created_at",
              "updated_at",
              "finished_at",
              "labels",
              "issue_state",
              "comments",
              "priority",
              "issue_type",
              "issue_state_detail",
              "issue_type_detail"
            ],
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
    "Issues"
  ]
}
```
