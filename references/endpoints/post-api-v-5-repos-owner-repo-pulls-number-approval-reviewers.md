# Assign user to review Pull Request
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-approval-reviewers](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-approval-reviewers)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/reviewers`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls_{number}_approval_reviewers`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | PR number, which is the ordinal number of PRs in this repository. Corresponds to iid |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "description": "User name list",
  "properties": {
    "add": {
      "description": "IsNewReviewer, if true, will add a reviewer, if false, it will overwrite and update the reviewer, default is false",
      "type": "boolean"
    },
    "reviewers": {
      "description": "User's personal space address, separated by commas",
      "type": "string"
    }
  },
  "required": [
    "reviewers"
  ],
  "type": "object"
}
```
Example:
```json
{
  "add": "true",
  "reviewers": "user1"
}
```
## Responses
### `200`
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
        "title": "avatar",
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "login": {
        "title": "Account",
        "type": "string"
      },
      "name": {
        "title": "Nickname",
        "type": "string"
      },
      "object_id": {
        "title": "id",
        "type": "string"
      }
    },
    "required": [
      "id",
      "login",
      "name",
      "object_id"
    ],
    "type": "object"
  },
  "type": "array"
}
```
## JSON Request Example
```json
{
  "add": true,
  "reviewers": "string"
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
    "reviewers": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls_{number}_approval_reviewers",
  "parameters": [
    {
      "description": "Repository space address (address path of the enterprise, organization, or individual)",
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
      "description": "PR number, which is the ordinal number of PRs in this repository. Corresponds to iid",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/reviewers",
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
    "name": "Assign user to review Pull Request",
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
        "reviewers"
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
        },
        {
          "description": {
            "content": "(Required) PR number, which is the ordinal number of PRs in this repository. Corresponds to iid",
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
          "reviewers": "user1"
        },
        "schema": {
          "description": "User name list",
          "properties": {
            "add": {
              "description": "IsNewReviewer, if true, will add a reviewer, if false, it will overwrite and update the reviewer, default is false",
              "type": "boolean"
            },
            "reviewers": {
              "description": "User's personal space address, separated by commas",
              "type": "string"
            }
          },
          "required": [
            "reviewers"
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
          "schema": {
            "items": {
              "properties": {
                "avatar_url": {
                  "title": "avatar",
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "login": {
                  "title": "Account",
                  "type": "string"
                },
                "name": {
                  "title": "Nickname",
                  "type": "string"
                },
                "object_id": {
                  "title": "id",
                  "type": "string"
                }
              },
              "required": [
                "id",
                "login",
                "name",
                "object_id"
              ],
              "type": "object"
            },
            "type": "array"
          }
        }
      },
      "description": "",
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
  "tags": []
}
```
