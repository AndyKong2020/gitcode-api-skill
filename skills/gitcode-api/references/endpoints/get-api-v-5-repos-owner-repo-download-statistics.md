# Download Count Statistics
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-download-statistics](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-download-statistics)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/download_statistics`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_download_statistics`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| start_date | query | false | string | The start date for the statistics includes the current date (e.g.: 2024-01-06) |
| end_date | query | false | string | The end date for statistics includes the current date (e.g., 2024-12-06) |
| direction | query | false | string | Sort order: asc for ascending, desc for descending. Default: desc |
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
    "download_statistics_detail": {
      "items": {
        "properties": {
          "pdate": {
            "type": "string"
          },
          "repo_id": {
            "type": "string"
          },
          "today_dl_cnt": {
            "type": "integer"
          },
          "total_dl_cnt": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "download_statistics_history_total": {
      "type": "integer"
    },
    "download_statistics_total": {
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
      "download_statistics_detail": [
        {
          "pdate": "2024-11-13",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 38
        },
        {
          "pdate": "2024-11-14",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 38
        },
        {
          "pdate": "2024-11-15",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 38
        },
        {
          "pdate": "2024-11-16",
          "repo_id": "625513",
          "today_dl_cnt": 5,
          "total_dl_cnt": 43
        },
        {
          "pdate": "2024-11-17",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 43
        },
        {
          "pdate": "2024-11-18",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 43
        },
        {
          "pdate": "2024-11-19",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 43
        },
        {
          "pdate": "2024-11-20",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 43
        },
        {
          "pdate": "2024-11-21",
          "repo_id": "625513",
          "today_dl_cnt": 2,
          "total_dl_cnt": 45
        },
        {
          "pdate": "2024-11-22",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 45
        },
        {
          "pdate": "2024-11-23",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 45
        },
        {
          "pdate": "2024-11-24",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 45
        },
        {
          "pdate": "2024-11-25",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 45
        },
        {
          "pdate": "2024-11-26",
          "repo_id": "625513",
          "today_dl_cnt": 0,
          "total_dl_cnt": 45
        }
      ],
      "download_statistics_history_total": 45,
      "download_statistics_total": 7
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_download_statistics",
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
      "description": "The start date for the statistics includes the current date (e.g.: 2024-01-06)",
      "in": "query",
      "name": "start_date",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The end date for statistics includes the current date (e.g., 2024-12-06)",
      "in": "query",
      "name": "end_date",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order: asc for ascending, desc for descending. Default: desc",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/download_statistics",
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
    "name": "Download Count Statistics",
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
        "download_statistics"
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
            "content": "The start date for the statistics includes the current date (e.g.: 2024-01-06)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "start_date",
          "value": ""
        },
        {
          "description": {
            "content": "The end date for statistics includes the current date (e.g., 2024-12-06)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "end_date",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order: asc for ascending, desc for descending. Default: desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
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
                "download_statistics_detail": [
                  {
                    "pdate": "2024-11-13",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 38
                  },
                  {
                    "pdate": "2024-11-14",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 38
                  },
                  {
                    "pdate": "2024-11-15",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 38
                  },
                  {
                    "pdate": "2024-11-16",
                    "repo_id": "625513",
                    "today_dl_cnt": 5,
                    "total_dl_cnt": 43
                  },
                  {
                    "pdate": "2024-11-17",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 43
                  },
                  {
                    "pdate": "2024-11-18",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 43
                  },
                  {
                    "pdate": "2024-11-19",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 43
                  },
                  {
                    "pdate": "2024-11-20",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 43
                  },
                  {
                    "pdate": "2024-11-21",
                    "repo_id": "625513",
                    "today_dl_cnt": 2,
                    "total_dl_cnt": 45
                  },
                  {
                    "pdate": "2024-11-22",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 45
                  },
                  {
                    "pdate": "2024-11-23",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 45
                  },
                  {
                    "pdate": "2024-11-24",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 45
                  },
                  {
                    "pdate": "2024-11-25",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 45
                  },
                  {
                    "pdate": "2024-11-26",
                    "repo_id": "625513",
                    "today_dl_cnt": 0,
                    "total_dl_cnt": 45
                  }
                ],
                "download_statistics_history_total": 45,
                "download_statistics_total": 7
              }
            }
          },
          "schema": {
            "properties": {
              "download_statistics_detail": {
                "items": {
                  "properties": {
                    "pdate": {
                      "type": "string"
                    },
                    "repo_id": {
                      "type": "string"
                    },
                    "today_dl_cnt": {
                      "type": "integer"
                    },
                    "total_dl_cnt": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "download_statistics_history_total": {
                "type": "integer"
              },
              "download_statistics_total": {
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
    "Repositories"
  ]
}
```
