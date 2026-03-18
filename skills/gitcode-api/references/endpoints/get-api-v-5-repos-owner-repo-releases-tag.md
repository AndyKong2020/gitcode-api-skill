# Get Single Release of Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tag](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-releases-tag)
Category: Release
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/releases/{tag}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_releases_{tag}`
- Tags: `Release`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| tag | path | true | string | Tag Name |
| access_token | query | true | string | User authorization code |
| temp_download_url | query | false | string | Whether to return the source package and attachment temporary download address, default false |
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
          },
          "type": {
            "type": "string"
          }
        },
        "required": [
          "browser_download_url",
          "name",
          "type"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_releases_{tag}",
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
      "description": "Tag Name",
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
    },
    {
      "description": "Whether to return the source package and attachment temporary download address, default false",
      "in": "query",
      "name": "temp_download_url",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/releases/{tag}",
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
    "name": "Get Single Release of Repository",
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
            "content": "(Required) User authorization code",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "Whether to return the source package and attachment temporary download address, default false",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "temp_download_url",
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
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "browser_download_url",
                    "name",
                    "type"
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
