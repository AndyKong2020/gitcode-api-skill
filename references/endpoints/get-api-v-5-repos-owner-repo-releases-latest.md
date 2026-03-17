# Get the Latest Release of the Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-latest](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-latest)
Category: Release
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/releases/latest`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_releases_latest`
- Tags: `Release`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
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
        "required": [
          "browser_download_url",
          "name"
        ],
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
      "required": [
        "id",
        "login",
        "name",
        "avatar_url",
        "html_url",
        "type",
        "url"
      ],
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
      "type": "boolean"
    },
    "tag_name": {
      "type": "string"
    },
    "target_commitish": {
      "type": "string"
    }
  },
  "required": [
    "tag_name",
    "target_commitish",
    "prerelease",
    "name",
    "body",
    "author",
    "created_at",
    "assets"
  ],
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
          "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.zip",
          "name": "YanF1-V0.0.1.zip"
        },
        {
          "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar.gz",
          "name": "YanF1-V0.0.1.tar.gz"
        },
        {
          "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar.bz2",
          "name": "YanF1-V0.0.1.tar.bz2"
        },
        {
          "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar",
          "name": "YanF1-V0.0.1.tar"
        }
      ],
      "author": {
        "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/df/ae/64d7f5ae52df30ea2b696064187dbf4871e29217a1a9de303bbc46f43dbb0dd6.png?time=1737363381562",
        "html_url": "https://test.gitcode.net/yanfan",
        "id": "645",
        "login": "yanfan",
        "name": "abcabcabc",
        "type": "User",
        "url": "https://api-test.gitcode.net/api/v5/users/yanfan"
      },
      "body": "V0.0.1",
      "created_at": "2024-04-15T20:43:35+08:00",
      "name": "V0.0.1",
      "prerelease": false,
      "tag_name": "V0.0.1",
      "target_commitish": "b33d10690347a36ccbf7464fe16466c1409f9533"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_releases_latest",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/latest",
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
    "name": "Get the Latest Release of the Repository",
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
        "latest"
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
                    "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.zip",
                    "name": "YanF1-V0.0.1.zip"
                  },
                  {
                    "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar.gz",
                    "name": "YanF1-V0.0.1.tar.gz"
                  },
                  {
                    "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar.bz2",
                    "name": "YanF1-V0.0.1.tar.bz2"
                  },
                  {
                    "browser_download_url": "https://test.gitcode.net/test_associate/YanF1/-/archive/V0.0.1/YanF1-V0.0.1.tar",
                    "name": "YanF1-V0.0.1.tar"
                  }
                ],
                "author": {
                  "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/df/ae/64d7f5ae52df30ea2b696064187dbf4871e29217a1a9de303bbc46f43dbb0dd6.png?time=1737363381562",
                  "html_url": "https://test.gitcode.net/yanfan",
                  "id": "645",
                  "login": "yanfan",
                  "name": "abcabcabc",
                  "type": "User",
                  "url": "https://api-test.gitcode.net/api/v5/users/yanfan"
                },
                "body": "V0.0.1",
                "created_at": "2024-04-15T20:43:35+08:00",
                "name": "V0.0.1",
                "prerelease": false,
                "tag_name": "V0.0.1",
                "target_commitish": "b33d10690347a36ccbf7464fe16466c1409f9533"
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
                  "required": [
                    "browser_download_url",
                    "name"
                  ],
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
                "required": [
                  "id",
                  "login",
                  "name",
                  "avatar_url",
                  "html_url",
                  "type",
                  "url"
                ],
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
                "type": "boolean"
              },
              "tag_name": {
                "type": "string"
              },
              "target_commitish": {
                "type": "string"
              }
            },
            "required": [
              "tag_name",
              "target_commitish",
              "prerelease",
              "name",
              "body",
              "author",
              "created_at",
              "assets"
            ],
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
