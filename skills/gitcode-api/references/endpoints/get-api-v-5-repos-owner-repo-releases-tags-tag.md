# Get Repository Release By Tag Name
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tags-tag](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tags-tag)
Category: Release
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/releases/tags/{tag}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_releases_tags_{tag}`
- Tags: `Release`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| tag | path | true | string | Tag Name |
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
    "assets": {
      "items": {
        "properties": {
          "browser_download_url": {
            "type": "string"
          },
          "name": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
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
        },
        "type": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "body": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "prerelease": {
      "type": "integer"
    },
    "tag_name": {
      "type": "string"
    },
    "target_commitish": {
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
      "body": "learn serde description",
      "created_at": "2025-01-16T19:58:07+08:00",
      "name": "learn serde",
      "prerelease": false,
      "tag_name": "v1.0.217",
      "target_commitish": "930401b0dd58a809fce34da091b8aa3d6083cb33"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_releases_tags_{tag}",
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
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/tags/{tag}",
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
    "name": "Get Repository Release By Tag Name",
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
        "tags",
        ":tag"
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
                "body": "learn serde description",
                "created_at": "2025-01-16T19:58:07+08:00",
                "name": "learn serde",
                "prerelease": false,
                "tag_name": "v1.0.217",
                "target_commitish": "930401b0dd58a809fce34da091b8aa3d6083cb33"
              }
            }
          },
          "schema": {
            "properties": {
              "assets": {
                "items": {
                  "properties": {
                    "browser_download_url": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
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
                  },
                  "type": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "body": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "prerelease": {
                "type": "integer"
              },
              "tag_name": {
                "type": "string"
              },
              "target_commitish": {
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
    "Release"
  ]
}
```
