# Create Branch
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-branches](https://docs.gitcode.com/en/docs/apis/post-api-v-5-repos-owner-repo-branches)
Category: Branch
- Method: `POST`
- Path: `/api/v5/repos/{owner}/{repo}/branches`
- Operation ID: `post_api_v5_repos_{owner}_{repo}_branches`
- Tags: `Branch`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (address path of the enterprise, organization, or individual) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
## Request Body
#### `application/json`
Schema:
```json
{
  "properties": {
    "branch_name": {
      "description": "The name of the newly created branch",
      "type": "string"
    },
    "refs": {
      "description": "Start point name, default: master",
      "type": "string"
    }
  },
  "required": [
    "refs",
    "branch_name"
  ],
  "type": "object"
}
```
Example:
```json
""
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
  "properties": {
    "commit": {
      "properties": {
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
        "sha": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      },
      "type": "object"
    },
    "name": {
      "type": "string"
    },
    "protected": {
      "type": "integer"
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
      "commit": {
        "commit": {
          "author": {
            "date": "2024-09-10T08:29:18Z",
            "email": "dengmengmian@noreply.gitcode.com",
            "name": "dengmengmian"
          },
          "committer": {
            "date": "2024-09-10T08:29:18Z",
            "email": "dengmengmian@noreply.gitcode.com",
            "name": "dengmengmian"
          },
          "message": "test"
        },
        "sha": "1af35823b8bbcaf68776cd6cb0ecbf88cfdec905",
        "url": "https://test.gitcode.net/api/v5/repos/dengmengmian/test03/commits/1af35823b8bbcaf68776cd6cb0ecbf88cfdec905"
      },
      "name": "gitcode",
      "protected": false
    }
  }
}
```
## JSON Request Example
```json
{
  "branch_name": "string",
  "refs": "string"
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
    "branch_name": "string",
    "refs": "string"
  },
  "method": "post",
  "operationId": "post_api_v5_repos_{owner}_{repo}_branches",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/branches",
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
    "name": "Create Branch",
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
        "branches"
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
        }
      ]
    }
  },
  "requestBody": {
    "content": {
      "application/json": {
        "example": "",
        "schema": {
          "properties": {
            "branch_name": {
              "description": "The name of the newly created branch",
              "type": "string"
            },
            "refs": {
              "description": "Start point name, default: master",
              "type": "string"
            }
          },
          "required": [
            "refs",
            "branch_name"
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
                "commit": {
                  "commit": {
                    "author": {
                      "date": "2024-09-10T08:29:18Z",
                      "email": "dengmengmian@noreply.gitcode.com",
                      "name": "dengmengmian"
                    },
                    "committer": {
                      "date": "2024-09-10T08:29:18Z",
                      "email": "dengmengmian@noreply.gitcode.com",
                      "name": "dengmengmian"
                    },
                    "message": "test"
                  },
                  "sha": "1af35823b8bbcaf68776cd6cb0ecbf88cfdec905",
                  "url": "https://test.gitcode.net/api/v5/repos/dengmengmian/test03/commits/1af35823b8bbcaf68776cd6cb0ecbf88cfdec905"
                },
                "name": "gitcode",
                "protected": false
              }
            }
          },
          "schema": {
            "properties": {
              "commit": {
                "properties": {
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
                  "sha": {
                    "type": "string"
                  },
                  "url": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "name": {
                "type": "string"
              },
              "protected": {
                "type": "integer"
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
    "Branch"
  ]
}
```
