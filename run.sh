#!/bin/bash
source venv/bin/activate

# Usage: ./run.sh <url> [-p <path>] [-n] [-v]
function usage() {
	echo "Usage: $0 <url> [-p <path>] [-n] [-v]"
	echo "  <url>         YouTube video or playlist URL (required)"
	echo "  -p <path>     Optional subfolder path under downloads/"
	echo "  -n            Normalize audio volume"
	echo "  -v            Enable verbose logging"
	exit 1
}

if [ $# -lt 1 ]; then
	usage
fi

URL=""
EXTRA_PATH=""
NORMALIZE=""
VERBOSE=""

while [[ $# -gt 0 ]]; do
	key="$1"
	case $key in
		-p|--path)
			EXTRA_PATH="$2"
			shift # past argument
			shift # past value
			;;
		-n|--normalize)
			NORMALIZE="-n"
			shift # past argument
			;;
		-v|--verbose)
			VERBOSE="-v"
			shift # past argument
			;;
		-h|--help)
			usage
			;;
		*)
			if [ -z "$URL" ]; then
				URL="$1"
				shift # past argument
			else
				echo "Unknown argument: $1"
				usage
			fi
			;;
	esac
done

if [ -z "$URL" ]; then
	usage
fi

python main.py "$URL" ${EXTRA_PATH:+-p "$EXTRA_PATH"} $NORMALIZE $VERBOSE