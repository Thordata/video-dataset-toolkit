# Data Policy

This document defines the data governance requirements for the Video Dataset Toolkit.

It applies to dataset manifests, metadata examples, documentation, code examples, and any future media or dataset assets published in this repository.

## Policy Status

This document describes the repository's public data-handling requirements.

It does not grant access to any dataset, media asset, source platform, or third-party content. It does not replace legal, licensing, privacy, security, or contractual review.

## Current Repository Scope

This repository currently contains code documentation, schema documentation, and synthetic metadata-only examples.

It does not currently distribute:

- Video
- Audio
- Subtitles
- Comments
- Personal information
- Sensitive personal data
- Restricted source material
- Customer data
- Access-controlled media

## Data Publication Principles

Any future dataset, metadata collection, or sample asset must be reviewed before publication.

The maintainer must confirm:

- The data source
- The collection or acquisition method
- The authorization or rights basis
- The applicable license
- Whether commercial use is permitted
- Whether AI training and evaluation are permitted
- Whether modification and derivative use are permitted
- Whether redistribution is permitted
- Whether personal information is present
- How privacy and publicity rights are handled
- How corrections and takedown requests will be handled
- The review date and responsible reviewer

If any required item cannot be confirmed, the material must not be published as a public downloadable asset.

## Metadata-Only Publication

When source media cannot be publicly redistributed, the repository may publish permitted metadata or documentation if:

- The metadata itself may be lawfully shared
- It does not contain personal or sensitive information
- It does not expose private URLs, credentials, or access tokens
- It does not reproduce restricted subtitles, comments, or source content
- It does not claim rights that have not been verified
- The applicable access restrictions are clearly documented

Metadata publication does not grant permission to download, copy, train on, modify, or redistribute the related source media.

## License And Permitted Use

Every public dataset or media asset must have documented usage terms.

The documentation should state, where applicable:

- License name or SPDX identifier
- Commercial-use status
- AI training status
- Evaluation status
- Modification and derivative-use status
- Redistribution status
- Attribution requirements
- Notice requirements
- Geographic or platform restrictions
- Expiration or revocation conditions

The MIT License in this repository applies only to the repository's code and documentation. It does not grant rights to any third-party dataset, media, metadata, source-platform content, or derived data.

## Personal Information And Privacy

Do not publish personal information unless its lawful basis, permitted use, and publication requirements have been reviewed.

This includes, but is not limited to:

- Names linked to identifiable individuals
- Email addresses
- Telephone numbers
- Precise location information
- Faces or biometric identifiers
- Voiceprints
- Account identifiers
- Usernames linked to individuals
- Private comments or messages
- Sensitive personal information

When personal information is not necessary for the documented use case, it must be removed, redacted, anonymized, or excluded.

Anonymization must not be assumed to be effective without appropriate review.

## Audio, Subtitles, Comments, And Derived Content

Audio, subtitles, comments, descriptions, annotations, transcripts, embeddings, and other derived content may have separate rights and privacy restrictions.

Before publication, maintainers must review each content type separately.

Do not assume that permission to use a video also permits:

- Audio extraction
- Subtitle publication
- Comment publication
- Transcript publication
- Face or voice identification
- Embedding publication
- Commercial use
- AI training
- Redistribution

## Prohibited Content

Do not upload or publish:

- Unauthorized video or audio
- Copyrighted source material without confirmed rights
- Restricted subtitles, comments, transcripts, or annotations
- Personal or sensitive personal information
- Credentials, API keys, tokens, or private keys
- Private URLs or authenticated download links
- Confidential contracts or internal authorization evidence
- Customer data without documented permission
- Content obtained by bypassing access controls
- Data with unclear commercial, AI-training, or redistribution terms

## Synthetic Examples

Synthetic examples are preferred when they can demonstrate a workflow without distributing source media.

Synthetic examples must be clearly labeled and must not be presented as real-world data.

Examples should use placeholder values such as:

- `SYNTHETIC_EXAMPLE`
- `REVIEW_REQUIRED`
- `REPLACE_WITH_APPROVED_PATH`

Synthetic examples must not contain real personal information, private paths, credentials, or copied third-party content.

## Review Gate

A future public data release should pass the following review sequence:

1. Identify the source and acquisition method.
2. Confirm the rights or authorization basis.
3. Confirm the applicable license.
4. Review commercial-use permissions.
5. Review AI training and evaluation permissions.
6. Review modification and redistribution permissions.
7. Review privacy, publicity, and personal-information risks.
8. Document restrictions and attribution requirements.
9. Assign a responsible reviewer.
10. Record the review date.
11. Publish only the approved scope.
12. Monitor corrections and takedown requests.

If the review is incomplete, publish documentation, code, or synthetic examples only.

## Corrections And Takedown Requests

Requests concerning data rights, privacy, attribution, or incorrect metadata should be submitted through the repository's documented contact channel or a private security or privacy channel when sensitive details are involved.

Do not publish sensitive personal information or confidential authorization evidence in a public issue.

A maintainer should:

- Record the request
- Restrict or remove the disputed material when appropriate
- Review the relevant source and authorization records
- Correct inaccurate metadata
- Document the resolution
- Restore material only after the issue is resolved

## Maintainer Responsibilities

Maintainers are responsible for:

- Keeping data documentation accurate
- Avoiding unsupported rights or license claims
- Reviewing public examples before release
- Protecting credentials and confidential information
- Responding to valid rights and privacy concerns
- Updating this policy when the project scope changes

## Questions

For technical questions, open an issue in this repository without attaching restricted data.

For commercial data access or partnership questions, contact the [Thordata team](https://www.thordata.com/contact-us).

## Related Documents

- [Manifest Schema](manifest-schema.md)
- [Repository README](../README.md)
- [MIT License](../LICENSE)
