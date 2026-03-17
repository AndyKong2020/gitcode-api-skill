# Search Repositories
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-repositories](https://docs.gitcode.com/en/docs/apis/get-api-v-5-search-repositories)
Category: Search
- Method: `GET`
- Path: `/api/v5/search/repositories`
- Operation ID: `get_api_v5_search_repositories`
- Tags: `Search`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| page | query | false | integer | Current page number, maximum is 100. |
| per_page | query | false | integer | Number of pages, maximum 20 |
| q | query | true | string | Search keyword |
| sort | query | false | string | sort_field: The sorting field, can be last_push_at (update time), stars_count (stars count), forks_count (fork count). Defaults to best match. |
| order | query | false | string | Sort order (default: desc) |
| owner | query | false | string | Repository space address (organization or individual's address path) |
| fork | query | false | string | Whether to search for repositories containing forks; if displayed, subject to whitelist restrictions, default: no |
| language | query | false | string | Filter repositories by the specified language |
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
      "created_at": {
        "type": "string"
      },
      "default_branch": {
        "type": "string"
      },
      "description": {
        "type": "string"
      },
      "enterprise": {
        "properties": {
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "path": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "fork": {
        "type": "integer"
      },
      "forks_count": {
        "type": "integer"
      },
      "full_name": {
        "type": "string"
      },
      "has_issue": {
        "type": "integer"
      },
      "homepage": {
        "type": "string"
      },
      "http_url_to_repo": {
        "type": "string"
      },
      "human_name": {
        "type": "string"
      },
      "id": {
        "type": "integer"
      },
      "internal": {
        "type": "integer"
      },
      "issue_template_source": {
        "type": "string"
      },
      "members": {
        "items": {
          "type": "string"
        },
        "type": "array"
      },
      "name": {
        "type": "string"
      },
      "namespace": {
        "properties": {
          "html_url": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "name": {
            "type": "string"
          },
          "path": {
            "type": "string"
          },
          "type": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "open_issues_count": {
        "type": "integer"
      },
      "owner": {
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
      },
      "path": {
        "type": "string"
      },
      "permission": {
        "properties": {
          "push": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "private": {
        "type": "integer"
      },
      "public": {
        "type": "integer"
      },
      "pushed_at": {
        "type": "string"
      },
      "relation": {
        "type": "string"
      },
      "ssh_url_to_repo": {
        "type": "string"
      },
      "stargazers_count": {
        "type": "integer"
      },
      "status": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "watchers_count": {
        "type": "integer"
      },
      "web_url": {
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
      "created_at": "2023-12-18T00:42:15.557+08:00",
      "default_branch": "main",
      "description": "Allure Report is a flexible, lightweight multi-language test reporting tool. It provides clear graphical reports and allows everyone involved in the development process to extract the maximum of information from the everyday testing process",
      "enterprise": {
        "html_url": "https://gitcode.com/al",
        "id": 2192652,
        "path": "al",
        "type": "enterprise"
      },
      "fork": false,
      "forks_count": 0,
      "full_name": "gh_mirrors/al/allure2",
      "has_issue": false,
      "homepage": "https://gitcode.com/gh_mirrors/al/allure2",
      "http_url_to_repo": "https://gitcode.com/gh_mirrors/al/allure2.git",
      "human_name": "GitHub Acceleration Program / al / allure2",
      "id": 1431191,
      "internal": false,
      "issue_template_source": "project",
      "members": [
        "Gitcode-Assistant",
        "coco_gitcode",
        "gitshumei"
      ],
      "name": "allure2",
      "namespace": {
        "html_url": "https://gitcode.com/al",
        "id": 2192652,
        "name": "al",
        "path": "al",
        "type": "enterprise"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "69090",
        "login": "coco_gitcode",
        "name": "GitCode high-quality project",
        "type": "User"
      },
      "path": "allure2",
      "permission": {
        "push": false
      },
      "private": false,
      "public": true,
      "pushed_at": "2024-08-06T23:34:38.476+08:00",
      "relation": "",
      "ssh_url_to_repo": "git@gitcode.com:gh_mirrors/al/allure2.git",
      "stargazers_count": 9,
      "status": "start",
      "updated_at": "2024-11-05T10:54:59.948+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/gh_mirrors/al/allure2",
      "watchers_count": 4,
      "web_url": "https://gitcode.com/gh_mirrors/al/allure2"
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "created_at": "2023-12-16T20:28:57.687+08:00",
      "default_branch": "master",
      "description": "Tiny, fast, non-dependent and fully loaded printf implementation for embedded systems. Extensive test suite passing.",
      "enterprise": {
        "html_url": "https://gitcode.com/pr",
        "id": 2192766,
        "path": "pr",
        "type": "enterprise"
      },
      "fork": false,
      "forks_count": 0,
      "full_name": "gh_mirrors/pr/printf",
      "has_issue": false,
      "homepage": "https://gitcode.com/gh_mirrors/pr/printf",
      "http_url_to_repo": "https://gitcode.com/gh_mirrors/pr/printf.git",
      "human_name": "GitHub Acceleration Program / pr / printf",
      "id": 1401745,
      "internal": false,
      "issue_template_source": "project",
      "members": [
        "Gitcode-Assistant",
        "coco_gitcode",
        "gitshumei"
      ],
      "name": "printf",
      "namespace": {
        "html_url": "https://gitcode.com/pr",
        "id": 2192766,
        "name": "pr",
        "path": "pr",
        "type": "enterprise"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "69090",
        "login": "coco_gitcode",
        "name": "GitCode high-quality project",
        "type": "User"
      },
      "path": "printf",
      "permission": {
        "push": false
      },
      "private": false,
      "public": true,
      "pushed_at": "2024-08-10T00:28:30.350+08:00",
      "relation": "",
      "ssh_url_to_repo": "git@gitcode.com:gh_mirrors/pr/printf.git",
      "stargazers_count": 8,
      "status": "start",
      "updated_at": "2024-09-27T21:48:26.980+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/gh_mirrors/pr/printf",
      "watchers_count": 0,
      "web_url": "https://gitcode.com/gh_mirrors/pr/printf"
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
  "operationId": "get_api_v5_search_repositories",
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
      "description": "Number of pages, maximum 20",
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
      "description": "sort_field: The sorting field, can be last_push_at (update time), stars_count (stars count), forks_count (fork count). Defaults to best match.",
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
      "description": "Repository space address (organization or individual's address path)",
      "in": "query",
      "name": "owner",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Whether to search for repositories containing forks; if displayed, subject to whitelist restrictions, default: no",
      "in": "query",
      "name": "fork",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Filter repositories by the specified language",
      "in": "query",
      "name": "language",
      "required": false,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/search/repositories",
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
    "name": "Search Repositories",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "search",
        "repositories"
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
            "content": "Number of pages, maximum 20",
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
            "content": "sort_field: The sorting field, can be last_push_at (update time), stars_count (stars count), forks_count (fork count). Defaults to best match.",
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
            "content": "Repository space address (organization or individual's address path)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "owner",
          "value": ""
        },
        {
          "description": {
            "content": "Whether to search for repositories containing forks; if displayed, subject to whitelist restrictions, default: no",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "fork",
          "value": ""
        },
        {
          "description": {
            "content": "Filter repositories by the specified language",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "language",
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
                "created_at": "2023-12-18T00:42:15.557+08:00",
                "default_branch": "main",
                "description": "Allure Report is a flexible, lightweight multi-language test reporting tool. It provides clear graphical reports and allows everyone involved in the development process to extract the maximum of information from the everyday testing process",
                "enterprise": {
                  "html_url": "https://gitcode.com/al",
                  "id": 2192652,
                  "path": "al",
                  "type": "enterprise"
                },
                "fork": false,
                "forks_count": 0,
                "full_name": "gh_mirrors/al/allure2",
                "has_issue": false,
                "homepage": "https://gitcode.com/gh_mirrors/al/allure2",
                "http_url_to_repo": "https://gitcode.com/gh_mirrors/al/allure2.git",
                "human_name": "GitHub Acceleration Program / al / allure2",
                "id": 1431191,
                "internal": false,
                "issue_template_source": "project",
                "members": [
                  "Gitcode-Assistant",
                  "coco_gitcode",
                  "gitshumei"
                ],
                "name": "allure2",
                "namespace": {
                  "html_url": "https://gitcode.com/al",
                  "id": 2192652,
                  "name": "al",
                  "path": "al",
                  "type": "enterprise"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "69090",
                  "login": "coco_gitcode",
                  "name": "GitCode high-quality project",
                  "type": "User"
                },
                "path": "allure2",
                "permission": {
                  "push": false
                },
                "private": false,
                "public": true,
                "pushed_at": "2024-08-06T23:34:38.476+08:00",
                "relation": "",
                "ssh_url_to_repo": "git@gitcode.com:gh_mirrors/al/allure2.git",
                "stargazers_count": 9,
                "status": "start",
                "updated_at": "2024-11-05T10:54:59.948+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/gh_mirrors/al/allure2",
                "watchers_count": 4,
                "web_url": "https://gitcode.com/gh_mirrors/al/allure2"
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "created_at": "2023-12-16T20:28:57.687+08:00",
                "default_branch": "master",
                "description": "Tiny, fast, non-dependent and fully loaded printf implementation for embedded systems. Extensive test suite passing.",
                "enterprise": {
                  "html_url": "https://gitcode.com/pr",
                  "id": 2192766,
                  "path": "pr",
                  "type": "enterprise"
                },
                "fork": false,
                "forks_count": 0,
                "full_name": "gh_mirrors/pr/printf",
                "has_issue": false,
                "homepage": "https://gitcode.com/gh_mirrors/pr/printf",
                "http_url_to_repo": "https://gitcode.com/gh_mirrors/pr/printf.git",
                "human_name": "GitHub Acceleration Program / pr / printf",
                "id": 1401745,
                "internal": false,
                "issue_template_source": "project",
                "members": [
                  "Gitcode-Assistant",
                  "coco_gitcode",
                  "gitshumei"
                ],
                "name": "printf",
                "namespace": {
                  "html_url": "https://gitcode.com/pr",
                  "id": 2192766,
                  "name": "pr",
                  "path": "pr",
                  "type": "enterprise"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "69090",
                  "login": "coco_gitcode",
                  "name": "GitCode high-quality project",
                  "type": "User"
                },
                "path": "printf",
                "permission": {
                  "push": false
                },
                "private": false,
                "public": true,
                "pushed_at": "2024-08-10T00:28:30.350+08:00",
                "relation": "",
                "ssh_url_to_repo": "git@gitcode.com:gh_mirrors/pr/printf.git",
                "stargazers_count": 8,
                "status": "start",
                "updated_at": "2024-09-27T21:48:26.980+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/gh_mirrors/pr/printf",
                "watchers_count": 0,
                "web_url": "https://gitcode.com/gh_mirrors/pr/printf"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "created_at": {
                  "type": "string"
                },
                "default_branch": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "enterprise": {
                  "properties": {
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "path": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "fork": {
                  "type": "integer"
                },
                "forks_count": {
                  "type": "integer"
                },
                "full_name": {
                  "type": "string"
                },
                "has_issue": {
                  "type": "integer"
                },
                "homepage": {
                  "type": "string"
                },
                "http_url_to_repo": {
                  "type": "string"
                },
                "human_name": {
                  "type": "string"
                },
                "id": {
                  "type": "integer"
                },
                "internal": {
                  "type": "integer"
                },
                "issue_template_source": {
                  "type": "string"
                },
                "members": {
                  "items": {
                    "type": "string"
                  },
                  "type": "array"
                },
                "name": {
                  "type": "string"
                },
                "namespace": {
                  "properties": {
                    "html_url": {
                      "type": "string"
                    },
                    "id": {
                      "type": "integer"
                    },
                    "name": {
                      "type": "string"
                    },
                    "path": {
                      "type": "string"
                    },
                    "type": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "open_issues_count": {
                  "type": "integer"
                },
                "owner": {
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
                },
                "path": {
                  "type": "string"
                },
                "permission": {
                  "properties": {
                    "push": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "private": {
                  "type": "integer"
                },
                "public": {
                  "type": "integer"
                },
                "pushed_at": {
                  "type": "string"
                },
                "relation": {
                  "type": "string"
                },
                "ssh_url_to_repo": {
                  "type": "string"
                },
                "stargazers_count": {
                  "type": "integer"
                },
                "status": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "watchers_count": {
                  "type": "integer"
                },
                "web_url": {
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
