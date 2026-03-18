# Get PR Associated Issue
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-issues)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/issues`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_issues`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number: defaults to 1 |
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
  "items": {
    "properties": {
      "body": {
        "type": "string"
      },
      "labels": {
        "items": {
          "properties": {
            "color": {
              "type": "string"
            },
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "textColor": {
              "type": "string"
            },
            "title": {
              "type": "string"
            },
            "type": {
              "type": "null"
            }
          },
          "type": "object"
        },
        "type": "array"
      },
      "number": {
        "type": "string"
      },
      "state": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "user": {
        "properties": {
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
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
      "body": "What is the problem?",
      "labels": [
        {
          "color": "#008672",
          "id": 381445,
          "name": "help wanted",
          "textColor": "#FFFFFF",
          "title": "help wanted",
          "type": null
        }
      ],
      "number": "1",
      "state": "open",
      "title": "stability test",
      "url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/issues/1",
      "user": {
        "id": "681",
        "login": "test",
        "name": "test"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_issues",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
      "description": "Current page number: defaults to 1",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/issues",
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
    "name": "Get PR Associated Issue",
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
        "pulls",
        ":number",
        "issues"
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
            "content": "Current page number: defaults to 1",
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
        },
        {
          "description": {
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
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
                "body": "What is the problem?",
                "labels": [
                  {
                    "color": "#008672",
                    "id": 381445,
                    "name": "help wanted",
                    "textColor": "#FFFFFF",
                    "title": "help wanted",
                    "type": null
                  }
                ],
                "number": "1",
                "state": "open",
                "title": "stability test",
                "url": "https://api.gitcode.com/api/v5/repos/sytest/paopao/issues/1",
                "user": {
                  "id": "681",
                  "login": "test",
                  "name": "test"
                }
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "body": {
                  "type": "string"
                },
                "labels": {
                  "items": {
                    "properties": {
                      "color": {
                        "type": "string"
                      },
                      "id": {
                        "type": "integer"
                      },
                      "name": {
                        "type": "string"
                      },
                      "textColor": {
                        "type": "string"
                      },
                      "title": {
                        "type": "string"
                      },
                      "type": {
                        "type": "null"
                      }
                    },
                    "type": "object"
                  },
                  "type": "array"
                },
                "number": {
                  "type": "string"
                },
                "state": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
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
    "Pull Requests"
  ]
}
```
