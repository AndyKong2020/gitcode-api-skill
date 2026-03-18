# Get File Blob
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-git-blobs-sha](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-git-blobs-sha)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/git/blobs/{sha}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_git_blobs_{sha}`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| sha | path | true | string | The Blob SHA of the file, which can be obtained via the [Get Contents in Specific Repository Path] API. |
| access_token | query | true | string | User authorization code |
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
    "content": {
      "type": "string"
    },
    "encoding": {
      "type": "string"
    },
    "sha": {
      "type": "string"
    },
    "size": {
      "type": "integer"
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
      "content": "JXU2RDRCJXU4QkQ1d2ViaG9vaw==",
      "encoding": "base64",
      "sha": "e5699fe1b360d6c799ee58b24fb5a670b1e14851",
      "size": 19,
      "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/git/blobs/e5699fe1b360d6c799ee58b24fb5a670b1e14851"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_git_blobs_{sha}",
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
      "description": "The Blob SHA of the file, which can be obtained via the [Get Contents in Specific Repository Path] API.",
      "example": "",
      "in": "path",
      "name": "sha",
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
  "path": "/api/v5/repos/{owner}/{repo}/git/blobs/{sha}",
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
    "name": "Get File Blob",
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
        "git",
        "blobs",
        ":sha"
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
            "content": "(Required) The Blob SHA of the file, which can be obtained via the [Get Contents in Specific Repository Path] API.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sha",
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
                "content": "JXU2RDRCJXU4QkQ1d2ViaG9vaw==",
                "encoding": "base64",
                "sha": "e5699fe1b360d6c799ee58b24fb5a670b1e14851",
                "size": 19,
                "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/git/blobs/e5699fe1b360d6c799ee58b24fb5a670b1e14851"
              }
            }
          },
          "schema": {
            "properties": {
              "content": {
                "type": "string"
              },
              "encoding": {
                "type": "string"
              },
              "sha": {
                "type": "string"
              },
              "size": {
                "type": "integer"
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
