#1. 예측함수
predict.merge <- function(response){ #1행의 데이터 프레임이 와야 한다.
  now <- 1 #현재 노드 번호
  now.pred <- merged.tree[[1]][[9]] #현재 예측값
  now.stage <- 0 #현재 스테이지 번호
  repeat{
    all <- length(merged.tree) #전체 노드 수
    canbenext <- c() #현재 노드 번호를 아버지 노드로 갖는 노드 번호들
    for(i in 1:all){
      search <- merged.tree[[i]] #해당 번호의 노드 정보를 끄집어 내서
      if(now %in% search[[2]]){ #만약 노드의 아버지 노드가 현재 노드 번호라면
        if(length(search[[3]]) == 3){ #그리고 결합된 노드가 아니라면
          canbenext <- c(canbenext,i) #이를 기록해두어라
        }
      }
    }
    #이제 기록된 노드들 중 하나로 가야한다. 
    #그런데 기록된 노드들의 분할 변수와 기준은 동일할 것이다.
    split.varid <- merged.tree[[canbenext[1]]][[3]][1] #분할 변수
    split.split <- merged.tree[[canbenext[1]]][[3]][2] #분할 기준
    #이때 분할변수 번호는 데이터의 변수 순서와 동일하다.
    if(response[,as.numeric(split.varid)] < split.split){
      splitted <- "under" #분할 결과를 나타낸다.
    }else{splitted <- "upper"}
    
    #분할결과와 동일한 결과를 보여주는 자식노드로 이동시킨다.
    for(j in canbenext){
      roading <- merged.tree[[j]]
      if(roading[[3]][3] == splitted){
        now <- j #이동한 노드의 번호
        now.pred <- merged.tree[[j]][[9]] #이동한 노드의 예측값
        now.stage <- merged.tree[[j]][[8]] #이동한 stage 번호
      }else{next}
    }
    
    #만약 이동한 노드가 다른 노드와 결합한 경우 그쪽으로 이동해줘야 한다.
    if(merged.tree[[now]][[6]] == "combined"){
      for(m in 1:all){
        search.com <- merged.tree[[m]]
        if(now %in% search.com[[7]]){
          now <- m
          now.pred <- merged.tree[[m]][[9]]
          now.stage <- merged.tree[[m]][[8]]
        }
      }
    }
    if(merged.tree[[now]][[6]] == "terminal") break
  }
  now <<- now
  now.pred <<- now.pred
  now.stage <<- now.stage
}

#2. 모델생성함수
merged.tree.make <- function(data.train, number, critical.t, critical.s){
  merged.tree <- list() #전체 정보를 담을 list
  aftersplit.train <- list()
  aftersplit.train[[1]] <- 1 #노드 번호호
  aftersplit.train[[2]] <- NULL #아버지노드 정보
  aftersplit.train[[3]] <- NULL # 분할 정보
  aftersplit.train[[4]] <- data.train #training data
  aftersplit.train[[5]] <- "yes" #분할대상여부
  aftersplit.train[[6]] <- "terminal" #노드 상태 
  aftersplit.train[[7]] <- NULL #결합 대상 노드 번호
  aftersplit.train[[8]] <- 0 #스테이지 번호
  aftersplit.train[[9]] <- mean(aftersplit.train[[4]]$score)
  
  merged.tree[[1]] <- aftersplit.train #노드번호와 list 번호가 동일하다.
  
  for(m in 1:number){
    no.number <- length(merged.tree) #list에 존재하는 노드 수
    splitting <- c() #분할 대상 노드의 번호
    for(i in 1:no.number){
      d <- merged.tree[[i]] #해당 노드 번호의 노드 정보를 끄집어 내고
      if(d[[5]] == "yes"){
        splitting <- c(splitting, d[[1]]) #만약 분할대상여부가 yes라면 노드 번호를 기록하라.
      }
    }
    splitting #분할대상노드의 번호다.
    
    #(2). 분할 대상 노드 분할하고 저장하기 
    for(i in splitting){
      node.info <- merged.tree[[i]] #분할 대상 노드의 정보를 끄집어낸다.
      merged.tree[[i]][[5]] <- "no" #일단 분할 대상 노드가 되었기 때문에 yes를 no로 바꿔준다.
      d.train <- node.info[[4]] #해당 노드에 존재하는 training data를 뽑아낸다.
      if(dim(d.train)[1] <= 5) next #만약 5 미만이라면 분할하지 말고, 아니면 분할을 진행한다.
      merged.tree[[i]][[6]] <- "interval" #분할을 할 것이므로 노드 상태를 바꿔준다. 
      
      #이제 해당 노드의 training data를 대상으로 1회 분할을 시행한다.
      dt.testing <- rpart(score ~ .,
                  data = d.train,
                  control = rpart.control(minsplit = 6,
                                          maxdepth = 1,
                                          cp = 0.000))
      dt.testing <- as.party(dt.testing) #작으면 2번, 크면 3번 노드에 간다.
      if(depth(dt.testing) == 0){
        merged.tree[[i]][[6]] <- "terminal"
        next
      } #가끔 도저히 나눌수가 없어서 안나누는 경우가 존재함. 이 경우는 패스
      #만약 통과했다면 이제 진짜 분할을 진행한다.
      repeat{
        dt <- rpart(score ~ .,
                    data = d.train,
                    control = rpart.control(minsplit = 6,
                                            maxdepth = 1,
                                            cp = 0.000))
        dt <- as.party(dt) #작으면 2번, 크면 3번 노드에 간다.
        if(depth(dt) == 0){ #만약 분할이 이루어지지 않았다면 이건 no인 상태의 terminal이 된다.
          merged.tree[[i]][[6]] <- "terminal"
          break
        } 
        #분할이 되었다면 분할 정보를 끄집어 낸다.
        node <- node_party(dt) 
        listing <- as.list(node)
        varid <- listing[[1]]$split$varid #변수 번호이자 열 번호
        standard <- listing[[1]]$split$breaks #분할 기준
        
        #기준에 따라 아버지 노드의 training data를 나눈다.
        under.train.index <- d.train[,varid] < standard #rpart의 경우 0.5가 기준으로 잡힘
        under.train <- d.train[under.train.index,] #2번 노드로 간 training data(즉, 문항을 틀린 애들)
        
        upper.train.index <- d.train[,varid] >= standard
        upper.train <- d.train[upper.train.index,] #3번 노드로 간 training data(즉, 문항을 맞힌 애들)
        
        if(mean(under.train$score) >= mean(upper.train$score)){ #만약 문항을 맞추었음에도 점수가 더 낮으면...
          d.train[,varid] <- 0 #그러면 해당 변수들의 값을 전부 0으로 만들어버리고 재분할을 진행한다. 
          next
        }else{ #만약 맞추어서 더 높은 점수가 나오면 분할을 종료한다.
          break
        }
      }
      # break이 되었다면 dt가 최종 결과일 것이다.
      if(depth(dt) == 0){ #근데 결과적으로 분할이 안될 수 있다. 이 경우 terminal로 바꾸고 다음 분할로 넘어간다.
        merged.tree[[i]][[6]] <- "terminal"
        next
      }
      
      #여기까지 왔다는건 제대로 분할이 이루어졌다는 애기. 이에 따라 노드 정보를 기록한다.
      #이제 진행된 분할에 따라 두 개의 노드 정보를 구성하고 저장한다. 
      info.after <- list()
      info.after[[1]] <- length(merged.tree) + 1 #노드 번호
      info.after[[2]] <- i #아버지 노드의 번호
      info.after[[3]] <- c(varid, standard, "under") #분할 기준
      info.after[[4]] <- under.train #해당 노드에 간 training data
      info.after[[5]] <- "yes" #분할 대상 여부
      info.after[[6]] <- "terminal" #노드 상태
      info.after[[7]] <- NULL #결합된 노드 번호
      info.after[[8]] <- m #스테이지 번호 및 출제 문항 수
      info.after[[9]] <- mean(info.after[[4]]$score) #예측값
      
      #이를 merged.tree에 순서대로 넣어놓는다.
      merged.tree[[length(merged.tree) + 1]] <- info.after
      
      info.after <- list()
      info.after[[1]] <- length(merged.tree) + 1 #노드 번호호
      info.after[[2]] <- i #아버지 노드의 번호
      info.after[[3]] <- c(varid, standard, "upper") #분할 기준
      info.after[[4]] <- upper.train #해당 노드에 간 training data
      info.after[[5]] <- "yes" #분할 대상 여부
      info.after[[6]] <- "terminal" #노드 상태
      info.after[[7]] <- NULL #결합된 노드 번호
      info.after[[8]] <- m #스테이지 번호 및 출제 문항 수
      info.after[[9]] <- mean(info.after[[4]]$score) #예측값
      
      #이를 merged.tree에 순서대로 넣어놓는다.
      merged.tree[[length(merged.tree) + 1]] <- info.after
    }
    
    ##########################t-test를 통한 결합#################################################
    count <- c()
    
    repeat{
      #(3). 결합하기 : t-test를 이용하기 
      #먼저 결합 대상이 될 수 있는 노드들의 번호를 끄집어낸다.
      total <- length(merged.tree) #전체 노드 수
      num <- c() #t.test를 진행할 노드들의 번호를 기록할 것임.
      for(i in 1:total){
        dd <- merged.tree[[i]]
        if(dd[[5]] == "yes"){ #yes라는건 이번에 나온 노드들이면서 아직 합체가 안된 애들을 의미한다. 
          num <- c(num, i) #노드번호와 순서는 일치한다.(즉, 앞 번호의 노드가 앞에 오고 뒷 번호는 뒤에 온다.)
        }
      }
      num #결합 대상이 될 수 있는 노드들의 번호다.
      if(length(num) %in% c(0,1)) break # 만약 0개, 1개면 끝내라.
      
      #두번째로 해당 노드들을 대상으로 t-test를 진행한다.
      statistic <- c() #해당 stage 노드 간 test의 통계량을 담을 공벡터
      for(i in num){ #i는 기준 노드를 의미한다.
        stand <- merged.tree[[i]]
        standard.dat <- stand[[4]] #해당 노드의 training data
        if(sd(standard.dat$score) == 0){ #sd가 0이라는 애기는 전부 동일한 결과변수
          merged.tree[[i]][[5]] <- "no" #이때는 당연히 결합도, 분할도 멈추어야 할 것이다.
          next
        }
        compare.num <- num[i < num] #비교 대상 노드(이는 당연히 이보다 더 큰 번호의 노드들이 대상일 것임.)
        for(j in compare.num){
          com <- merged.tree[[j]] 
          compare.dat <- com[[4]] #분할 대상 노드의 training data
          if(sd(compare.dat$score) == 0){# 여기서도 마찬가지
            merged.tree[[j]][[5]] <- "no"
            next
          }
          t.result <- t.test(standard.dat$score, compare.dat$score)
          statistic <- c(statistic, abs(t.result$statistic))
        }
      }
      
      #2개였던게 1개가 되어 통계량 산출이 안된 경우는 break해줘야 함.
      if(length(statistic) == 0) break
      
      
      #세번째로 결합 대상이 존재하는지 확인하기
      if(min(statistic) > critical.t){ #만약 기록된 통계량이 기준보다 크다면 패스!
        combining.number <- c()
        count <- c(count,1) #count에 1이 추가됨으로써 끝난다. 
      }else{ #만약 아니라면 그 짝들의 번호를 찾아야 한다.
        combining.number <- c()
        minimum <- min(statistic) #이게 최소값의 통계량이다.
        for(i in num){
          stand <- merged.tree[[i]]
          standard.dat <- stand[[4]] #해당 노드의 training data
          if(sd(standard.dat$score) == 0){
            merged.tree[[i]][[5]] <- "no"
            next
          }
          compare.num <- num[i < num] #비교 대상 노드
          for(j in compare.num){
            com <- merged.tree[[j]]
            compare.dat <- com[[4]] #분할 대상 노드의 training data
            if(sd(compare.dat$score) == 0){
              merged.tree[[j]][[5]] <- "no"
              next
            }
            t.result <- t.test(standard.dat$score, compare.dat$score)
            if(abs(t.result$statistic) == minimum){
              combining.number <- c(i,j) #번호를 저장한다.(만약 같은게 존재하면 뒤에것 먼저 결합되겠군.)
            }
          }
        }
      }
      
      #결합해야할 노드들의 정보를 끄집어낸다.
      if(!is.null(combining.number)){#만약 결합해야할게 존재한다면,
        d1 <- merged.tree[[combining.number[1]]] #결합할 노드 1
        d2 <- merged.tree[[combining.number[2]]] #결합할 노드 2
        
        combining.node <- list() #결합해서 생성한 노드의 정보가 담긴다.
        combining.node[[1]] <- length(merged.tree) + 1 #노드 번호
        combining.node[[2]] <- c(d1[[2]], d2[[2]]) #해당 노드들의 아버지 노드 번호가 담긴다.
        combining.node[[3]] <- c(d1[[3]], d2[[3]]) #해당 노드들의 분할정보가 담긴다.(length가 6이상이 되겠지.)
        combining.node[[4]] <- rbind(d1[[4]], d2[[4]]) #해당노드들의 training data가 결합되어 담긴다.
        combining.node[[5]] <- "yes" #분할 대상 여부
        combining.node[[6]] <- "terminal" #노드의 상태
        combining.node[[7]] <- combining.number # 결합된 노드 번호가 담긴다.
        combining.node[[8]] <- m #스테이지 번호(매번 바꿔줄 것)
        combining.node[[9]] <- mean(combining.node[[4]]$score) #예측값
        
        merged.tree[[length(merged.tree)+1]] <- combining.node #이를 넣는다.
        
        #이제 결합 대상이 된 노드들의 정보를 변경한다.
        merged.tree[[combining.number[1]]][[5]] <- "no"
        merged.tree[[combining.number[1]]][[6]] <- "combined"
        
        merged.tree[[combining.number[2]]][[5]] <- "no"
        merged.tree[[combining.number[2]]][[6]] <- "combined"
        
        #결합된 노드의 정보를 확인한다.
        merged.tree[[length(merged.tree)]] 
      }
      if(length(count) == 1) break
    }
    
    ##########################cohen's d를 통한 결합#################################################
    count <- c()
    
    repeat{
      #(4). 결합하기 : SMD(cohen's d)를 이용하기
      #먼저 대상 노드들의 번호를 끄집어낸다.
      total <- length(merged.tree) #전체 노드 수
      num <- c()
      for(i in 1:total){
        dd <- merged.tree[[i]]
        if(dd[[5]] == "yes"){
          num <- c(num, i) #노드번호와 순서는 일치한다!
        }
      }
      num #해당 스테이지에 해당하는 node 번호다.
      if(length(num) %in% c(0,1)) break
      
      #두번째로, 해당 노드들을 대상으로 SMD를 계산한다.
      mean.diff <- c() #해당 stage 노드 간 SMD를 담을 공벡터
      for(i in num){
        stand <- merged.tree[[i]]
        standard.dat <- stand[[4]] #해당 노드의 training data
        cohen.standard <- as.data.frame(cbind(group = rep("A", dim(standard.dat)[1]), score = standard.dat$score))
        compare.num <- num[i < num] #비교 대상 노드
        for(j in compare.num){
          com <- merged.tree[[j]]
          compare.dat <- com[[4]] #분할 대상 노드의 training data
          cohen.compare <- as.data.frame(cbind(group = rep("B", dim(compare.dat)[1]), score = compare.dat$score))
          cohen.dat <- rbind(cohen.standard, cohen.compare)
          cohen.dat[,2] <- as.numeric(cohen.dat[,2])
          cohen.result <- cohen.d(cohen.dat, group = "group")
          mean.diff <- c(mean.diff, abs(cohen.result$cohen.d[2]))
        }
      }
      mean.diff
      
      #2개였던게 1개가 되어 통계량 산출이 안된 경우는 break해줘야 함.
      if(length(mean.diff) == 0) break
      
      if(min(mean.diff) > critical.s){
        combining.number <- c()
        count <- c(count,1) 
      }else{ #만약 아니라면 그 짝들의 번호를 찾아야 한다.
        combining.number <- c()
        minimum <- min(mean.diff)
        for(i in num){
          stand <- merged.tree[[i]]
          standard.dat <- stand[[4]] #해당 노드의 training data
          cohen.standard <- as.data.frame(cbind(group = rep("A", dim(standard.dat)[1]), score = standard.dat$score))
          compare.num <- num[i < num] #비교 대상 노드
          for(j in compare.num){
            com <- merged.tree[[j]]
            compare.dat <- com[[4]] #분할 대상 노드의 training data
            cohen.compare <- as.data.frame(cbind(group = rep("B", dim(compare.dat)[1]), score = compare.dat$score))
            cohen.dat <- rbind(cohen.standard, cohen.compare)
            cohen.dat[,2] <- as.numeric(cohen.dat[,2])
            cohen.result <- cohen.d(cohen.dat, group = "group")
            if(abs(cohen.result$cohen.d[2]) == minimum){
              combining.number <- c(i,j) #번호를 저장한다.
            }
          }
        }
      }
      
      if(!is.null(combining.number)){
        d1 <- merged.tree[[combining.number[1]]]
        d2 <- merged.tree[[combining.number[2]]]
        
        combining.node <- list() #결합해서 생성한 노드의 정보가 담긴다.
        combining.node[[1]] <- length(merged.tree) + 1 #노드 번호
        combining.node[[2]] <- c(d1[[2]], d2[[2]]) #해당 노드들의 아버지 노드 번호가 담긴다.
        combining.node[[3]] <- c(d1[[3]], d2[[3]]) #해당 노드들의 분할정보가 담긴다.
        combining.node[[4]] <- rbind(d1[[4]], d2[[4]]) #해당노드들의 training data가 결합되어 담긴다.
        combining.node[[5]] <- "yes" #분할 대상 여부
        combining.node[[6]] <- "terminal" #노드의 상태태
        combining.node[[7]] <- combining.number # 결합된 노드 번호가 담긴다.
        combining.node[[8]] <- m #스테이지 번호(매번 바꿔줄 것)
        combining.node[[9]] <- mean(combining.node[[4]]$score)
        
        merged.tree[[length(merged.tree)+1]] <- combining.node #이를 넣는다.
        
        #이제 결합 대상이 된 노드들의 정보를 변경한다.
        merged.tree[[combining.number[1]]][[5]] <- "no"
        merged.tree[[combining.number[1]]][[6]] <- "combined"
        
        merged.tree[[combining.number[2]]][[5]] <- "no"
        merged.tree[[combining.number[2]]][[6]] <- "combined"
        
        #결합된 노드의 정보를 확인한다.
        merged.tree[[length(merged.tree)]] 
      }
      if(length(count) == 1) break
    }
  }
  merged.tree <<- merged.tree
}

#3. k-fold cross validation 함수
cv.10fold.merge<- function(data.cv, cv.mdt,t.search, s.search, noi){
  #(1). 예측함수
  predict.merge <- function(response){ #1행의 데이터 프레임이 와야 한다.
    now <- 1 #현재 노드 번호
    now.pred <- merged.tree[[1]][[9]] #현재 예측값
    now.stage <- 0 #현재 스테이지 번호
    repeat{
      all <- length(merged.tree) #전체 노드 수
      canbenext <- c() #현재 노드 번호를 아버지 노드로 갖는 노드 번호들
      for(i in 1:all){
        search <- merged.tree[[i]] #해당 번호의 노드 정보를 끄집어 내서
        if(now %in% search[[2]]){ #만약 노드의 아버지 노드가 현재 노드 번호라면
          if(length(search[[3]]) == 3){ #그리고 결합된 노드가 아니라면
            canbenext <- c(canbenext,i) #이를 기록해두어라
          }
        }
      }
      #이제 기록된 노드들 중 하나로 가야한다. 
      #그런데 기록된 노드들의 분할 변수와 기준은 동일할 것이다.
      split.varid <- merged.tree[[canbenext[1]]][[3]][1] #분할 변수
      split.split <- merged.tree[[canbenext[1]]][[3]][2] #분할 기준
      #이때 분할변수 번호는 데이터의 변수 순서와 동일하다.
      if(response[,as.numeric(split.varid)] < split.split){ #만약 틀렸다면
        splitted <- "under" #분할 결과를 나타낸다.
      }else{splitted <- "upper"} #만약 맞혔다면
      
      #분할결과와 동일한 결과를 보여주는 자식노드로 이동시킨다.
      for(j in canbenext){ #j는 combining node가 아니다!
        roading <- merged.tree[[j]]
        if(roading[[3]][3] == splitted){
          now <- j #이동한 노드의 번호
          now.pred <- merged.tree[[j]][[9]] #이동한 노드의 예측값
          now.stage <- merged.tree[[j]][[8]] #이동한 stage 번호
        }else{next}
      }
      
      #만약 이동한 노드가 다른 노드와 결합한 경우 그쪽으로 이동해줘야 한다.
      if(merged.tree[[now]][[6]] == "combined"){
        for(m in 1:all){# all은 전체 노드 수를 의미한다.
          search.com <- merged.tree[[m]] #이렇게 처리하면 여러번 결합된 노드일지라도 결국 최종 결합 노드로 이동되게 된다.
          if(now %in% search.com[[7]]){
            now <- m
            now.pred <- merged.tree[[m]][[9]]
            now.stage <- merged.tree[[m]][[8]]
          }
        }
      }
      if(merged.tree[[now]][[6]] == "terminal") break
    }
    now <<- now
    now.pred <<- now.pred
    now.stage <<- now.stage
  }
  
  #(2). 생성함수
  merged.tree.make <- function(data.train, number, critical.t, critical.s){
    merged.tree <- list() #전체 정보를 담을 list
    aftersplit.train <- list()
    aftersplit.train[[1]] <- 1 #노드 번호호
    aftersplit.train[[2]] <- NULL #아버지노드 정보
    aftersplit.train[[3]] <- NULL # 분할 정보
    aftersplit.train[[4]] <- data.train #training data
    aftersplit.train[[5]] <- "yes" #분할대상여부
    aftersplit.train[[6]] <- "terminal" #노드 상태 
    aftersplit.train[[7]] <- NULL #결합 대상 노드 번호
    aftersplit.train[[8]] <- 0 #스테이지 번호
    aftersplit.train[[9]] <- mean(aftersplit.train[[4]]$score)
    
    merged.tree[[1]] <- aftersplit.train #노드번호와 list 번호가 동일하다.
    
    for(m in 1:number){
      no.number <- length(merged.tree) #list에 존재하는 노드 수
      splitting <- c() #분할 대상 노드의 번호
      for(i in 1:no.number){
        d <- merged.tree[[i]] #해당 노드 번호의 노드 정보를 끄집어 내고
        if(d[[5]] == "yes"){
          splitting <- c(splitting, d[[1]]) #만약 분할대상여부가 yes라면 노드 번호를 기록하라.
        }
      }
      splitting #분할대상노드의 번호다.
      
      #(2). 분할 대상 노드 분할하고 저장하기 
      for(i in splitting){
        node.info <- merged.tree[[i]] #분할 대상 노드의 정보를 끄집어낸다.
        merged.tree[[i]][[5]] <- "no" #일단 분할 대상 노드가 되었기 때문에 yes를 no로 바꿔준다.
        d.train <- node.info[[4]] #해당 노드에 존재하는 training data를 뽑아낸다.
        if(dim(d.train)[1] <= 5) next #만약 5 미만이라면 분할하지 말고, 아니면 분할을 진행한다.
        merged.tree[[i]][[6]] <- "interval" #분할을 할 것이므로 노드 상태를 바꿔준다. 
        
        #이제 해당 노드의 training data를 대상으로 1회 분할을 시행한다.
        dt.testing <- rpart(score ~ .,
                            data = d.train,
                            control = rpart.control(minsplit = 6,
                                                    maxdepth = 1,
                                                    cp = 0.000))
        dt.testing <- as.party(dt.testing) #작으면 2번, 크면 3번 노드에 간다.
        if(depth(dt.testing) == 0){
          merged.tree[[i]][[6]] <- "terminal"
          next
        } #가끔 도저히 나눌수가 없어서 안나누는 경우가 존재함. 이 경우는 패스
        #만약 통과했다면 이제 진짜 분할을 진행한다.
        repeat{
          dt <- rpart(score ~ .,
                      data = d.train,
                      control = rpart.control(minsplit = 6,
                                              maxdepth = 1,
                                              cp = 0.000))
          dt <- as.party(dt) #작으면 2번, 크면 3번 노드에 간다.
          if(depth(dt) == 0){ #만약 분할이 이루어지지 않았다면 이건 no인 상태의 terminal이 된다.
            merged.tree[[i]][[6]] <- "terminal"
            break
          } 
          #분할이 되었다면 분할 정보를 끄집어 낸다.
          node <- node_party(dt) 
          listing <- as.list(node)
          varid <- listing[[1]]$split$varid #변수 번호이자 열 번호
          standard <- listing[[1]]$split$breaks #분할 기준
          
          #기준에 따라 아버지 노드의 training data를 나눈다.
          under.train.index <- d.train[,varid] < standard #rpart의 경우 0.5가 기준으로 잡힘
          under.train <- d.train[under.train.index,] #2번 노드로 간 training data(즉, 문항을 틀린 애들)
          
          upper.train.index <- d.train[,varid] >= standard
          upper.train <- d.train[upper.train.index,] #3번 노드로 간 training data(즉, 문항을 맞힌 애들)
          
          if(mean(under.train$score) >= mean(upper.train$score)){ #만약 문항을 맞추었음에도 점수가 더 낮으면...
            d.train[,varid] <- 0 #그러면 해당 변수들의 값을 전부 0으로 만들어버리고 재분할을 진행한다. 
            next
          }else{ #만약 맞추어서 더 높은 점수가 나오면 분할을 종료한다.
            break
          }
        }
        # break이 되었다면 dt가 최종 결과일 것이다.
        if(depth(dt) == 0){ #근데 결과적으로 분할이 안될 수 있다. 이 경우 terminal로 바꾸고 다음 분할로 넘어간다.
          merged.tree[[i]][[6]] <- "terminal"
          next
        }
        
        #여기까지 왔다는건 제대로 분할이 이루어졌다는 애기. 이에 따라 노드 정보를 기록한다.
        #이제 진행된 분할에 따라 두 개의 노드 정보를 구성하고 저장한다. 
        info.after <- list()
        info.after[[1]] <- length(merged.tree) + 1 #노드 번호
        info.after[[2]] <- i #아버지 노드의 번호
        info.after[[3]] <- c(varid, standard, "under") #분할 기준
        info.after[[4]] <- under.train #해당 노드에 간 training data
        info.after[[5]] <- "yes" #분할 대상 여부
        info.after[[6]] <- "terminal" #노드 상태
        info.after[[7]] <- NULL #결합된 노드 번호
        info.after[[8]] <- m #스테이지 번호 및 출제 문항 수
        info.after[[9]] <- mean(info.after[[4]]$score) #예측값
        
        #이를 merged.tree에 순서대로 넣어놓는다.
        merged.tree[[length(merged.tree) + 1]] <- info.after
        
        info.after <- list()
        info.after[[1]] <- length(merged.tree) + 1 #노드 번호호
        info.after[[2]] <- i #아버지 노드의 번호
        info.after[[3]] <- c(varid, standard, "upper") #분할 기준
        info.after[[4]] <- upper.train #해당 노드에 간 training data
        info.after[[5]] <- "yes" #분할 대상 여부
        info.after[[6]] <- "terminal" #노드 상태
        info.after[[7]] <- NULL #결합된 노드 번호
        info.after[[8]] <- m #스테이지 번호 및 출제 문항 수
        info.after[[9]] <- mean(info.after[[4]]$score) #예측값
        
        #이를 merged.tree에 순서대로 넣어놓는다.
        merged.tree[[length(merged.tree) + 1]] <- info.after
      }
      
      ##########################t-test를 통한 결합#################################################
      count <- c()
      
      repeat{
        #(3). 결합하기 : t-test를 이용하기 
        #먼저 결합 대상이 될 수 있는 노드들의 번호를 끄집어낸다.
        total <- length(merged.tree) #전체 노드 수
        num <- c() #t.test를 진행할 노드들의 번호를 기록할 것임.
        for(i in 1:total){
          dd <- merged.tree[[i]]
          if(dd[[5]] == "yes"){ #yes라는건 이번에 나온 노드들이면서 아직 합체가 안된 애들을 의미한다. 
            num <- c(num, i) #노드번호와 순서는 일치한다.(즉, 앞 번호의 노드가 앞에 오고 뒷 번호는 뒤에 온다.)
          }
        }
        num #결합 대상이 될 수 있는 노드들의 번호다.
        if(length(num) %in% c(0,1)) break # 만약 0개, 1개면 끝내라.
        
        #두번째로 해당 노드들을 대상으로 t-test를 진행한다.
        statistic <- c() #해당 stage 노드 간 test의 통계량을 담을 공벡터
        for(i in num){ #i는 기준 노드를 의미한다.
          stand <- merged.tree[[i]]
          standard.dat <- stand[[4]] #해당 노드의 training data
          if(sd(standard.dat$score) == 0){ #sd가 0이라는 애기는 전부 동일한 결과변수
            merged.tree[[i]][[5]] <- "no" #이때는 당연히 결합도, 분할도 멈추어야 할 것이다.
            next
          }
          compare.num <- num[i < num] #비교 대상 노드(이는 당연히 이보다 더 큰 번호의 노드들이 대상일 것임.)
          for(j in compare.num){
            com <- merged.tree[[j]] 
            compare.dat <- com[[4]] #분할 대상 노드의 training data
            if(sd(compare.dat$score) == 0){# 여기서도 마찬가지
              merged.tree[[j]][[5]] <- "no"
              next
            }
            t.result <- t.test(standard.dat$score, compare.dat$score)
            statistic <- c(statistic, abs(t.result$statistic))
          }
        }
        
        #2개였던게 1개가 되어 통계량 산출이 안된 경우는 break해줘야 함.
        if(length(statistic) == 0) break
        
        
        #세번째로 결합 대상이 존재하는지 확인하기
        if(min(statistic) > critical.t){ #만약 기록된 통계량이 기준보다 크다면 패스!
          combining.number <- c()
          count <- c(count,1) #count에 1이 추가됨으로써 끝난다. 
        }else{ #만약 아니라면 그 짝들의 번호를 찾아야 한다.
          combining.number <- c()
          minimum <- min(statistic) #이게 최소값의 통계량이다.
          for(i in num){
            stand <- merged.tree[[i]]
            standard.dat <- stand[[4]] #해당 노드의 training data
            if(sd(standard.dat$score) == 0){
              merged.tree[[i]][[5]] <- "no"
              next
            }
            compare.num <- num[i < num] #비교 대상 노드
            for(j in compare.num){
              com <- merged.tree[[j]]
              compare.dat <- com[[4]] #분할 대상 노드의 training data
              if(sd(compare.dat$score) == 0){
                merged.tree[[j]][[5]] <- "no"
                next
              }
              t.result <- t.test(standard.dat$score, compare.dat$score)
              if(abs(t.result$statistic) == minimum){
                combining.number <- c(i,j) #번호를 저장한다.(만약 같은게 존재하면 뒤에것 먼저 결합되겠군.)
              }
            }
          }
        }
        
        #결합해야할 노드들의 정보를 끄집어낸다.
        if(!is.null(combining.number)){#만약 결합해야할게 존재한다면,
          d1 <- merged.tree[[combining.number[1]]] #결합할 노드 1
          d2 <- merged.tree[[combining.number[2]]] #결합할 노드 2
          
          combining.node <- list() #결합해서 생성한 노드의 정보가 담긴다.
          combining.node[[1]] <- length(merged.tree) + 1 #노드 번호
          combining.node[[2]] <- c(d1[[2]], d2[[2]]) #해당 노드들의 아버지 노드 번호가 담긴다.
          combining.node[[3]] <- c(d1[[3]], d2[[3]]) #해당 노드들의 분할정보가 담긴다.(length가 6이상이 되겠지.)
          combining.node[[4]] <- rbind(d1[[4]], d2[[4]]) #해당노드들의 training data가 결합되어 담긴다.
          combining.node[[5]] <- "yes" #분할 대상 여부
          combining.node[[6]] <- "terminal" #노드의 상태
          combining.node[[7]] <- combining.number # 결합된 노드 번호가 담긴다.
          combining.node[[8]] <- m #스테이지 번호(매번 바꿔줄 것)
          combining.node[[9]] <- mean(combining.node[[4]]$score) #예측값
          
          merged.tree[[length(merged.tree)+1]] <- combining.node #이를 넣는다.
          
          #이제 결합 대상이 된 노드들의 정보를 변경한다.
          merged.tree[[combining.number[1]]][[5]] <- "no"
          merged.tree[[combining.number[1]]][[6]] <- "combined"
          
          merged.tree[[combining.number[2]]][[5]] <- "no"
          merged.tree[[combining.number[2]]][[6]] <- "combined"
          
          #결합된 노드의 정보를 확인한다.
          merged.tree[[length(merged.tree)]] 
        }
        if(length(count) == 1) break
      }
      
      ##########################cohen's d를 통한 결합#################################################
      count <- c()
      
      repeat{
        #(4). 결합하기 : SMD(cohen's d)를 이용하기
        #먼저 대상 노드들의 번호를 끄집어낸다.
        total <- length(merged.tree) #전체 노드 수
        num <- c()
        for(i in 1:total){
          dd <- merged.tree[[i]]
          if(dd[[5]] == "yes"){
            num <- c(num, i) #노드번호와 순서는 일치한다!
          }
        }
        num #해당 스테이지에 해당하는 node 번호다.
        if(length(num) %in% c(0,1)) break
        
        #두번째로, 해당 노드들을 대상으로 SMD를 계산한다.
        mean.diff <- c() #해당 stage 노드 간 SMD를 담을 공벡터
        for(i in num){
          stand <- merged.tree[[i]]
          standard.dat <- stand[[4]] #해당 노드의 training data
          cohen.standard <- as.data.frame(cbind(group = rep("A", dim(standard.dat)[1]), score = standard.dat$score))
          compare.num <- num[i < num] #비교 대상 노드
          for(j in compare.num){
            com <- merged.tree[[j]]
            compare.dat <- com[[4]] #분할 대상 노드의 training data
            cohen.compare <- as.data.frame(cbind(group = rep("B", dim(compare.dat)[1]), score = compare.dat$score))
            cohen.dat <- rbind(cohen.standard, cohen.compare)
            cohen.dat[,2] <- as.numeric(cohen.dat[,2])
            cohen.result <- cohen.d(cohen.dat, group = "group")
            mean.diff <- c(mean.diff, abs(cohen.result$cohen.d[2]))
          }
        }
        mean.diff
        
        #2개였던게 1개가 되어 통계량 산출이 안된 경우는 break해줘야 함.
        if(length(mean.diff) == 0) break
        
        if(min(mean.diff) > critical.s){
          combining.number <- c()
          count <- c(count,1) 
        }else{ #만약 아니라면 그 짝들의 번호를 찾아야 한다.
          combining.number <- c()
          minimum <- min(mean.diff)
          for(i in num){
            stand <- merged.tree[[i]]
            standard.dat <- stand[[4]] #해당 노드의 training data
            cohen.standard <- as.data.frame(cbind(group = rep("A", dim(standard.dat)[1]), score = standard.dat$score))
            compare.num <- num[i < num] #비교 대상 노드
            for(j in compare.num){
              com <- merged.tree[[j]]
              compare.dat <- com[[4]] #분할 대상 노드의 training data
              cohen.compare <- as.data.frame(cbind(group = rep("B", dim(compare.dat)[1]), score = compare.dat$score))
              cohen.dat <- rbind(cohen.standard, cohen.compare)
              cohen.dat[,2] <- as.numeric(cohen.dat[,2])
              cohen.result <- cohen.d(cohen.dat, group = "group")
              if(abs(cohen.result$cohen.d[2]) == minimum){
                combining.number <- c(i,j) #번호를 저장한다.
              }
            }
          }
        }
        
        if(!is.null(combining.number)){
          d1 <- merged.tree[[combining.number[1]]]
          d2 <- merged.tree[[combining.number[2]]]
          
          combining.node <- list() #결합해서 생성한 노드의 정보가 담긴다.
          combining.node[[1]] <- length(merged.tree) + 1 #노드 번호
          combining.node[[2]] <- c(d1[[2]], d2[[2]]) #해당 노드들의 아버지 노드 번호가 담긴다.
          combining.node[[3]] <- c(d1[[3]], d2[[3]]) #해당 노드들의 분할정보가 담긴다.
          combining.node[[4]] <- rbind(d1[[4]], d2[[4]]) #해당노드들의 training data가 결합되어 담긴다.
          combining.node[[5]] <- "yes" #분할 대상 여부
          combining.node[[6]] <- "terminal" #노드의 상태태
          combining.node[[7]] <- combining.number # 결합된 노드 번호가 담긴다.
          combining.node[[8]] <- m #스테이지 번호(매번 바꿔줄 것)
          combining.node[[9]] <- mean(combining.node[[4]]$score)
          
          merged.tree[[length(merged.tree)+1]] <- combining.node #이를 넣는다.
          
          #이제 결합 대상이 된 노드들의 정보를 변경한다.
          merged.tree[[combining.number[1]]][[5]] <- "no"
          merged.tree[[combining.number[1]]][[6]] <- "combined"
          
          merged.tree[[combining.number[2]]][[5]] <- "no"
          merged.tree[[combining.number[2]]][[6]] <- "combined"
          
          #결합된 노드의 정보를 확인한다.
          merged.tree[[length(merged.tree)]] 
        }
        if(length(count) == 1) break
      }
    }
    merged.tree <<- merged.tree
  }
  
  error.t <- c()
  min.s <- c()
  cv.result <- foreach(i = t.search, .combine = rbind, .packages = c("caret","rpart","party","partykit","psych")) %dopar% {
    t.conditionm <- c() #t를 고정하고, s를 변화시켰을 때 mae를 기록한다.
    for(j in s.search){ #j는 critical.s다
      sum.error <- c() #t = i이고 s = j일때의 error값들을 기록할것임.
      for(u in 1:length(cv.mdt)){ #u는 현재 test data의 index를 의미한다.
        testingfold <- cv.mdt[[u]]
        testing.dat <- data.cv[testingfold,] #현재 test data
        training.dat <- data.cv[-testingfold,] #현재 training data
        merged.tree.make(data.train = training.dat, number = noi, critical.t = i, critical.s = j)
        
        pred.function <- c()
        for(q in 1:dim(testing.dat)[1]){
          response <- testing.dat[q,]
          predict.merge(response)
          pred.function <- c(pred.function, now.pred)
        }
        error.cv <- MAE(pred.function, testing.dat$score)
        sum.error <- c(sum.error, error.cv)
      }
      score.error <- mean(sum.error)
      t.conditionm <- c(t.conditionm, score.error)
    }
    c(i, s.search[which.min(t.conditionm)], min(t.conditionm))
  }
  cv.result <- as.data.frame(cv.result)
  cv.result <<- cv.result
  final.t <<- cv.result[which.min(cv.result[,3]),1]
  final.s <<- cv.result[which.min(cv.result[,3]),2]
  return(c(final.t,final.s))
}