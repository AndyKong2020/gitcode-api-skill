# Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Reply to Pull Request comment
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-discussions-discussions-id-comments](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-pulls-number-discussions-discussions-id-comments)
Category: Pull Requests
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/discussions/{discussion_id}/comments`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_pulls_{number}_discussions_{discussions_id}_comments`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Warehouse's space address (the path of the organization or individual's address) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| discussion_id | path | true | string | Discussion ID |
| access_token | query | false | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "body": {
      "type": "string"
    }
  },
  "required": [
    "body"
  ],
  "type": "object"
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
  "properties": {
    "body": {
      "type": "string"
    },
    "id": {
      "description": "Discussion ID",
      "type": "string"
    },
    "noteId": {
      "description": "comment_id",
      "type": "integer"
    }
  },
  "required": [
    "id",
    "body",
    "noteId"
  ],
  "type": "object"
}
```
## JSON Request Example
```json
{
  "body": "string"
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
    "body": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_pulls_{number}_discussions_{discussions_id}_comments",
  "parameters": [
    {
      "description": "Warehouse's space address (the path of the organization or individual's address)",
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
        "type": "integer"
      }
    },
    {
      "description": "Discussion ID",
      "in": "path",
      "name": "discussion_id",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/discussions/{discussion_id}/comments",
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
    "name": "Please professionally translate the following content into English, keeping the format unchanged. If the content is empty, do not translate it. Do not output anything else or any prompts!! Reply to Pull Request comment",
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
        "discussions",
        ":discussion_id",
        "comments"
      ],
      "query": [
        {
          "description": {
            "content": "User authorization code",
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
            "content": "(Required) Warehouse's space address (the path of the organization or individual's address)",
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
        },
        {
          "description": {
            "content": "(Required) Discussion ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "discussion_id",
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
          "properties": {
            "body": {
              "type": "string"
            }
          },
          "required": [
            "body"
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
            "properties": {
              "body": {
                "type": "string"
              },
              "id": {
                "description": "Discussion ID",
                "type": "string"
              },
              "noteId": {
                "description": "comment_id",
                "type": "integer"
              }
            },
            "required": [
              "id",
              "body",
              "noteId"
            ],
            "type": "object"
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
