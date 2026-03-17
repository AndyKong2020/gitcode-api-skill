# Get Repository Contributors Statistics
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-contributors-statistic](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-contributors-statistic)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/contributors/statistic`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_contributors_statistic`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| author | query | false | string | Filter contributors by username. Supports specifying a username to get contribution data for that user. Returns contribution data for all users by default. |
| current_user | query | false | boolean | Whether to return data only for the current user. `true` indicates that only the contribution data of the current user will be returned; `false` or omission will result in returning the contribution data of all users. When set to `true`, it has a higher priority than the `author` parameter. |
| since | query | false | string | Start date, formatted as `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the start time of the contribution data returned. |
| until | query | false | string | End date in the format of `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the end time of the contribution data returned. |
| ref_name | query | false | string | Specify the ref_name (branch name, commit ID, or tag name) to get contribution data. If not provided or empty, use the `default branch`. |
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
  "items": {
    "properties": {
      "contributions": {
        "items": {
          "properties": {
            "additions": {
              "type": "integer"
            },
            "commit_count": {
              "type": "integer"
            },
            "date": {
              "type": "string"
            },
            "deletions": {
              "type": "integer"
            },
            "total_changes": {
              "type": "integer"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "email": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "overview": {
        "properties": {
          "additions": {
            "type": "integer"
          },
          "commit_count": {
            "type": "integer"
          },
          "deletions": {
            "type": "integer"
          },
          "total_changes": {
            "type": "integer"
          }
        },
        "type": "object"
      }
    },
    "type": "object"
  },
  "type": "array"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "contributions": [
        {
          "additions": 759,
          "commit_count": 5,
          "date": "2024-12-05",
          "deletions": 0,
          "total_changes": 759
        },
        {
          "additions": 2,
          "commit_count": 2,
          "date": "2024-12-08",
          "deletions": 0,
          "total_changes": 2
        },
        {
          "additions": 1,
          "commit_count": 1,
          "date": "2024-12-09",
          "deletions": 0,
          "total_changes": 1
        }
      ],
      "email": "aa@ss.com",
      "name": "test",
      "overview": {
        "additions": 762,
        "commit_count": 8,
        "deletions": 0,
        "total_changes": 0
      }
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_contributors_statistic",
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
    },
    {
      "description": "Filter contributors by username. Supports specifying a username to get contribution data for that user. Returns contribution data for all users by default.",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Whether to return data only for the current user. `true` indicates that only the contribution data of the current user will be returned; `false` or omission will result in returning the contribution data of all users. When set to `true`, it has a higher priority than the `author` parameter.",
      "in": "query",
      "name": "current_user",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    },
    {
      "description": "Start date, formatted as `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the start time of the contribution data returned.",
      "in": "query",
      "name": "since",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "End date in the format of `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the end time of the contribution data returned.",
      "in": "query",
      "name": "until",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Specify the ref_name (branch name, commit ID, or tag name) to get contribution data. If not provided or empty, use the `default branch`.",
      "in": "query",
      "name": "ref_name",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/contributors/statistic",
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
    "name": "Get Repository Contributors Statistics",
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
        "contributors",
        "statistic"
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
            "content": "Filter contributors by username. Supports specifying a username to get contribution data for that user. Returns contribution data for all users by default.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Whether to return data only for the current user. `true` indicates that only the contribution data of the current user will be returned; `false` or omission will result in returning the contribution data of all users. When set to `true`, it has a higher priority than the `author` parameter.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "current_user",
          "value": ""
        },
        {
          "description": {
            "content": "Start date, formatted as `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the start time of the contribution data returned.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "since",
          "value": ""
        },
        {
          "description": {
            "content": "End date in the format of `YYYY-MM-DD` or `YYYY-MM-DD HH:mm:ss`. Used to limit the end time of the contribution data returned.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "until",
          "value": ""
        },
        {
          "description": {
            "content": "Specify the ref_name (branch name, commit ID, or tag name) to get contribution data. If not provided or empty, use the `default branch`.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "ref_name",
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
                "contributions": [
                  {
                    "additions": 759,
                    "commit_count": 5,
                    "date": "2024-12-05",
                    "deletions": 0,
                    "total_changes": 759
                  },
                  {
                    "additions": 2,
                    "commit_count": 2,
                    "date": "2024-12-08",
                    "deletions": 0,
                    "total_changes": 2
                  },
                  {
                    "additions": 1,
                    "commit_count": 1,
                    "date": "2024-12-09",
                    "deletions": 0,
                    "total_changes": 1
                  }
                ],
                "email": "aa@ss.com",
                "name": "test",
                "overview": {
                  "additions": 762,
                  "commit_count": 8,
                  "deletions": 0,
                  "total_changes": 0
                }
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "contributions": {
                  "items": {
                    "properties": {
                      "additions": {
                        "type": "integer"
                      },
                      "commit_count": {
                        "type": "integer"
                      },
                      "date": {
                        "type": "string"
                      },
                      "deletions": {
                        "type": "integer"
                      },
                      "total_changes": {
                        "type": "integer"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "email": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "overview": {
                  "properties": {
                    "additions": {
                      "type": "integer"
                    },
                    "commit_count": {
                      "type": "integer"
                    },
                    "deletions": {
                      "type": "integer"
                    },
                    "total_changes": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                }
              },
              "type": "object"
            },
            "type": "array"
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
