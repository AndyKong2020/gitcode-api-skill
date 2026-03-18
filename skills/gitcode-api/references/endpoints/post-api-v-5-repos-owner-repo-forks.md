# Fork a Repository
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-forks](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-forks)
Category: Repositories
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/forks`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_forks`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "name": {
      "description": "Name of the repository after forking. Defaults to the source repository name.",
      "type": "string"
    },
    "organization": {
      "description": "Full address of the organizational space. If not filled, it defaults to forking to the user's personal space address.",
      "type": "string"
    },
    "path": {
      "description": "Forked repository address after forking. Default: Source repository address",
      "type": "string"
    }
  },
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
    "full_name": {
      "type": "string"
    },
    "human_name": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "namespace": {
      "properties": {
        "cell": {
          "type": "string"
        },
        "develop_mode": {
          "type": "string"
        },
        "enable_file_control": {
          "type": "integer"
        },
        "full_name": {
          "type": "string"
        },
        "full_path": {
          "type": "string"
        },
        "id": {
          "type": "integer"
        },
        "kind": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "path": {
          "type": "string"
        },
        "visibility_level": {
          "type": "integer"
        }
      },
      "type": "object"
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
      "full_name": "xiaogang_test/fork2",
      "human_name": "test organization / fork2",
      "id": 729292,
      "namespace": {
        "cell": "default",
        "develop_mode": "normal",
        "enable_file_control": false,
        "full_name": "test organization",
        "full_path": "xiaogang_test",
        "id": 138108,
        "kind": "group",
        "name": "test organization",
        "path": "xiaogang_test",
        "visibility_level": 20
      },
      "url": "https://api.gitcode.com/api/v5/repos/xiaogang_test/fork2"
    }
  }
}
```
## JSON Request Example
```json
{
  "name": "string",
  "organization": "string",
  "path": "string"
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
    "name": "string",
    "organization": "string",
    "path": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_forks",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/forks",
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
    "name": "Fork a Repository",
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
        "forks"
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "name": {
              "description": "Name of the repository after forking. Defaults to the source repository name.",
              "type": "string"
            },
            "organization": {
              "description": "Full address of the organizational space. If not filled, it defaults to forking to the user's personal space address.",
              "type": "string"
            },
            "path": {
              "description": "Forked repository address after forking. Default: Source repository address",
              "type": "string"
            }
          },
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
                "full_name": "xiaogang_test/fork2",
                "human_name": "test organization / fork2",
                "id": 729292,
                "namespace": {
                  "cell": "default",
                  "develop_mode": "normal",
                  "enable_file_control": false,
                  "full_name": "test organization",
                  "full_path": "xiaogang_test",
                  "id": 138108,
                  "kind": "group",
                  "name": "test organization",
                  "path": "xiaogang_test",
                  "visibility_level": 20
                },
                "url": "https://api.gitcode.com/api/v5/repos/xiaogang_test/fork2"
              }
            }
          },
          "schema": {
            "properties": {
              "full_name": {
                "type": "string"
              },
              "human_name": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "namespace": {
                "properties": {
                  "cell": {
                    "type": "string"
                  },
                  "develop_mode": {
                    "type": "string"
                  },
                  "enable_file_control": {
                    "type": "integer"
                  },
                  "full_name": {
                    "type": "string"
                  },
                  "full_path": {
                    "type": "string"
                  },
                  "id": {
                    "type": "integer"
                  },
                  "kind": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "path": {
                    "type": "string"
                  },
                  "visibility_level": {
                    "type": "integer"
                  }
                },
                "type": "object"
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
