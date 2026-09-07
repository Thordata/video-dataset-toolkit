# Manifest Schema

This document defines the draft manifest format for the Video Dataset Toolkit.

The current schema is intended for documentation and design discussion. It does not grant access to any dataset or media asset.

## Status

Draft for the initial `0.1.0` schema.

The schema may change before the first executable toolkit release. Changes to required fields, field types, or permitted values should be documented and versioned.

## Purpose

A dataset manifest is a machine-readable description of a dataset and its records.

A manifest can describe:

- Dataset identity and version
- Data description
- License and permitted-use status
- Record identifiers
- Media locations
- Basic media properties
- Provenance and rights-review status

The manifest should describe data without embedding video, audio, subtitles, comments, or personal information.

## Top-Level Object

The top-level manifest is a JSON object.

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `dataset_id` | string | Yes | Stable identifier for the dataset |
| `version` | string | Yes | Version of the dataset manifest |
| `description` | string | Yes | Human-readable description of the dataset |
| `license` | string | Yes | License or license-review status |
| `commercial_use` | string | Yes | Commercial-use permission status |
| `ai_training` | string | Yes | AI training and evaluation permission status |
| `redistribution` | string | Yes | Redistribution permission status |
| `records` | array | Yes | List of dataset records |

## Top-Level Field Requirements

### `dataset_id`

A stable identifier for the dataset.

Requirements:

- Must be a non-empty string
- Should use lowercase letters, numbers, and hyphens
- Should not contain private customer names or confidential information
- Should remain stable across manifest revisions for the same dataset

Example:

```text
example-video-dataset
```

### `version`

The version of the dataset manifest.

Use a versioning scheme that makes changes clear. Semantic versioning is recommended for the initial implementation.

Example:

```text
0.1.0
```

### `description`

A concise description of the dataset.

The description must not claim rights, licenses, or permitted uses that have not been reviewed.

### `license`

The applicable license or current review status.

Possible values include:

- `REVIEW_REQUIRED`
- `APPROVED`
- `RESTRICTED`
- `NOT_APPLICABLE`

A production dataset should use the formal license name or SPDX identifier after review.

Examples:

```text
MIT
CC-BY-4.0
REVIEW_REQUIRED
```

The code license of this repository does not automatically apply to any dataset or media described by a manifest.

### `commercial_use`

The status of commercial-use permission.

Possible values include:

- `APPROVED`
- `NOT_PERMITTED`
- `REVIEW_REQUIRED`
- `RESTRICTED`
- `NOT_APPLICABLE`

Do not use `APPROVED` unless the applicable license or authorization has been reviewed.

### `ai_training`

The status of permission for AI training, fine-tuning, evaluation, or related use.

Possible values include:

- `APPROVED`
- `NOT_PERMITTED`
- `REVIEW_REQUIRED`
- `RESTRICTED`
- `NOT_APPLICABLE`

The value must reflect the applicable license and authorization terms.

### `redistribution`

The status of permission to redistribute the described data or media.

Possible values include:

- `APPROVED`
- `METADATA_ONLY`
- `NOT_PERMITTED`
- `REVIEW_REQUIRED`
- `RESTRICTED`
- `NOT_APPLICABLE`

Use `METADATA_ONLY` when the metadata may be shared but the source media may not be redistributed.

### `records`

An array of record objects.

Each record must have a unique `record_id` within the manifest.

An empty array is allowed for a documentation-only manifest, but a production dataset release should document why no records are included.

## Record Object

### Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `record_id` | string | Yes | Stable unique identifier for the record |
| `media_path` | string | Yes | Approved relative path or documented media reference |
| `media_type` | string | Yes | Type of media described by the record |
| `source` | string | Yes | Provenance or source status |
| `rights_status` | string | Yes | Rights-review status for the record |
| `duration_seconds` | number | No | Media duration in seconds |
| `width` | integer | No | Media width in pixels |
| `height` | integer | No | Media height in pixels |
| `frame_rate` | number | No | Media frame rate |
| `video_codec` | string | No | Video codec identifier |
| `container` | string | No | Media container format |
| `language` | string | No | Language code or `und` when unknown |

## Record Field Requirements

### `record_id`

A stable unique identifier for one dataset record.

Requirements:

- Must be a non-empty string
- Must be unique within the manifest
- Should not contain names, email addresses, or other personal information
- Should remain stable when non-semantic metadata changes

Example:

```text
example-000001
```

### `media_path`

A relative path or documented reference to the media.

Requirements:

- Must not contain credentials or access tokens
- Must not expose private filesystem paths
- Must not point to unauthorized or restricted material
- Must use a documented path convention
- Must be reviewed before publication

The example value below is intentionally a placeholder:

```text
REPLACE_WITH_APPROVED_PATH
```

### `media_type`

The type of media represented by the record.

For this initial video-focused schema, the expected value is:

```text
video
```

Additional media types require a documented schema change.

### `source`

The provenance status or source category for the record.

The value must not expose confidential contracts, private credentials, or unnecessary personal information.

The current example uses:

```text
SYNTHETIC_EXAMPLE
```

This indicates that the record is a placeholder and does not identify a real source asset.

### `rights_status`

The rights-review status for the record.

Possible values include:

- `REVIEW_REQUIRED`
- `APPROVED`
- `RESTRICTED`
- `NOT_PERMITTED`
- `METADATA_ONLY`

Do not use `APPROVED` until the source, license, commercial-use terms, AI-training terms, privacy considerations, and redistribution scope have been reviewed.

### `duration_seconds`

The media duration in seconds.

Requirements:

- Must be a number
- Must be greater than or equal to `0`
- Must not be used to imply that the media file is publicly available

### `width` and `height`

The media dimensions in pixels.

Requirements:

- Must be integers
- Must be greater than `0` when present
- Must describe the referenced media accurately

### `frame_rate`

The media frame rate.

Requirements:

- Must be a number
- Must be greater than `0` when present
- Variable frame-rate media requires additional documentation

### `video_codec`

The video codec identifier, such as:

```text
H264
```

The value should use a documented naming convention.

### `container`

The media container format, such as:

```text
MP4
```

The value should describe the actual container rather than the codec.

### `language`

The primary language code for relevant audio, text, or annotation metadata.

Use a documented language code. Use:

```text
und
```

when the language is unknown or not applicable.

## Example Manifest

The following is a metadata-only example:

```json
{
  "dataset_id": "example-video-dataset",
  "version": "0.1.0",
  "description": "Synthetic metadata-only example manifest",
  "license": "REVIEW_REQUIRED",
  "commercial_use": "REVIEW_REQUIRED",
  "ai_training": "REVIEW_REQUIRED",
  "redistribution": "REVIEW_REQUIRED",
  "records": [
    {
      "record_id": "example-000001",
      "media_path": "REPLACE_WITH_APPROVED_PATH",
      "media_type": "video",
      "duration_seconds": 30.0,
      "width": 1920,
      "height": 1080,
      "frame_rate": 30.0,
      "source": "SYNTHETIC_EXAMPLE",
      "rights_status": "REVIEW_REQUIRED"
    }
  ]
}
```

This example does not represent a real dataset and does not authorize downloading, training, modifying, or redistributing any media.

## Validation Rules

A future validator should check at least:

- The document is valid JSON
- The top-level value is an object
- All required top-level fields are present
- All required fields have the expected type
- `records` is an array
- Every record has a unique `record_id`
- Numeric media fields are non-negative
- `media_type` uses a supported value
- Rights-related fields use documented values
- No credentials or access tokens are present
- No prohibited personal information is present

## Data Protection Requirements

Do not place the following in a public manifest:

- Passwords
- API keys
- Access tokens
- Private URLs
- Private filesystem paths
- Unnecessary personal information
- Facial-recognition identifiers
- Voiceprints
- Restricted subtitles or comments
- Confidential contract details
- Unreviewed source or license claims

## Versioning

Changes to the schema should update:

- The schema version
- This document
- Example manifest files
- Validation rules
- Relevant tests

Breaking changes should use a new major version or be clearly documented before adoption.

## Related Files

- [`README.md`](../README.md)
- [`manifest.example.json`](../examples/manifest.example.json)
- [`metadata.example.json`](../examples/metadata.example.json)
- [`LICENSE`](../LICENSE)

## License

This documentation is released under the MIT License included in this repository.

The schema and code license do not grant rights to any third-party dataset, media, metadata, source platform, or derived data.
