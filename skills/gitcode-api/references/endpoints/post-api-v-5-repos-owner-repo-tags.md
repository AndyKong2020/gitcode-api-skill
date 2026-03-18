# Create a Tag for a Repository
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-tags](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-tags)
Category: Tag
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/tags`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_tags`
- Tags: `Tag`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "refs": {
      "description": "Start point name, default is main",
      "type": "string"
    },
    "tag_message": {
      "description": "Tag Description, defaults to empty",
      "type": "string"
    },
    "tag_name": {
      "description": "The name of the newly created label",
      "type": "string"
    }
  },
  "required": [
    "refs",
    "tag_name"
  ],
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
      "type": "null"
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
      "commit": {
        "date": "2024-04-08T13:13:33+00:00",
        "sha": "5d165dae3b073d3e92ca91c3edcb21994361462c"
      },
      "message": "",
      "name": "tag2",
      "tagger": null
    }
  }
}
```
## JSON Request Example
```json
{
  "refs": "string",
  "tag_message": "string",
  "tag_name": "string"
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
    "refs": "string",
    "tag_message": "string",
    "tag_name": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_tags",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/tags",
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
    "name": "Create a Tag for a Repository",
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "refs": {
              "description": "Start point name, default is main",
              "type": "string"
            },
            "tag_message": {
              "description": "Tag Description, defaults to empty",
              "type": "string"
            },
            "tag_name": {
              "description": "The name of the newly created label",
              "type": "string"
            }
          },
          "required": [
            "refs",
            "tag_name"
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "commit": {
                  "date": "2024-04-08T13:13:33+00:00",
                  "sha": "5d165dae3b073d3e92ca91c3edcb21994361462c"
                },
                "message": "",
                "name": "tag2",
                "tagger": null
              }
            }
          },
          "schema": {
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
                "type": "null"
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
    "Tag"
  ]
}
```
