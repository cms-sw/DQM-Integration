#! /bin/sh
#as used by wassh
HOSTS[0]={srv-c2c05-06,srv-c2c05-07,srv-c2c05-08,srv-c2c05-09}
HOSTS[1]=srv-c2d05-19
HOSTS[2]=srv-c2d05-19
HOSTS[3]=srv-c2d05-19
HOSTS[4]=srv-c2d05-19

APPS[0]="fileCollector"
APPS[1]="fileMerger"
APPS[2]="fileRegister"
APPS[3]="fileTransfer"
APPS[4]="fileTransferVerify"

ALIVECHK[0]="/nfshome0/dqmpro/filecollector/alivecheck_fileCollector.sh"
ALIVECHK[1]="/nfshome0/dqmpro/filecollector/alivecheck_fileMerger.sh"
ALIVECHK[2]="/nfshome0/dqmpro/filecollector/alivecheck_fileRegister.sh"
ALIVECHK[3]="/nfshome0/dqmpro/filecollector/alivecheck_fileTransfer.sh"
ALIVECHK[4]="/nfshome0/dqmpro/filecollector/alivecheck_fileTransferVerify.sh"

PROC_ID[0]=$(ps -eF|grep fileCollector.py | grep -v grep | awk '{print($2)}')
PROC_ID[1]=$(ps -eF|grep fileMerger.py | grep -v grep | awk '{print($2)}')
PROC_ID[2]=$(ps -eF|grep fileRegister.py | grep -v grep | awk '{print($2)}')
PROC_ID[3]=$(ps -eF|grep fileTransfer.py | grep -v grep | awk '{print($2)}')
PROC_ID[4]=$(ps -eF|grep fileTransferVerify.py | grep -v grep | awk '{print($2)}')
ACTION=""
case $1 in
  start)
    ACTION="start" ;;
  stop)
    ACTION="stop" ;;
  restart)
    ACTION="restart" ;;
  "" | *)
    echo unknown action. Please use [start,stop,restart]
    exit;;
esac
MODULE=""
case $2 in
  Collector)
    MODULE="[0]"
    ;;
  Merger)
    MODULE="[1]"
    ;;
  Register)
    MODULE="[2]"
    ;;
  Transfer)
    MODULE="[3]"
    ;;
  Verify)
    MODULE="[4]"
    ;;
  All)
    MODULE="[@]"
    ;;
  "" | *)
    echo unknown module. Please use [Collector,Merger,Register,Transfer,Verify,All]
    exit;;
esac
shopt -s nocaseglob
case $ACTION in
      start)
        if [[ $MODULE == "[@]" ]]
        then 
          service=0
        else
          service=$(eval echo "\$"$MODULE)
        fi
        for i in `eval echo \$\{HOSTS$MODULE\}`
        do 
          for j in `eval echo $i`
          do 
            if [[ $HOSTNAME =~ $j ]]
            then
              echo Running ${ALIVECHK[$service]} on LOCALHOST
              ${ALIVECHK[$service]}
            else
              echo Running ${ALIVECHK[$service]} on $j
              ssh $j ${ALIVECHK[$service]}
            fi
            echo ......................................................
          done
          service=$(( $service + 1 ))
        done
        ;;
      stop)
        if [[ $MODULE == "[@]" ]]
        then 
          service=0
        else
          service=$(eval echo "\$"$MODULE)
        fi
        for i in `eval echo \$\{HOSTS$MODULE\}`
        do 
          for j in `eval echo $i`
          do 
            if [[ $HOSTNAME =~ $j ]]
            then
              echo Stopping ${APPS[$service]} on LOCALHOST
              kill -9 ${PROC_ID[$service]}
            else
              echo Stopping ${APPS[$service]} on $j
              ssh $j "kill -9 \$(ps -eF|grep ${APPS[$service]}.py | grep -v grep | awk '{print(\$2)}')"
            fi
            echo ......................................................
          done
          service=$(( $service + 1 ))
        done
        ;;
      restart)
        if [[ $MODULE == "[@]" ]]
        then 
          service=0
        else
          service=$(eval echo "\$"$MODULE)
        fi
        for i in `eval echo \$\{HOSTS$MODULE\}`
        do 
          for j in `eval echo $i`
          do 
            if [[ $HOSTNAME =~ $j ]]
            then
              echo Stopping ${APPS[$service]} on LOCALHOST
              kill -9 ${PROC_ID[$service]}
              echo Running ${ALIVECHK[$service]} on LOCALHOST
              ${ALIVECHK[$service]}
            else
              echo Stopping ${APPS[$service]} on $j
              ssh $j "kill -9 \$(ps -eF|grep ${APPS[$service]}.py | grep -v grep | awk '{print(\$2)}')"
              echo Running ${ALIVECHK[$service]} on $j
              ssh $j ${ALIVECHK[$service]}
            fi
            echo ......................................................
          done
          service=$(( $service + 1 ))
        done
        ;;
    esac
