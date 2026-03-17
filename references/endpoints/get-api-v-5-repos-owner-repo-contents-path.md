# Get Contents at Specific Repository Path
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-contents-path](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-contents-path)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/contents/{path}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_contents_{path}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| path | path | true | string | The path of the file. |
| access_token | query | true | string | User authorization code |
| ref | query | false | string | Branch, tag, or commit. Defaults to the repository's default branch (main). |
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
  "properties": {
    "_links": {
      "properties": {
        "html": {
          "type": "string"
        },
        "self": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "content": {
      "type": "string"
    },
    "download_url": {
      "type": "string"
    },
    "encoding": {
      "type": "string"
    },
    "html_url": {
      "type": "string"
    },
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
    },
    "url": {
      "type": "string"
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
      "_links": {
        "html": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
        "self": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
      },
      "content": "JXU2RDRCJXU4QkQ1d2ViaG9vaw==",
      "download_url": "https://gitcode.com/daming_1/zhu_di/raw/master/Note2.md",
      "encoding": "base64",
      "html_url": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
      "name": "Note2.md",
      "path": "Note2.md",
      "sha": "e5699fe1b360d6c799ee58b24fb5a670b1e14851",
      "size": 19,
      "type": "file",
      "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_contents_{path}",
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
    },
    {
      "description": "Branch, tag, or commit. Defaults to the repository's default branch (main).",
      "in": "query",
      "name": "ref",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/contents/{path}",
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
    "name": "Get Contents at Specific Repository Path",
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
        },
        {
          "description": {
            "content": "Branch, tag, or commit. Defaults to the repository's default branch (main).",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "ref",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "_links": {
                  "html": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
                  "self": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
                },
                "content": "JXU2RDRCJXU4QkQ1d2ViaG9vaw==",
                "download_url": "https://gitcode.com/daming_1/zhu_di/raw/master/Note2.md",
                "encoding": "base64",
                "html_url": "https://gitcode.com/daming_1/zhu_di/blob/master/Note2.md",
                "name": "Note2.md",
                "path": "Note2.md",
                "sha": "e5699fe1b360d6c799ee58b24fb5a670b1e14851",
                "size": 19,
                "type": "file",
                "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/contents/Note2.md"
              }
            }
          },
          "schema": {
            "properties": {
              "_links": {
                "properties": {
                  "html": {
                    "type": "string"
                  },
                  "self": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "content": {
                "type": "string"
              },
              "download_url": {
                "type": "string"
              },
              "encoding": {
                "type": "string"
              },
              "html_url": {
                "type": "string"
              },
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
              },
              "url": {
                "type": "string"
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
