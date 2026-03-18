# Get Code Contribution
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-owner-repo-repository-commit-statistics](https://docs.gitcode.com/en/docs/apis/get-api-v-5-owner-repo-repository-commit-statistics)
Category: Commit
- Method: `GET`
- Path: `/api/v5/{owner}/{repo}/repository/commit_statistics`
- Operation ID: `get_api_v5_{owner}_{repo}_repository_commit_statistics`
- Tags: `Commit`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| branch_name | query | true | string | branch name |
| author | query | false | string | Author username |
| only_self | query | false | boolean | Query Individual |
| since | query | false | string | Return only commits on or after this date. |
| until | query | false | string | Return only commits up to and including this date. |
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
    "commits": {
      "items": {
        "properties": {
          "author_name": {
            "type": "string"
          },
          "date": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "statistics": {
      "items": {
        "properties": {
          "add_lines": {
            "type": "integer"
          },
          "branch": {
            "type": "string"
          },
          "commit_count": {
            "type": "integer"
          },
          "delete_lines": {
            "type": "integer"
          },
          "nick_name": {
            "type": "string"
          },
          "project_id": {
            "type": "integer"
          },
          "user_name": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "total": {
      "type": "integer"
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
      "commits": [
        {
          "author_name": "tester",
          "date": "2024-11-12"
        },
        {
          "author_name": "tester",
          "date": "2024-01-15"
        }
      ],
      "statistics": [
        {
          "add_lines": 4370,
          "branch": "main",
          "commit_count": 123,
          "delete_lines": 351,
          "nick_name": "testing",
          "project_id": 1359,
          "user_name": "tester"
        }
      ],
      "total": 1
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
  "operationId": "get_api_v5_{owner}_{repo}_repository_commit_statistics",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "branch name",
      "in": "query",
      "name": "branch_name",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Author username",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Query Individual",
      "in": "query",
      "name": "only_self",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    },
    {
      "description": "Return only commits on or after this date.",
      "in": "query",
      "name": "since",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Return only commits up to and including this date.",
      "in": "query",
      "name": "until",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/{owner}/{repo}/repository/commit_statistics",
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
    "name": "Get Code Contribution",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        ":owner",
        ":repo",
        "repository",
        "commit_statistics"
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
            "content": "(Required) branch name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "branch_name",
          "value": ""
        },
        {
          "description": {
            "content": "Author username",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Query Individual",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "only_self",
          "value": ""
        },
        {
          "description": {
            "content": "Return only commits on or after this date.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
          "value": ""
        },
        {
          "description": {
            "content": "Return only commits up to and including this date.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "until",
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
                "commits": [
                  {
                    "author_name": "tester",
                    "date": "2024-11-12"
                  },
                  {
                    "author_name": "tester",
                    "date": "2024-01-15"
                  }
                ],
                "statistics": [
                  {
                    "add_lines": 4370,
                    "branch": "main",
                    "commit_count": 123,
                    "delete_lines": 351,
                    "nick_name": "testing",
                    "project_id": 1359,
                    "user_name": "tester"
                  }
                ],
                "total": 1
              }
            }
          },
          "schema": {
            "properties": {
              "commits": {
                "items": {
                  "properties": {
                    "author_name": {
                      "type": "string"
                    },
                    "date": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "statistics": {
                "items": {
                  "properties": {
                    "add_lines": {
                      "type": "integer"
                    },
                    "branch": {
                      "type": "string"
                    },
                    "commit_count": {
                      "type": "integer"
                    },
                    "delete_lines": {
                      "type": "integer"
                    },
                    "nick_name": {
                      "type": "string"
                    },
                    "project_id": {
                      "type": "integer"
                    },
                    "user_name": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "total": {
                "type": "integer"
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
    "Commit"
  ]
}
```
