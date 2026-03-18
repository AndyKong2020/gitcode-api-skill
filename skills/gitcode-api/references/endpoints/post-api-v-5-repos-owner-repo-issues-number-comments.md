# Create Issue Comment
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-issues-number-comments](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-issues-number-comments)
Category: Issues
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/issues/{number}/comments`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_issues_{number}_comments`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | issue number |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "body": {
      "description": "The contents of the comment.",
      "type": "string"
    }
  },
  "required": [
    "body"
  ],
  "type": "object"
}
```
Example:
```json
""
```
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
    "created_at": {
      "type": "null"
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
      "type": "null"
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
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "body": "Comment content.",
      "created_at": null,
      "id": 271624,
      "target": {
        "issue": {
          "id": 152134,
          "nubmer": 1,
          "title": ""
        }
      },
      "updated_at": null,
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
## JSON Request Example
```json
{
  "body": "string"
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
  "jsonRequestBodyExample": {
    "body": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_issues_{number}_comments",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/issues/{number}/comments",
  "postman": {
    "body": {
      "mode": "raw",
      "options": {
        "raw": {
          "language": "json"
        }
      },
      "raw": ""
    },
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "application/json"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "POST",
    "name": "Create Issue Comment",
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "body": {
              "description": "The contents of the comment.",
              "type": "string"
            }
          },
          "required": [
            "body"
          ],
          "type": "object"
        }
      }
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
                "created_at": null,
                "id": 271624,
                "target": {
                  "issue": {
                    "id": 152134,
                    "nubmer": 1,
                    "title": ""
                  }
                },
                "updated_at": null,
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
            "properties": {
              "body": {
                "type": "string"
              },
              "created_at": {
                "type": "null"
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
                "type": "null"
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
