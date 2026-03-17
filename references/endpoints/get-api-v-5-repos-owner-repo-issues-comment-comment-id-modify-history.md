# Get the modification history of issue comments
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-comment-comment-id-modify-history](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-comment-comment-id-modify-history)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/issues/comment/{comment_id}/modify_history`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_issues_comment_{comment_id}_modify_history`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| comment_id | path | true | string | Comment ID |
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
  "items": {
    "properties": {
      "content": {
        "title": "Modified content",
        "type": "string"
      },
      "created": {
        "title": "Is it creating",
        "type": "boolean"
      },
      "created_at": {
        "title": "creation time",
        "type": "string"
      },
      "deleted": {
        "title": "Has it been deleted",
        "type": "boolean"
      },
      "id": {
        "type": "string"
      },
      "updated_at": {
        "title": "Update time",
        "type": "string"
      },
      "updated_user": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "object_id": {
            "type": "string"
          }
        },
        "required": [
          "login",
          "name",
          "avatar_url",
          "object_id"
        ],
        "type": "object"
      },
      "user": {
        "properties": {
          "avatar_url": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "object_id": {
            "type": "string"
          }
        },
        "required": [
          "login",
          "name",
          "avatar_url",
          "object_id"
        ],
        "title": "User Information",
        "type": "object"
      }
    },
    "required": [
      "id",
      "created_at",
      "updated_at",
      "deleted",
      "created",
      "content",
      "user",
      "updated_user"
    ],
    "type": "object"
  },
  "type": "array"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_issues_comment_{comment_id}_modify_history",
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
      "description": "Comment ID",
      "in": "path",
      "name": "comment_id",
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
  "path": "/api/v5/repos/{owner}/{repo}/issues/comment/{comment_id}/modify_history",
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
    "name": "Get the modification history of issue comments",
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
        "comment",
        ":comment_id",
        "modify_history"
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
            "content": "(Required) Comment ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "comment_id",
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
            "items": {
              "properties": {
                "content": {
                  "title": "Modified content",
                  "type": "string"
                },
                "created": {
                  "title": "Is it creating",
                  "type": "boolean"
                },
                "created_at": {
                  "title": "creation time",
                  "type": "string"
                },
                "deleted": {
                  "title": "Has it been deleted",
                  "type": "boolean"
                },
                "id": {
                  "type": "string"
                },
                "updated_at": {
                  "title": "Update time",
                  "type": "string"
                },
                "updated_user": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "object_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "login",
                    "name",
                    "avatar_url",
                    "object_id"
                  ],
                  "type": "object"
                },
                "user": {
                  "properties": {
                    "avatar_url": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "object_id": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "login",
                    "name",
                    "avatar_url",
                    "object_id"
                  ],
                  "title": "User Information",
                  "type": "object"
                }
              },
              "required": [
                "id",
                "created_at",
                "updated_at",
                "deleted",
                "created",
                "content",
                "user",
                "updated_user"
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
