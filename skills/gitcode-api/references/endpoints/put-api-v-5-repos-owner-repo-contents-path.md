# Update File
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-contents-path](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-contents-path)
Category: Repositories
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/contents/{path}`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_contents_{path}`
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
    "author[email]": {
      "description": "Author's email, defaults to the current user's email.",
      "type": "string"
    },
    "author[name]": {
      "description": "Author's name, defaults to the current user's name",
      "type": "string"
    },
    "branch": {
      "description": "Branch name. Defaults to the repository's default branch.",
      "type": "string"
    },
    "content": {
      "description": "File content to be base64 encoded",
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
    "content",
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
          "required": [
            "name",
            "email",
            "date"
          ],
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
          "required": [
            "name",
            "email",
            "date"
          ],
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
      "required": [
        "sha",
        "author",
        "committer",
        "message",
        "tree",
        "parents"
      ],
      "type": "object"
    },
    "content": {
      "properties": {
        "name": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "sha": {
          "type": "string"
        },
        "size": {
          "type": "integer"
        },
        "type": {
          "type": "string"
        }
      },
      "required": [
        "name",
        "path",
        "size",
        "sha",
        "type"
      ],
      "type": "object"
    }
  },
  "required": [
    "commit",
    "content"
  ],
  "type": "object"
}
```
Example:
```json
{
  "content": {
    "_links": {
      "html": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
      "self": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
    },
    "download_url": "https://gitcode.com/daming_1/zhu_di/raw/master/Note2.md",
    "html_url": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
    "name": "Note2.md",
    "path": "Note2.md",
    "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
  }
}
```
## JSON Request Example
```json
{
  "author[email]": "string",
  "author[name]": "string",
  "branch": "string",
  "content": "string",
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
    "author[email]": "string",
    "author[name]": "string",
    "branch": "string",
    "content": "string",
    "message": "string",
    "sha": "string"
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_contents_{path}",
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
    "method": "PUT",
    "name": "Update File",
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
            "author[email]": {
              "description": "Author's email, defaults to the current user's email.",
              "type": "string"
            },
            "author[name]": {
              "description": "Author's name, defaults to the current user's name",
              "type": "string"
            },
            "branch": {
              "description": "Branch name. Defaults to the repository's default branch.",
              "type": "string"
            },
            "content": {
              "description": "File content to be base64 encoded",
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
            "content",
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
          "example": {
            "content": {
              "_links": {
                "html": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
                "self": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
              },
              "download_url": "https://gitcode.com/daming_1/zhu_di/raw/master/Note2.md",
              "html_url": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
              "name": "Note2.md",
              "path": "Note2.md",
              "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
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
                    "required": [
                      "name",
                      "email",
                      "date"
                    ],
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
                    "required": [
                      "name",
                      "email",
                      "date"
                    ],
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
                "required": [
                  "sha",
                  "author",
                  "committer",
                  "message",
                  "tree",
                  "parents"
                ],
                "type": "object"
              },
              "content": {
                "properties": {
                  "name": {
                    "type": "string"
                  },
                  "path": {
                    "type": "string"
                  },
                  "sha": {
                    "type": "string"
                  },
                  "size": {
                    "type": "integer"
                  },
                  "type": {
                    "type": "string"
                  }
                },
                "required": [
                  "name",
                  "path",
                  "size",
                  "sha",
                  "type"
                ],
                "type": "object"
              }
            },
            "required": [
              "commit",
              "content"
            ],
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
