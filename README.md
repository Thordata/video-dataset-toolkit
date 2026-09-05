# Video Dataset Toolkit

Tools and documentation for inspecting, validating, documenting, and preparing video datasets for AI workflows.

## Project Status

Early development.

This repository currently defines the project's scope, data principles, manifest format, and planned technical direction. The initial implementation will focus on dataset manifests, metadata validation, media inspection, and reproducible data quality reporting.

This repository does not currently distribute video, audio, subtitles, comments, personal information, or other source media.

## Why This Project

Reliable video dataset workflows require more than media files. They also require:

- Consistent metadata
- Clear data provenance
- File and media quality checks
- Reproducible dataset splits
- License and usage documentation
- Validation before training or evaluation
- Clear separation between code, metadata, and source media

This toolkit is intended to help data and machine learning teams build documented and reproducible video dataset workflows.

## Intended Users

This project is designed for:

- Video dataset engineers
- Computer vision teams
- Vision-language and multimodal AI teams
- Embodied AI and robotics teams
- Video retrieval researchers
- Data engineering and machine learning platform teams

## Planned Capabilities

The initial roadmap includes:

- Dataset manifest validation
- Required metadata field validation
- Video file inspection
- Duration, resolution, frame rate, and codec checks
- File integrity and missing-file checks
- Dataset statistics and quality reports
- Dataset split documentation
- Provenance and license documentation
- Reproducible inspection workflows
- Automated checks through continuous integration

Features will be added incrementally after the manifest format and metadata model have been reviewed.

## Scope

The toolkit is intended to support dataset preparation and quality control before data is used for:

- Model training
- Model evaluation
- Video retrieval
- Computer vision research
- Multimodal AI workflows
- Robotics and embodied AI research
- Internal data engineering pipelines

The toolkit does not provide access to any third-party dataset or source platform.

## Non-Goals

This project does not:

- Provide unauthorized access to video platforms
- Bypass authentication, access controls, or technical restrictions
- Grant rights to third-party media or datasets
- Replace legal, licensing, privacy, or security review
- Distribute source media without confirmed redistribution rights
- Collect personal information by default
- Serve as a complete training or annotation platform

## Dataset Manifest

A dataset manifest is a structured record describing the files or records in a dataset.

A future manifest may include fields such as:

```json
{
  "dataset_id": "example-video-dataset",
  "version": "0.1.0",
  "description": "Example metadata-only dataset manifest",
  "license": "REVIEW_REQUIRED",
  "commercial_use": "REVIEW_REQUIRED",
  "ai_training": "REVIEW_REQUIRED",
  "redistribution": "REVIEW_REQUIRED",
  "records": [
    {
      "record_id": "example-000001",
      "media_path": "REPLACE_WITH_APPROVED_PATH",
      "media_type": "video",
      "duration_seconds": 0,
      "width": 0,
      "height": 0,
      "frame_rate": 0,
      "source": "REVIEW_REQUIRED",
      "rights_status": "REVIEW_REQUIRED"
    }
  ]
}
```

This is a schema illustration only. It is not a downloadable dataset. All rights-related fields must be reviewed before use.

## Metadata Principles

Metadata should be:

- Explicitly defined
- Consistent across records
- Machine-readable where possible
- Traceable to a documented source
- Separated from restricted source media
- Versioned when the schema changes
- Reviewed before publication or redistribution

Metadata must not include secrets, credentials, unnecessary personal information, or restricted content.

## Data And Rights Policy

Before any future sample asset or dataset is published, its maintainer must review and document:

- Data source
- Collection or acquisition method
- Authorization or rights basis
- Applicable license
- Commercial-use permission
- AI training and evaluation permission
- Modification and derivative-use permission
- Redistribution permission
- Privacy and personal-information considerations
- Takedown or correction contact
- Review date and responsible reviewer

If public redistribution is not permitted or cannot be confirmed, the repository should publish only permitted documentation, metadata, synthetic examples, or an access-request process.

Do not upload:

- Unauthorized video or audio
- Copyrighted source material without confirmed rights
- Subtitles, comments, or other restricted content
- Personal information or sensitive personal data
- Credentials, API keys, tokens, or private files
- Access-controlled source material
- Data whose commercial, AI-training, or redistribution terms are unclear

## Installation

Installation instructions will be added when the first executable release is available.

Until then, this repository should be treated as a documentation and project-scoping repository.

## Usage

Usage examples will be added together with the first validated implementation.

Do not use this repository as evidence that any third-party video or dataset may be downloaded, trained on, modified, or redistributed.

## Planned Repository Structure

```text
video-dataset-toolkit/
├── README.md
├── LICENSE
├── pyproject.toml
├── examples/
│   ├── manifest.example.json
│   └── metadata.example.json
├── src/
│   └── video_dataset_toolkit/
├── tests/
├── docs/
│   ├── data-policy.md
│   ├── data-quality.md
│   └── manifest-schema.md
└── .github/
    └── workflows/
```

Files will be added as the technical implementation is reviewed and developed.

## Development Roadmap

### Documentation And Schema

- [ ] Define the initial manifest schema
- [ ] Define required and optional metadata fields
- [ ] Document provenance and rights fields
- [ ] Add metadata-only examples
- [ ] Document validation rules

### Validation

- [ ] Validate manifest syntax
- [ ] Validate required fields
- [ ] Detect duplicate record identifiers
- [ ] Detect missing or invalid paths
- [ ] Validate supported metadata types
- [ ] Generate basic validation reports

### Media Inspection

- [ ] Inspect media duration
- [ ] Inspect resolution and frame rate
- [ ] Inspect codec and container information
- [ ] Detect unreadable or incomplete files
- [ ] Record inspection results without copying restricted media

### Quality And Reproducibility

- [ ] Generate dataset statistics
- [ ] Document dataset splits
- [ ] Add reproducible command examples
- [ ] Add automated tests
- [ ] Add continuous integration
- [ ] Publish the first tagged release

## Responsible Use

Use this toolkit only for lawful and authorized data workflows.

When working with video or multimedia data:

- Respect applicable laws and regulations
- Respect intellectual property rights
- Respect privacy and publicity rights
- Follow source-platform terms and access restrictions
- Confirm licensing terms before use
- Confirm AI training and evaluation permissions
- Confirm commercial-use permissions
- Confirm redistribution permissions
- Remove or restrict data that cannot be lawfully used or shared

The code license for this repository does not grant rights to any third-party media, dataset, metadata, source platform, or derived data.

## Contributing

Issues and pull requests are welcome for documentation improvements, schema discussions, validation design, and reproducible examples.

Please do not include restricted media, personal information, credentials, or confidential business information in issues, pull requests, or repository attachments.

Before contributing code or examples, make sure that all included content can be publicly shared under its applicable license.

## License

The code and documentation in this repository are released under the MIT License.

The MIT License applies only to this repository's code and documentation. It does not apply to third-party datasets, media, metadata, source-platform content, or other external materials.

See the [MIT License](LICENSE) for details.

## Thordata

For video data and multimodal data solutions, visit the [Thordata Video Data platform](https://www.thordata.com/products/multi-platform-video-datasets).

For documentation and integration resources, visit the [Thordata documentation](https://doc.thordata.com).

For commercial, data access, or partnership questions, [contact the Thordata team](https://www.thordata.com/contact-us).
