# Get All Comments of a Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-comments](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-comments)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_comments`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number: defaults to 1 |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| direction | query | false | integer | Optional. Ascending/descending (asc/desc) |
| comment_type | query | false | string | Optional. Filter by comment type. Code line comment / PR ordinary comment: diff_comment / pr_comment |
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
      "comment_type": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "diff_file": {
        "type": "string"
      },
      "diff_position": {
        "properties": {
          "end_new_line": {
            "type": "integer"
          },
          "end_old_line": {
            "type": "integer"
          },
          "start_new_line": {
            "type": "integer"
          },
          "start_old_line": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "discussion_id": {
        "description": "Discussion ID",
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "reply": {
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
              "type": "object"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "resolved": {
        "type": "boolean"
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
          "id",
          "login",
          "name",
          "avatar_url",
          "html_url"
        ],
        "type": "object"
      }
    },
    "required": [
      "id",
      "body",
      "created_at",
      "updated_at",
      "user",
      "comment_type",
      "resolved",
      "diff_file",
      "diff_position",
      "discussion_id"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
{
  "body": "111",
  "created_at": "2024-04-19T07:48:59.755+00:00",
  "id": "de772738e6dab92174c0e86c052ccf9bed24f747",
  "updated_at": "2024-04-19T07:48:59.755+00:00",
  "user": {
    "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/cb/da/6cb18d9ae9f1a94b4f640d3b848351c352c7869f33d0cb68e7acad4f224c4e23.png",
    "html_url": "https://test.gitcode.net/Lzm_0916",
    "id": 708,
    "login": "Lzm_0916",
    "name": "Lzm_0916"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_comments",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
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
    },
    {
      "description": "Optional. Ascending/descending (asc/desc)",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Optional. Filter by comment type. Code line comment / PR ordinary comment: diff_comment / pr_comment",
      "in": "query",
      "name": "comment_type",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/comments",
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
    "name": "Get All Comments of a Pull Request",
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
        },
        {
          "description": {
            "content": "Optional. Ascending/descending (asc/desc)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "Optional. Filter by comment type. Code line comment / PR ordinary comment: diff_comment / pr_comment",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "comment_type",
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
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
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
            "body": "111",
            "created_at": "2024-04-19T07:48:59.755+00:00",
            "id": "de772738e6dab92174c0e86c052ccf9bed24f747",
            "updated_at": "2024-04-19T07:48:59.755+00:00",
            "user": {
              "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/cb/da/6cb18d9ae9f1a94b4f640d3b848351c352c7869f33d0cb68e7acad4f224c4e23.png",
              "html_url": "https://test.gitcode.net/Lzm_0916",
              "id": 708,
              "login": "Lzm_0916",
              "name": "Lzm_0916"
            }
          },
          "schema": {
            "items": {
              "properties": {
                "body": {
                  "type": "string"
                },
                "comment_type": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "diff_file": {
                  "type": "string"
                },
                "diff_position": {
                  "properties": {
                    "end_new_line": {
                      "type": "integer"
                    },
                    "end_old_line": {
                      "type": "integer"
                    },
                    "start_new_line": {
                      "type": "integer"
                    },
                    "start_old_line": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "discussion_id": {
                  "description": "Discussion ID",
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "reply": {
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
                        "type": "object"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "resolved": {
                  "type": "boolean"
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
                    "id",
                    "login",
                    "name",
                    "avatar_url",
                    "html_url"
                  ],
                  "type": "object"
                }
              },
              "required": [
                "id",
                "body",
                "created_at",
                "updated_at",
                "user",
                "comment_type",
                "resolved",
                "diff_file",
                "diff_position",
                "discussion_id"
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
    "Pull Requests"
  ]
}
```
