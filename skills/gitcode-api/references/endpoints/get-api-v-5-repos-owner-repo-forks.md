# View Repository Forks
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-forks](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-forks)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/forks`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_forks`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| sort | query | false | string | Sort by: fork time (newest, oldest), stars count (stargazers) |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| created_after | query | false | string | Created after this |
| created_before | query | false | string | Created before this |
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
      "created_at": {
        "type": "string"
      },
      "description": {
        "type": "string"
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
        "type": "object"
      },
      "owner": {
        "properties": {
          "id": {
            "type": "integer"
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
      "parent": {
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          },
          "id": {
            "type": "integer"
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
            "type": "object"
          },
          "url": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "private": {
        "type": "integer"
      },
      "public": {
        "type": "integer"
      },
      "pushed_at": {
        "type": "string"
      },
      "status": {
        "type": "string"
      },
      "updated_at": {
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
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "created_at": "2024-07-29T15:42:45.149+08:00",
      "description": "",
      "full_name": "wangwt/RuoYi",
      "human_name": "wangwt / RuoYi",
      "id": 567682,
      "namespace": {
        "html_url": "https://test.gitcode.net/wangwt",
        "id": 153748,
        "name": "wangwt",
        "path": "wangwt",
        "type": "personal"
      },
      "owner": {
        "id": 970,
        "login": "wangwt",
        "name": "wangwt"
      },
      "parent": {
        "full_name": "xiaogang/RuoYi",
        "human_name": "xiaogang / RuoYi",
        "id": 517092,
        "namespace": {
          "html_url": "https://test.gitcode.net/xiaogang",
          "id": 137117,
          "name": "xiaogang",
          "path": "xiaogang",
          "type": "personal"
        },
        "url": "https://api.gitcode.com/api/v5/repos/xiaogang/RuoYi"
      },
      "private": false,
      "public": true,
      "pushed_at": "2024-11-08T16:24:10.576+08:00",
      "status": "",
      "updated_at": "2024-07-29T15:42:45.149+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/wangwt/RuoYi"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_forks",
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
      "description": "Sort by: fork time (newest, oldest), stars count (stargazers)",
      "in": "query",
      "name": "sort",
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
      "description": "Created after this",
      "in": "query",
      "name": "created_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Created before this",
      "in": "query",
      "name": "created_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/forks",
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
    "name": "View Repository Forks",
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
        "forks"
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
            "content": "Sort by: fork time (newest, oldest), stars count (stargazers)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
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
            "content": "Created after this",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_after",
          "value": ""
        },
        {
          "description": {
            "content": "Created before this",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "created_before",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "created_at": "2024-07-29T15:42:45.149+08:00",
                "description": "",
                "full_name": "wangwt/RuoYi",
                "human_name": "wangwt / RuoYi",
                "id": 567682,
                "namespace": {
                  "html_url": "https://test.gitcode.net/wangwt",
                  "id": 153748,
                  "name": "wangwt",
                  "path": "wangwt",
                  "type": "personal"
                },
                "owner": {
                  "id": 970,
                  "login": "wangwt",
                  "name": "wangwt"
                },
                "parent": {
                  "full_name": "xiaogang/RuoYi",
                  "human_name": "xiaogang / RuoYi",
                  "id": 517092,
                  "namespace": {
                    "html_url": "https://test.gitcode.net/xiaogang",
                    "id": 137117,
                    "name": "xiaogang",
                    "path": "xiaogang",
                    "type": "personal"
                  },
                  "url": "https://api.gitcode.com/api/v5/repos/xiaogang/RuoYi"
                },
                "private": false,
                "public": true,
                "pushed_at": "2024-11-08T16:24:10.576+08:00",
                "status": "",
                "updated_at": "2024-07-29T15:42:45.149+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/wangwt/RuoYi"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "created_at": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
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
                  "type": "object"
                },
                "owner": {
                  "properties": {
                    "id": {
                      "type": "integer"
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
                "parent": {
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
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
                      "type": "object"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "private": {
                  "type": "integer"
                },
                "public": {
                  "type": "integer"
                },
                "pushed_at": {
                  "type": "string"
                },
                "status": {
                  "type": "string"
                },
                "updated_at": {
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
    "Repositories"
  ]
}
```
