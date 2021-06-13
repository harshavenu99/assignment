from __future__ import print_function
import logging
import sys
import os
from runway.cfngin.session_cache import get_session


LOGGER = logging.getLogger(__name__)
LEGACY_PYTHON = sys.version_info[0] < 3


def ami(context, provider, **kwargs):
    session = get_session(provider.region)
    s3_resource = session.resource('s3')
    bucket_name = kwargs.get('s3_bucket')

    print()

    ami = s3_resource.Object(bucket_name, f"ami.txt").get()["Body"].read().decode("utf-8")
    return {'ami': ami}
