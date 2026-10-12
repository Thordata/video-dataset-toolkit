import argparse
import json
import sys
from pathlib import Path


PERMISSION_FIELDS = (
    "license",
    "commercial_use",
    "ai_training",
    "redistribution",
)

PERMISSION_VALUES = {
    "APPROVED",
    "NOT_PERMITTED",
    "REVIEW_REQUIRED",
    "RESTRICTED",
    "NOT_APPLICABLE",
    "METADATA_ONLY",
}


def load_manifest(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError(f"Manifest not found: {path}")
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {exc}")


def validate_manifest(manifest):
    errors = []

    if not isinstance(manifest, dict):
        return ["Top-level manifest must be an object."]

    required_fields = (
        "dataset_id",
        "version",
        "description",
        "license",
        "commercial_use",
        "ai_training",
        "redistribution",
        "records",
    )

    for field in required_fields:
        if field not in manifest:
            errors.append(f"Missing required field: {field}")

    for field in PERMISSION_FIELDS:
        value = manifest.get(field)
        if value is not None and value not in PERMISSION_VALUES:
            errors.append(
                f"{field} must be one of: "
                f"{', '.join(sorted(PERMISSION_VALUES))}"
            )

    records = manifest.get("records")
    if not isinstance(records, list):
        errors.append("records must be an array.")
        return errors

    seen_ids = set()
    required_record_fields = {
        "record_id",
        "media_path",
        "media_type",
        "rights_status",
    }

    for index, record in enumerate(records):
        prefix = f"records[{index}]"

        if not isinstance(record, dict):
            errors.append(f"{prefix} must be an object.")
            continue

        missing = required_record_fields - record.keys()
        for field in sorted(missing):
            errors.append(f"{prefix} missing required field: {field}")

        record_id = record.get("record_id")
        if record_id in seen_ids:
            errors.append(f"{prefix} has duplicate record_id: {record_id}")
        elif record_id is not None:
            seen_ids.add(record_id)

        media_type = record.get("media_type")
        if media_type is not None and media_type not in {
            "video",
            "audio",
            "image",
            "text",
            "multimodal",
        }:
            errors.append(f"{prefix}.media_type is not supported: {media_type}")

        rights_status = record.get("rights_status")
        if rights_status is not None and rights_status not in PERMISSION_VALUES:
            errors.append(
                f"{prefix}.rights_status is not one of the "
                "documented permission values."
            )

        for field in (
            "duration_seconds",
            "width",
            "height",
            "frame_rate",
        ):
            value = record.get(field)
            if value is not None:
                if not isinstance(value, (int, float)) or isinstance(value, bool):
                    errors.append(f"{prefix}.{field} must be numeric.")
                elif value < 0:
                    errors.append(f"{prefix}.{field} must not be negative.")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate a video dataset manifest."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser(
        "validate",
        help="Validate a JSON manifest.",
    )
    validate_parser.add_argument("manifest", type=Path)

    args = parser.parse_args()

    if args.command == "validate":
        try:
            manifest = load_manifest(args.manifest)
        except ValueError as exc:
            print(f"Validation failed: {exc}")
            return 1

        errors = validate_manifest(manifest)
        if errors:
            print("Validation failed:")
            for error in errors:
                print(f"- {error}")
            return 1

        print(f"Manifest is valid: {args.manifest}")
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
