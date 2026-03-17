# Get Pull Request Comment
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-comments-id](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-comments-id)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/comments/{id}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_comments_{id}`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| id | path | true | string | Comment ID |
| access_token | query | true | string | User authorization code |
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
  "properties": {
    "body": {
      "type": "string"
    },
    "comment_type": {
      "type": "string"
    },
    "created_at": {
      "type": "string"
    },
    "discussion_id": {
      "description": "Discussion ID",
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "position": {
      "properties": {
        "base_sha": {
          "description": "Basic SHA",
          "type": "string"
        },
        "head_sha": {
          "description": "Head SHA",
          "type": "string"
        },
        "new_line": {
          "description": "New line number",
          "type": "integer"
        },
        "new_path": {
          "description": "New path",
          "type": "string"
        },
        "old_line": {
          "description": "Old Serial Number",
          "type": "integer"
        },
        "old_path": {
          "description": "Old path",
          "type": "string"
        },
        "position_type": {
          "description": "Type of Location",
          "type": "string"
        },
        "start_new_line": {
          "description": "1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9. \n10. \n11. \n12. \n13. \n14. \n15. \n16. \n17. \n18. \n19. \n20.",
          "type": "integer"
        },
        "start_old_line": {
          "description": "Starting old serial number",
          "type": "integer"
        },
        "start_sha": {
          "description": "Starting SHA",
          "type": "string"
        }
      },
      "type": "object"
    },
    "target": {
      "properties": {
        "issue": {
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
          "type": "object"
        }
      },
      "type": "object"
    },
    "updated_at": {
      "type": "string"
    },
    "user": {
      "properties": {
        "id": {
          "type": "string"
        },
        "login": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string"
        }
      },
      "type": "object"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "body": "1111112222222",
  "comment_type": "DiscussionNote",
  "created_at": "2024-09-27T14:58:51+08:00",
  "id": 1486664,
  "target": {
    "issue": {
      "id": 478892,
      "number": "478892",
      "title": "1111"
    }
  },
  "updated_at": "2024-09-27T14:58:51+08:00",
  "user": {
    "id": "303745",
    "login": "yinlin",
    "name": "yinlin-nickname",
    "type": "User"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_comments_{id}",
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
      "description": "Comment ID",
      "example": "",
      "in": "path",
      "name": "id",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/comments/{id}",
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
    "name": "Get Pull Request Comment",
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
        "comments",
        ":id"
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
          "key": "id",
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
          "example": {
            "body": "1111112222222",
            "comment_type": "DiscussionNote",
            "created_at": "2024-09-27T14:58:51+08:00",
            "id": 1486664,
            "target": {
              "issue": {
                "id": 478892,
                "number": "478892",
                "title": "1111"
              }
            },
            "updated_at": "2024-09-27T14:58:51+08:00",
            "user": {
              "id": "303745",
              "login": "yinlin",
              "name": "yinlin-nickname",
              "type": "User"
            }
          },
          "schema": {
            "properties": {
              "body": {
                "type": "string"
              },
              "comment_type": {
                "type": "string"
              },
              "created_at": {
                "type": "string"
              },
              "discussion_id": {
                "description": "Discussion ID",
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "position": {
                "properties": {
                  "base_sha": {
                    "description": "Basic SHA",
                    "type": "string"
                  },
                  "head_sha": {
                    "description": "Head SHA",
                    "type": "string"
                  },
                  "new_line": {
                    "description": "New line number",
                    "type": "integer"
                  },
                  "new_path": {
                    "description": "New path",
                    "type": "string"
                  },
                  "old_line": {
                    "description": "Old Serial Number",
                    "type": "integer"
                  },
                  "old_path": {
                    "description": "Old path",
                    "type": "string"
                  },
                  "position_type": {
                    "description": "Type of Location",
                    "type": "string"
                  },
                  "start_new_line": {
                    "description": "1. \n2. \n3. \n4. \n5. \n6. \n7. \n8. \n9. \n10. \n11. \n12. \n13. \n14. \n15. \n16. \n17. \n18. \n19. \n20.",
                    "type": "integer"
                  },
                  "start_old_line": {
                    "description": "Starting old serial number",
                    "type": "integer"
                  },
                  "start_sha": {
                    "description": "Starting SHA",
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "target": {
                "properties": {
                  "issue": {
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
                    "type": "object"
                  }
                },
                "type": "object"
              },
              "updated_at": {
                "type": "string"
              },
              "user": {
                "properties": {
                  "id": {
                    "type": "string"
                  },
                  "login": {
                    "type": "string"
                  },
                  "name": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  }
                },
                "type": "object"
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
    "Pull Requests"
  ]
}
```
