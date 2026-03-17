# Delete Enterprise milestones
Source: [https://docs.gitcode.com/en/docs/apis/delete-api-v-8-enterprise-enterprise-id-milestones-milestone-id](https://docs.gitcode.com/en/docs/apis/delete-api-v-8-enterprise-enterprise-id-milestones-milestone-id)
Category: Enterprise
- Method: `DELETE`
- Path: `/api/v8/enterprises/{enterprise}/milestones/{milestone_id}`
- Operation ID: `delete_api_v8_enterprise_{enterprise_id}_milestones_{milestone_id}`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| enterprise | path | true | string | Enterprise ID |
| milestone_id | path | true | string | Milestone ID |
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
#### `*/*`
Schema:
```json
{}
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
  "method": "delete",
  "operationId": "delete_api_v8_enterprise_{enterprise_id}_milestones_{milestone_id}",
  "parameters": [
    {
      "description": "Enterprise ID",
      "in": "path",
      "name": "enterprise",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "Milestone ID",
      "in": "path",
      "name": "milestone_id",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User authorization code",
      "example": "",
      "in": "query",
      "name": "access_token",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v8/enterprises/{enterprise}/milestones/{milestone_id}",
  "postman": {
    "description": {
      "content": "",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Accept",
        "value": "*/*"
      }
    ],
    "method": "DELETE",
    "name": "Delete Enterprise milestones",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v8",
        "enterprises",
        ":enterprise",
        "milestones",
        ":milestone_id"
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
            "content": "(Required) Enterprise ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "enterprise",
          "type": "any",
          "value": ""
        },
        {
          "description": {
            "content": "(Required) Milestone ID",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "milestone_id",
          "type": "any",
          "value": ""
        }
      ]
    }
  },
  "responses": {
    "200": {
      "content": {
        "*/*": {
          "schema": {}
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
  "tags": []
}
```
