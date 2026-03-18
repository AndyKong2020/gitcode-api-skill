# Get All Issues Of A Company
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues)
Category: Issues
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/issues`
- Operation ID: `get_api_v5_enterprises_{enterprise}_issues`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | The path of the enterprise (path/login) |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Issue state: open, closed, all. Default: open. |
| labels | query | false | string | A comma-separated list of labels. Such as: bug, performance |
| sort | query | false | string | Sorting criterion: creation time (created), update time (updated_at). Default: created_at |
| direction | query | false | string | Sort order: asc for ascending, desc for descending. Default: desc |
| since | query | false | string | The start update time, with the time format required to be ISO 8601. |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| milestone | query | false | string | Based on the milestone title. "none" for those without any milestones, "\*" for all with milestones. |
| assignee | query | false | string | The user's username. "none" represents no assignee, and "*" represents all assignees. |
| creator | query | false | string | The username of the user who creates the Issues |
| program | query | false | string | Project name to which the item belongs. "none" represents items that do not belong to any project, and "\*" represents items that belong to all projects. |
| created_at | query | false | string | Task Creation Date, format: YYYY-MM-DD |
| created_before | query | false | string | Task creation deadline, format YYYY-MM-DD |
| search | query | false | string | Search for issue by keyword in title or content |
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
      "assignee": {
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
          "type": {
            "type": "string"
          }
        },
        "required": [
          "avatar_url",
          "html_url",
          "id",
          "login",
          "name",
          "type"
        ],
        "type": "object"
      },
      "body": {
        "type": "string"
      },
      "comments": {
        "type": "integer"
      },
      "created_at": {
        "type": "string"
      },
      "deadline": {
        "type": "string"
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
          "properties": {
            "color": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          },
          "required": [
            "id",
            "name",
            "color"
          ],
          "type": "object"
        },
        "type": "array"
      },
      "milestone": {
        "properties": {
          "created_at": {
            "type": "string"
          },
          "description": {
            "type": "string"
          },
          "due_on": {
            "type": "string"
          },
          "html_url": {
            "type": "string"
          },
          "number": {
            "type": "integer"
          },
          "repository_id": {
            "type": "integer"
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
          "url": {
            "type": "string"
          }
        },
        "required": [
          "created_at",
          "description",
          "due_on",
          "html_url",
          "number",
          "repository_id",
          "state",
          "title",
          "updated_at",
          "url"
        ],
        "type": "object"
      },
      "number": {
        "type": "string"
      },
      "parent_id": {
        "type": "integer"
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
          "full_name": {
            "type": "string"
          },
          "human_name": {
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
          "url": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "full_name",
          "human_name",
          "path",
          "name",
          "url",
          "assigner",
          "paas"
        ],
        "type": "object"
      },
      "repository_url": {
        "type": "string"
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
      "url": {
        "type": "string"
      },
      "user": {
        "properties": {
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
      "deadline",
      "labels",
      "issue_state",
      "comments",
      "priority",
      "issue_type",
      "issue_state_detail",
      "issue_type_detail",
      "parent_id",
      "url",
      "repository_url",
      "assignee"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "body": "2222",
  "comments": 0,
  "created_at": "2024-11-20T15:40:35+08:00",
  "html_url": "https://gitcode.com/xiaogang_test/test222/issues/7",
  "id": 340035,
  "issue_state": "Undelivered",
  "issue_state_detail": {
    "id": 222,
    "serial": 1,
    "title": "Undelivered"
  },
  "issue_type": "requirement",
  "issue_type_detail": {
    "id": 629,
    "is_system": false,
    "title": "requirement"
  },
  "labels": [],
  "number": "7",
  "parent_id": 0,
  "priority": 0,
  "repository": {
    "assigner": {},
    "full_name": "xiaogang_test/test222",
    "human_name": "test organization / test222",
    "id": 249609,
    "name": "test222",
    "paas": "",
    "path": "test222",
    "url": "https://gitcode.com/xiaogang_test/test222"
  },
  "state": "open",
  "title": "2222",
  "updated_at": "2024-11-20T15:40:35+08:00",
  "url": "https://gitcode.com/api/v5/repos/xiaogang_test/test222/issues/7",
  "user": {
    "id": "65f96506b3a9e65264980447",
    "login": "xiaogang",
    "name": "xiaogang"
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
  "operationId": "get_api_v5_enterprises_{enterprise}_issues",
  "parameters": [
    {
      "description": "The path of the enterprise (path/login)",
      "example": "",
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
      "description": "Issue state: open, closed, all. Default: open.",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "A comma-separated list of labels. Such as: bug, performance",
      "in": "query",
      "name": "labels",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sorting criterion: creation time (created), update time (updated_at). Default: created_at",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order: asc for ascending, desc for descending. Default: desc",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The start update time, with the time format required to be ISO 8601.",
      "in": "query",
      "name": "since",
      "required": false,
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
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Based on the milestone title. \"none\" for those without any milestones, \"\\*\" for all with milestones.",
      "in": "query",
      "name": "milestone",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The user's username. \"none\" represents no assignee, and \"*\" represents all assignees.",
      "in": "query",
      "name": "assignee",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The username of the user who creates the Issues",
      "in": "query",
      "name": "creator",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Project name to which the item belongs. \"none\" represents items that do not belong to any project, and \"\\*\" represents items that belong to all projects.",
      "in": "query",
      "name": "program",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Task Creation Date, format: YYYY-MM-DD",
      "in": "query",
      "name": "created_at",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Task creation deadline, format YYYY-MM-DD",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Search for issue by keyword in title or content",
      "in": "query",
      "name": "search",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/enterprises/{enterprise}/issues",
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
    "name": "Get All Issues Of A Company",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "enterprises",
        ":enterprise",
        "issues"
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
            "content": "Issue state: open, closed, all. Default: open.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "A comma-separated list of labels. Such as: bug, performance",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "labels",
          "value": ""
        },
        {
          "description": {
            "content": "Sorting criterion: creation time (created), update time (updated_at). Default: created_at",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order: asc for ascending, desc for descending. Default: desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "The start update time, with the time format required to be ISO 8601.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
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
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "Based on the milestone title. \"none\" for those without any milestones, \"\\*\" for all with milestones.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "milestone",
          "value": ""
        },
        {
          "description": {
            "content": "The user's username. \"none\" represents no assignee, and \"*\" represents all assignees.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "assignee",
          "value": ""
        },
        {
          "description": {
            "content": "The username of the user who creates the Issues",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "creator",
          "value": ""
        },
        {
          "description": {
            "content": "Project name to which the item belongs. \"none\" represents items that do not belong to any project, and \"\\*\" represents items that belong to all projects.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "program",
          "value": ""
        },
        {
          "description": {
            "content": "Task Creation Date, format: YYYY-MM-DD",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_at",
          "value": ""
        },
        {
          "description": {
            "content": "Task creation deadline, format YYYY-MM-DD",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
          "value": ""
        },
        {
          "description": {
            "content": "Search for issue by keyword in title or content",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "search",
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
          "example": {
            "body": "2222",
            "comments": 0,
            "created_at": "2024-11-20T15:40:35+08:00",
            "html_url": "https://gitcode.com/xiaogang_test/test222/issues/7",
            "id": 340035,
            "issue_state": "Undelivered",
            "issue_state_detail": {
              "id": 222,
              "serial": 1,
              "title": "Undelivered"
            },
            "issue_type": "requirement",
            "issue_type_detail": {
              "id": 629,
              "is_system": false,
              "title": "requirement"
            },
            "labels": [],
            "number": "7",
            "parent_id": 0,
            "priority": 0,
            "repository": {
              "assigner": {},
              "full_name": "xiaogang_test/test222",
              "human_name": "test organization / test222",
              "id": 249609,
              "name": "test222",
              "paas": "",
              "path": "test222",
              "url": "https://gitcode.com/xiaogang_test/test222"
            },
            "state": "open",
            "title": "2222",
            "updated_at": "2024-11-20T15:40:35+08:00",
            "url": "https://gitcode.com/api/v5/repos/xiaogang_test/test222/issues/7",
            "user": {
              "id": "65f96506b3a9e65264980447",
              "login": "xiaogang",
              "name": "xiaogang"
            }
          },
          "schema": {
            "items": {
              "properties": {
                "assignee": {
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
                    "type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "avatar_url",
                    "html_url",
                    "id",
                    "login",
                    "name",
                    "type"
                  ],
                  "type": "object"
                },
                "body": {
                  "type": "string"
                },
                "comments": {
                  "type": "integer"
                },
                "created_at": {
                  "type": "string"
                },
                "deadline": {
                  "type": "string"
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
                    "properties": {
                      "color": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "id",
                      "name",
                      "color"
                    ],
                    "type": "object"
                  },
                  "type": "array"
                },
                "milestone": {
                  "properties": {
                    "created_at": {
                      "type": "string"
                    },
                    "description": {
                      "type": "string"
                    },
                    "due_on": {
                      "type": "string"
                    },
                    "html_url": {
                      "type": "string"
                    },
                    "number": {
                      "type": "integer"
                    },
                    "repository_id": {
                      "type": "integer"
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
                    "url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "created_at",
                    "description",
                    "due_on",
                    "html_url",
                    "number",
                    "repository_id",
                    "state",
                    "title",
                    "updated_at",
                    "url"
                  ],
                  "type": "object"
                },
                "number": {
                  "type": "string"
                },
                "parent_id": {
                  "type": "integer"
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
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
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
                    "url": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "id",
                    "full_name",
                    "human_name",
                    "path",
                    "name",
                    "url",
                    "assigner",
                    "paas"
                  ],
                  "type": "object"
                },
                "repository_url": {
                  "type": "string"
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
                "url": {
                  "type": "string"
                },
                "user": {
                  "properties": {
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
                "deadline",
                "labels",
                "issue_state",
                "comments",
                "priority",
                "issue_type",
                "issue_state_detail",
                "issue_type_detail",
                "parent_id",
                "url",
                "repository_url",
                "assignee"
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
    "Issues"
  ]
}
```
