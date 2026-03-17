# Create New File
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-contents-path](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-contents-path)
Category: Repositories
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/contents/{path}`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_contents_{path}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| path | path | true | string | File path |
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
      "description": "The submitted branch",
      "type": "string"
    },
    "content": {
      "description": "File content to be base64 encoded",
      "type": "string"
    },
    "message": {
      "description": "The commit message for the submitted commit.",
      "type": "string"
    }
  },
  "required": [
    "content",
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
            "properties": {
              "sha": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "type": "array"
        },
        "sha": {
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
          "date": "2024-04-11T09:15:20+00:00",
          "email": "13328943+gitcode_admin@user.noreply.gitcode.com",
          "name": "GitCode2023"
        },
        "committer": {
          "date": "2024-04-11T09:15:20+00:00",
          "email": "noreply@gitcode.com",
          "name": "Gitee"
        },
        "message": "22222",
        "parents": [
          {
            "sha": "0117aa5c6bc8e33d18ad8911afa3cbb54a1faabe"
          }
        ],
        "sha": "668cb104692b30d537b07f3721df9956d073d343"
      }
    }
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
  "message": "string"
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
    "message": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_contents_{path}",
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
      "description": "File path",
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
    "method": "POST",
    "name": "Create New File",
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
            "content": "(Required) File path",
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
              "description": "The submitted branch",
              "type": "string"
            },
            "content": {
              "description": "File content to be base64 encoded",
              "type": "string"
            },
            "message": {
              "description": "The commit message for the submitted commit.",
              "type": "string"
            }
          },
          "required": [
            "content",
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
                    "date": "2024-04-11T09:15:20+00:00",
                    "email": "13328943+gitcode_admin@user.noreply.gitcode.com",
                    "name": "GitCode2023"
                  },
                  "committer": {
                    "date": "2024-04-11T09:15:20+00:00",
                    "email": "noreply@gitcode.com",
                    "name": "Gitee"
                  },
                  "message": "22222",
                  "parents": [
                    {
                      "sha": "0117aa5c6bc8e33d18ad8911afa3cbb54a1faabe"
                    }
                  ],
                  "sha": "668cb104692b30d537b07f3721df9956d073d343"
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
                      "properties": {
                        "sha": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "type": "array"
                  },
                  "sha": {
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
