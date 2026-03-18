# Get All Repository Issues
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/issues`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_issues`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| state | query | false | string | Issue state: open, closed, or all. Default is all. |
| labels | query | false | string | A comma-separated list of labels. Such as: bug, performance |
| sort | query | false | string | Sorting criterion: creation time (created), update time (updated). Default: created |
| direction | query | false | string | Sort order: asc for ascending, desc for descending. Default: desc |
| since | query | false | string | The start update time, with the time format required as 2024-11-10T08:10:30.000%2B08:00 (Note that the + sign needs to be URL encoded as %2B) |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| created_at | query | false | string | Task creation time, for example: 2024-11-20T13:00:21+08:00 |
| milestone | query | false | string | According to the milestone title. none for no milestones |
| assignee | query | false | string | Issue Assignee ID |
| creator | query | false | string | The username of the user who creates the Issues |
| created_after | query | false | string | Returns issues created after the specified time, for example: 2024-11-20T13:00:21+08:00 |
| created_before | query | false | string | Returns questions created before the specified time, for example: 2024-11-20T13:00:21+08:00 |
| updated_after | query | false | string | Returns issues updated after the specified time, for example: 2024-11-20T13:00:21+08:00 |
| updated_before | query | false | string | Returns issues updated before the specified time, for example: 2024-11-20T13:00:21+08:00 |
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
      "body": {
        "type": "string"
      },
      "comments": {
        "type": "integer"
      },
      "created_at": {
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
      "issue_type_detail",
      "assignee",
      "milestone"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "assignee": {
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
        "events_url": null,
        "followers_url": null,
        "following_url": null,
        "gists_url": null,
        "html_url": "https://test.gitcode.net/dengmengmian",
        "id": "661ce4eab470b1430d456154",
        "login": "dengmengmian",
        "member_role": null,
        "name": "MaFan_",
        "organizations_url": null,
        "received_events_url": null,
        "remark": null,
        "repos_url": null,
        "starred_url": null,
        "subscriptions_url": null,
        "type": null,
        "url": null
      },
      "body": "abcabcabc",
      "created_at": "2024-04-18T14:35:15.479+08:00",
      "finished_at": null,
      "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/15",
      "id": 152642,
      "issue_state": "opened",
      "issue_state_detail": null,
      "issue_type": null,
      "labels": [
        {
          "color": "#428BCA",
          "id": 382379,
          "name": "enim"
        },
        {
          "color": "#428BCA",
          "id": 382378,
          "name": "proident"
        },
        {
          "color": "#428BCA",
          "id": 382377,
          "name": "qui"
        }
      ],
      "number": "15",
      "priority": null,
      "repository": {
        "assignee": null,
        "assignees_number": null,
        "assigner": null,
        "created_at": "2024-04-15T16:27:45.090+08:00",
        "description": "",
        "full_name": "dengmengmian / test01",
        "id": 280713,
        "name": "test01",
        "paas": null,
        "path": "test01",
        "pushed_at": null,
        "testers": null,
        "testers_number": null,
        "updated_at": "2024-04-15T16:27:45.090+08:00"
      },
      "state": "opened",
      "title": "half month data",
      "updated_at": "2024-04-20T15:20:30.111+08:00",
      "user": {
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
        "events_url": null,
        "followers_url": null,
        "following_url": null,
        "gists_url": null,
        "html_url": "https://test.gitcode.net/dengmengmian",
        "id": "661ce4eab470b1430d456154",
        "login": "dengmengmian",
        "member_role": null,
        "name": "MaFan_",
        "organizations_url": null,
        "received_events_url": null,
        "remark": null,
        "repos_url": null,
        "starred_url": null,
        "subscriptions_url": null,
        "type": null,
        "url": null
      }
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "assignee": {
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
        "events_url": null,
        "followers_url": null,
        "following_url": null,
        "gists_url": null,
        "html_url": "https://test.gitcode.net/dengmengmian",
        "id": "661ce4eab470b1430d456154",
        "login": "dengmengmian",
        "member_role": null,
        "name": "MaFan_",
        "organizations_url": null,
        "received_events_url": null,
        "remark": null,
        "repos_url": null,
        "starred_url": null,
        "subscriptions_url": null,
        "type": null,
        "url": null
      },
      "body": "abcabcabc",
      "created_at": "2024-04-16T14:38:43.464+08:00",
      "finished_at": "2024-04-16T14:49:45.166+08:00",
      "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/14",
      "id": 152467,
      "issue_state": "closed",
      "issue_state_detail": null,
      "issue_type": null,
      "labels": [
        {
          "color": "#428BCA",
          "id": 382389,
          "name": "ad"
        },
        {
          "color": "#428BCA",
          "id": 382388,
          "name": "id"
        }
      ],
      "number": "14",
      "priority": null,
      "repository": {
        "assignee": null,
        "assignees_number": null,
        "assigner": null,
        "created_at": "2024-04-15T16:27:45.090+08:00",
        "description": "",
        "full_name": "dengmengmian / test01",
        "id": 280713,
        "name": "test01",
        "paas": null,
        "path": "test01",
        "pushed_at": null,
        "testers": null,
        "testers_number": null,
        "updated_at": "2024-04-15T16:27:45.090+08:00"
      },
      "state": "closed",
      "title": "abcabcabc",
      "updated_at": "2024-04-18T18:27:21.955+08:00",
      "user": {
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
        "events_url": null,
        "followers_url": null,
        "following_url": null,
        "gists_url": null,
        "html_url": "https://test.gitcode.net/dengmengmian",
        "id": "661ce4eab470b1430d456154",
        "login": "dengmengmian",
        "member_role": null,
        "name": "MaFan_",
        "organizations_url": null,
        "received_events_url": null,
        "remark": null,
        "repos_url": null,
        "starred_url": null,
        "subscriptions_url": null,
        "type": null,
        "url": null
      }
    }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_issues",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "example": "",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "example": "",
      "in": "path",
      "name": "repo",
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
      "description": "Issue state: open, closed, or all. Default is all.",
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
      "description": "Sorting criterion: creation time (created), update time (updated). Default: created",
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
      "description": "The start update time, with the time format required as 2024-11-10T08:10:30.000%2B08:00 (Note that the + sign needs to be URL encoded as %2B)",
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
      "description": "Task creation time, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_at",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "According to the milestone title. none for no milestones",
      "in": "query",
      "name": "milestone",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Issue Assignee ID",
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
      "description": "Returns issues created after the specified time, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns questions created before the specified time, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns issues updated after the specified time, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Returns issues updated before the specified time, for example: 2024-11-20T13:00:21+08:00",
      "in": "query",
      "name": "updated_before",
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
  "path": "/api/v5/repos/{owner}/{repo}/issues",
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
    "name": "Get All Repository Issues",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo",
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
            "content": "Issue state: open, closed, or all. Default is all.",
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
            "content": "Sorting criterion: creation time (created), update time (updated). Default: created",
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
            "content": "The start update time, with the time format required as 2024-11-10T08:10:30.000%2B08:00 (Note that the + sign needs to be URL encoded as %2B)",
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
            "content": "Task creation time, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_at",
          "value": ""
        },
        {
          "description": {
            "content": "According to the milestone title. none for no milestones",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "milestone",
          "value": ""
        },
        {
          "description": {
            "content": "Issue Assignee ID",
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
            "content": "Returns issues created after the specified time, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_after",
          "value": ""
        },
        {
          "description": {
            "content": "Returns questions created before the specified time, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
          "value": ""
        },
        {
          "description": {
            "content": "Returns issues updated after the specified time, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_after",
          "value": ""
        },
        {
          "description": {
            "content": "Returns issues updated before the specified time, for example: 2024-11-20T13:00:21+08:00",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "updated_before",
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
            "content": "(Required) Repository space address (organization or individual's address path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Repository path (path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "assignee": {
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                  "events_url": null,
                  "followers_url": null,
                  "following_url": null,
                  "gists_url": null,
                  "html_url": "https://test.gitcode.net/dengmengmian",
                  "id": "661ce4eab470b1430d456154",
                  "login": "dengmengmian",
                  "member_role": null,
                  "name": "MaFan_",
                  "organizations_url": null,
                  "received_events_url": null,
                  "remark": null,
                  "repos_url": null,
                  "starred_url": null,
                  "subscriptions_url": null,
                  "type": null,
                  "url": null
                },
                "body": "abcabcabc",
                "created_at": "2024-04-18T14:35:15.479+08:00",
                "finished_at": null,
                "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/15",
                "id": 152642,
                "issue_state": "opened",
                "issue_state_detail": null,
                "issue_type": null,
                "labels": [
                  {
                    "color": "#428BCA",
                    "id": 382379,
                    "name": "enim"
                  },
                  {
                    "color": "#428BCA",
                    "id": 382378,
                    "name": "proident"
                  },
                  {
                    "color": "#428BCA",
                    "id": 382377,
                    "name": "qui"
                  }
                ],
                "number": "15",
                "priority": null,
                "repository": {
                  "assignee": null,
                  "assignees_number": null,
                  "assigner": null,
                  "created_at": "2024-04-15T16:27:45.090+08:00",
                  "description": "",
                  "full_name": "dengmengmian / test01",
                  "id": 280713,
                  "name": "test01",
                  "paas": null,
                  "path": "test01",
                  "pushed_at": null,
                  "testers": null,
                  "testers_number": null,
                  "updated_at": "2024-04-15T16:27:45.090+08:00"
                },
                "state": "opened",
                "title": "half month data",
                "updated_at": "2024-04-20T15:20:30.111+08:00",
                "user": {
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                  "events_url": null,
                  "followers_url": null,
                  "following_url": null,
                  "gists_url": null,
                  "html_url": "https://test.gitcode.net/dengmengmian",
                  "id": "661ce4eab470b1430d456154",
                  "login": "dengmengmian",
                  "member_role": null,
                  "name": "MaFan_",
                  "organizations_url": null,
                  "received_events_url": null,
                  "remark": null,
                  "repos_url": null,
                  "starred_url": null,
                  "subscriptions_url": null,
                  "type": null,
                  "url": null
                }
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "assignee": {
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                  "events_url": null,
                  "followers_url": null,
                  "following_url": null,
                  "gists_url": null,
                  "html_url": "https://test.gitcode.net/dengmengmian",
                  "id": "661ce4eab470b1430d456154",
                  "login": "dengmengmian",
                  "member_role": null,
                  "name": "MaFan_",
                  "organizations_url": null,
                  "received_events_url": null,
                  "remark": null,
                  "repos_url": null,
                  "starred_url": null,
                  "subscriptions_url": null,
                  "type": null,
                  "url": null
                },
                "body": "abcabcabc",
                "created_at": "2024-04-16T14:38:43.464+08:00",
                "finished_at": "2024-04-16T14:49:45.166+08:00",
                "html_url": "https://test.gitcode.net/dengmengmian/test01/issues/14",
                "id": 152467,
                "issue_state": "closed",
                "issue_state_detail": null,
                "issue_type": null,
                "labels": [
                  {
                    "color": "#428BCA",
                    "id": 382389,
                    "name": "ad"
                  },
                  {
                    "color": "#428BCA",
                    "id": 382388,
                    "name": "id"
                  }
                ],
                "number": "14",
                "priority": null,
                "repository": {
                  "assignee": null,
                  "assignees_number": null,
                  "assigner": null,
                  "created_at": "2024-04-15T16:27:45.090+08:00",
                  "description": "",
                  "full_name": "dengmengmian / test01",
                  "id": 280713,
                  "name": "test01",
                  "paas": null,
                  "path": "test01",
                  "pushed_at": null,
                  "testers": null,
                  "testers_number": null,
                  "updated_at": "2024-04-15T16:27:45.090+08:00"
                },
                "state": "closed",
                "title": "abcabcabc",
                "updated_at": "2024-04-18T18:27:21.955+08:00",
                "user": {
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/fa/fe/f32a9fecc53e890afbd48fd098b0f6c5f20f062581400c76c85e5baab3f0d5b2.png",
                  "events_url": null,
                  "followers_url": null,
                  "following_url": null,
                  "gists_url": null,
                  "html_url": "https://test.gitcode.net/dengmengmian",
                  "id": "661ce4eab470b1430d456154",
                  "login": "dengmengmian",
                  "member_role": null,
                  "name": "MaFan_",
                  "organizations_url": null,
                  "received_events_url": null,
                  "remark": null,
                  "repos_url": null,
                  "starred_url": null,
                  "subscriptions_url": null,
                  "type": null,
                  "url": null
                }
              }
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
                "body": {
                  "type": "string"
                },
                "comments": {
                  "type": "integer"
                },
                "created_at": {
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
                "issue_type_detail",
                "assignee",
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
