# Revised comments and inspection opinions, status resolved
Source: [https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pulls-number-comments-discussions-id](https://docs.gitcode.com/en/docs/apis/put-api-v-5-repos-owner-repo-pulls-number-comments-discussions-id)
Category: Pull Requests
- Method: `PUT`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/comments/{discussion_id}`
- Operation ID: `put_api_v5_repos_{owner}_{repo}_pulls_{number}_comments_{discussions_id}`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | PR number, which is the ordinal number of PRs in this repository. Corresponds to iid |
| discussion_id | path | true | string | Discussion ID (string type id) |
| access_token | query | false | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "resolved": {
      "description": "Has it been resolved?",
      "type": "boolean"
    }
  },
  "required": [
    "resolved"
  ],
  "type": "object"
}
```
Example:
```json
{
  "resolved": true
}
```
## Responses
### `200`
Headers:
```json
{}
```
## JSON Request Example
```json
{
  "resolved": true
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
    "resolved": true
  },
  "method": "put",
  "operationId": "put_api_v5_repos_{owner}_{repo}_pulls_{number}_comments_{discussions_id}",
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
      "description": "Discussion ID (string type id)",
      "in": "path",
      "name": "discussion_id",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/comments/{discussion_id}",
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
      }
    ],
    "method": "PUT",
    "name": "Revised comments and inspection opinions, status resolved",
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
        "comments",
        ":discussion_id"
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
        },
        {
          "description": {
            "content": "(Required) Discussion ID (string type id)",
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
        "example": {
          "resolved": true
        },
        "schema": {
          "properties": {
            "resolved": {
              "description": "Has it been resolved?",
              "type": "boolean"
            }
          },
          "required": [
            "resolved"
          ],
          "type": "object"
        }
      }
    }
  },
  "responses": {
    "200": {
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
