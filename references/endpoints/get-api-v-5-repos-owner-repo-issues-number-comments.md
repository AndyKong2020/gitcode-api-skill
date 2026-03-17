# Get All Comments of a Specific Issue in the Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number-comments](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number-comments)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/issues/{number}/comments`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_issues_{number}_comments`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | Issue Number (case-sensitive, do not add #) |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| order | query | false | string | Sort order: asc(default), desc |
| since | query | false | string | The start update time, with the time format required as 2024-11-10T08:10:30.000%2B08:00 (Note that the + sign needs to be URL encoded as %2B) |
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
      "body": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "target": {
        "properties": {
          "issue": {
            "properties": {
              "id": {
                "type": "integer"
              },
              "nubmer": {
                "type": "integer"
              },
              "title": {
                "type": "string"
              }
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "updated_at": {
        "type": "string"
      },
      "user": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "events_url": {
            "type": "null"
          },
          "followers_url": {
            "type": "null"
          },
          "following_url": {
            "type": "null"
          },
          "gists_url": {
            "type": "null"
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
          "member_role": {
            "type": "null"
          },
          "name": {
            "type": "string"
          },
          "organizations_url": {
            "type": "null"
          },
          "received_events_url": {
            "type": "null"
          },
          "remark": {
            "type": "null"
          },
          "repos_url": {
            "type": "null"
          },
          "starred_url": {
            "type": "null"
          },
          "subscriptions_url": {
            "type": "null"
          },
          "type": {
            "type": "null"
          },
          "url": {
            "type": "null"
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
      "body": "Comment content.",
      "created_at": "2024-04-19T17:50:18.199+08:00",
      "id": 271624,
      "target": {
        "issue": {
          "id": 152134,
          "nubmer": 1,
          "title": ""
        }
      },
      "updated_at": "2024-04-19T17:50:18.199+08:00",
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_issues_{number}_comments",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
      "description": "Issue Number (case-sensitive, do not add #)",
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
      "description": "Sort order: asc(default), desc",
      "in": "query",
      "name": "order",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/issues/{number}/comments",
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
    "name": "Get All Comments of a Specific Issue in the Repository",
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
        "issues",
        ":number",
        "comments"
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
            "content": "Sort order: asc(default), desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "order",
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
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) Repository space address (address path of the enterprise, organization, or individual)",
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
            "content": "(Required) Issue Number (case-sensitive, do not add #)",
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
                "body": "Comment content.",
                "created_at": "2024-04-19T17:50:18.199+08:00",
                "id": 271624,
                "target": {
                  "issue": {
                    "id": 152134,
                    "nubmer": 1,
                    "title": ""
                  }
                },
                "updated_at": "2024-04-19T17:50:18.199+08:00",
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
                "body": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "target": {
                  "properties": {
                    "issue": {
                      "properties": {
                        "id": {
                          "type": "integer"
                        },
                        "nubmer": {
                          "type": "integer"
                        },
                        "title": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                },
                "updated_at": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "events_url": {
                      "type": "null"
                    },
                    "followers_url": {
                      "type": "null"
                    },
                    "following_url": {
                      "type": "null"
                    },
                    "gists_url": {
                      "type": "null"
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
                    "member_role": {
                      "type": "null"
                    },
                    "name": {
                      "type": "string"
                    },
                    "organizations_url": {
                      "type": "null"
                    },
                    "received_events_url": {
                      "type": "null"
                    },
                    "remark": {
                      "type": "null"
                    },
                    "repos_url": {
                      "type": "null"
                    },
                    "starred_url": {
                      "type": "null"
                    },
                    "subscriptions_url": {
                      "type": "null"
                    },
                    "type": {
                      "type": "null"
                    },
                    "url": {
                      "type": "null"
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
    "Issues"
  ]
}
```
