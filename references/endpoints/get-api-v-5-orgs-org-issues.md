# Get Issues Of A Certain Organization Of Current User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-orgs-org-issues)
Category: Issues
- Method: `GET`
- Path: `/api/v5/orgs/{org}/issues`
- Operation ID: `get_api_v5_orgs_{org}_issues`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| org | path | true | string | Organization's path (path/login) |
| access_token | query | true | string | User authorization code |
| filter | query | false | string | Filter parameter: assigned to the authorized user, created by the authorized user, or including both (all). Default: assigned |
| state | query | false | string | Issue status: open, closed; default: open |
| labels | query | false | string | A comma-separated list of labels. For example: bug, performance |
| sort | query | false | string | Sorting based on: creation time (created), update time (updated_at). Default: created_at |
| direction | query | false | string | Sort order: ascending (asc), descending (desc). Default: desc |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| created_at | query | false | string | Task creation time, with the same format as above. |
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
          "serial"
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
      "assignee",
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
      "repository_url"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "body": "1",
  "comments": 0,
  "created_at": "2024-10-12T18:27:27+08:00",
  "html_url": "https://gitcode.com/Go-Tribe/test01/issues/1",
  "id": 495900,
  "labels": [],
  "number": "1",
  "parent_id": 0,
  "priority": 0,
  "repository": {
    "full_name": "Go-Tribe/test01",
    "human_name": "gotribe / test01",
    "id": 4016571,
    "name": "test01",
    "owner": {
      "id": "650d67fbae6d795139b49b41",
      "login": "dengmengmian",
      "name": "Mavan"
    },
    "path": "test01",
    "url": "https://gitcode.com/Go-Tribe/test01"
  },
  "state": "open",
  "title": "1",
  "updated_at": "2024-10-12T18:27:27+08:00"
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
  "operationId": "get_api_v5_orgs_{org}_issues",
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
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Filter parameter: assigned to the authorized user, created by the authorized user, or including both (all). Default: assigned",
      "in": "query",
      "name": "filter",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Issue status: open, closed; default: open",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "A comma-separated list of labels. For example: bug, performance",
      "in": "query",
      "name": "labels",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sorting based on: creation time (created), update time (updated_at). Default: created_at",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order: ascending (asc), descending (desc). Default: desc",
      "in": "query",
      "name": "direction",
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
      "description": "Task creation time, with the same format as above.",
      "in": "query",
      "name": "created_at",
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
  "path": "/api/v5/orgs/{org}/issues",
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
    "name": "Get Issues Of A Certain Organization Of Current User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "orgs",
        ":org",
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
            "content": "Filter parameter: assigned to the authorized user, created by the authorized user, or including both (all). Default: assigned",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "filter",
          "value": ""
        },
        {
          "description": {
            "content": "Issue status: open, closed; default: open",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        },
        {
          "description": {
            "content": "A comma-separated list of labels. For example: bug, performance",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "labels",
          "value": ""
        },
        {
          "description": {
            "content": "Sorting based on: creation time (created), update time (updated_at). Default: created_at",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order: ascending (asc), descending (desc). Default: desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
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
            "content": "Task creation time, with the same format as above.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_at",
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
          "example": {
            "body": "1",
            "comments": 0,
            "created_at": "2024-10-12T18:27:27+08:00",
            "html_url": "https://gitcode.com/Go-Tribe/test01/issues/1",
            "id": 495900,
            "labels": [],
            "number": "1",
            "parent_id": 0,
            "priority": 0,
            "repository": {
              "full_name": "Go-Tribe/test01",
              "human_name": "gotribe / test01",
              "id": 4016571,
              "name": "test01",
              "owner": {
                "id": "650d67fbae6d795139b49b41",
                "login": "dengmengmian",
                "name": "Mavan"
              },
              "path": "test01",
              "url": "https://gitcode.com/Go-Tribe/test01"
            },
            "state": "open",
            "title": "1",
            "updated_at": "2024-10-12T18:27:27+08:00"
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
                    "serial"
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
                "assignee",
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
                "repository_url"
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
