# Pull Request Commit File List
Source: [https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-files](https://docs.gitcode.com/en/docs/apis/get-api-v-5-repos-owner-repo-pulls-number-files)
Category: Pull Requests
- Method: `GET`
- Path: `/api/v5/repos/{owner}/{repo}/pulls/{number}/files`
- Operation ID: `get_api_v5_repos_{owner}_{repo}_pulls_{number}_files`
- Tags: `Pull Requests`
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| owner | path | true | string | Repository space address (organization or individual's address path) |
| repo | path | true | string | Repository path (path) |
| number | path | true | integer | The ordinal number of the PR in this repository, i.e., which PR it is. |
| access_token | query | true | string | User authorization code |
## Request Body
No request body.
## Responses
### `200`
Successful Response
Headers:
```json
{
  "total_added_lines": {
    "description": "",
    "required": false,
    "schema": {
      "type": "string"
    }
  },
  "total_removed_lines": {
    "description": "",
    "required": false,
    "schema": {
      "type": "string"
    }
  }
}
```
#### `application/json`
Schema:
```json
{
  "items": {
    "properties": {
      "additions": {
        "type": "string"
      },
      "blob_url": {
        "type": "string"
      },
      "deletions": {
        "type": "string"
      },
      "filename": {
        "type": "string"
      },
      "patch": {
        "properties": {
          "a_mode": {
            "type": "string"
          },
          "added_lines": {
            "type": "integer"
          },
          "b_mode": {
            "type": "string"
          },
          "deleted_file": {
            "type": "integer"
          },
          "diff": {
            "type": "string"
          },
          "new_file": {
            "type": "integer"
          },
          "new_path": {
            "type": "string"
          },
          "old_path": {
            "type": "string"
          },
          "removed_lines": {
            "type": "integer"
          },
          "renamed_file": {
            "type": "integer"
          },
          "too_large": {
            "type": "integer"
          }
        },
        "type": "object"
      },
      "raw_url": {
        "type": "string"
      },
      "sha": {
        "type": "string"
      },
      "source_branch": {
        "description": "Source branch",
        "type": "string"
      },
      "source_project": {
        "description": "Source Repository",
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "path": {
            "type": "string"
          }
        },
        "required": [
          "human_name",
          "path"
        ],
        "type": "object"
      },
      "status": {
        "type": "string"
      },
      "target_branch": {
        "description": "Target branch",
        "type": "string"
      },
      "target_project": {
        "description": "Target Repository",
        "properties": {
          "full_name": {
            "type": "string"
          },
          "human_name": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "path": {
            "type": "string"
          }
        },
        "type": "object"
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
      "additions": "3",
      "blob_url": "https://ra w.gitcode.com/zzero/demo/blob/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/README.md",
      "deletions": "1",
      "filename": "README.md",
      "patch": {
        "a_mode": "100644",
        "b_mode": "100644",
        "deleted_file": false,
        "diff": "@@ -13,4 +13,6 @@ demo\n \n > covid_19 A simulation animation of an infectious population outbreak\n \n-> leetcode Algorithm solutions\n\\ No newline at end of file\n>+> leetcode Algorithm solutions\n+\n>+> juc package test\n\\ No newline at end of file",
        "new_file": false,
        "new_path": "README.md",
        "old_path": "README.md",
        "renamed_file": false,
        "too_large": false
      },
      "raw_url": "https://ra w.gitcode.com/zzero/demo/raw/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/README.md",
      "sha": "45e1211262a0ed24eeb85ac37f7776259ef0e7e1",
      "status": null
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "additions": "3",
      "blob_url": "https://ra w.gitcode.com/zzero/demo/blob/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
      "deletions": "0",
      "filename": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
      "patch": {
        "a_mode": "100644",
        "b_mode": "100644",
        "deleted_file": false,
        "diff": "@@ -15,6 +15,9 @@ public class VolatileDemo {\n         System.out.println(\"service end\");\n     }\n\n+    /**\n+     * Test method entry\n+     */\n     public static void main(String[] args) throws InterruptedException {\n         VolatileDemo v = new VolatileDemo();\n         new Thread(v::service, \"thread-1\").start();",
        "new_file": false,
        "new_path": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
        "old_path": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
        "renamed_file": false,
        "too_large": false
      },
      "raw_url": "https://ra w.gitcode.com/zzero/demo/raw/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
      "sha": "45e1211262a0ed24eeb85ac37f7776259ef0e7e1",
      "status": null
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
  "operationId": "get_api_v5_repos_{owner}_{repo}_pulls_{number}_files",
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
      "description": "The ordinal number of the PR in this repository, i.e., which PR it is.",
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
  "path": "/api/v5/repos/{owner}/{repo}/pulls/{number}/files",
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
    "name": "Pull Request Commit File List",
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
        "pulls",
        ":number",
        "files"
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
            "content": "(Required) The ordinal number of the PR in this repository, i.e., which PR it is.",
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
                "additions": "3",
                "blob_url": "https://ra w.gitcode.com/zzero/demo/blob/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/README.md",
                "deletions": "1",
                "filename": "README.md",
                "patch": {
                  "a_mode": "100644",
                  "b_mode": "100644",
                  "deleted_file": false,
                  "diff": "@@ -13,4 +13,6 @@ demo\n \n > covid_19 A simulation animation of an infectious population outbreak\n \n-> leetcode Algorithm solutions\n\\ No newline at end of file\n>+> leetcode Algorithm solutions\n+\n>+> juc package test\n\\ No newline at end of file",
                  "new_file": false,
                  "new_path": "README.md",
                  "old_path": "README.md",
                  "renamed_file": false,
                  "too_large": false
                },
                "raw_url": "https://ra w.gitcode.com/zzero/demo/raw/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/README.md",
                "sha": "45e1211262a0ed24eeb85ac37f7776259ef0e7e1",
                "status": null
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "additions": "3",
                "blob_url": "https://ra w.gitcode.com/zzero/demo/blob/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
                "deletions": "0",
                "filename": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
                "patch": {
                  "a_mode": "100644",
                  "b_mode": "100644",
                  "deleted_file": false,
                  "diff": "@@ -15,6 +15,9 @@ public class VolatileDemo {\n         System.out.println(\"service end\");\n     }\n\n+    /**\n+     * Test method entry\n+     */\n     public static void main(String[] args) throws InterruptedException {\n         VolatileDemo v = new VolatileDemo();\n         new Thread(v::service, \"thread-1\").start();",
                  "new_file": false,
                  "new_path": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
                  "old_path": "src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
                  "renamed_file": false,
                  "too_large": false
                },
                "raw_url": "https://ra w.gitcode.com/zzero/demo/raw/45e1211262a0ed24eeb85ac37f7776259ef0e7e1/src/main/java/com/zhzh/sc/demo/juc/lock/VolatileDemo.java",
                "sha": "45e1211262a0ed24eeb85ac37f7776259ef0e7e1",
                "status": null
              }
            }
          },
          "schema": {
            "items": {
              "properties": {
                "additions": {
                  "type": "string"
                },
                "blob_url": {
                  "type": "string"
                },
                "deletions": {
                  "type": "string"
                },
                "filename": {
                  "type": "string"
                },
                "patch": {
                  "properties": {
                    "a_mode": {
                      "type": "string"
                    },
                    "added_lines": {
                      "type": "integer"
                    },
                    "b_mode": {
                      "type": "string"
                    },
                    "deleted_file": {
                      "type": "integer"
                    },
                    "diff": {
                      "type": "string"
                    },
                    "new_file": {
                      "type": "integer"
                    },
                    "new_path": {
                      "type": "string"
                    },
                    "old_path": {
                      "type": "string"
                    },
                    "removed_lines": {
                      "type": "integer"
                    },
                    "renamed_file": {
                      "type": "integer"
                    },
                    "too_large": {
                      "type": "integer"
                    }
                  },
                  "type": "object"
                },
                "raw_url": {
                  "type": "string"
                },
                "sha": {
                  "type": "string"
                },
                "source_branch": {
                  "description": "Source branch",
                  "type": "string"
                },
                "source_project": {
                  "description": "Source Repository",
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "path": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "human_name",
                    "path"
                  ],
                  "type": "object"
                },
                "status": {
                  "type": "string"
                },
                "target_branch": {
                  "description": "Target branch",
                  "type": "string"
                },
                "target_project": {
                  "description": "Target Repository",
                  "properties": {
                    "full_name": {
                      "type": "string"
                    },
                    "human_name": {
                      "type": "string"
                    },
                    "id": {
                      "type": "string"
                    },
                    "path": {
                      "type": "string"
                    }
                  },
                  "type": "object"
                }
              },
              "type": "object"
            },
            "type": "array"
          }
        }
      },
      "description": "Successful Response",
      "headers": {
        "total_added_lines": {
          "description": "",
          "required": false,
          "schema": {
            "type": "string"
          }
        },
        "total_removed_lines": {
          "description": "",
          "required": false,
          "schema": {
            "type": "string"
          }
        }
      }
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
