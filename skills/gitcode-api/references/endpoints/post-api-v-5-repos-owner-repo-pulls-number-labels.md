# Create Pull Request Label
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-labels](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-labels)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/labels`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls_{number}_labels`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "items": {
    "description": "Label name",
    "type": "string"
  },
  "type": "array"
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
}
```
Example:
```json
{
  "color": "#008672",
  "id": 381445,
  "name": "help wanted",
  "textColor": "#FFFFFF",
  "title": "help wanted",
  "type": null
}
```
## JSON Request Example
```json
[
  "string"
]
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
  "jsonRequestBodyExample": [
    "string"
  ],
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls_{number}_labels",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/labels",
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
    "name": "Create Pull Request Label",
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
        "labels"
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
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "items": {
            "description": "Label name",
            "type": "string"
          },
          "type": "array"
        }
      }
    }
  },
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "color": "#008672",
            "id": 381445,
            "name": "help wanted",
            "textColor": "#FFFFFF",
            "title": "help wanted",
            "type": null
          },
          "schema": {
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
