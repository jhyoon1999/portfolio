library(tidyverse)
library(leaflet)
library(httr)
library(jsonlite)
library(glue)
library(readxl)

api.result <- tibble()

address.list <- "GPS 데이터를 수집할 아파트의 지번주소 데이터를 불러와주세요."

#불러온 데이터의 크기(행의 수)를 지정해주세요.
start <- 1 
end <- 90000

api_key <- "API 키를 입력해주세요."

#반복적인 요청으로 인한 순간적인 밴을 고려해 오류 상황에서도 코드를 계속 실행할 수 있는 tryCatch 활용
repeat{
  tryCatch(expr = 
             for(i in start:end){ 
               target <<- address.list[i]
               
               addre.result <<- GET(url = 'https://dapi.kakao.com/v2/local/search/address.json',
                                    query = list(query = target),
                                    add_headers(Authorization = paste0("KakaoAK ", api_key))) %>% 
                 content(as = 'text') %>% 
                 fromJSON()
               
               addre.result.speci <<- addre.result$documents
               
               if(is.null(addre.result.speci$address)){ 
                 resulting <<- tibble(add.ji = NA, 
                                      add.lon = NA, 
                                      add.lat = NA,
                                      add.bcode = NA)
                 api.result <<- rbind(api.result, resulting)
                 next  
               }
               
               addre.result.speci <<- addre.result.speci[1,] 
               
               
               if(sum(is.na(addre.result.speci$address)) == 1){
                 resulting <<- tibble(add.ji = NA, 
                                      add.lon = as.character(addre.result.speci$x), 
                                      add.lat = as.character(addre.result.speci$y),
                                      add.bcode = NA)
                 api.result <<- rbind(api.result, resulting)
                 next  
               }
               
               
               if(sum(is.na(addre.result.speci$address)) != 0){
                 print(i)
                 break
               }
               
               
               resulting <<- tibble(add.ji = as.character(addre.result.speci$address$address_name), 
                                    add.lon = as.character(addre.result.speci$address$x), 
                                    add.lat = as.character(addre.result.speci$address$y),
                                    add.bcode = as.character(addre.result.speci$address$b_code))
               api.result <<- rbind(api.result, resulting)
             },
           error = function(e){
             print(start)
             start <<- dim(api.result)[1] + 1
             print(start)
           },
           warning = NULL,
           finally = NULL)
  
  if(dim(api.result)[1] == end){ 
    break
  }
}
