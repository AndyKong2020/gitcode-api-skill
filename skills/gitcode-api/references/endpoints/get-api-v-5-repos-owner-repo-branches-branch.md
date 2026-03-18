# Get Single Branch
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-branches-branch](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-branches-branch)
Category: Branch
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/branches/{branch}`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_branches_{branch}`
- Tags: `Branch`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| branch | path | true | string | Branch name |
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
    "can_push": {
      "type": "integer"
    },
    "commit": {
      "properties": {
        "author_avatar_url": {
          "type": "string"
        },
        "author_email": {
          "type": "string"
        },
        "author_iam_id": {
          "type": "null"
        },
        "author_name": {
          "type": "string"
        },
        "author_user_name": {
          "type": "null"
        },
        "authored_date": {
          "type": "string"
        },
        "committed_date": {
          "type": "string"
        },
        "committer_avatar_url": {
          "type": "string"
        },
        "committer_email": {
          "type": "string"
        },
        "committer_name": {
          "type": "string"
        },
        "committer_user_name": {
          "type": "null"
        },
        "created_at": {
          "type": "string"
        },
        "gpg_primary_key_id": {
          "type": "null"
        },
        "id": {
          "type": "string"
        },
        "message": {
          "type": "string"
        },
        "open_gpg_verified": {
          "type": "null"
        },
        "parent_ids": {
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "relate_url": {
          "type": "null"
        },
        "short_id": {
          "type": "string"
        },
        "title": {
          "type": "string"
        },
        "verification_status": {
          "type": "null"
        }
      },
      "type": "object"
    },
    "default": {
      "type": "integer"
    },
    "developers_can_merge": {
      "type": "integer"
    },
    "developers_can_push": {
      "type": "integer"
    },
    "merged": {
      "type": "integer"
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
      "can_push": true,
      "commit": {
        "author_avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
        "author_email": "csdntest13@noreply.gitcode.com",
        "author_iam_id": null,
        "author_name": "csdntest13",
        "author_user_name": null,
        "authored_date": "2024-04-15T14:38:50.000Z",
        "committed_date": "2024-04-15T14:38:50.000Z",
        "committer_avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
        "committer_email": "csdntest13@noreply.gitcode.com",
        "committer_name": "csdntest13",
        "committer_user_name": null,
        "created_at": "2024-04-15T14:38:50.000Z",
        "gpg_primary_key_id": null,
        "id": "b6d44deb0ca73d7a50916d0fea02c72edd6c924e",
        "message": "dev add new file\n\nCreated-by: csdntest13\nAuthor-id: 494\nMR-id: 68629\nCommit-by: csdntest13\nMerged-by: csdntest13\nE2E-issues: \nDescription: commit message\n\nSee merge request: One/One!56",
        "open_gpg_verified": null,
        "parent_ids": [
          "13956ffeb5e5e1ce60c2ed91d3e579fc50b1f167",
          "3e42dcb9c09b39972c65536dad71651322470f28"
        ],
        "relate_url": null,
        "short_id": "b6d44deb",
        "title": "merge refs/merge-requests/56/head into dev",
        "verification_status": null
      },
      "default": false,
      "developers_can_merge": false,
      "developers_can_push": false,
      "merged": false,
      "name": "dev",
      "protected": false
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_branches_{branch}",
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
      "description": "Branch name",
      "example": "",
      "in": "path",
      "name": "branch",
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
  "path": "/api/v5/repos/{owner}/{repo}/branches/{branch}",
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
    "name": "Get Single Branch",
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
        "branches",
        ":branch"
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
            "content": "(Required) Branch name",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "branch",
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
                "can_push": true,
                "commit": {
                  "author_avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                  "author_email": "csdntest13@noreply.gitcode.com",
                  "author_iam_id": null,
                  "author_name": "csdntest13",
                  "author_user_name": null,
                  "authored_date": "2024-04-15T14:38:50.000Z",
                  "committed_date": "2024-04-15T14:38:50.000Z",
                  "committer_avatar_url": "https://gitcode-img.obs.cn-south-1.myhuaweicloud.com:443/ec/ba/4e7c4661b6154a7dd088d9fe64b4893383a2e318bf362350ce18d44df6ac7e37.png?time=1711533165876",
                  "committer_email": "csdntest13@noreply.gitcode.com",
                  "committer_name": "csdntest13",
                  "committer_user_name": null,
                  "created_at": "2024-04-15T14:38:50.000Z",
                  "gpg_primary_key_id": null,
                  "id": "b6d44deb0ca73d7a50916d0fea02c72edd6c924e",
                  "message": "dev add new file\n\nCreated-by: csdntest13\nAuthor-id: 494\nMR-id: 68629\nCommit-by: csdntest13\nMerged-by: csdntest13\nE2E-issues: \nDescription: commit message\n\nSee merge request: One/One!56",
                  "open_gpg_verified": null,
                  "parent_ids": [
                    "13956ffeb5e5e1ce60c2ed91d3e579fc50b1f167",
                    "3e42dcb9c09b39972c65536dad71651322470f28"
                  ],
                  "relate_url": null,
                  "short_id": "b6d44deb",
                  "title": "merge refs/merge-requests/56/head into dev",
                  "verification_status": null
                },
                "default": false,
                "developers_can_merge": false,
                "developers_can_push": false,
                "merged": false,
                "name": "dev",
                "protected": false
              }
            }
          },
          "schema": {
            "properties": {
              "can_push": {
                "type": "integer"
              },
              "commit": {
                "properties": {
                  "author_avatar_url": {
                    "type": "string"
                  },
                  "author_email": {
                    "type": "string"
                  },
                  "author_iam_id": {
                    "type": "null"
                  },
                  "author_name": {
                    "type": "string"
                  },
                  "author_user_name": {
                    "type": "null"
                  },
                  "authored_date": {
                    "type": "string"
                  },
                  "committed_date": {
                    "type": "string"
                  },
                  "committer_avatar_url": {
                    "type": "string"
                  },
                  "committer_email": {
                    "type": "string"
                  },
                  "committer_name": {
                    "type": "string"
                  },
                  "committer_user_name": {
                    "type": "null"
                  },
                  "created_at": {
                    "type": "string"
                  },
                  "gpg_primary_key_id": {
                    "type": "null"
                  },
                  "id": {
                    "type": "string"
                  },
                  "message": {
                    "type": "string"
                  },
                  "open_gpg_verified": {
                    "type": "null"
                  },
                  "parent_ids": {
                    "items": {
                      "type": "string"
                    },
                    "type": "array"
                  },
                  "relate_url": {
                    "type": "null"
                  },
                  "short_id": {
                    "type": "string"
                  },
                  "title": {
                    "type": "string"
                  },
                  "verification_status": {
                    "type": "null"
                  }
                },
                "type": "object"
              },
              "default": {
                "type": "integer"
              },
              "developers_can_merge": {
                "type": "integer"
              },
              "developers_can_push": {
                "type": "integer"
              },
              "merged": {
                "type": "integer"
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
