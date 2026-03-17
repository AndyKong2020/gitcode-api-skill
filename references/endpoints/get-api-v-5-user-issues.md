# Get All Issues Of Authorized User
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-issues)
Category: Issues
- Method: `GET`
- Path: `/api/v5/user/issues`
- Operation ID: `get_api_v5_user_issues`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| filter | query | false | string | Filter parameter: assigned if the authorized user is responsible for it, created if the authorized user created it, all if it includes both of the previous conditions. Default: assigned |
| state | query | false | string | Issue status: open, progressing, closed, rejected. Default: open |
| labels | query | false | string | A comma-separated list of labels. Such as: bug, performance |
| sort | query | false | string | Sorting criterion: creation time (created), update time (updated_at). Default: created_at |
| direction | query | false | string | Sort order: asc for ascending, desc for descending. Default: desc |
| since | query | false | string | The start update time, with the time format required to be ISO 8601. |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| schedule | query | false | string | Planning start date, format: 20181006T173008+80-20181007T173008+80 (range), or -20181007T173008+80 (less than 20181007T173008+80), or 20181006T173008+80- (greater than 20181006T173008+80), the time format must be 20181006T173008+80 |
| deadline | query | false | string | Planning end date, with the same format as above. |
| created_at | query | false | string | Task creation time, with the same format as above. |
| finished_at | query | false | string | Task completion time, which is the point in time when the task was last transitioned to the completed state. The format is the same as above. |
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
      "depth": {
        "type": "integer"
      },
      "html_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
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
          "namespace": {
            "properties": {
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
              },
              "type": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "type",
              "name",
              "path",
              "html_url"
            ],
            "type": "object"
          },
          "owner": {
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
          "namespace",
          "owner",
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
      "assignee",
      "repository",
      "created_at",
      "updated_at",
      "labels",
      "comments",
      "priority",
      "depth",
      "parent_id",
      "milestone"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "assignee": {
    "avatar_url": "https://cdn-img.gitcode.com/db/cf/dbc07f37245cab6693ef7a3ba7eb101634f480c263fa294f6b366e4a0fe60a45.png?time=1720429708203",
    "html_url": "https://gitcode.com/yinlin",
    "id": "303745",
    "login": "yinlin",
    "name": "yinlin-nickname",
    "type": "User"
  },
  "body": "Test content\n\nAs mentioned: https://gitcode.com/gitcode-dev/releases-log/issues/617\nRequirement document address\n\nhttps://gitcode.com/gitcode-dev/releases-log/issues/617\nUI design diagram address\n\nNone\nTechnical solution address\n\nNone\nImpact scope\n\nServices involved in release\n\ngitcode-fe\nDeveloper\n\nLiu Aolin\nPR file changes diffs\n\nhttps://gitcode.com/gitcode-dev/gitcode-fe/merge_requests/3661/diffs\nDependencies\n\nNone\nAPI adjustments\n\nNone\nDatabase adjustments\n\nNone\nNacos configuration adjustments\n\nNone\nOperations and maintenance adjustments\n\nNone",
  "html_url": "https://gitcode.com/gitcode-dev/gitcode-TestTask/issues/319",
  "id": 490786,
  "number": "319",
  "state": "open",
  "title": "The size of attachment images in the comment is increased from 2M to 10M, allowing users to upload larger image attachments."
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
  "operationId": "get_api_v5_user_issues",
  "parameters": [
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
      "description": "Filter parameter: assigned if the authorized user is responsible for it, created if the authorized user created it, all if it includes both of the previous conditions. Default: assigned",
      "in": "query",
      "name": "filter",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Issue status: open, progressing, closed, rejected. Default: open",
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
      "description": "Planning start date, format: 20181006T173008+80-20181007T173008+80 (range), or -20181007T173008+80 (less than 20181007T173008+80), or 20181006T173008+80- (greater than 20181006T173008+80), the time format must be 20181006T173008+80",
      "in": "query",
      "name": "schedule",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Planning end date, with the same format as above.",
      "in": "query",
      "name": "deadline",
      "required": false,
      "schema": {
        "type": "string"
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
      "description": "Task completion time, which is the point in time when the task was last transitioned to the completed state. The format is the same as above.",
      "in": "query",
      "name": "finished_at",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/user/issues",
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
    "name": "Get All Issues Of Authorized User",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
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
            "content": "Filter parameter: assigned if the authorized user is responsible for it, created if the authorized user created it, all if it includes both of the previous conditions. Default: assigned",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "filter",
          "value": ""
        },
        {
          "description": {
            "content": "Issue status: open, progressing, closed, rejected. Default: open",
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
            "content": "Planning start date, format: 20181006T173008+80-20181007T173008+80 (range), or -20181007T173008+80 (less than 20181007T173008+80), or 20181006T173008+80- (greater than 20181006T173008+80), the time format must be 20181006T173008+80",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "schedule",
          "value": ""
        },
        {
          "description": {
            "content": "Planning end date, with the same format as above.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "deadline",
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
            "content": "Task completion time, which is the point in time when the task was last transitioned to the completed state. The format is the same as above.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "finished_at",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "assignee": {
              "avatar_url": "https://cdn-img.gitcode.com/db/cf/dbc07f37245cab6693ef7a3ba7eb101634f480c263fa294f6b366e4a0fe60a45.png?time=1720429708203",
              "html_url": "https://gitcode.com/yinlin",
              "id": "303745",
              "login": "yinlin",
              "name": "yinlin-nickname",
              "type": "User"
            },
            "body": "Test content\n\nAs mentioned: https://gitcode.com/gitcode-dev/releases-log/issues/617\nRequirement document address\n\nhttps://gitcode.com/gitcode-dev/releases-log/issues/617\nUI design diagram address\n\nNone\nTechnical solution address\n\nNone\nImpact scope\n\nServices involved in release\n\ngitcode-fe\nDeveloper\n\nLiu Aolin\nPR file changes diffs\n\nhttps://gitcode.com/gitcode-dev/gitcode-fe/merge_requests/3661/diffs\nDependencies\n\nNone\nAPI adjustments\n\nNone\nDatabase adjustments\n\nNone\nNacos configuration adjustments\n\nNone\nOperations and maintenance adjustments\n\nNone",
            "html_url": "https://gitcode.com/gitcode-dev/gitcode-TestTask/issues/319",
            "id": 490786,
            "number": "319",
            "state": "open",
            "title": "The size of attachment images in the comment is increased from 2M to 10M, allowing users to upload larger image attachments."
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
                "depth": {
                  "type": "integer"
                },
                "html_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
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
                    "namespace": {
                      "properties": {
                        "html_url": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "id",
                        "type",
                        "name",
                        "path",
                        "html_url"
                      ],
                      "type": "object"
                    },
                    "owner": {
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
                    "namespace",
                    "owner",
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
                "assignee",
                "repository",
                "created_at",
                "updated_at",
                "labels",
                "comments",
                "priority",
                "depth",
                "parent_id",
                "milestone"
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
