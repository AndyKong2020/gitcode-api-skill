# Assign Users to Test Pull Requests
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-testers](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-testers)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/testers`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls_{number}_testers`
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
  "properties": {
    "add": {
      "description": "\"Is new tester added\", true will add a new tester, false will cover and update the tester, default false",
      "type": "boolean"
    },
    "testers": {
      "description": "User's personal space address, separated by commas",
      "type": "string"
    }
  },
  "required": [
    "testers"
  ],
  "type": "object"
}
```
Example:
```json
{
  "add": "true",
  "testers": "user1"
}
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
      "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
      "id": 43,
      "login": "green",
      "name": "green"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "id": 452,
      "login": "zhanghq2",
      "name": "zhanghq2"
    }
  }
}
```
## JSON Request Example
```json
{
  "add": true,
  "testers": "string"
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
    "add": true,
    "testers": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls_{number}_testers",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/testers",
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
    "name": "Assign Users to Test Pull Requests",
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
        "testers"
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
        "example": {
          "add": "true",
          "testers": "user1"
        },
        "schema": {
          "properties": {
            "add": {
              "description": "\"Is new tester added\", true will add a new tester, false will cover and update the tester, default false",
              "type": "boolean"
            },
            "testers": {
              "description": "User's personal space address, separated by commas",
              "type": "string"
            }
          },
          "required": [
            "testers"
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
                "avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/be/fb/7b9e393fbd80ca315dec249f2be6e6a7378f591609b6525798bc6d95abedc992.png?time=1712128581171",
                "id": 43,
                "login": "green",
                "name": "green"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "id": 452,
                "login": "zhanghq2",
                "name": "zhanghq2"
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
