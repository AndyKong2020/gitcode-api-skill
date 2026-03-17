# Update Repository Release
Source: [https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-releases-tag](https://docs.gitcode.com/en/docs/apis/patch-api-v-5-repos-owner-repo-releases-tag)
Category: Release
- Method: `PATCH`
- Path: `/api/v5/repos/{owner}/{repo}/releases/{tag}`
- Operation ID: `patch-api-v-5-repos-owner-repo-releases-tag`
- Tags: `Release`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| tag | path | true | string | Tag Name |
| access_token | query | false | string | User authorization code |
| Content-Type | header | false | string |  |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "body": {
      "description": "Release Description",
      "type": "string"
    },
    "name": {
      "description": "Release Name",
      "type": "string"
    }
  },
  "required": [
    "name",
    "body"
  ],
  "type": "object"
}
```
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {},
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "assets": [
        {
          "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.zip",
          "name": "serde-v1.0.217.zip"
        },
        {
          "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar.gz",
          "name": "serde-v1.0.217.tar.gz"
        },
        {
          "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar.bz2",
          "name": "serde-v1.0.217.tar.bz2"
        },
        {
          "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar",
          "name": "serde-v1.0.217.tar"
        }
      ],
      "author": {
        "avatar_url": "https://cdn-img.gitcode.com/de/af/61d5ea0ffc926181d235ba5a66f58dc51734500a1eda9b0d429d71300c20a149.png?time=1732777805505",
        "html_url": "https://gitcode.com/fenglonghui",
        "id": "26593",
        "login": "fenglonghui",
        "name": "dragon glory",
        "type": "User",
        "url": "https://api.gitcode.com/api/v5/users/fenglonghui"
      },
      "body": "description1",
      "created_at": "2025-01-16T19:58:07+08:00",
      "name": "release1 Name",
      "prerelease": false,
      "tag_name": "v1.0.217",
      "target_commitish": "930401b0dd58a809fce34da091b8aa3d6083cb33"
    }
  }
}
```
## JSON Request Example
```json
{
  "body": "string",
  "name": "string"
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
    "body": "string",
    "name": "string"
  },
  "method": "patch",
  "operationId": "patch-api-v-5-repos-owner-repo-releases-tag",
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
      "description": "Tag Name",
      "example": "",
      "in": "path",
      "name": "tag",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "",
      "example": "application/json",
      "in": "header",
      "name": "Content-Type",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/{tag}",
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
    "method": "PATCH",
    "name": "Update Repository Release",
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
        "releases",
        ":tag"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
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
        },
        {
          "description": {
            "content": "(Required) Tag Name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "tag",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "body": {
              "description": "Release Description",
              "type": "string"
            },
            "name": {
              "description": "Release Name",
              "type": "string"
            }
          },
          "required": [
            "name",
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
                "assets": [
                  {
                    "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.zip",
                    "name": "serde-v1.0.217.zip"
                  },
                  {
                    "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar.gz",
                    "name": "serde-v1.0.217.tar.gz"
                  },
                  {
                    "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar.bz2",
                    "name": "serde-v1.0.217.tar.bz2"
                  },
                  {
                    "browser_download_url": "https://gitcode.com/rust-learning/serde/-/archive/v1.0.217/serde-v1.0.217.tar",
                    "name": "serde-v1.0.217.tar"
                  }
                ],
                "author": {
                  "avatar_url": "https://cdn-img.gitcode.com/de/af/61d5ea0ffc926181d235ba5a66f58dc51734500a1eda9b0d429d71300c20a149.png?time=1732777805505",
                  "html_url": "https://gitcode.com/fenglonghui",
                  "id": "26593",
                  "login": "fenglonghui",
                  "name": "dragon glory",
                  "type": "User",
                  "url": "https://api.gitcode.com/api/v5/users/fenglonghui"
                },
                "body": "description1",
                "created_at": "2025-01-16T19:58:07+08:00",
                "name": "release1 Name",
                "prerelease": false,
                "tag_name": "v1.0.217",
                "target_commitish": "930401b0dd58a809fce34da091b8aa3d6083cb33"
              }
            }
          },
          "schema": {
            "properties": {},
            "type": "object"
          }
        }
      },
      "description": "",
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
    "Release"
  ]
}
```
