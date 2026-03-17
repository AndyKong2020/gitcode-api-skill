# Get All Commit Information for a Specific Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-commits](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-commits)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/commits`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_commits`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
| page | query | false | string | Current page number |
| per_page | query | false | string | Number of items per page |
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
      "author": {
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
      },
      "commit": {
        "properties": {
          "author": {
            "properties": {
              "date": {
                "type": "string"
              },
              "email": {
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
          },
          "committer": {
            "properties": {
              "email": {
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
          },
          "message": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "committer": {
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
      },
      "html_url": {
        "type": "string"
      },
      "parents": {
        "properties": {
          "sha": {
            "type": "string"
          },
          "shas": {
            "items": {
              "type": "string"
            },
            "type": "array"
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
  "type": "array"
}
```
Example:
```json
{
  "author": {
    "avatar_url": "https://gitcode/pic.png",
    "html_url": "https://gitcode.com/test",
    "id": "id123",
    "login": "test",
    "name": "test"
  },
  "commit": {
    "author": {
      "date": "2024-03-28T11:19:33+08:00",
      "email": "test@test.com",
      "login": "test",
      "name": "test"
    },
    "committer": {
      "email": "test@test.com",
      "login": "test",
      "name": "test"
    },
    "message": "!5 333 * add 1/2/3/4. * add 1/2/3. "
  },
  "committer": {
    "avatar_url": "https://gitcode/pic.png",
    "html_url": "https://gitcode.com/test",
    "id": "id123",
    "login": "test",
    "name": "test"
  },
  "html_url": "https://gitcode.com/sytest/paopao/blob/91861a9668041fc1c0ff51d1db66b6297179f5e6",
  "parents": {
    "sha": "2e208a1e38f6a5a7b0cc3787688067ba082a8bb7",
    "shas": [
      "2e208a1e38f6a5a7b0cc3787688067ba082a8bb7"
    ]
  },
  "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_commits",
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
      "description": "Current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Number of items per page",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/commits",
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
    "name": "Get All Commit Information for a Specific Pull Request",
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
        "commits"
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
            "content": "Current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "Number of items per page",
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
            "author": {
              "avatar_url": "https://gitcode/pic.png",
              "html_url": "https://gitcode.com/test",
              "id": "id123",
              "login": "test",
              "name": "test"
            },
            "commit": {
              "author": {
                "date": "2024-03-28T11:19:33+08:00",
                "email": "test@test.com",
                "login": "test",
                "name": "test"
              },
              "committer": {
                "email": "test@test.com",
                "login": "test",
                "name": "test"
              },
              "message": "!5 333 * add 1/2/3/4. * add 1/2/3. "
            },
            "committer": {
              "avatar_url": "https://gitcode/pic.png",
              "html_url": "https://gitcode.com/test",
              "id": "id123",
              "login": "test",
              "name": "test"
            },
            "html_url": "https://gitcode.com/sytest/paopao/blob/91861a9668041fc1c0ff51d1db66b6297179f5e6",
            "parents": {
              "sha": "2e208a1e38f6a5a7b0cc3787688067ba082a8bb7",
              "shas": [
                "2e208a1e38f6a5a7b0cc3787688067ba082a8bb7"
              ]
            },
            "sha": "91861a9668041fc1c0ff51d1db66b6297179f5e6"
          },
          "schema": {
            "items": {
              "properties": {
                "author": {
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
                },
                "commit": {
                  "properties": {
                    "author": {
                      "properties": {
                        "date": {
                          "type": "string"
                        },
                        "email": {
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
                    },
                    "committer": {
                      "properties": {
                        "email": {
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
                    },
                    "message": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "committer": {
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
                },
                "html_url": {
                  "type": "string"
                },
                "parents": {
                  "properties": {
                    "sha": {
                      "type": "string"
                    },
                    "shas": {
                      "items": {
                        "type": "string"
                      },
                      "type": "array"
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
