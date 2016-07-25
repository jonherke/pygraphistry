#!/bin/sh -xe
C1=graphistry/nginx-central-vizservers:1.1.0.32
C2=graphistry/nginx-central-vizservers:1.1.0.32.httponly
C3=graphistry/splunkfwd:6.4.1
C4=graphistry/central-and-vizservers:$1
C5=mongo:2
for i in    $C1 $C2 $C3 $C4 $C5 ; do (docker rmi $i || true) ; docker pull $i ; done
docker save $C1 $C2 $C3 $C4 $C5 | gzip -c6 > containers.lxc.gz
for i in    $C1 $C2 $C3 $C4 $C5 ; do docker rmi $i ; done
sed -i -e 's_$1_'$1'_' launch.sh
cp ../documentation/certs.txt .
tar -cvzf tmp.tar.gz instructions.txt certs.txt containers.lxc.gz load.sh launch.sh
SUFFIX=`sha1sum tmp.tar.gz | cut -d ' ' -f 1`
TARBALL=graphistry-release-${2}-${SUFFIX}.tar.gz
mv tmp.tar.gz ${TARBALL}
s3cmd -c /home/ubuntu/.s3cfg put ${TARBALL} s3://graphistry.releases/
