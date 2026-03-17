# Get Operation Logs for a Specific Issue
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-issues-number-operate-logs](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-issues-number-operate-logs)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/issues/{number}/operate_logs`
- Operation ID: `get_api_v5_repos_{owner}_issues_{number}_operate_logs`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| number | path | true | string | issue number |
| access_token | query | true | string | User authorization code |
| repo | query | true | string | Repository path (path) |
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
      "action_type": {
        "type": "string"
      },
      "base": {
        "properties": {
          "assigner": {
            "type": "null"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "sha": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "body": {
        "type": "string"
      },
      "content": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "head": {
        "properties": {
          "assigner": {
            "properties": {
              "login": {
                "type": "string"
              },
              "name": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "name": {
                "type": "string"
              },
              "path": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "sha": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "id": {
        "type": "integer"
      },
      "issue_id": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "update_at": {
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
      "action_type": "add_issue_mr_link",
      "base": {
        "assigner": null,
        "ref": "main",
        "repo": {
          "name": "test01",
          "path": "test01"
        },
        "sha": "32cff0d8faaa0c044d0f94957e656051986e8403"
      },
      "body": "new: Added file 1.text",
      "content": "Create issue mr links: **new: Added file 1.text** #1",
      "created_at": "2024-04-20T15:20:24.009+08:00",
      "head": {
        "assigner": {
          "login": "dengmengmian",
          "name": "MaFan_"
        },
        "ref": "develop",
        "repo": {
          "name": "test01",
          "path": "test01"
        },
        "sha": "dd954d3a779edc86dae5b4b60c7f24dd0f195bf4"
      },
      "id": 272199,
      "issue_id": "152642",
      "title": "new: Added file 1.text",
      "update_at": "2024-04-20T15:20:24.009+08:00",
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
      "action_type": "milestone",
      "base": null,
      "body": null,
      "content": "changed milestone to testew",
      "created_at": "2024-04-20T15:20:09.305+08:00",
      "head": null,
      "id": 272198,
      "issue_id": "152642",
      "title": null,
      "update_at": "2024-04-20T15:20:09.305+08:00",
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
  "operationId": "get_api_v5_repos_{owner}_issues_{number}_operate_logs",
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
      "description": "issue number",
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
      "description": "Repository path (path)",
      "in": "query",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/issues/{number}/operate_logs",
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
    "name": "Get Operation Logs for a Specific Issue",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        "issues",
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
            "content": "(Required) Repository path (path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
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
            "content": "(Required) issue number",
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
                "action_type": "add_issue_mr_link",
                "base": {
                  "assigner": null,
                  "ref": "main",
                  "repo": {
                    "name": "test01",
                    "path": "test01"
                  },
                  "sha": "32cff0d8faaa0c044d0f94957e656051986e8403"
                },
                "body": "new: Added file 1.text",
                "content": "Create issue mr links: **new: Added file 1.text** #1",
                "created_at": "2024-04-20T15:20:24.009+08:00",
                "head": {
                  "assigner": {
                    "login": "dengmengmian",
                    "name": "MaFan_"
                  },
                  "ref": "develop",
                  "repo": {
                    "name": "test01",
                    "path": "test01"
                  },
                  "sha": "dd954d3a779edc86dae5b4b60c7f24dd0f195bf4"
                },
                "id": 272199,
                "issue_id": "152642",
                "title": "new: Added file 1.text",
                "update_at": "2024-04-20T15:20:24.009+08:00",
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
                "action_type": "milestone",
                "base": null,
                "body": null,
                "content": "changed milestone to testew",
                "created_at": "2024-04-20T15:20:09.305+08:00",
                "head": null,
                "id": 272198,
                "issue_id": "152642",
                "title": null,
                "update_at": "2024-04-20T15:20:09.305+08:00",
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
                "action_type": {
                  "type": "string"
                },
                "base": {
                  "properties": {
                    "assigner": {
                      "type": "null"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "body": {
                  "type": "string"
                },
                "content": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "head": {
                  "properties": {
                    "assigner": {
                      "properties": {
                        "login": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "name": {
                          "type": "string"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "id": {
                  "type": "integer"
                },
                "issue_id": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "update_at": {
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
