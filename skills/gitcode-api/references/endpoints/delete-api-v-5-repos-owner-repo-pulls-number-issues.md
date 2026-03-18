# Pull Request Delete the associated issue
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-pulls-number-issues](https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-pulls-number-issues)
Category: Pull Requests
- Method: `DELETE`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/issues`
- Operation ID: `delete_api_v5_repos_{owner}_{repo}_pulls_{number}_issues`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "items": {
    "description": "Which issue number, the ordinal number of the Issue in this repository",
    "type": "integer"
  },
  "type": "array"
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
      "id": {
        "type": "integer"
      },
      "number": {
        "type": "string"
      },
      "title": {
        "type": "string"
      }
    },
    "required": [
      "id",
      "number",
      "title"
    ],
    "type": "object"
  },
  "type": "array"
}
```
Example:
```json
[
  {
    "id": 553397,
    "number": "3",
    "title": "222"
  },
  {
    "id": 553716,
    "number": "7",
    "title": "123"
  },
  {
    "id": 553721,
    "number": "8",
    "title": "[Bug]: 111"
  },
  {
    "id": 546954,
    "number": "1",
    "title": "asd"
  }
]
```
## JSON Request Example
```json
[
  0
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
    0
  ],
  "method": "delete",
  "operationId": "delete_api_v5_repos_{owner}_{repo}_pulls_{number}_issues",
  "parameters": [
    {
      "description": "Repository space address (organization or individual's address path)",
      "in": "path",
      "name": "owner",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path (path)",
      "in": "path",
      "name": "repo",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
      "in": "path",
      "name": "number",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/issues",
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
    "method": "DELETE",
    "name": "Pull Request Delete the associated issue",
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
        "schema": {
          "items": {
            "description": "Which issue number, the ordinal number of the Issue in this repository",
            "type": "integer"
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
          "example": [
            {
              "id": 553397,
              "number": "3",
              "title": "222"
            },
            {
              "id": 553716,
              "number": "7",
              "title": "123"
            },
            {
              "id": 553721,
              "number": "8",
              "title": "[Bug]: 111"
            },
            {
              "id": 546954,
              "number": "1",
              "title": "asd"
            }
          ],
          "schema": {
            "items": {
              "properties": {
                "id": {
                  "type": "integer"
                },
                "number": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "number",
                "title"
              ],
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
