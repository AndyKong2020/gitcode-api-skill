# Get All Repository Commits
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-commits](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-commits)
Category: Commit
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/commits`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_commits`
- Tags: `Commit`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| sha | query | false | string | Submit the starting SHA value |
| path | query | false | string | The commit containing the file |
| author | query | false | string | Submit the author's email or personal space address (username/login) |
| since | query | false | string | Submission start time, time format (2024-11-08T16:25:44Z) |
| until | query | false | string | The final submission time, in the format (2024-11-08T16:25:44Z) |
| page | query | false | string | The current page number |
| per_page | query | false | string | The number of items per page, with a maximum of 100. The default is 20. |
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
          "email": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "comments_url": {
        "type": "string"
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
              }
            },
            "type": "object"
          },
          "committer": {
            "properties": {
              "date": {
                "type": "string"
              },
              "email": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "message": {
            "type": "string"
          },
          "tree": {
            "properties": {
              "sha": {
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            },
            "type": "object"
          }
        },
        "type": "object"
      },
      "committer": {
        "properties": {
          "date": {
            "type": "string"
          },
          "email": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "html_url": {
        "type": "string"
      },
      "parents": {
        "items": {
          "properties": {
            "sha": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "sha": {
        "type": "string"
      },
      "url": {
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
    "email": "my@dengmengmian.com",
    "login": "underwater dreaming (Ma Fan)",
    "type": "User"
  },
  "comments_url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/66a12f572722ebe2cad44f44d48e253a0f027e09/comments",
  "commit": {
    "author": {
      "date": "2024-09-25T08:14:59+08:00",
      "email": "my@dengmengmian.com"
    },
    "committer": {
      "date": "2024-09-25T08:14:59+08:00",
      "email": "my@dengmengmian.com"
    },
    "message": "feat: all issue numbers changed to string type",
    "tree": {
      "sha": "6214a5921eda7f5148f249587b74201d5946a6d4",
      "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/git/trees/6214a5921eda7f5148f249587b74201d5946a6d4"
    }
  },
  "committer": {
    "date": "2024-09-25T08:14:59+08:00",
    "email": "my@dengmengmian.com",
    "type": "User"
  },
  "html_url": "https://test.gitcode.net/mactribe/test02/commits/detail/66a12f572722ebe2cad44f44d48e253a0f027e09",
  "parents": [
    {
      "sha": "0c41318014c472534a2abc2e0aa498fd49d046f1",
      "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/0c41318014c472534a2abc2e0aa498fd49d046f1"
    }
  ],
  "sha": "66a12f572722ebe2cad44f44d48e253a0f027e09",
  "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/66a12f572722ebe2cad44f44d48e253a0f027e09"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_commits",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Submit the starting SHA value",
      "in": "query",
      "name": "sha",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The commit containing the file",
      "in": "query",
      "name": "path",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Submit the author's email or personal space address (username/login)",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Submission start time, time format (2024-11-08T16:25:44Z)",
      "in": "query",
      "name": "since",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The final submission time, in the format (2024-11-08T16:25:44Z)",
      "in": "query",
      "name": "until",
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
        "type": "string"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/commits",
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
    "name": "Get All Repository Commits",
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
            "content": "Submit the starting SHA value",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sha",
          "value": ""
        },
        {
          "description": {
            "content": "The commit containing the file",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "path",
          "value": ""
        },
        {
          "description": {
            "content": "Submit the author's email or personal space address (username/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Submission start time, time format (2024-11-08T16:25:44Z)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
          "value": ""
        },
        {
          "description": {
            "content": "The final submission time, in the format (2024-11-08T16:25:44Z)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "until",
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
              "email": "my@dengmengmian.com",
              "login": "underwater dreaming (Ma Fan)",
              "type": "User"
            },
            "comments_url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/66a12f572722ebe2cad44f44d48e253a0f027e09/comments",
            "commit": {
              "author": {
                "date": "2024-09-25T08:14:59+08:00",
                "email": "my@dengmengmian.com"
              },
              "committer": {
                "date": "2024-09-25T08:14:59+08:00",
                "email": "my@dengmengmian.com"
              },
              "message": "feat: all issue numbers changed to string type",
              "tree": {
                "sha": "6214a5921eda7f5148f249587b74201d5946a6d4",
                "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/git/trees/6214a5921eda7f5148f249587b74201d5946a6d4"
              }
            },
            "committer": {
              "date": "2024-09-25T08:14:59+08:00",
              "email": "my@dengmengmian.com",
              "type": "User"
            },
            "html_url": "https://test.gitcode.net/mactribe/test02/commits/detail/66a12f572722ebe2cad44f44d48e253a0f027e09",
            "parents": [
              {
                "sha": "0c41318014c472534a2abc2e0aa498fd49d046f1",
                "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/0c41318014c472534a2abc2e0aa498fd49d046f1"
              }
            ],
            "sha": "66a12f572722ebe2cad44f44d48e253a0f027e09",
            "url": "https://api.gitcode.com/api/v5/repos/mactribe/test02/commits/66a12f572722ebe2cad44f44d48e253a0f027e09"
          },
          "schema": {
            "items": {
              "properties": {
                "author": {
                  "properties": {
                    "email": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "comments_url": {
                  "type": "string"
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
                        }
                      },
                      "type": "object"
                    },
                    "committer": {
                      "properties": {
                        "date": {
                          "type": "string"
                        },
                        "email": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "message": {
                      "type": "string"
                    },
                    "tree": {
                      "properties": {
                        "sha": {
                          "type": "string"
                        },
                        "url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    }
                  },
                  "type": "object"
                },
                "committer": {
                  "properties": {
                    "date": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "html_url": {
                  "type": "string"
                },
                "parents": {
                  "items": {
                    "properties": {
                      "sha": {
                        "type": "string"
                      },
                      "url": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "sha": {
                  "type": "string"
                },
                "url": {
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
    "Commit"
  ]
}
```
