# Get User's Specific Repository
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo)
Category: Users
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}`
- Tags: `Users`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
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
    "assignees_number": {
      "type": "integer"
    },
    "assigner": {
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
    "created_at": {
      "type": "string"
    },
    "creator": {
      "properties": {
        "arts_id": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "id": {
          "type": "string"
        },
        "nickname": {
          "type": "string"
        },
        "photo": {
          "type": "string"
        },
        "username": {
          "type": "string"
        }
      },
      "type": "object"
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
    "license": {
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
    "private": {
      "type": "integer"
    },
    "project_labels": {
      "items": {
        "properties": {},
        "type": "object"
      },
      "type": "array"
    },
    "public": {
      "type": "integer"
    },
    "readme_url": {
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
}
```
Examples:
```json
{
  "1": {
    "summary": "Successful Example",
    "value": {
      "assignees_number": 0,
      "assigner": {
        "id": "332008",
        "login": "aron1",
        "name": "yanfan",
        "type": "User"
      },
      "created_at": "2024-10-22T22:14:06.922+08:00",
      "creator": {
        "arts_id": "332008",
        "email": "aron1@noreply.gitcode.com",
        "id": "660ba866683c570b25be06c8",
        "nickname": "yanfan",
        "photo": "https://cdn-img.gitcode.com/bd/ca/0115343247b338d0c53589a145501e84a58464272f2fb09b372cc3d2311b2b39.png?time=1722525295285",
        "username": "aron1"
      },
      "default_branch": "main",
      "description": "",
      "enterprise": {
        "html_url": "https://gitcode.com/aron1",
        "id": 1364544,
        "path": "aron1",
        "type": "user"
      },
      "fork": false,
      "forks_count": 0,
      "full_name": "aron1/Model10123001",
      "http_url_to_repo": "https://gitcode.com/aron1/Model10123001.git",
      "human_name": "aron1 / Model10123001tewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtew",
      "id": 4250980,
      "internal": false,
      "issue_template_source": "project",
      "license": "Apache_License_v2.0",
      "members": [
        "aron1"
      ],
      "name": "Model10123001tewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtew",
      "namespace": {
        "html_url": "https://gitcode.com/aron1",
        "id": 1364544,
        "name": "aron1",
        "path": "aron1"
      },
      "open_issues_count": 0,
      "owner": {
        "id": "332008",
        "login": "aron1",
        "name": "yanfan",
        "type": "User"
      },
      "path": "Model10123001",
      "private": true,
      "project_labels": [],
      "public": false,
      "readme_url": "https://gitcode.com/aron1/Model10123001/blob/main/README.md",
      "ssh_url_to_repo": "git@gitcode.com:aron1/Model10123001.git",
      "stargazers_count": 1,
      "status": "close",
      "updated_at": "2024-12-02T18:37:23.426+08:00",
      "url": "https://api.gitcode.com/api/v5/repos/aron1/Model10123001",
      "watchers_count": 0,
      "web_url": "https://gitcode.com/aron1/Model10123001"
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
  "operationId": "get_api_v5_repos_{owner}_{repo}",
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
    }
  ],
  "path": "/api/v5/repos/{owner}/{repo}",
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
    "name": "Get User's Specific Repository",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "repos",
        ":owner",
        ":repo"
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
                "assignees_number": 0,
                "assigner": {
                  "id": "332008",
                  "login": "aron1",
                  "name": "yanfan",
                  "type": "User"
                },
                "created_at": "2024-10-22T22:14:06.922+08:00",
                "creator": {
                  "arts_id": "332008",
                  "email": "aron1@noreply.gitcode.com",
                  "id": "660ba866683c570b25be06c8",
                  "nickname": "yanfan",
                  "photo": "https://cdn-img.gitcode.com/bd/ca/0115343247b338d0c53589a145501e84a58464272f2fb09b372cc3d2311b2b39.png?time=1722525295285",
                  "username": "aron1"
                },
                "default_branch": "main",
                "description": "",
                "enterprise": {
                  "html_url": "https://gitcode.com/aron1",
                  "id": 1364544,
                  "path": "aron1",
                  "type": "user"
                },
                "fork": false,
                "forks_count": 0,
                "full_name": "aron1/Model10123001",
                "http_url_to_repo": "https://gitcode.com/aron1/Model10123001.git",
                "human_name": "aron1 / Model10123001tewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtew",
                "id": 4250980,
                "internal": false,
                "issue_template_source": "project",
                "license": "Apache_License_v2.0",
                "members": [
                  "aron1"
                ],
                "name": "Model10123001tewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtewteewtew",
                "namespace": {
                  "html_url": "https://gitcode.com/aron1",
                  "id": 1364544,
                  "name": "aron1",
                  "path": "aron1"
                },
                "open_issues_count": 0,
                "owner": {
                  "id": "332008",
                  "login": "aron1",
                  "name": "yanfan",
                  "type": "User"
                },
                "path": "Model10123001",
                "private": true,
                "project_labels": [],
                "public": false,
                "readme_url": "https://gitcode.com/aron1/Model10123001/blob/main/README.md",
                "ssh_url_to_repo": "git@gitcode.com:aron1/Model10123001.git",
                "stargazers_count": 1,
                "status": "close",
                "updated_at": "2024-12-02T18:37:23.426+08:00",
                "url": "https://api.gitcode.com/api/v5/repos/aron1/Model10123001",
                "watchers_count": 0,
                "web_url": "https://gitcode.com/aron1/Model10123001"
              }
            }
          },
          "schema": {
            "properties": {
              "assignees_number": {
                "type": "integer"
              },
              "assigner": {
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
              "created_at": {
                "type": "string"
              },
              "creator": {
                "properties": {
                  "arts_id": {
                    "type": "string"
                  },
                  "email": {
                    "type": "string"
                  },
                  "id": {
                    "type": "string"
                  },
                  "nickname": {
                    "type": "string"
                  },
                  "photo": {
                    "type": "string"
                  },
                  "username": {
                    "type": "string"
                  }
                },
                "type": "object"
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
              "license": {
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
              "private": {
                "type": "integer"
              },
              "project_labels": {
                "items": {
                  "properties": {},
                  "type": "object"
                },
                "type": "array"
              },
              "public": {
                "type": "integer"
              },
              "readme_url": {
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
