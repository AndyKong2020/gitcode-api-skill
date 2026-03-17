# Get Repository Activity
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-events-access-token-your-token](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-events-access-token-your-token)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/events`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_events?access_token=your_token`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string |  |
| filter | query | false | string | filter: Criteria for filtering. Accepts 'all' (for all events), 'push', 'merged', 'issue', 'comments', 'team', 'project'. |
| author | query | false | string | event_trigger_user, input_username |
| before | query | false | string | Start date in the format `YYYY-MM-DD`. Used to limit the start time of the events returned. |
| after | query | false | string | End date in the format of `YYYY-MM-DD`. Used to limit the end time of the events returned. |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
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
    "events": {
      "items": {
        "properties": {
          "action": {
            "type": "integer"
          },
          "action_name": {
            "type": "string"
          },
          "author": {
            "properties": {
              "email": {
                "type": "string"
              },
              "iam_id": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              },
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              },
              "username": {
                "type": "string"
              },
              "web_url": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "author_id": {
            "type": "integer"
          },
          "author_username": {
            "type": "string"
          },
          "created_at": {
            "type": "string"
          },
          "filter_sensitive": {
            "type": "integer"
          },
          "project_id": {
            "type": "integer"
          },
          "title": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "has_next_page": {
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
      "events": [
        {
          "action": 22,
          "action_name": "opened",
          "author": {
            "email": "",
            "iam_id": "f09ca8d721eb49e4add47b67c0dbef81",
            "id": 607,
            "name": "xiaogang",
            "name_cn": "",
            "state": "active",
            "username": "xiaogang",
            "web_url": "https://gitcode.com/xiaogang"
          },
          "author_id": 607,
          "author_username": "xiaogang2",
          "created_at": "2024-11-19T07:01:02.714Z",
          "filter_sensitive": true,
          "project_id": 249609,
          "title": "{\"userid\":[496],\"username\":[\"xiaogang\"]}"
        }
      ],
      "has_next_page": false
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_events?access_token=your_token",
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
      "description": "",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "filter: Criteria for filtering. Accepts 'all' (for all events), 'push', 'merged', 'issue', 'comments', 'team', 'project'.",
      "in": "query",
      "name": "filter",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "event_trigger_user, input_username",
      "in": "query",
      "name": "author",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Start date in the format `YYYY-MM-DD`. Used to limit the start time of the events returned.",
      "in": "query",
      "name": "before",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "End date in the format of `YYYY-MM-DD`. Used to limit the end time of the events returned.",
      "in": "query",
      "name": "after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/events",
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
    "name": "Get Repository Activity",
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
        "events"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) ",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "access_token",
          "value": ""
        },
        {
          "description": {
            "content": "filter: Criteria for filtering. Accepts 'all' (for all events), 'push', 'merged', 'issue', 'comments', 'team', 'project'.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "filter",
          "value": ""
        },
        {
          "description": {
            "content": "event_trigger_user, input_username",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "author",
          "value": ""
        },
        {
          "description": {
            "content": "Start date in the format `YYYY-MM-DD`. Used to limit the start time of the events returned.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "before",
          "value": ""
        },
        {
          "description": {
            "content": "End date in the format of `YYYY-MM-DD`. Used to limit the end time of the events returned.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "after",
          "value": ""
        },
        {
          "description": {
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
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
                "events": [
                  {
                    "action": 22,
                    "action_name": "opened",
                    "author": {
                      "email": "",
                      "iam_id": "f09ca8d721eb49e4add47b67c0dbef81",
                      "id": 607,
                      "name": "xiaogang",
                      "name_cn": "",
                      "state": "active",
                      "username": "xiaogang",
                      "web_url": "https://gitcode.com/xiaogang"
                    },
                    "author_id": 607,
                    "author_username": "xiaogang2",
                    "created_at": "2024-11-19T07:01:02.714Z",
                    "filter_sensitive": true,
                    "project_id": 249609,
                    "title": "{\"userid\":[496],\"username\":[\"xiaogang\"]}"
                  }
                ],
                "has_next_page": false
              }
            }
          },
          "schema": {
            "properties": {
              "events": {
                "items": {
                  "properties": {
                    "action": {
                      "type": "integer"
                    },
                    "action_name": {
                      "type": "string"
                    },
                    "author": {
                      "properties": {
                        "email": {
                          "type": "string"
                        },
                        "iam_id": {
                          "type": "string"
                        },
                        "id": {
                          "type": "integer"
                        },
                        "name": {
                          "type": "string"
                        },
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        },
                        "username": {
                          "type": "string"
                        },
                        "web_url": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "author_id": {
                      "type": "integer"
                    },
                    "author_username": {
                      "type": "string"
                    },
                    "created_at": {
                      "type": "string"
                    },
                    "filter_sensitive": {
                      "type": "integer"
                    },
                    "project_id": {
                      "type": "integer"
                    },
                    "title": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "has_next_page": {
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
