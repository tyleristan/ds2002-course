#!/bin/bash

curl https://pbs.twimg.com/media/Efd3bWaXYAA3D57.jpg:large > epiccat.jpg
aws s3 cp epiccat.jpg s3://ds2002-twg2nk
aws s3 presign --expires-in 604800  s3://ds2002-twg2nk/epiccat.jpg

presigned URL gained: https://ds2002-twg2nk.s3.us-east-1.amazonaws.com/epiccat.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA6GBMHAX5GPXXMDWJ%2F20240314%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240314T193732Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDFtw4UFACy8Su7trcCLEAUzjUBNSv66nMDGCtnpOGYM6Z2cL%2BiNCLjapEcwXDcrsAL9buK54UubB5GZPy0jE98aObyxEmKpAbEMTRaXenZ0iicAbAkO6svoLM7I7eXpjU2Rfb2anB6sB3NcCZF0yWhwtWZ8d8SYXoT%2B%2BHNdefsRfbMmob%2BhhvAGiZik%2Bg35z%2FVNGb78teuWzfQzWnA617J112Rl%2FOZHO02jtY67gVh26uPx5%2FtEHTxSQZKfT8%2F%2BAWXlkFYEfQmYdn8oM2XBGj7j5bzwovKLNrwYyLZHSQFYVP6pYFL9b8iOoCI%2BEoqt7WHJgPT2e5ebBuN97Y8sAzxc5d2hYBsQxYg%3D%3D&X-Amz-Signature=0feed524b74656a4dc481ec515833c53c4a4318d96c33f435177f46e0a54059c

