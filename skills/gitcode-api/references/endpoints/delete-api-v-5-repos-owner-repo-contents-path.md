# Delete File
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-contents-path](https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-contents-path)
Category: Repositories
- Method: `DELETE`
- Path: `/api/v5/repos/{owner}/{repo}/contents/{path}`
- Operation ID: `delete_api_v5_repos_{owner}_{repo}_contents_{path}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| path | path | true | string | The path of the file. |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "branch": {
      "description": "Branch name. Defaults to the repository's default branch.",
      "type": "string"
    },
    "message": {
      "description": "commit message",
      "type": "string"
    },
    "sha": {
      "description": "The Blob SHA of the file",
      "type": "string"
    }
  },
  "required": [
    "sha",
    "message"
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
            "name": {
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
            },
            "name": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "message": {
          "type": "string"
        },
        "parents": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "sha": {
          "type": "string"
        },
        "tree": {
          "type": "string"
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
      "commit": {
        "author": {
          "date": "2024-11-25T02:11:56.000Z",
          "email": "1150456356@qq.com",
          "name": "xiaogang"
        },
        "committer": {
          "date": "2024-11-25T02:11:56.000Z",
          "email": "1150456356@qq.com",
          "name": "xiaogang"
        },
        "message": "API delete file",
        "parents": [
          "33e9ee7ccd32835a0fb9f2af99264931c06fbe11"
        ],
        "sha": "2a90c33ede2c1eafc5943727fd57129d870ad2e4",
        "tree": "791f24a0da8c8458e40da3243bde183d59773514"
      }
    }
  }
}
```
## JSON Request Example
```json
{
  "branch": "string",
  "message": "string",
  "sha": "string"
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
    "branch": "string",
    "message": "string",
    "sha": "string"
  },
  "method": "delete",
  "operationId": "delete_api_v5_repos_{owner}_{repo}_contents_{path}",
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
      "description": "The path of the file.",
      "example": "",
      "in": "path",
      "name": "path",
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
  "path": "/api/v5/repos/{owner}/{repo}/contents/{path}",
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
    "method": "DELETE",
    "name": "Delete File",
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
        "contents",
        ":path"
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
            "content": "(Required) The path of the file.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "path",
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
            "branch": {
              "description": "Branch name. Defaults to the repository's default branch.",
              "type": "string"
            },
            "message": {
              "description": "commit message",
              "type": "string"
            },
            "sha": {
              "description": "The Blob SHA of the file",
              "type": "string"
            }
          },
          "required": [
            "sha",
            "message"
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
                "commit": {
                  "author": {
                    "date": "2024-11-25T02:11:56.000Z",
                    "email": "1150456356@qq.com",
                    "name": "xiaogang"
                  },
                  "committer": {
                    "date": "2024-11-25T02:11:56.000Z",
                    "email": "1150456356@qq.com",
                    "name": "xiaogang"
                  },
                  "message": "API delete file",
                  "parents": [
                    "33e9ee7ccd32835a0fb9f2af99264931c06fbe11"
                  ],
                  "sha": "2a90c33ede2c1eafc5943727fd57129d870ad2e4",
                  "tree": "791f24a0da8c8458e40da3243bde183d59773514"
                }
              }
            }
          },
          "schema": {
            "properties": {
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
                      "name": {
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
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "message": {
                    "type": "string"
                  },
                  "parents": {
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  },
                  "sha": {
                    "type": "string"
                  },
                  "tree": {
                    "type": "string"
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
    "Repositories"
  ]
}
```
