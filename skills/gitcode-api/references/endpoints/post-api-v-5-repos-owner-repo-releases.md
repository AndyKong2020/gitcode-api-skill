# Create Repository Release
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-releases](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-releases)
Category: Release
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/releases`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_releases`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "body": {
      "description": "release description",
      "type": "string"
    },
    "name": {
      "description": "release name",
      "type": "string"
    },
    "tag_name": {
      "description": "tag name",
      "type": "string"
    },
    "target_commitish": {
      "description": "Branch name or commit SHA. If the tag does not exist and a new tag needs to be created, pass this parameter. If it is not passed, the latest commit of the default branch will be used.",
      "type": "string"
    }
  },
  "required": [
    "tag_name",
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
## JSON Request Example
```json
{
  "body": "string",
  "name": "string",
  "tag_name": "string",
  "target_commitish": "string"
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
    "name": "string",
    "tag_name": "string",
    "target_commitish": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_releases",
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
      "description": "Repository path",
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
  "path": "/api/v5/repos/{owner}/{repo}/releases",
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
    "name": "Create Repository Release",
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
        "releases"
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
            "content": "(Required) Repository path",
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
  "requestBody": {
    "content": {
      "application/json": {
        "schema": {
          "properties": {
            "body": {
              "description": "release description",
              "type": "string"
            },
            "name": {
              "description": "release name",
              "type": "string"
            },
            "tag_name": {
              "description": "tag name",
              "type": "string"
            },
            "target_commitish": {
              "description": "Branch name or commit SHA. If the tag does not exist and a new tag needs to be created, pass this parameter. If it is not passed, the latest commit of the default branch will be used.",
              "type": "string"
            }
          },
          "required": [
            "tag_name",
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
  "tags": []
}
```
