"""Utility functions for optional AWS S3 integration."""

import logging
import boto3
import os
from pathlib import Path

logger = logging.getLogger(__name__)


def download_from_s3(bucket: str, key: str, local_path: Path) -> None:
    """Download file from S3 (placeholder for cloud skills).

    Args:
        bucket: S3 bucket name
        key: S3 object key
        local_path: Local file path to save
    """
    if not all([os.getenv("AWS_ACCESS_KEY_ID"), os.getenv("AWS_SECRET_ACCESS_KEY")]):
        logger.info("AWS credentials not set, using local data")
        return
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION", "us-east-1"),
        )
        local_path.parent.mkdir(parents=True, exist_ok=True)
        s3.download_file(bucket, key, str(local_path))
        logger.info(f"Downloaded {key} from S3 bucket {bucket} to {local_path}")
    except Exception as e:
        logger.error(f"S3 download failed: {e}")
