# Get Enterprise Issue Associated Pull Requests
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number-pull-requests](https://docs.gitcode.com/en/docs/apis/get-api-v-5-enterprises-enterprise-issues-number-pull-requests)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/enterprises/{enterprise}/issues/{number}/pull_requests`
- Operation ID: `get_api_v5_enterprises_{enterprise}_issues_{number}_pull_requests`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | org(path/login) |
| number | path | true | integer | issue Global ID |
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
  "items": {
    "properties": {
      "added_lines": {
        "type": "integer"
      },
      "assignees": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "assignees_number": {
        "type": "integer"
      },
      "base": {
        "properties": {
          "label": {
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
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
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "sha": {
            "type": "string"
          },
          "user": {
            "properties": {
              "email": {
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
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "type": "object"
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
      "close_related_issue": {
        "type": "integer"
      },
      "closed_at": {
        "type": "string"
      },
      "comments_url": {
        "type": "string"
      },
      "commits_url": {
        "type": "string"
      },
      "created_at": {
        "type": "string"
      },
      "diff_refs": {
        "properties": {
          "base_sha": {
            "type": "string"
          },
          "head_sha": {
            "type": "string"
          },
          "start_sha": {
            "type": "string"
          }
        },
        "type": "object"
      },
      "diff_url": {
        "type": "string"
      },
      "draft": {
        "type": "integer"
      },
      "force_remove_source_branch": {
        "type": "integer"
      },
      "head": {
        "properties": {
          "label": {
            "type": "string"
          },
          "ref": {
            "type": "string"
          },
          "repo": {
            "properties": {
              "assigner": {
                "properties": {
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "description": {
                "type": "string"
              },
              "full_name": {
                "type": "string"
              },
              "full_path": {
                "type": "string"
              },
              "html_url": {
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
              "name": {
                "type": "string"
              },
              "owner": {
                "properties": {
                  "email": {
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
                  "name_cn": {
                    "type": "string"
                  },
                  "state": {
                    "type": "string"
                  }
                },
                "type": "object"
              },
              "path": {
                "type": "string"
              }
            },
            "type": "object"
          },
          "sha": {
            "type": "string"
          },
          "user": {
            "properties": {
              "email": {
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
              "name_cn": {
                "type": "string"
              },
              "state": {
                "type": "string"
              }
            },
            "type": "object"
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
      "iid": {
        "type": "integer"
      },
      "issue_url": {
        "type": "string"
      },
      "labels": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "locked": {
        "type": "integer"
      },
      "merge_request_type": {
        "type": "string"
      },
      "mergeable": {
        "type": "integer"
      },
      "merged_at": {
        "type": "string"
      },
      "notes": {
        "type": "integer"
      },
      "number": {
        "type": "integer"
      },
      "patch_url": {
        "type": "string"
      },
      "pipeline_status": {
        "type": "string"
      },
      "pipeline_status_with_code_quality": {
        "type": "string"
      },
      "project_id": {
        "type": "integer"
      },
      "prune_branch": {
        "type": "integer"
      },
      "removed_lines": {
        "type": "integer"
      },
      "review_mode": {
        "type": "string"
      },
      "source_branch": {
        "type": "string"
      },
      "source_git_url": {
        "type": "string"
      },
      "source_project_id": {
        "type": "integer"
      },
      "state": {
        "type": "string"
      },
      "target_branch": {
        "type": "string"
      },
      "testers": {
        "items": {
          "properties": {},
          "type": "object"
        },
        "type": "array"
      },
      "testers_number": {
        "type": "integer"
      },
      "title": {
        "type": "string"
      },
      "updated_at": {
        "type": "string"
      },
      "url": {
        "type": "string"
      },
      "user": {
        "properties": {
          "email": {
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
          "name_cn": {
            "type": "string"
          },
          "state": {
            "type": "string"
          }
        },
        "type": "object"
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
      "added_lines": 2,
      "assignees": [],
      "assignees_number": 0,
      "base": {
        "label": "abc",
        "ref": "abc",
        "repo": {
          "assigner": {
            "email": "malongge5@noreply.gitcode.com",
            "html_url": "https://test.gitcode.net/malongge5",
            "id": "6638af02bbeee41d0fe74c35",
            "login": "malongge5",
            "name": "malongge5",
            "name_cn": "",
            "state": "active"
          },
          "description": "my test code repository",
          "full_name": "owner-test/wonderful1",
          "full_path": "owner-test/wonderful1",
          "html_url": "https://test.gitcode.net/owner-test/wonderful1.git",
          "human_name": "test / wonderful1",
          "id": 686738,
          "internal": false,
          "name": "wonderful1",
          "owner": {
            "email": "malongge5@noreply.gitcode.com",
            "html_url": "https://test.gitcode.net/malongge5",
            "id": "6638af02bbeee41d0fe74c35",
            "login": "malongge5",
            "name": "malongge5",
            "name_cn": "",
            "state": "active"
          },
          "path": "wonderful1"
        },
        "sha": "44a8d3e1142468ab2db0fa8c3402a71ccf891572",
        "user": {
          "email": "malongge5@noreply.gitcode.com",
          "html_url": "https://test.gitcode.net/malongge5",
          "id": "6638af02bbeee41d0fe74c35",
          "login": "malongge5",
          "name": "malongge5",
          "name_cn": "",
          "state": "active"
        }
      },
      "body": "update: Update file README.md",
      "can_merge_check": true,
      "close_related_issue": 0,
      "closed_at": "",
      "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/comments",
      "commits_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/commits",
      "created_at": "2024-11-23T20:51:32+08:00",
      "diff_refs": {
        "base_sha": "91a8edc0db6889fc7309d3306da7b12113e4a73f",
        "head_sha": "9931ba43e2c485741192d8e9a0b698fed79100f9",
        "start_sha": "91a8edc0db6889fc7309d3306da7b12113e4a73f"
      },
      "diff_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1.diff",
      "draft": false,
      "force_remove_source_branch": false,
      "head": {
        "label": "wonderful1-patch-1",
        "ref": "wonderful1-patch-1",
        "repo": {
          "assigner": {
            "email": "malongge5@noreply.gitcode.com",
            "html_url": "https://test.gitcode.net/malongge5",
            "id": "6638af02bbeee41d0fe74c35",
            "login": "malongge5",
            "name": "malongge5",
            "name_cn": "",
            "state": "active"
          },
          "description": "my test code repository",
          "full_name": "owner-test/wonderful1",
          "full_path": "owner-test/wonderful1",
          "html_url": "https://test.gitcode.net/owner-test/wonderful1.git",
          "human_name": "test / wonderful1",
          "id": 686738,
          "internal": false,
          "name": "wonderful1",
          "owner": {
            "email": "malongge5@noreply.gitcode.com",
            "html_url": "https://test.gitcode.net/malongge5",
            "id": "6638af02bbeee41d0fe74c35",
            "login": "malongge5",
            "name": "malongge5",
            "name_cn": "",
            "state": "active"
          },
          "path": "wonderful1"
        },
        "sha": "9931ba43e2c485741192d8e9a0b698fed79100f9",
        "user": {
          "email": "malongge5@noreply.gitcode.com",
          "html_url": "https://test.gitcode.net/malongge5",
          "id": "6638af02bbeee41d0fe74c35",
          "login": "malongge5",
          "name": "malongge5",
          "name_cn": "",
          "state": "active"
        }
      },
      "html_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1",
      "id": 191980,
      "iid": 1,
      "issue_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/issues",
      "labels": [],
      "locked": false,
      "merge_request_type": "MergeRequest",
      "mergeable": true,
      "merged_at": "2024-11-25T20:40:19+08:00",
      "notes": 0,
      "number": 1,
      "patch_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1.patch",
      "pipeline_status": "",
      "pipeline_status_with_code_quality": "",
      "project_id": 686738,
      "prune_branch": false,
      "removed_lines": 2,
      "review_mode": "approval",
      "source_branch": "wonderful1-patch-1",
      "source_git_url": "ssh://git@test.gitcode.net:2222/owner-test/wonderful1.git",
      "source_project_id": 686738,
      "state": "merged",
      "target_branch": "abc",
      "testers": [],
      "testers_number": 0,
      "title": "hhhh",
      "updated_at": "2024-12-13T16:16:54+08:00",
      "url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1",
      "user": {
        "email": "",
        "html_url": "https://test.gitcode.net/csdn_fenglh",
        "id": "654c61e5560ed95fd216cf31",
        "login": "csdn_fenglh",
        "name": "fenglh",
        "name_cn": "",
        "state": "active"
      },
      "web_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1"
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
  "operationId": "get_api_v5_enterprises_{enterprise}_issues_{number}_pull_requests",
  "parameters": [
    {
      "description": "org(path/login)",
      "example": "",
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "issue Global ID",
      "example": 0,
      "in": "path",
      "name": "number",
      "required": true,
      "schema": {
        "type": "integer"
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
  "path": "/api/v5/enterprises/{enterprise}/issues/{number}/pull_requests",
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
    "name": "Get Enterprise Issue Associated Pull Requests",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "enterprises",
        ":enterprise",
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
        }
      ],
      "variable": [
        {
          "description": {
            "content": "(Required) org(path/login)",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) issue Global ID",
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
          "examples": {
            "1": {
              "summary": "Successful Example",
              "value": {
                "added_lines": 2,
                "assignees": [],
                "assignees_number": 0,
                "base": {
                  "label": "abc",
                  "ref": "abc",
                  "repo": {
                    "assigner": {
                      "email": "malongge5@noreply.gitcode.com",
                      "html_url": "https://test.gitcode.net/malongge5",
                      "id": "6638af02bbeee41d0fe74c35",
                      "login": "malongge5",
                      "name": "malongge5",
                      "name_cn": "",
                      "state": "active"
                    },
                    "description": "my test code repository",
                    "full_name": "owner-test/wonderful1",
                    "full_path": "owner-test/wonderful1",
                    "html_url": "https://test.gitcode.net/owner-test/wonderful1.git",
                    "human_name": "test / wonderful1",
                    "id": 686738,
                    "internal": false,
                    "name": "wonderful1",
                    "owner": {
                      "email": "malongge5@noreply.gitcode.com",
                      "html_url": "https://test.gitcode.net/malongge5",
                      "id": "6638af02bbeee41d0fe74c35",
                      "login": "malongge5",
                      "name": "malongge5",
                      "name_cn": "",
                      "state": "active"
                    },
                    "path": "wonderful1"
                  },
                  "sha": "44a8d3e1142468ab2db0fa8c3402a71ccf891572",
                  "user": {
                    "email": "malongge5@noreply.gitcode.com",
                    "html_url": "https://test.gitcode.net/malongge5",
                    "id": "6638af02bbeee41d0fe74c35",
                    "login": "malongge5",
                    "name": "malongge5",
                    "name_cn": "",
                    "state": "active"
                  }
                },
                "body": "update: Update file README.md",
                "can_merge_check": true,
                "close_related_issue": 0,
                "closed_at": "",
                "comments_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/comments",
                "commits_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/commits",
                "created_at": "2024-11-23T20:51:32+08:00",
                "diff_refs": {
                  "base_sha": "91a8edc0db6889fc7309d3306da7b12113e4a73f",
                  "head_sha": "9931ba43e2c485741192d8e9a0b698fed79100f9",
                  "start_sha": "91a8edc0db6889fc7309d3306da7b12113e4a73f"
                },
                "diff_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1.diff",
                "draft": false,
                "force_remove_source_branch": false,
                "head": {
                  "label": "wonderful1-patch-1",
                  "ref": "wonderful1-patch-1",
                  "repo": {
                    "assigner": {
                      "email": "malongge5@noreply.gitcode.com",
                      "html_url": "https://test.gitcode.net/malongge5",
                      "id": "6638af02bbeee41d0fe74c35",
                      "login": "malongge5",
                      "name": "malongge5",
                      "name_cn": "",
                      "state": "active"
                    },
                    "description": "my test code repository",
                    "full_name": "owner-test/wonderful1",
                    "full_path": "owner-test/wonderful1",
                    "html_url": "https://test.gitcode.net/owner-test/wonderful1.git",
                    "human_name": "test / wonderful1",
                    "id": 686738,
                    "internal": false,
                    "name": "wonderful1",
                    "owner": {
                      "email": "malongge5@noreply.gitcode.com",
                      "html_url": "https://test.gitcode.net/malongge5",
                      "id": "6638af02bbeee41d0fe74c35",
                      "login": "malongge5",
                      "name": "malongge5",
                      "name_cn": "",
                      "state": "active"
                    },
                    "path": "wonderful1"
                  },
                  "sha": "9931ba43e2c485741192d8e9a0b698fed79100f9",
                  "user": {
                    "email": "malongge5@noreply.gitcode.com",
                    "html_url": "https://test.gitcode.net/malongge5",
                    "id": "6638af02bbeee41d0fe74c35",
                    "login": "malongge5",
                    "name": "malongge5",
                    "name_cn": "",
                    "state": "active"
                  }
                },
                "html_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1",
                "id": 191980,
                "iid": 1,
                "issue_url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1/issues",
                "labels": [],
                "locked": false,
                "merge_request_type": "MergeRequest",
                "mergeable": true,
                "merged_at": "2024-11-25T20:40:19+08:00",
                "notes": 0,
                "number": 1,
                "patch_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1.patch",
                "pipeline_status": "",
                "pipeline_status_with_code_quality": "",
                "project_id": 686738,
                "prune_branch": false,
                "removed_lines": 2,
                "review_mode": "approval",
                "source_branch": "wonderful1-patch-1",
                "source_git_url": "ssh://git@test.gitcode.net:2222/owner-test/wonderful1.git",
                "source_project_id": 686738,
                "state": "merged",
                "target_branch": "abc",
                "testers": [],
                "testers_number": 0,
                "title": "hhhh",
                "updated_at": "2024-12-13T16:16:54+08:00",
                "url": "https://test.gitcode.net/api/v5/repos/owner-test/wonderful1/pulls/1",
                "user": {
                  "email": "",
                  "html_url": "https://test.gitcode.net/csdn_fenglh",
                  "id": "654c61e5560ed95fd216cf31",
                  "login": "csdn_fenglh",
                  "name": "fenglh",
                  "name_cn": "",
                  "state": "active"
                },
                "web_url": "https://test.gitcode.net/owner-test/wonderful1/merge_requests/1"
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "added_lines": {
                  "type": "integer"
                },
                "assignees": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "assignees_number": {
                  "type": "integer"
                },
                "base": {
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
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
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "user": {
                      "properties": {
                        "email": {
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
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "type": "object"
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
                "close_related_issue": {
                  "type": "integer"
                },
                "closed_at": {
                  "type": "string"
                },
                "comments_url": {
                  "type": "string"
                },
                "commits_url": {
                  "type": "string"
                },
                "created_at": {
                  "type": "string"
                },
                "diff_refs": {
                  "properties": {
                    "base_sha": {
                      "type": "string"
                    },
                    "head_sha": {
                      "type": "string"
                    },
                    "start_sha": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "diff_url": {
                  "type": "string"
                },
                "draft": {
                  "type": "integer"
                },
                "force_remove_source_branch": {
                  "type": "integer"
                },
                "head": {
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "ref": {
                      "type": "string"
                    },
                    "repo": {
                      "properties": {
                        "assigner": {
                          "properties": {
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "description": {
                          "type": "string"
                        },
                        "full_name": {
                          "type": "string"
                        },
                        "full_path": {
                          "type": "string"
                        },
                        "html_url": {
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
                        "name": {
                          "type": "string"
                        },
                        "owner": {
                          "properties": {
                            "email": {
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
                            "name_cn": {
                              "type": "string"
                            },
                            "state": {
                              "type": "string"
                            }
                          },
                          "type": "object"
                        },
                        "path": {
                          "type": "string"
                        }
                      },
                      "type": "object"
                    },
                    "sha": {
                      "type": "string"
                    },
                    "user": {
                      "properties": {
                        "email": {
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
                        "name_cn": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "type": "object"
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
                "iid": {
                  "type": "integer"
                },
                "issue_url": {
                  "type": "string"
                },
                "labels": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "locked": {
                  "type": "integer"
                },
                "merge_request_type": {
                  "type": "string"
                },
                "mergeable": {
                  "type": "integer"
                },
                "merged_at": {
                  "type": "string"
                },
                "notes": {
                  "type": "integer"
                },
                "number": {
                  "type": "integer"
                },
                "patch_url": {
                  "type": "string"
                },
                "pipeline_status": {
                  "type": "string"
                },
                "pipeline_status_with_code_quality": {
                  "type": "string"
                },
                "project_id": {
                  "type": "integer"
                },
                "prune_branch": {
                  "type": "integer"
                },
                "removed_lines": {
                  "type": "integer"
                },
                "review_mode": {
                  "type": "string"
                },
                "source_branch": {
                  "type": "string"
                },
                "source_git_url": {
                  "type": "string"
                },
                "source_project_id": {
                  "type": "integer"
                },
                "state": {
                  "type": "string"
                },
                "target_branch": {
                  "type": "string"
                },
                "testers": {
                  "items": {
                    "properties": {},
                    "type": "object"
                  },
                  "type": "array"
                },
                "testers_number": {
                  "type": "integer"
                },
                "title": {
                  "type": "string"
                },
                "updated_at": {
                  "type": "string"
                },
                "url": {
                  "type": "string"
                },
                "user": {
                  "properties": {
                    "email": {
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
                    "name_cn": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    }
                  },
                  "type": "object"
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
    "Pull Requests"
  ]
}
```
