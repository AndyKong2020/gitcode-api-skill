# Get Pull Requests Associated with the Issue
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number-pull-requests](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-issues-number-pull-requests)
Category: Issues
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/issues/{number}/pull_requests`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_issues_{number}_pull_requests`
- Tags: `Issues`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| number | path | true | string | Issue Number (case-sensitive, do not add #) |
| access_token | query | true | string | User authorization code |
| mode | query | false | integer | 1 (enhanced mode, pass the above parameter, return the mergeable status of PR); 0 (default, do not return mergeable status) |
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
    "assignees": {
      "items": {
        "properties": {
          "avatar_url": {
            "type": "null"
          },
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "login": {
            "type": "string"
          },
          "name": {
            "type": "null"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "base": {
      "properties": {
        "assigner": {
          "type": "null"
        },
        "ref": {
          "type": "string"
        },
        "repo": {
          "properties": {
            "name": {
              "type": "string"
            },
            "path": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "sha": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "body": {
      "type": "string"
    },
    "can_merge_check": {
      "type": "integer"
    },
    "closed_at": {
      "type": "null"
    },
    "created_at": {
      "type": "string"
    },
    "diff_url": {
      "type": "string"
    },
    "head": {
      "properties": {
        "assigner": {
          "properties": {
            "login": {
              "type": "string"
            },
            "name": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "ref": {
          "type": "string"
        },
        "repo": {
          "properties": {
            "name": {
              "type": "string"
            },
            "path": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "sha": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "html_url": {
      "type": "string"
    },
    "id": {
      "type": "integer"
    },
    "labels": {
      "items": {
        "properties": {
          "color": {
            "type": "string"
          },
          "created_at": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "repository_id": {
            "type": "null"
          },
          "text_color": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          },
          "url": {
            "type": "null"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "merged_at": {
      "type": "null"
    },
    "number": {
      "type": "integer"
    },
    "state": {
      "type": "string"
    },
    "testers": {
      "items": {
        "properties": {
          "avatar_url": {
            "type": "null"
          },
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "string"
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
    },
    "title": {
      "type": "string"
    },
    "updated_at": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Example:
```json
{
  "assignees": [
    {
      "avatar_url": null,
      "html_url": "https://api.gitcode.net/test",
      "id": "65803cddcf1e2d1aa3d2e99f",
      "login": "test",
      "name": null
    }
  ],
  "base": {
    "assigner": null,
    "ref": "main",
    "repo": {
      "name": "paopao1",
      "path": "paopao1"
    },
    "sha": "667d4ac032b2faa13d019753ac218b4f78338273"
  },
  "body": "new: Added file test.txt 1",
  "can_merge_check": true,
  "closed_at": null,
  "created_at": "2024-04-12T17:50:55.253+08:00",
  "diff_url": "https://api.gitcode.net/test/test/merge_requests/1/diffs",
  "head": {
    "assigner": {
      "login": "test",
      "name": "test"
    },
    "ref": "develop",
    "repo": {
      "name": "paopao1",
      "path": "paopao1"
    },
    "sha": "061c446d55aae78c7a0f096b2d2dd0d6a1afb170"
  },
  "html_url": "https://api.gitcode.net/test/test/merge_requests/1",
  "id": 67585,
  "labels": [
    {
      "color": "#CCCCCC",
      "created_at": "2024-04-19",
      "id": 383707,
      "name": "wontfix",
      "repository_id": null,
      "text_color": "#333333",
      "updated_at": "2024-04-19",
      "url": null
    }
  ],
  "merged_at": null,
  "number": 1,
  "state": "open",
  "testers": [
    {
      "avatar_url": null,
      "html_url": "https://api.gitcode.net/test",
      "id": "65803cddcf1e2d1aa3d2e99f",
      "login": "test",
      "name": "test"
    }
  ],
  "title": "1",
  "updated_at": "2024-04-20T15:58:30.657+08:00"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_issues_{number}_pull_requests",
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
      "description": "Issue Number (case-sensitive, do not add #)",
      "example": "",
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
    },
    {
      "description": "1 (enhanced mode, pass the above parameter, return the mergeable status of PR); 0 (default, do not return mergeable status)",
      "in": "query",
      "name": "mode",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/issues/{number}/pull_requests",
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
    "name": "Get Pull Requests Associated with the Issue",
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
        "pull_requests"
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
            "content": "1 (enhanced mode, pass the above parameter, return the mergeable status of PR); 0 (default, do not return mergeable status)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "mode",
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
            "content": "(Required) Issue Number (case-sensitive, do not add #)",
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
  "responses": {
    "200": {
      "content": {
        "application/json": {
          "example": {
            "assignees": [
              {
                "avatar_url": null,
                "html_url": "https://api.gitcode.net/test",
                "id": "65803cddcf1e2d1aa3d2e99f",
                "login": "test",
                "name": null
              }
            ],
            "base": {
              "assigner": null,
              "ref": "main",
              "repo": {
                "name": "paopao1",
                "path": "paopao1"
              },
              "sha": "667d4ac032b2faa13d019753ac218b4f78338273"
            },
            "body": "new: Added file test.txt 1",
            "can_merge_check": true,
            "closed_at": null,
            "created_at": "2024-04-12T17:50:55.253+08:00",
            "diff_url": "https://api.gitcode.net/test/test/merge_requests/1/diffs",
            "head": {
              "assigner": {
                "login": "test",
                "name": "test"
              },
              "ref": "develop",
              "repo": {
                "name": "paopao1",
                "path": "paopao1"
              },
              "sha": "061c446d55aae78c7a0f096b2d2dd0d6a1afb170"
            },
            "html_url": "https://api.gitcode.net/test/test/merge_requests/1",
            "id": 67585,
            "labels": [
              {
                "color": "#CCCCCC",
                "created_at": "2024-04-19",
                "id": 383707,
                "name": "wontfix",
                "repository_id": null,
                "text_color": "#333333",
                "updated_at": "2024-04-19",
                "url": null
              }
            ],
            "merged_at": null,
            "number": 1,
            "state": "open",
            "testers": [
              {
                "avatar_url": null,
                "html_url": "https://api.gitcode.net/test",
                "id": "65803cddcf1e2d1aa3d2e99f",
                "login": "test",
                "name": "test"
              }
            ],
            "title": "1",
            "updated_at": "2024-04-20T15:58:30.657+08:00"
          },
          "schema": {
            "properties": {
              "assignees": {
                "items": {
                  "properties": {
                    "avatar_url": {
                      "type": "null"
                    },
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "login": {
                      "type": "string"
                    },
                    "name": {
                      "type": "null"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "base": {
                "properties": {
                  "assigner": {
                    "type": "null"
                  },
                  "ref": {
                    "type": "string"
                  },
                  "repo": {
                    "properties": {
                      "name": {
                        "type": "string"
                      },
                      "path": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "sha": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "body": {
                "type": "string"
              },
              "can_merge_check": {
                "type": "integer"
              },
              "closed_at": {
                "type": "null"
              },
              "created_at": {
                "type": "string"
              },
              "diff_url": {
                "type": "string"
              },
              "head": {
                "properties": {
                  "assigner": {
                    "properties": {
                      "login": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "ref": {
                    "type": "string"
                  },
                  "repo": {
                    "properties": {
                      "name": {
                        "type": "string"
                      },
                      "path": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "sha": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "html_url": {
                "type": "string"
              },
              "id": {
                "type": "integer"
              },
              "labels": {
                "items": {
                  "properties": {
                    "color": {
                      "type": "string"
                    },
                    "created_at": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "repository_id": {
                      "type": "null"
                    },
                    "text_color": {
                      "type": "string"
                    },
                    "updated_at": {
                      "type": "string"
                    },
                    "url": {
                      "type": "null"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "merged_at": {
                "type": "null"
              },
              "number": {
                "type": "integer"
              },
              "state": {
                "type": "string"
              },
              "testers": {
                "items": {
                  "properties": {
                    "avatar_url": {
                      "type": "null"
                    },
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
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
              },
              "title": {
                "type": "string"
              },
              "updated_at": {
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
    "Issues"
  ]
}
```
