# List Repositories Starred by Authorized Users
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-starred](https://docs.gitcode.com/en/docs/apis/get-api-v-5-user-starred)
Category: Users
- Method: `GET`
- Path: `/api/v5/user/starred`
- Operation ID: `get_api_v5_user_starred`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| access_token | query | true | string | User authorization code |
| sort | query | false | string | created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time |
| direction | query | false | string | sort direction, default: desc |
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
      "has_issues": {
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
      "parent": {
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "parentfull_name": {
        "type": "string"
      },
      "path": {
        "type": "string"
      },
      "permission": {
        "properties": {
          "admin": {
            "type": "integer"
          },
          "pull": {
            "type": "integer"
          },
          "push": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "private": {
        "type": "integer"
      },
      "project_creator": {
        "type": "string"
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
      "created_at": "2024-12-11T17:41:14.536+08:00",
      "default_branch": "main",
      "description": "Trump",
      "enterprise": {
        "html_url": "https://gitcode.com/xiaogang",
        "id": 137117,
        "path": "xiaogang",
        "type": "user"
      },
      "fork": true,
      "forks_count": 0,
      "full_name": "xiaogang/private-new2",
      "has_issue": false,
      "has_issues": false,
      "homepage": "https://gitcode.com/xiaogang/private-new2",
      "http_url_to_repo": "https://gitcode.com/xiaogang/private-new2.git",
      "human_name": "xiaogang / private-new2",
      "id": 777621,
      "internal": false,
      "issue_template_source": "project",
      "members": [
        "xiaogang"
      ],
      "name": "private-new2",
      "namespace": {
        "html_url": "https://gitcode.com/xiaogang",
        "id": 137117,
        "name": "xiaogang",
        "path": "xiaogang",
        "type": "user"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "496",
        "login": "xiaogang",
        "name": "Xiao Gang",
        "type": "User"
      },
      "parent": {
        "full_name": "xiaogang_test/private-new",
        "human_name": "xiaogang_test / private-new"
      },
      "parentfull_name": "xiaogang_test/private-new",
      "path": "private-new2",
      "permission": {
        "admin": true,
        "pull": true,
        "push": true
      },
      "private": false,
      "project_creator": "xiaogang",
      "public": true,
      "pushed_at": "2024-12-20T19:14:34.979+08:00",
      "relation": "master",
      "ssh_url_to_repo": "ssh://git@gitcode.com:2222/xiaogang/private-new2.git",
      "stargazers_count": 1,
      "status": "start",
      "updated_at": "2024-12-11T17:41:14.536+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/xiaogang/private-new2",
      "watchers_count": 0,
      "web_url": "https://gitcode.com/xiaogang/private-new2"
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
  "operationId": "get_api_v5_user_starred",
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
      "description": "created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time",
      "in": "query",
      "name": "sort",
      "required": false,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "sort direction, default: desc",
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
  "path": "/api/v5/user/starred",
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
    "name": "List Repositories Starred by Authorized Users",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "user",
        "starred"
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
            "content": "created/last_push Sort by repository creation time (created) or last push time (updated), default: creation time",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "sort",
          "value": ""
        },
        {
          "description": {
            "content": "sort direction, default: desc",
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
                "created_at": "2024-12-11T17:41:14.536+08:00",
                "default_branch": "main",
                "description": "Trump",
                "enterprise": {
                  "html_url": "https://gitcode.com/xiaogang",
                  "id": 137117,
                  "path": "xiaogang",
                  "type": "user"
                },
                "fork": true,
                "forks_count": 0,
                "full_name": "xiaogang/private-new2",
                "has_issue": false,
                "has_issues": false,
                "homepage": "https://gitcode.com/xiaogang/private-new2",
                "http_url_to_repo": "https://gitcode.com/xiaogang/private-new2.git",
                "human_name": "xiaogang / private-new2",
                "id": 777621,
                "internal": false,
                "issue_template_source": "project",
                "members": [
                  "xiaogang"
                ],
                "name": "private-new2",
                "namespace": {
                  "html_url": "https://gitcode.com/xiaogang",
                  "id": 137117,
                  "name": "xiaogang",
                  "path": "xiaogang",
                  "type": "user"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "496",
                  "login": "xiaogang",
                  "name": "Xiao Gang",
                  "type": "User"
                },
                "parent": {
                  "full_name": "xiaogang_test/private-new",
                  "human_name": "xiaogang_test / private-new"
                },
                "parentfull_name": "xiaogang_test/private-new",
                "path": "private-new2",
                "permission": {
                  "admin": true,
                  "pull": true,
                  "push": true
                },
                "private": false,
                "project_creator": "xiaogang",
                "public": true,
                "pushed_at": "2024-12-20T19:14:34.979+08:00",
                "relation": "master",
                "ssh_url_to_repo": "ssh://git@gitcode.com:2222/xiaogang/private-new2.git",
                "stargazers_count": 1,
                "status": "start",
                "updated_at": "2024-12-11T17:41:14.536+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/xiaogang/private-new2",
                "watchers_count": 0,
                "web_url": "https://gitcode.com/xiaogang/private-new2"
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
                "has_issues": {
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
                "parent": {
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "parentfull_name": {
                  "type": "string"
                },
                "path": {
                  "type": "string"
                },
                "permission": {
                  "properties": {
                    "admin": {
                      "type": "integer"
                    },
                    "pull": {
                      "type": "integer"
                    },
                    "push": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "private": {
                  "type": "integer"
                },
                "project_creator": {
                  "type": "string"
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
    "Users"
  ]
}
```
