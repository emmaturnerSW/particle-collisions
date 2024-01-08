import hashlib


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Usage: {} <tag>".format(sys.argv[0]))
        sys.exit(1)


#  <token>-[<value>]__   (repeat)
#
# Recognized tokens (unrecognized tokens are ignored):
#  p       - project (e.g., "confluent-kafka-python")
#  bld     - builder (e.g., "travis")

def collect_s3(s3, min_age_days=60):
    """ Collect artifacts from S3 """
    now = datetime.now(timezone.utc)
    eligible = []
    totcnt = 0

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--delete",
                        help="WARNING! Don't just check, actually delete "
                        "S3 objects.",
                        action="store_true")
    parser.add_argument("--age", help="Minimum object age in days.",
                        type=int, default=360)
