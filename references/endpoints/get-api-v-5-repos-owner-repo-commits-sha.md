# A Commit in a Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-commits-sha](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-commits-sha)
Category: Commit
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/commits/{sha}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_commits_{sha}`
- Tags: `Commit`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| sha | path | true | string | The submitted SHA value or branch name. |
| access_token | query | true | string | User authorization code |
| show_diff | query | false | boolean | Default is false; when true, returns the files field, which contains up to 100 changed file names in the local commit. |
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
    "comments_url": {
      "type": "string"
    },
    "commit": {
      "properties": {
        "author": {
          "properties": {
            "date": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "name": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "committer": {
          "properties": {
            "date": {
              "type": "string"
            },
            "email": {
              "type": "string"
            },
            "name": {
              "type": "string"
            }
          },
          "type": "object"
        },
        "message": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "files": {
      "items": {
        "properties": {
          "content_url": {
            "type": "string"
          },
          "filename": {
            "type": "string"
          },
          "raw_url": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "html_url": {
      "type": "string"
    },
    "sha": {
      "type": "string"
    },
    "stats": {
      "properties": {
        "additions": {
          "type": "integer"
        },
        "deletions": {
          "type": "integer"
        },
        "total": {
          "type": "integer"
        }
      },
      "type": "object"
    },
    "url": {
      "type": "string"
    }
  },
  "type": "object"
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "comments_url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/commits/7ffc0a0deb709143f6be12a55e218fab9233ca37/comments",
      "commit": {
        "author": {
          "date": "2024-04-14T07:25:11+00:00",
          "email": "7543745+centking@user.noreply.gitcode.com",
          "name": "score占比"
        },
        "committer": {
          "date": "2024-04-14T07:25:11+00:00",
          "email": "noreply@gitcode.com",
          "name": "Gitee"
        },
        "message": "Test submission information"
      },
      "files": [
        {
          "content_url": "https://gitcode.com/test-owner/test-repo/blob/b0e267d8bbed9b568623528c216f8f8489689a61/pom.xml",
          "filename": "pom.xml",
          "raw_url": "https://raw.gitcode.com/test-owner/test-repo/raw/b0e267d8bbed9b568623528c216f8f8489689a61/pom.xml"
        }
      ],
      "html_url": "https://gitcode.com/daming_1/zhu_di/commit/7ffc0a0deb709143f6be12a55e218fab9233ca37",
      "sha": "7ffc0a0deb709143f6be12a55e218fab9233ca37",
      "stats": {
        "additions": 1,
        "deletions": 1,
        "total": 2
      },
      "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/commits/7ffc0a0deb709143f6be12a55e218fab9233ca37"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_commits_{sha}",
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
      "description": "The submitted SHA value or branch name.",
      "example": "",
      "in": "path",
      "name": "sha",
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
      "description": "Default is false; when true, returns the files field, which contains up to 100 changed file names in the local commit.",
      "in": "query",
      "name": "show_diff",
      "required": false,
      "schema": {
        "type": "boolean"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/commits/{sha}",
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
    "name": "A Commit in a Repository",
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
        "commits",
        ":sha"
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
            "content": "Default is false; when true, returns the files field, which contains up to 100 changed file names in the local commit.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "show_diff",
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
            "content": "(Required) The submitted SHA value or branch name.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sha",
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
                "comments_url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/commits/7ffc0a0deb709143f6be12a55e218fab9233ca37/comments",
                "commit": {
                  "author": {
                    "date": "2024-04-14T07:25:11+00:00",
                    "email": "7543745+centking@user.noreply.gitcode.com",
                    "name": "score占比"
                  },
                  "committer": {
                    "date": "2024-04-14T07:25:11+00:00",
                    "email": "noreply@gitcode.com",
                    "name": "Gitee"
                  },
                  "message": "Test submission information"
                },
                "files": [
                  {
                    "content_url": "https://gitcode.com/test-owner/test-repo/blob/b0e267d8bbed9b568623528c216f8f8489689a61/pom.xml",
                    "filename": "pom.xml",
                    "raw_url": "https://raw.gitcode.com/test-owner/test-repo/raw/b0e267d8bbed9b568623528c216f8f8489689a61/pom.xml"
                  }
                ],
                "html_url": "https://gitcode.com/daming_1/zhu_di/commit/7ffc0a0deb709143f6be12a55e218fab9233ca37",
                "sha": "7ffc0a0deb709143f6be12a55e218fab9233ca37",
                "stats": {
                  "additions": 1,
                  "deletions": 1,
                  "total": 2
                },
                "url": "https://gitcode.com/api/v5/repos/daming_1/zhu_di/commits/7ffc0a0deb709143f6be12a55e218fab9233ca37"
              }
            }
          },
          "schema": {
            "properties": {
              "comments_url": {
                "type": "string"
              },
              "commit": {
                "properties": {
                  "author": {
                    "properties": {
                      "date": {
                        "type": "string"
                      },
                      "email": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "committer": {
                    "properties": {
                      "date": {
                        "type": "string"
                      },
                      "email": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      }
                    },
                    "type": "object"
                  },
                  "message": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "files": {
                "items": {
                  "properties": {
                    "content_url": {
                      "type": "string"
                    },
                    "filename": {
                      "type": "string"
                    },
                    "raw_url": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "html_url": {
                "type": "string"
              },
              "sha": {
                "type": "string"
              },
              "stats": {
                "properties": {
                  "additions": {
                    "type": "integer"
                  },
                  "deletions": {
                    "type": "integer"
                  },
                  "total": {
                    "type": "integer"
                  }
                },
                "type": "object"
              },
              "url": {
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
    "Commit"
  ]
}
```
