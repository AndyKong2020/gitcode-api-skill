# Delete Issue Label
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-issues-number-labels-name](https://docs.gitcode.com/en/docs/apis/delete-api-v-5-repos-owner-repo-issues-number-labels-name)
Category: Issues
- Method: `DELETE`
- Path: `/api/v5/repos/{owner}/{repo}/issues/{number}/labels/{name}`
- Operation ID: `delete_api_v5_repos_{owner}_{repo}_issues_{number}_labels_{name}`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | Which issue number, the ordinal number of the Issue in this repository |
| name | path | true | string | Tag names (for batch deletion, separate with English commas, e.g., bug,feature) |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
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
  "properties": {},
  "type": "object"
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
  "method": "delete",
  "operationId": "delete_api_v5_repos_{owner}_{repo}_issues_{number}_labels_{name}",
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
      "description": "Which issue number, the ordinal number of the Issue in this repository",
      "example": "",
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Tag names (for batch deletion, separate with English commas, e.g., bug,feature)",
      "example": "",
      "in": "path",
      "name": "name",
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
  "path": "/api/v5/repos/{owner}/{repo}/issues/{number}/labels/{name}",
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
    "method": "DELETE",
    "name": "Delete Issue Label",
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
        "issues",
        ":number",
        "labels",
        ":name"
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
            "content": "(Required) Which issue number, the ordinal number of the Issue in this repository",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "number",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Tag names (for batch deletion, separate with English commas, e.g., bug,feature)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "name",
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
          "schema": {
            "properties": {},
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
  "tags": [
    "Issues"
  ]
}
```
