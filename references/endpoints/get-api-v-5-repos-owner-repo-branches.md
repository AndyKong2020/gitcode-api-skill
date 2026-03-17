# Get All Project Branches
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-branches](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-branches)
Category: Branch
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/branches`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_branches`
- Tags: `Branch`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| access_token | query | true | string | User authorization code |
| sort | query | false | string | Sort field by name/updated |
| direction | query | false | string | sort direction asc/desc |
| page | query | false | integer | The current page number |
| per_page | query | false | integer | The number of items per page, with a maximum of 100. The default is 20. |
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
  "items": {
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
  },
  "type": "array"
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
            "date": "2024-04-16T08:41:20.000Z",
            "email": "Lzm_0916@noreply.gitcode.com",
            "name": "Lzm_0916"
          },
          "committer": {
            "date": "2024-04-16T08:41:20.000Z",
            "email": "Lzm_0916@noreply.gitcode.com",
            "name": "Lzm_0916"
          },
          "message": "submit test class"
        },
        "sha": "1d45587145552af003cd32cc6fde9ac9d9e5fd42",
        "url": "https://test.gitcode.net/api/v5/repos/Lzm_0916/test/commits/1d45587145552af003cd32cc6fde9ac9d9e5fd42"
      },
      "name": "main",
      "protected": true
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_branches",
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
      "description": "User authorization code",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort field by name/updated",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "sort direction asc/desc",
      "in": "query",
      "name": "direction",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "The current page number",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 100. The default is 20.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}/branches",
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
    "name": "Get All Project Branches",
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
        },
        {
          "description": {
            "content": "Sort field by name/updated",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "sort direction asc/desc",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "direction",
          "value": ""
        },
        {
          "description": {
            "content": "The current page number",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 100. The default is 20.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
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
                "commit": {
                  "commit": {
                    "author": {
                      "date": "2024-04-16T08:41:20.000Z",
                      "email": "Lzm_0916@noreply.gitcode.com",
                      "name": "Lzm_0916"
                    },
                    "committer": {
                      "date": "2024-04-16T08:41:20.000Z",
                      "email": "Lzm_0916@noreply.gitcode.com",
                      "name": "Lzm_0916"
                    },
                    "message": "submit test class"
                  },
                  "sha": "1d45587145552af003cd32cc6fde9ac9d9e5fd42",
                  "url": "https://test.gitcode.net/api/v5/repos/Lzm_0916/test/commits/1d45587145552af003cd32cc6fde9ac9d9e5fd42"
                },
                "name": "main",
                "protected": true
              }
            }
          },
          "schema": {
            "items": {
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
    "Branch"
  ]
}
```
