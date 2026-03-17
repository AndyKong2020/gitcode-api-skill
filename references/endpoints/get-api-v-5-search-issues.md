# Search Issues
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-issues](https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-issues)
Category: Search
- Method: `GET`
- Path: `/api/v5/search/issues`
- Operation ID: `get_api_v5_search_issues`
- Tags: `Search`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number, maximum is 100. |
| per_page | query | false | integer | The number of items per page, with a maximum of 50. |
| q | query | true | string | Search keyword |
| sort | query | false | string | sort_field: The sorting field,可以选择 created_at (creation time) or last_push_at (update time), with a default of best match. |
| order | query | false | string | Sort order (default: desc) |
| repo | query | false | string | Repository path |
| state | query | false | string | Filter issues by their specified states, open or closed. |
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
      "body": {
        "type": "string"
      },
      "comments": {
        "type": "integer"
      },
      "created_at": {
        "type": "string"
      },
      "html_url": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "labels": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "number": {
        "type": "string"
      },
      "parent_id": {
        "type": "integer"
      },
      "priority": {
        "type": "integer"
      },
      "repository": {
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "owner": {
            "properties": {
              "avatar_url": {
                "type": "string"
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
              },
              "type": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "path": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "state": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
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
      "body": "test",
      "comments": 0,
      "created_at": "2024-11-07T18:11:23+08:00",
      "html_url": "https://gitcode.com/youlai/vue3-element-admin/issues/1",
      "id": 548499,
      "labels": [],
      "number": "1",
      "parent_id": 0,
      "priority": 0,
      "repository": {
        "full_name": "youlai/vue3-element-admin",
        "human_name": "YouKai Open Source Organization / vue3-element-admin",
        "id": 3771502,
        "name": "vue3-element-admin",
        "owner": {
          "avatar_url": "https://cdn-img.gitcode.com/fc/ae/3f96c31289ae838297c61f385af9c2e6357216a1906205f56d50f3e268319d8b.png?time=1724590827689",
          "html_url": "https://gitcode.com/u013737132",
          "id": "6553a045ac27540b6bfcb436",
          "login": "u013737132",
          "name": "YouLai Technology",
          "type": "User"
        },
        "path": "vue3-element-admin",
        "url": "https://gitcode.com/youlai/vue3-element-admin"
      },
      "state": "open",
      "title": "test",
      "updated_at": "2024-11-07T18:11:23+08:00"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "body": "11111",
      "comments": 2,
      "created_at": "2024-11-01T14:12:21+08:00",
      "html_url": "https://gitcode.com/openUBMC-test/openubmc-ci/issues/4",
      "id": 518776,
      "labels": [],
      "number": "4",
      "parent_id": 0,
      "priority": 0,
      "repository": {
        "full_name": "openUBMC-test/openubmc-ci",
        "human_name": "openUBMC-test / openubmc-ci",
        "id": 4261097,
        "name": "openubmc-ci",
        "owner": {
          "avatar_url": "https://cdn-img.gitcode.com/fd/ab/256f0d7a9b2b771a883a9a2975f6bb8804dbcc53df334a63a508306f86fe6c2c.jpg",
          "html_url": "https://gitcode.com/levi3053",
          "id": "671af08b9a767f4c7b6b0681",
          "login": "levi3053",
          "name": "BellllllYu@N.L¡",
          "type": "User"
        },
        "path": "openubmc-ci",
        "url": "https://gitcode.com/openUBMC-test/openubmc-ci"
      },
      "state": "open",
      "title": "test_1",
      "updated_at": "2024-11-01T14:15:00+08:00"
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
  "operationId": "get_api_v5_search_issues",
  "parameters": [
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
      "description": "Current page number, maximum is 100.",
      "in": "query",
      "name": "page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "The number of items per page, with a maximum of 50.",
      "in": "query",
      "name": "per_page",
      "required": false,
      "schema": {
        "type": "integer"
      }
    },
    {
      "description": "Search keyword",
      "in": "query",
      "name": "q",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "sort_field: The sorting field,可以选择 created_at (creation time) or last_push_at (update time), with a default of best match.",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Sort order (default: desc)",
      "in": "query",
      "name": "order",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Repository path",
      "in": "query",
      "name": "repo",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Filter issues by their specified states, open or closed.",
      "in": "query",
      "name": "state",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/search/issues",
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
    "name": "Search Issues",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "search",
        "issues"
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
            "content": "Current page number, maximum is 100.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "page",
          "value": ""
        },
        {
          "description": {
            "content": "The number of items per page, with a maximum of 50.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "per_page",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Search keyword",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "q",
          "value": ""
        },
        {
          "description": {
            "content": "sort_field: The sorting field,可以选择 created_at (creation time) or last_push_at (update time), with a default of best match.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "Sort order (default: desc)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "order",
          "value": ""
        },
        {
          "description": {
            "content": "Repository path",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "repo",
          "value": ""
        },
        {
          "description": {
            "content": "Filter issues by their specified states, open or closed.",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "state",
          "value": ""
        }
      ],
      "variable": []
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
                "body": "test",
                "comments": 0,
                "created_at": "2024-11-07T18:11:23+08:00",
                "html_url": "https://gitcode.com/youlai/vue3-element-admin/issues/1",
                "id": 548499,
                "labels": [],
                "number": "1",
                "parent_id": 0,
                "priority": 0,
                "repository": {
                  "full_name": "youlai/vue3-element-admin",
                  "human_name": "YouKai Open Source Organization / vue3-element-admin",
                  "id": 3771502,
                  "name": "vue3-element-admin",
                  "owner": {
                    "avatar_url": "https://cdn-img.gitcode.com/fc/ae/3f96c31289ae838297c61f385af9c2e6357216a1906205f56d50f3e268319d8b.png?time=1724590827689",
                    "html_url": "https://gitcode.com/u013737132",
                    "id": "6553a045ac27540b6bfcb436",
                    "login": "u013737132",
                    "name": "YouLai Technology",
                    "type": "User"
                  },
                  "path": "vue3-element-admin",
                  "url": "https://gitcode.com/youlai/vue3-element-admin"
                },
                "state": "open",
                "title": "test",
                "updated_at": "2024-11-07T18:11:23+08:00"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "body": "11111",
                "comments": 2,
                "created_at": "2024-11-01T14:12:21+08:00",
                "html_url": "https://gitcode.com/openUBMC-test/openubmc-ci/issues/4",
                "id": 518776,
                "labels": [],
                "number": "4",
                "parent_id": 0,
                "priority": 0,
                "repository": {
                  "full_name": "openUBMC-test/openubmc-ci",
                  "human_name": "openUBMC-test / openubmc-ci",
                  "id": 4261097,
                  "name": "openubmc-ci",
                  "owner": {
                    "avatar_url": "https://cdn-img.gitcode.com/fd/ab/256f0d7a9b2b771a883a9a2975f6bb8804dbcc53df334a63a508306f86fe6c2c.jpg",
                    "html_url": "https://gitcode.com/levi3053",
                    "id": "671af08b9a767f4c7b6b0681",
                    "login": "levi3053",
                    "name": "BellllllYu@N.L¡",
                    "type": "User"
                  },
                  "path": "openubmc-ci",
                  "url": "https://gitcode.com/openUBMC-test/openubmc-ci"
                },
                "state": "open",
                "title": "test_1",
                "updated_at": "2024-11-01T14:15:00+08:00"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "body": {
                  "type": "string"
                },
                "comments": {
                  "type": "integer"
                },
                "created_at": {
                  "type": "string"
                },
                "html_url": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "labels": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "number": {
                  "type": "string"
                },
                "parent_id": {
                  "type": "integer"
                },
                "priority": {
                  "type": "integer"
                },
                "repository": {
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "owner": {
                      "properties": {
                        "avatar_url": {
                          "type": "string"
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
                        },
                        "type": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "path": {
                      "type": "string"
                    },
                    "url": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "state": {
                  "type": "string"
                },
                "title": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
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
    "Search"
  ]
}
```
