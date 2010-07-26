#!/bin/zsh
BASE_DIR=/dqmdata/offline/repository/data/OnlineData
Counter=0
log(){
  echo $(date +"%F %T") \[OnlineSynchronyzer/$$\] $1
}
while [ 1 ]
do 
  if [[ $Counter -gt 7 ]]
  then
    Counter=0
    #log "INFO: Starting daily full tree synchronization"
    #cd $BASE_DIR/original
    #[[ $(pwd) == $BASE_DIR/original ]] && wget -q -e robots=off --mirror -np -nH --cut-dirs=5 -T120 \
    #   --ca-dir /etc/grid-security/certificates \
    #   --private-key /dqmdata/auth/proxy.pem \
    #   --certificate /dqmdata/auth/proxy.pem \
    #   https://cmsweb.cern.ch/dqm/online/data/browse/Original/ || (log "ERROR: Could not go to $BASE_DIR/original";exit)
    #cd $BASE_DIR/merged
    #[[ $(pwd) == $BASE_DIR/merged ]] && wget -q -e robots=off --mirror -np -nH --cut-dirs=5 -T120 \
    #   --ca-dir /etc/grid-security/certificates \
    #   --private-key /dqmdata/auth/proxy.pem \
    #   --certificate /dqmdata/auth/proxy.pem \
    #   https://cmsweb.cern.ch/dqm/online/data/browse/Merged/ || (log "ERROR: Could not go to $BASE_DIR/Merged";exit)
    #log "INFO: Finished daily full tree synchronization"
    continue
  fi
  Counter=$(( $Counter + 1 ))
  cd $BASE_DIR/original
  latestLocalDir=$(find $BASE_DIR/original -maxdepth 1 -type d -exec basename {} \; | sort -n | tail -n 1)
  latestDir=$(wget -O- \
    --ca-dir /etc/grid-security/certificates --private-key /dqmdata/auth/proxy.pem \
    --certificate /dqmdata/auth/proxy.pem \
    https://cmsweb.cern.ch/dqm/online/data/browse/Original/ 2>&1|
    egrep -oe "<tr><td><a.*</a>" | egrep -o "'>.*<" | egrep -o "[0-9]{5}xxxx" |sort -r | head -n 1)
  dirs=({${latestLocalDir/xxxx/}..${latestDir/xxxx/}}xxxx)
  log "INFO: Starting partial synchronization of original files"
  for d in $dirs
  do 
    log "INFO: Synchronizing  https://cmsweb.cern.ch/dqm/online/data/browse/Original/$d"
    wget -q -e robots=off --mirror -np -nH --cut-dirs=5 -T120 \
       --ca-dir /etc/grid-security/certificates \
       --private-key /dqmdata/auth/proxy.pem \
       --certificate /dqmdata/auth/proxy.pem \
       https://cmsweb.cern.ch/dqm/online/data/browse/Original/$d
  done
  log "INFO: Finished partial synchronization of original files"

  cd $BASE_DIR/merged
  latestLocalDir=$(find $BASE_DIR/merged -maxdepth 1 -type d -exec basename {} \; | sort -n | tail -n 1)
  latestDir=$(wget -O- \
    --ca-dir /etc/grid-security/certificates --private-key /dqmdata/auth/proxy.pem \
    --certificate /dqmdata/auth/proxy.pem \
    https://cmsweb.cern.ch/dqm/online/data/browse/Merged/ 2>&1|
    egrep -oe "<tr><td><a.*</a>" | egrep -o "'>.*<" | egrep -o "[0-9]{5}xxxx" |sort -r | head -n 1)
  dirs=({${latestLocalDir/xxxx/}..${latestDir/xxxx/}}xxxx)
  log "INFO: Starting partial synchronization of merged files"
  if [[ X$latestDir != X ]]
  then 
    for d in $dirs
    do
      log "INFO: Synchronizing  https://cmsweb.cern.ch/dqm/online/data/browse/Merged/$d"
      wget -q -e robots=off --mirror -np -nH --cut-dirs=5 -T120 \
         --ca-dir /etc/grid-security/certificates \
         --private-key /dqmdata/auth/proxy.pem \
         --certificate /dqmdata/auth/proxy.pem \
         https://cmsweb.cern.ch/dqm/online/data/browse/Merged/$d
    done
    log "INFO: Finished partial synchronization of merged files"
  fi
  sleep $(( 3600 * 4 ))
done
