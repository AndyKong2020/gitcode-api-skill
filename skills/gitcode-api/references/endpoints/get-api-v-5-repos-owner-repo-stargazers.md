# List Users Who Have Starred the Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-stargazers](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-stargazers)
Category: Repositories
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/stargazers`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_stargazers`
- Tags: `Repositories`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
| starred_after | query | false | string | After the star |
| starred_before | query | false | string | Before the star |
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
      "avatar_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "login": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "starred_at": {
        "type": "string"
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
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/bc/cd/6bc422546cdf276c147f267030d83a43e927fec67ca66f0b22f7e03556206fa3.jpg",
      "id": 496,
      "login": "xiaogang",
      "name": "xiaogang",
      "starred_at": "2024-11-13T16:15:53.287+08:00"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_stargazers",
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
    },
    {
      "description": "After the star",
      "in": "query",
      "name": "starred_after",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Before the star",
      "in": "query",
      "name": "starred_before",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/stargazers",
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
    "name": "List Users Who Have Starred the Repository",
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
        "stargazers"
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
        },
        {
          "description": {
            "content": "After the star",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "starred_after",
          "value": ""
        },
        {
          "description": {
            "content": "Before the star",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "starred_before",
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
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/bc/cd/6bc422546cdf276c147f267030d83a43e927fec67ca66f0b22f7e03556206fa3.jpg",
                "id": 496,
                "login": "xiaogang",
                "name": "xiaogang",
                "starred_at": "2024-11-13T16:15:53.287+08:00"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "avatar_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "login": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "starred_at": {
                  "type": "string"
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
