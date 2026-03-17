# Create Repository Task Label
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-labels](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-labels)
Category: Labels
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/labels`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_labels`
- Tags: `Labels`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/x-www-form-urlencoded`
Schema:
```json
{
  "properties": {
    "color": {
      "description": "Label new color. E.g. #fff",
      "example": "",
      "type": "string"
    },
    "name": {
      "description": "Label name",
      "example": "",
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
    "color": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "color": "#fff",
  "id": 12738109,
  "name": "test1"
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
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_labels",
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
  "path": "/api/v5/repos/{owner}/{repo}/labels",
  "postman": {
    "body": {
      "mode": "urlencoded",
      "urlencoded": []
    },
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "application/x-www-form-urlencoded"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "POST",
    "name": "Create Repository Task Label",
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
      "application/x-www-form-urlencoded": {
        "example": "",
        "schema": {
          "properties": {
            "color": {
              "description": "Label new color. E.g. #fff",
              "example": "",
              "type": "string"
            },
            "name": {
              "description": "Label name",
              "example": "",
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
          "example": {
            "color": "#fff",
            "id": 12738109,
            "name": "test1"
          },
          "schema": {
            "properties": {
              "color": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "name": {
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
    "Labels"
  ]
}
```
