# List All Tags Of The Project
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-tags](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-tags)
Category: Tag
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/tags`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_tags`
- Tags: `Tag`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number: Default is 1 |
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
      "commit": {
        "properties": {
          "date": {
            "type": "string"
          },
          "sha": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "message": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "tagger": {
        "properties": {
          "date": {
            "type": "string"
          },
          "email": {
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
      "commit": {
        "date": "2024-04-14T02:59:22+00:00",
        "sha": "3e43581d16bc456802a1fee673b9a2a9b9618f0f"
      },
      "message": "111",
      "name": "v1.0",
      "tagger": {
        "date": "2024-04-14T06:18:54+00:00",
        "email": "7543745+centking@user.noreply.gitcode.com",
        "name": "score占比"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_tags",
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
      "description": "Current page number: Default is 1",
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
  "path": "/api/v5/repos/{owner}/{repo}/tags",
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
    "name": "List All Tags Of The Project",
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
        "tags"
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
            "content": "Current page number: Default is 1",
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
                "commit": {
                  "date": "2024-04-14T02:59:22+00:00",
                  "sha": "3e43581d16bc456802a1fee673b9a2a9b9618f0f"
                },
                "message": "111",
                "name": "v1.0",
                "tagger": {
                  "date": "2024-04-14T06:18:54+00:00",
                  "email": "7543745+centking@user.noreply.gitcode.com",
                  "name": "score占比"
                }
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "commit": {
                  "properties": {
                    "date": {
                      "type": "string"
                    },
                    "sha": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "message": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "tagger": {
                  "properties": {
                    "date": {
                      "type": "string"
                    },
                    "email": {
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
    "Tag"
  ]
}
```
