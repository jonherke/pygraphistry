#!/bin/sh -xe
C1=graphistry/nginx-central-vizservers:1.4.0.32
C2=graphistry/nginx-central-vizservers:1.4.0.32.httponly
C3=graphistry/splunkfwd:6.4.1
C4=graphistry/central-and-vizservers:${VIZ_VERSION}
C4a=graphistry/central-and-vizservers:${VIZ_VERSION}.multicore
C5=mongo:2
C6=postgres:9-alpine
C7=graphistry/s3cmd-postgres:latest
C8=graphistry/pivot-app:${PIVOT_VERSION}
# C9=graphistry/user-service:${VIZ_VERSION}
C10=graphistry/prometheus:${VIZ_VERSION}
BUCKET=s3://graphistry-releases/
for i in    $C1 $C2 $C3 $C4 $C4a $C5 $C6 $C7 $C8 $C10; do (docker rmi $i || true) ; docker pull $i ; done
docker save $C1 $C2 $C3 $C4 $C4a $C5 $C6 $C7 $C8 $C10| pigz -b500 > containers.lxc.gz
for i in    $C1 $C2 $C3 $C4 $C4a $C5 $C6 $C7 $C8 $C10; do (docker rmi $i || true) ; done

# if no argument is passed into this script, continue as normal
# if an argument is passed, don't zip/upload - this is just for local dev.
if [ -z "$1" ]
  then
    sed -i -e 's_$1_'${VIZ_VERSION}'_' launch.sh
    sed -i -e 's_$2_'${PIVOT_VERSION}'_' launch.sh
    cp ../documentation/certs.txt .
    GZIP=-1 tar -cvzf tmp.tar.gz instructions.md certs.txt containers.lxc.gz load.sh launch.sh make-api-key.sh
    SUFFIX=`sha1sum tmp.tar.gz | cut -d ' ' -f 1`
    TARBALL=graphistry-app-${BUILD_NUMBER}-${VIZ_VERSION}-${PIVOT_VERSION}-${SUFFIX}.tar.gz
    mv tmp.tar.gz ${TARBALL}
    s3cmd -c /home/ubuntu/.s3cfg --multipart-chunk-size-mb=200 put ${TARBALL} ${BUCKET}

    echo SUCCESS. If you want to share this with your friends, give them the following link, which expires in a month and a half.

    s3cmd -c /home/ubuntu/.s3cfg signurl ${BUCKET}${TARBALL} +4000000
  else
    echo PREPROCESSING DONE, NOT UPLOADING! 
fi
