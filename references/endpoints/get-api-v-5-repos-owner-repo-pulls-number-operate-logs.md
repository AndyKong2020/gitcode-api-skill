# Get Operation Logs for a Specific Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-operate-logs](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-operate-logs)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/operate_logs`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_operate_logs`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string |  |
| access_token | query | true | string | User authorization code |
| sort | query | false | string | Sorted in descending order by default. |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
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
      "action": {
        "type": "string"
      },
      "action_type": {
        "type": "string"
      },
      "assignee": {
        "type": "null"
      },
      "content": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "discussion_id": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "merge_request_id": {
        "type": "integer"
      },
      "project": {
        "type": "string"
      },
      "proposer": {
        "type": "null"
      },
      "updated_at": {
        "type": "string"
      },
      "user": {
        "properties": {
          "avatar_path": {
            "type": "null"
          },
          "avatar_url": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "iam_id": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "is_member": {
            "type": "null"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "name_cn": {
            "type": "string"
          },
          "nick_name": {
            "type": "string"
          },
          "state": {
            "type": "string"
          },
          "tenant_name": {
            "type": "null"
          },
          "web_url": {
            "type": "string"
          }
        },
        "type": "object"
      }
    },
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
      "action": "add_mr_issue_link",
      "action_type": "add_mr_issue_link",
      "assignee": null,
      "content": "Create mr issue link: **boudoirripinings-24 issue** #79",
      "created_at": "2024-04-23T11:32:08.522+08:00",
      "discussion_id": "18a5ab21f57cda175b8eabc2ec829a9e04d4d458",
      "id": 274531,
      "merge_request_id": 70067,
      "project": "One/One",
      "proposer": null,
      "updated_at": "2024-04-23T11:32:08.522+08:00",
      "user": {
        "avatar_path": null,
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
        "email": "csdntest13@noreply.gitcode.com",
        "iam_id": "d8b3e018b2364546b946886a669d50fc",
        "id": "65f94ab6f21fa3084fc04823",
        "is_member": null,
        "login": "csdntest13",
        "name": "csdntest13",
        "name_cn": "csdntest13",
        "nick_name": "csdntest13_gitcode",
        "state": "active",
        "tenant_name": null,
        "web_url": "https://test.gitcode.net/csdntest13"
      }
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "action": "add_mr_issue_link",
      "action_type": "add_mr_issue_link",
      "assignee": null,
      "content": "Create mr issue link: **Issue 25 of boudoirripinings** #80",
      "created_at": "2024-04-23T11:32:07.588+08:00",
      "discussion_id": "9b4b01dbe059dbdc120afd8bdf9fd865d4ea42b1",
      "id": 274529,
      "merge_request_id": 70067,
      "project": "One/One",
      "proposer": null,
      "updated_at": "2024-04-23T11:32:07.588+08:00",
      "user": {
        "avatar_path": null,
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
        "email": "csdntest13@noreply.gitcode.com",
        "iam_id": "d8b3e018b2364546b946886a669d50fc",
        "id": "65f94ab6f21fa3084fc04823",
        "is_member": null,
        "login": "csdntest13",
        "name": "csdntest13",
        "name_cn": "csdntest13",
        "nick_name": "csdntest13_gitcode",
        "state": "active",
        "tenant_name": null,
        "web_url": "https://test.gitcode.net/csdntest13"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_operate_logs",
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
      "description": "",
      "example": "",
      "in": "path",
      "name": "number",
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
      "description": "Sorted in descending order by default.",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/operate_logs",
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
    "name": "Get Operation Logs for a Specific Pull Request",
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
        "pulls",
        ":number",
        "operate_logs"
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
            "content": "Sorted in descending order by default.",
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
        },
        {
          "description": {
            "content": "(Required) ",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "action": "add_mr_issue_link",
                "action_type": "add_mr_issue_link",
                "assignee": null,
                "content": "Create mr issue link: **boudoirripinings-24 issue** #79",
                "created_at": "2024-04-23T11:32:08.522+08:00",
                "discussion_id": "18a5ab21f57cda175b8eabc2ec829a9e04d4d458",
                "id": 274531,
                "merge_request_id": 70067,
                "project": "One/One",
                "proposer": null,
                "updated_at": "2024-04-23T11:32:08.522+08:00",
                "user": {
                  "avatar_path": null,
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                  "email": "csdntest13@noreply.gitcode.com",
                  "iam_id": "d8b3e018b2364546b946886a669d50fc",
                  "id": "65f94ab6f21fa3084fc04823",
                  "is_member": null,
                  "login": "csdntest13",
                  "name": "csdntest13",
                  "name_cn": "csdntest13",
                  "nick_name": "csdntest13_gitcode",
                  "state": "active",
                  "tenant_name": null,
                  "web_url": "https://test.gitcode.net/csdntest13"
                }
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "action": "add_mr_issue_link",
                "action_type": "add_mr_issue_link",
                "assignee": null,
                "content": "Create mr issue link: **Issue 25 of boudoirripinings** #80",
                "created_at": "2024-04-23T11:32:07.588+08:00",
                "discussion_id": "9b4b01dbe059dbdc120afd8bdf9fd865d4ea42b1",
                "id": 274529,
                "merge_request_id": 70067,
                "project": "One/One",
                "proposer": null,
                "updated_at": "2024-04-23T11:32:07.588+08:00",
                "user": {
                  "avatar_path": null,
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                  "email": "csdntest13@noreply.gitcode.com",
                  "iam_id": "d8b3e018b2364546b946886a669d50fc",
                  "id": "65f94ab6f21fa3084fc04823",
                  "is_member": null,
                  "login": "csdntest13",
                  "name": "csdntest13",
                  "name_cn": "csdntest13",
                  "nick_name": "csdntest13_gitcode",
                  "state": "active",
                  "tenant_name": null,
                  "web_url": "https://test.gitcode.net/csdntest13"
                }
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "action": {
                  "type": "string"
                },
                "action_type": {
                  "type": "string"
                },
                "assignee": {
                  "type": "null"
                },
                "content": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "discussion_id": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "merge_request_id": {
                  "type": "integer"
                },
                "project": {
                  "type": "string"
                },
                "proposer": {
                  "type": "null"
                },
                "updated_at": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "avatar_path": {
                      "type": "null"
                    },
                    "avatar_url": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    },
                    "iam_id": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "is_member": {
                      "type": "null"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "name_cn": {
                      "type": "string"
                    },
                    "nick_name": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    },
                    "tenant_name": {
                      "type": "null"
                    },
                    "web_url": {
                      "type": "string"
                    }
                  },
                  "type": "object"
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
  "tags": [
    "Pull Requests"
  ]
}
```
