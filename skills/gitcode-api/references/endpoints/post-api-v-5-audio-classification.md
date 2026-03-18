# Audio Classification
Source: [https://docs.gitcode.com/en/docs/apis/post-api-v-5-audio-classification](https://docs.gitcode.com/en/docs/apis/post-api-v-5-audio-classification)
Category: AI hub
- Method: `POST`
- Path: `/api/v5/audio/classification`
- Operation ID: `post-api-v-5-audio-classification`
- Tags: None
- Deprecated: `false`
## Parameters
| Name | In | Required | Type | Description |
| --- | --- | --- | --- | --- |
| model | query | true | string | Model Name, default is audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim |
| Authorization | header | true | string | User Personal Token |
## Request Body
#### `multipart/form-data`
Schema:
```json
{
  "properties": {
    "file": {
      "description": "Audio file (support mp3, wav)",
      "format": "binary",
      "type": "string"
    }
  },
  "required": [
    "file"
  ],
  "type": "object"
}
```
## Responses
### `200`
Headers:
```json
{}
```
#### `application/json`
Schema:
```json
{
  "properties": {
    "emotionItems": {
      "description": "Emotion Classification Result List (Formatted)",
      "items": {
        "description": "Emotion Classification Item (Formatted)",
        "properties": {
          "label": {
            "description": "Category Name",
            "example": "Excitement level",
            "type": "string"
          },
          "labelEn": {
            "description": "Category Name (English)",
            "example": "Arousal",
            "type": "string"
          },
          "value": {
            "description": "Numbers",
            "example": "0.6820112466812134",
            "type": "string"
          },
          "valueDesc": {
            "description": "Numerical Description",
            "example": "Excited",
            "type": "string"
          },
          "valueDescEn": {
            "description": "Numerical Description (English)",
            "example": "slightly excited",
            "type": "string"
          }
        },
        "type": "object"
      },
      "type": "array"
    },
    "emotion_class": {
      "properties": {
        "arousal": {
          "description": "Arousal Score (Emotional Activation Level: e.g., Excited/Calm)",
          "type": "number"
        },
        "dominance": {
          "description": "Dominance Score (Emotional Control: e.g., Dominant/Submissive)",
          "type": "number"
        },
        "valence": {
          "description": "Potency Score (Emotional Valence: e.g., Pleasant/Unpleasant)",
          "type": "number"
        }
      },
      "type": "object"
    },
    "vector": {
      "description": "Vector representation of audio files",
      "type": "number"
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
      "emotion_class": {
        "arousal": 0.38037118315696716,
        "dominance": 0.4589272439479828,
        "valence": 0.5078083276748657
      },
      "emotion_items": [
        {
          "label": "Excitement level",
          "label_en": "Arousal",
          "value": "0.38037118315696716",
          "value_desc": "Calmed",
          "value_desc_en": "Calm"
        },
        {
          "label": "Emotion Polarity",
          "label_en": "Valence",
          "value": "0.5078083276748657",
          "value_desc": "Neutral",
          "value_desc_en": "Neutral"
        },
        {
          "label": "Control sense",
          "label_en": "Dominance",
          "value": "0.4589272439479828",
          "value_desc": "Neutral",
          "value_desc_en": "Medium Control"
        }
      ],
      "vector": null
    }
  },
  "2": {
    "summary": "Successful Example",
    "value": {
      "emotionItems": [
        {
          "label": "",
          "labelEn": "",
          "value": "",
          "valueDesc": "",
          "valueDescEn": ""
        }
      ]
    }
  }
}
```
## Raw OpenAPI Operation
```json
{
  "deprecated": false,
  "description": "Emotion classification and recognition of audio files",
  "info": {
    "description": "",
    "title": "GicodeOpenAPI",
    "version": "1.0.0"
  },
  "method": "post",
  "operationId": "post-api-v-5-audio-classification",
  "parameters": [
    {
      "description": "Model Name, default is audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim",
      "in": "query",
      "name": "model",
      "required": true,
      "schema": {
        "type": "string"
      }
    },
    {
      "description": "User Personal Token",
      "example": "",
      "in": "header",
      "name": "Authorization",
      "required": true,
      "schema": {
        "type": "string"
      }
    }
  ],
  "path": "/api/v5/audio/classification",
  "postman": {
    "body": {
      "formdata": [],
      "mode": "formdata"
    },
    "description": {
      "content": "Emotion classification and recognition of audio files",
      "type": "text/plain"
    },
    "header": [
      {
        "key": "Content-Type",
        "value": "multipart/form-data"
      },
      {
        "key": "Accept",
        "value": "application/json"
      }
    ],
    "method": "POST",
    "name": "Audio Classification",
    "url": {
      "host": [
        "{{baseUrl}}"
      ],
      "path": [
        "api",
        "v5",
        "audio",
        "classification"
      ],
      "query": [
        {
          "description": {
            "content": "(Required) Model Name, default is audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim",
            "type": "text/plain"
          },
          "disabled": false,
          "key": "model",
          "value": ""
        }
      ],
      "variable": []
    }
  },
  "requestBody": {
    "content": {
      "multipart/form-data": {
        "schema": {
          "properties": {
            "file": {
              "description": "Audio file (support mp3, wav)",
              "format": "binary",
              "type": "string"
            }
          },
          "required": [
            "file"
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
                "emotion_class": {
                  "arousal": 0.38037118315696716,
                  "dominance": 0.4589272439479828,
                  "valence": 0.5078083276748657
                },
                "emotion_items": [
                  {
                    "label": "Excitement level",
                    "label_en": "Arousal",
                    "value": "0.38037118315696716",
                    "value_desc": "Calmed",
                    "value_desc_en": "Calm"
                  },
                  {
                    "label": "Emotion Polarity",
                    "label_en": "Valence",
                    "value": "0.5078083276748657",
                    "value_desc": "Neutral",
                    "value_desc_en": "Neutral"
                  },
                  {
                    "label": "Control sense",
                    "label_en": "Dominance",
                    "value": "0.4589272439479828",
                    "value_desc": "Neutral",
                    "value_desc_en": "Medium Control"
                  }
                ],
                "vector": null
              }
            },
            "2": {
              "summary": "Successful Example",
              "value": {
                "emotionItems": [
                  {
                    "label": "",
                    "labelEn": "",
                    "value": "",
                    "valueDesc": "",
                    "valueDescEn": ""
                  }
                ]
              }
            }
          },
          "schema": {
            "properties": {
              "emotionItems": {
                "description": "Emotion Classification Result List (Formatted)",
                "items": {
                  "description": "Emotion Classification Item (Formatted)",
                  "properties": {
                    "label": {
                      "description": "Category Name",
                      "example": "Excitement level",
                      "type": "string"
                    },
                    "labelEn": {
                      "description": "Category Name (English)",
                      "example": "Arousal",
                      "type": "string"
                    },
                    "value": {
                      "description": "Numbers",
                      "example": "0.6820112466812134",
                      "type": "string"
                    },
                    "valueDesc": {
                      "description": "Numerical Description",
                      "example": "Excited",
                      "type": "string"
                    },
                    "valueDescEn": {
                      "description": "Numerical Description (English)",
                      "example": "slightly excited",
                      "type": "string"
                    }
                  },
                  "type": "object"
                },
                "type": "array"
              },
              "emotion_class": {
                "properties": {
                  "arousal": {
                    "description": "Arousal Score (Emotional Activation Level: e.g., Excited/Calm)",
                    "type": "number"
                  },
                  "dominance": {
                    "description": "Dominance Score (Emotional Control: e.g., Dominant/Submissive)",
                    "type": "number"
                  },
                  "valence": {
                    "description": "Potency Score (Emotional Valence: e.g., Pleasant/Unpleasant)",
                    "type": "number"
                  }
                },
                "type": "object"
              },
              "vector": {
                "description": "Vector representation of audio files",
                "type": "number"
              }
            },
            "type": "object"
          }
        }
      },
      "description": "",
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
