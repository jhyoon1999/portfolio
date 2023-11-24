library(shiny)
library(shinymanager)
library(dplyr)
library(ggplot2)
library(stringr)
library(rsconnect)
library(DT)
require(showtext)
library(scales)
library(openxlsx)
library(shinyjs)
library(caret)
library(randomForest)

# define some credentials
credentials <- data.frame(
  user = c("***", "****"), # mandatory
  password = c("****", "****"), # mandatory
  start = c("2022-09-04"), # optinal (all others)
  expire = c(NA, NA),
  admin = c(FALSE, TRUE),
  comment = "JW international web browser",
  stringsAsFactors = FALSE
)

font_add_google(name = 'Nanum Gothic',
                regular.wt = 400, bold.wt = 700)

showtext_auto()
showtext_opts(dpi = 112)

load("context.final.RData")

#### 유저 인터페이스 ####
ui <- navbarPage(
  "제이더블유 브라우저",
  
  shinyjs::useShinyjs(),
  
  ### 데이터 추출파트 ###
  tabPanel("데이터 추출",
           fluidPage(
             fluidRow(
               column(2, #표준산업분류의 text input
                      textInput(inputId = "bigcluster", label = "대분류"),
                      textInput(inputId = "midcluster", label = "중분류"),
                      textInput(inputId = "smallcluster", label = "소분류"),
                      textInput(inputId = "secluster", label = "세분류"),
                      textInput(inputId = "sesecluster", label = "세세분류"),
                      textInput(inputId = "industry", label = "주요사업"),
                      selectInput(inputId = "region", label = "지역",
                                  choices = region.list, multiple = T)
               ),
               column(2, #기업개요의 text input
                      selectInput(inputId = "method.select", label = "재무정보 조회 방법",
                                  choices = method.selecting, multiple = F),
                      selectInput(inputId = "year.select", label = "재무정보의 년도",
                                  choices = finance.date, multiple = TRUE),
                      selectInput(inputId = "class.company.select", label = "개인법인구분",
                                  choices = class.company),
                      selectInput(inputId = "staff.count.onoff.select", label = "종업원수 결측값 포함여부", 
                                  choices = staff.count.onoff),
                      sliderInput(inputId = "staff.count.slider", label = "종업원수(결측값 포함시 작동X)",
                                  min = min(dat.basic$종업원수, na.rm = T), max = max(dat.basic$종업원수, na.rm = T),
                                  value = c(min(dat.basic$종업원수, na.rm = T), max(dat.basic$종업원수, na.rm = T))),
                      actionButton(inputId = "extracting", label = "데이터 추출",class = "btn-danger")#UI 액션버튼추가중 ####
               ),
               
               
               column(8, #아웃풋을 놓는 곳이다.
                      tabsetPanel(
                        tabPanel(title = "결측치 정보", 
                                 DT::dataTableOutput("na.table"),
                                 br(),
                                 downloadButton(outputId = "download.basic", label = "데이터 다운로드")
                        ),
                        
                        tabPanel(title = "개요요약",
                                 plotOutput("sesebar"),
                                 plotOutput("main.industry"),
                                 plotOutput("selproduct")
                        ),
                        
                        tabPanel(title = "재무요약",
                                 plotOutput("jabon.ker"),
                                 plotOutput("income.ker"),
                                 plotOutput("money.ker")
                        )
                      )
               )
             ),
             
             br(),
             hr(),
             br(),
             
             fluidRow(
               tabsetPanel(
                 tabPanel(title = "표준산업분류",
                          column(2, DT::dataTableOutput("w")),
                          column(2, DT::dataTableOutput("ww")),
                          column(2, DT::dataTableOutput("www")),
                          column(3, DT::dataTableOutput("wwww")),
                          column(3, DT::dataTableOutput("wwwww"))
                 ),
                 
                 tabPanel(title = "표준산업분류 세부검색",
                          column(4,
                                 selectInput(inputId = "select.big", label = "대분류 목록", choices = unique(industry.code$대분류)),
                                 selectInput(inputId = "select.mid", label = "중분류 목록", choices = NULL),
                                 selectInput(inputId = "select.small", label = "소분류 목록", choices = NULL),
                                 selectInput(inputId = "select.se", label = "세분류 목록", choices = NULL)
                          ),
                          column(8,
                                 DT::dataTableOutput("industry.table")))
               )
             )
           )
           
  ),
  
  ### 개요정보 파트 ###
  tabPanel("개요정보",
           fluidPage(
             fluidRow(
               column(2,
                      selectInput(inputId = "select.gaeyo.inform", label = "개요정보 선택",
                                  choices = gaeyo.select)),
               column(10,
                      plotOutput("gaeyo.bar", click = "click.gaeyo"),
                      br(),
                      downloadButton(outputId = "download.gaeyo", label = "데이터 다운로드"))
             ),
             br(),
             hr(),
             br(),
             fluidRow(
               column(12,
                      DT::dataTableOutput("gaeyo.table"))
             )
           )
  ),
  
  ### 재무정보 파트 ###
  tabPanel("재무정보",
           fluidPage(
             fluidRow(
               column(2,
                      selectInput(inputId = "select.jaemu.outlier", label = "이상치(outlier) 포함 여부", choices = outlier.select),
                      selectInput(inputId = "select.jaemu.inform", label = "재무정보 선택", choices = jaemu.select),
                      selectInput(inputId = "select.jaemu.year", label = "재무년도 선택", choices = finance.date, multiple = T)
               ),
               column(10,
                      plotOutput("jaemu.hist", brush = brushOpts(id = "brush.jaemu", direction = "x", resetOnNew = T)),
                      br(),
                      downloadButton(outputId = "download.jaemu", label = "데이터 다운로드"))
             ),
             br(),
             hr(),
             br(),
             fluidRow(
               column(12,
                      DT::dataTableOutput("data.brush")
               )
             )
           )
  ),
  
  ### 가설검정 파트 ###
  tabPanel("가설검정",
           fluidPage(
             fluidRow(
               column(2,
                      selectInput(inputId = "met", label = "대상재무정보", choices = jaemu.select)),
               column(2,
                      selectInput(inputId = "g1.s", label = "대상년도1", choices = finance.date)),
               column(2,
                      selectInput(inputId = "g2.s", label = "대상년도2", choices = finance.date)),
               column(2,
                      selectInput(inputId = "altern", label = "대립가설 형태", choices = alter))
             ),
             fluidRow(
               column(6,
                      plotOutput(outputId = "g1plot")),
               column(6,
                      plotOutput(outputId = "g2plot"))
             ),
             fluidRow(
               column(12,
                      h4("대상년도1"),
                      DT::dataTableOutput("g1summary"),
                      br(),
                      h4("대상년도2"),
                      DT::dataTableOutput("g2summary"),
                      br(),
                      h4("가설검정 결과"),
                      verbatimTextOutput(outputId = "result.test")
               )
             )
           )
  ),
  
  ### AI 파트 ###
  tabPanel("AI 분석",
           fluidPage(
             fluidRow(
               column(4,
                      selectInput(inputId = "ai.selecting", label = "AI 선택", choices = ai.select,
                      )
               ),
               column(8,
                      textOutput("ai.infor", container = tags$h4)
               )
             ),
             fluidRow(
               column(2,
                      numericInput(inputId = "ai1", label = "총자산세전순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai2", label = "총자산순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai3", label = "자기자본세전순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai19", label = "총자산회전율", 
                                   value = 0, min = -999, max = 999)
               ),
               
               column(2,
                      numericInput(inputId = "ai4", label = "자기자본순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai5", label = "자본금세전순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai6", label = "자본금순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai20", label = "자기자본회전율", 
                                   value = 0, min = -999, max = 999)
               ),
               
               column(2,
                      numericInput(inputId = "ai7", label = "매출액세전순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai8", label = "매출액순이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai9", label = "매출액영업이익률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai21", label = "자본금회전율", 
                                   value = 0, min = -999, max = 999)
               ),
               
               column(2,
                      numericInput(inputId = "ai10", label = "매출원가대매출액", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai11", label = "자기자본비율", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai12", label = "유동비율", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai22", label = "비유동자산회전율", 
                                   value = 0, min = -999, max = 999)
               ),
               
               column(2,
                      numericInput(inputId = "ai13", label = "비유동비율", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai14", label = "비유동장기적합률", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai15", label = "부채비율", 
                                   value = 0, min = -999, max = 999)
               ),
               
               column(2,
                      numericInput(inputId = "ai16", label = "유동부채비율", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai17", label = "비유동부채비율", 
                                   value = 0, min = -999, max = 999),
                      numericInput(inputId = "ai18", label = "순운전자본대총자본", 
                                   value = 0, min = -999, max = 999),
                      actionButton(inputId = "start.pred", label = "예측시작!", class = "btn-danger")
               )
             ),
             br(),
             hr(),
             br(),
             
             fluidRow(
               column(4,
                      tabsetPanel(
                        tabPanel(title = "재무지표",
                                 DT::dataTableOutput("index.informing")
                        ),
                        
                        tabPanel(title = "입력 데이터",
                                 DT::dataTableOutput("now.predict.data")
                                 )
                      )
               ),
               
               column(8, 
                      tabsetPanel(
                        tabPanel(title = "AI 예측",
                                 textOutput("before.resulting", container = tags$h5),
                                 br(),
                                 textOutput("after.resulting", container = tags$h5)
                        ),
                        
                        tabPanel(title = "AI 학습정보",
                                 verbatimTextOutput("ai.performance")
                                 
                        ),
                        
                        tabPanel(title = "변수 중요도",
                                 plotOutput("ai.variable.importance")      
                        )
                      )
               )
             )
           )
  )
)



ui <- secure_app(ui)



#### 서버 ####
server <- function(input, output, session){
  
  #로그인 기능 추가하기
  res_auth <- secure_server(
    check_credentials = check_credentials(credentials)
  )
  
  dat <- eventReactive(input$extracting,{
    dat <- dat.basic
    
    #1. 대분류
    if(input$bigcluster != ""){
      big.clustering <- gsub(" ","", input$bigcluster)
      big.clustering <- strsplit(big.clustering, "or")
      big.clustering <- big.clustering[[1]]
      
      pattern <- big.clustering
      judge.big <- function(x){
        string <- x[['대분류']]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      sb <- apply(dat, 1, FUN = judge.big)
      dat <- dat[sb,]
    }
    
    #2. 중분류
    if(input$midcluster != ""){
      mid.clustering <- gsub(" ","", input$midcluster)
      mid.clustering <- strsplit(mid.clustering, "or")
      mid.clustering <- mid.clustering[[1]]
      
      pattern <- mid.clustering
      judge.mid <- function(x){
        string <- x[['중분류']]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      sm <- apply(dat, 1, FUN = judge.mid)
      dat <- dat[sm,]
    }
    
    #3. 소분류
    if(input$smallcluster != ""){
      small.clustering <- gsub(" ","", input$smallcluster)
      small.clustering <- strsplit(small.clustering, "or")
      small.clustering <- small.clustering[[1]]
      
      pattern <- small.clustering
      judge.small <- function(x){
        string <- x[['소분류']]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      ss <- apply(dat, 1, FUN = judge.small)
      dat <- dat[ss,]
    }
    
    #4.세분류
    if(input$secluster != ""){
      se.clustering <- gsub(" ","", input$secluster)
      se.clustering <- strsplit(se.clustering, "or")
      se.clustering <- se.clustering[[1]]
      
      pattern <- se.clustering
      judge.se <- function(x){
        string <- x[['세분류']]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      sss <- apply(dat, 1, FUN = judge.se)
      dat <- dat[sss,]
    }
    
    #5. 세세분류
    if(input$sesecluster != ""){
      sese.clustering <- gsub(" ", "", input$sesecluster)
      sese.clustering <- strsplit(sese.clustering, "or")
      sese.clustering <- sese.clustering[[1]]
      
      pattern <- sese.clustering
      judge.sese <- function(x){
        string <- x[['세세분류']]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      ssss <- apply(dat, 1, FUN = judge.sese)
      dat <- dat[ssss,]
    }
    
    #6. 주요산업
    if(input$industry != ""){
      industry.clustering <- gsub(" ", "", input$industry)
      industry.clustering <- strsplit(industry.clustering, "or")
      industry.clustering <- industry.clustering[[1]]
      
      pattern <- industry.clustering
      judge.industry <- function(x){
        string <- x[["주요사업(사업목적)"]]
        string <- gsub(" ","", string)
        if(is.na(string)){
          return(FALSE)
        }
        if(sum(str_detect(string = string, pattern = pattern)) > 0){
          return(TRUE)
        }else{
          return(FALSE)
        }
      }
      
      si <- apply(dat, 1, FUN = judge.industry)
      dat <- dat[si,]
    }
    
    #7. 지역
    if(!is.null(input$region)){
      select.region <- input$region
      
      region.want.id <- c()
      for(l in 1:length(select.region)){
        selecting.region <- select.region[l]
        id.region <- dat %>% filter(시도 == selecting.region)
        region.want.id <- c(region.want.id, id.region$ID)
      }
      target.id.region <- unique(region.want.id)
      dat <- dat %>% filter(ID %in% target.id.region)
    }
    
    #8. 종업원 수
    if(input$staff.count.onoff.select == "미포함"){
      dat <- dat %>% filter(!is.na(종업원수))
      dat <- dat %>% filter(종업원수 >= input$staff.count.slider[1] & 종업원수 <= input$staff.count.slider[2])
    }
    
    #9. 개인법인구분
    if(input$class.company.select != "전체"){
      dat <- dat %>% filter(개인법인구분 == input$class.company.select)
    }
    
    return(dat)
  })
  
  dat.f <- eventReactive(input$extracting,{
    dat.f <- dat.eco
    dat.pyu <- dat.eco.table
    
    #1. 년도별 재무정보
    if(!is.null(input$year.select)){
      year <- input$year.select
      dat.iding <- dat.pyu
      
      if(input$method.select == "And"){
        
        for(m in 1:length(year)){
          yearing <- year[m]
          dat.iding <- dat.iding %>% filter(str_detect(결산년도, yearing))
        }
        target.id <- dat.iding$ID
        dat.f <- dat.f %>% filter(ID %in% target.id)
      }else{
        id.or <- c()
        for(h in 1:length(year)){
          yearing <- year[h]
          dat.or <- dat.iding %>% filter(str_detect(결산년도, yearing))
          id.or <- c(id.or, dat.or$ID)
        }
        target.id <- unique(id.or)
        dat.f <- dat.f %>% filter(ID %in% target.id)
      }
    }
    
    return(dat.f)
  })
  
  #데이터 매칭
  dated <- reactive({
    req(dat())
    dated <- dat()
    dated <- dated %>% filter(ID %in% dat.f()$ID)
    return(dated)
  })
  
  dated.f <- reactive({
    req(dat.f())
    dated.f <- dat.f()
    dated.f <- dated.f %>% filter(ID %in% dated()$ID)
    return(dated.f)
  })
  
  #또한 속도를 위해 현재 선택된 데이터에 해당하는 결측치 개수 체크하는 테이블 만들자.
  dated.na.fin <- reactive({
    req(dat.f())
    dated.na.fin <- dat.eco.na.table
    dated.na.fin <- dated.na.fin %>% filter(ID %in% dated.f()$ID)
    return(dated.na.fin)
  })
  
  
  ####결측치 정보의 아웃풋####
  na.data.table <- reactive({
    req(dated())
    req(dated.f())
    req(dated.na.fin())
    #데이터를 사용하기 편하게 지정해준다.
    dating <- dated()
    dating.f <- dated.f()
    dating.f.na <- dated.na.fin()
    
    na.counting <- c()
    #(1). 세세분류가 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating$세세분류)))
    
    #(2). 주요사업이 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating$`주요사업(사업목적)`)))
    
    #(3). 주소가 없는 기업
    na.counting <- c(na.counting,sum(is.na(dating$주소)))
    
    #(4). 종업원 수가 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating$종업원수)))
    
    #(5). 상품이 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating$`상품코드1`)))
    
    #(6). 매출처가 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating$`매출처1`)))
    
    #(7). 재무정보가 없는 기업
    na.counting <- c(na.counting, sum(is.na(dating.f.na$결측치)))
    
    na.data.table <- tibble(내용 = naming, `결측치수` = na.counting)
    na.data.table <- na.data.table %>% mutate(`유효수` = (dim(dating)[1] - `결측치수`))
    na.data.table <- na.data.table %>% mutate(`전체수` = dim(dating)[1])
    na.data.table <- na.data.table %>% mutate(`결측치 퍼센트` = round((`결측치수`/`전체수`)*100, digits = 1))
    na.data.table <- na.data.table %>% mutate(`결측치 퍼센트` = paste(`결측치 퍼센트`, "%", sep = ""))
    
    return(na.data.table)
  })
  
  
  output$na.table <- DT::renderDataTable({
    req(na.data.table())
    datatable(na.data.table(), options = list(dom = 'tp')) 
  })
  
  #### 개요정보 아웃풋 #####
  #1. 세세분류
  miniminicluster <- reactive({
    req(dated())
    #데이터 불러오기
    dating3 <- dated()
    dating3 <- dating3 %>% count(세세분류, sort = T)
    dating3 <- dating3 %>% filter(!is.na(세세분류))
    #상위 20개만
    dating3 <- dating3 %>% head(20)
    return(dating3)
  })
  
  output$sesebar <- renderPlot({
    req(miniminicluster())
    miniminibar <- miniminicluster()
    ggplot(miniminibar, aes(x = reorder(세세분류,n), y = n, label = n)) + 
      geom_col(position = "dodge") + 
      geom_text(position = position_dodge(width = 1),
                hjust = 0)+
      coord_flip() + xlab("세세분류") + ylab("빈도수")
  },res = 96)
  
  #2. 주요사업
  maining.industry <- reactive({
    req(dated())
    dating5 <- dated()
    
    list.industry <- tibble(주요사업 = dating5$`주요사업1`)
    list.industry <- rbind(list.industry, tibble(주요사업 = dating5$`주요사업2`))
    list.industry <- rbind(list.industry, tibble(주요사업 = dating5$`주요사업3`))
    list.industry <- rbind(list.industry, tibble(주요사업 = dating5$`주요사업4`))
    list.industry <- rbind(list.industry, tibble(주요사업 = dating5$`주요사업5`))
    
    list.industry <- na.omit(list.industry)
    maining.industry <- list.industry %>% count(주요사업, sort = T)
    
    #상위 20개만
    maining.industry <- maining.industry %>% head(20)
    return(maining.industry)
  })
  
  output$main.industry <- renderPlot({
    req(maining.industry())
    main.ind <- maining.industry()
    ggplot(main.ind, aes(x = reorder(주요사업,n), y = n, label = n))+
      geom_col(position = "dodge") + 
      geom_text(position = position_dodge(width = 1),
                hjust = 0)+
      coord_flip() + xlab("주요사업") + ylab("빈도수")
  }, res = 96)
  
  #3. 상품명
  productcluster <- reactive({
    req(dated())
    #데이터 불러오기
    dating4 <- dated()
    
    product.data <- dating4 %>% select(contains("상품명"))
    product.data.vec <- as.vector(as.matrix(product.data))
    product.data.frame <- as.data.frame(as.matrix(product.data.vec))
    names(product.data.frame) <- "상품명"
    product.counting <- product.data.frame %>% count(상품명, sort = T)
    product.counting <- product.counting %>% filter(!is.na(상품명))
    #상위 20개만
    product.counting.20 <- product.counting %>% head(20)
    product.counting.20
    
    return(product.counting.20)
  })
  
  output$selproduct <- renderPlot({
    req(productcluster())
    selbar <- productcluster()
    ggplot(selbar, aes(x = reorder(상품명,n), y = n, label = n)) + 
      geom_col(position = "dodge") + 
      geom_text(position = position_dodge(width = 1),
                hjust = 0)+
      coord_flip() + xlab("상품명") + ylab("빈도수")
  }, res = 96)
  
  
  #### 재무정보 아웃풋 ####
  #1. 자본총계
  output$jabon.ker <- renderPlot({
    req(dated.f())
    #데이터 불러오기
    jabon <- dated.f()
    
    #2016년이랑 2022년 지우자
    jabon.table <- jabon %>% filter(결산일자 %in% finance.date)
    
    #outlier 지우기
    outlier <- boxplot(jabon.table$자본총계)
    f.point <- outlier$stats[1,1]
    e.point <- outlier$stats[5,1]
    jabon.table.out <- jabon.table %>% filter(자본총계 > f.point & 자본총계 < e.point)
    
    #자본총계의 커널밀도함수 그리기
    options(scipen = 7)
    ggplot(jabon.table.out, aes(자본총계, colour = as.factor(결산일자))) + 
      geom_density(adjust = 1, alpha = 0.1)  + labs(colour = "년도") + 
      xlab("자본총계(단위:백만원)") + 
      scale_x_continuous(labels = scales::comma, 
                         limits = c(min(jabon.table.out$자본총계), max(jabon.table.out$자본총계)))
  }, res = 96)
  
  #2. 매출액
  output$income.ker <- renderPlot({
    req(dated.f())
    #데이터 불러오기
    incoming <- dated.f()
    
    #2016년이랑 2022년 지우자
    incoming.table <- incoming %>% filter(결산일자 %in% finance.date)
    
    #outlier 지우기
    outlier <- boxplot(incoming.table$매출액)
    f.point <- outlier$stats[1,1]
    e.point <- outlier$stats[5,1]
    incoming.table.out <- incoming.table %>% filter(매출액 > f.point & 매출액 < e.point)
    
    #매출액의 커널밀도함수 그리기
    options(scipen = 7)
    ggplot(incoming.table.out, aes(매출액, colour = as.factor(결산일자))) + 
      geom_density(adjust = 1, alpha = 0.1) + labs(colour = "년도") + xlab("매출액(단위:백만원)") + 
      scale_x_continuous(labels = scales::comma, limits = c(min(incoming.table.out$매출액), max(incoming.table.out$매출액)))
  }, res = 96)
  
  #3. 영업활동후현금후름
  output$money.ker <- renderPlot({
    req(dated.f())
    #데이터 불러오기
    moneying <- dated.f()
    
    #2016년이랑 2022년 지우자
    moneying.table <- moneying %>% filter(결산일자 %in% finance.date)
    
    #outlier 지우기
    outlier <- boxplot(moneying.table$영업활동후현금흐름)
    f.point <- outlier$stats[1,1]
    e.point <- outlier$stats[5,1]
    moneying.table.out <- moneying.table %>% filter(영업활동후현금흐름 > f.point & 영업활동후현금흐름 < e.point)
    
    #영업활동후현금흐름의 커널밀도함수 그리기
    options(scipen = 7)
    ggplot(moneying.table.out, aes(영업활동후현금흐름, colour = as.factor(결산일자))) + 
      geom_density(adjust = 1, alpha = 0.1)  + labs(colour = "년도") + 
      xlab("영업활동후현금흐름(단위:백만원)") + 
      scale_x_continuous(labels = scales::comma, limits = c(min(moneying.table.out$영업활동후현금흐름), max(moneying.table.out$영업활동후현금흐름)))
  }, res = 96)
  
  
  #### 표준산업분류표 검색기능 ####
  #첫번째)표준산업분류#
  output$w <- DT::renderDataTable(
    datatable(tibble(대분류 = unique(industry.code.all$대분류)),options = list(dom = 'tp'), filter = list(position = "top"))
  )
  
  output$ww<- DT::renderDataTable(
    datatable(tibble(중분류 = unique(industry.code.all$중분류)),options = list(dom = 'tp'), filter = list(position = "top"))
  )
  
  output$www <- DT::renderDataTable(
    datatable(tibble(소분류 = unique(industry.code.all$소분류)),options = list(dom = 'tp'), filter = list(position = "top"))
  )
  
  output$wwww <- DT::renderDataTable(
    datatable(tibble(세분류 = unique(industry.code.all$세분류)),options = list(dom = 'tp'), filter = list(position = "top"))
  )
  
  output$wwwww <- DT::renderDataTable(
    datatable(tibble(세세분류 = unique(industry.code.all$세세분류)),options = list(dom = 'tp'), filter = list(position = "top"))
  )
  
  #두번째)표준산업분류 세부검색#
  #1. 대분류
  big.code <- reactive({
    req(input$select.big)
    filter(industry.code, 대분류 == input$select.big)
  })
  
  #2. 중분류
  observeEvent(big.code(),{
    choices <- unique(big.code()$중분류)
    updateSelectInput(inputId = "select.mid", choices = choices)
  })
  mid.code <- reactive({
    req(input$select.mid)
    filter(big.code(), 중분류 == input$select.mid)
  })
  
  #3. 소분류
  observeEvent(mid.code(),{
    choices <- unique(mid.code()$소분류)
    updateSelectInput(inputId = "select.small", choices = choices)
  })
  small.code <- reactive({
    req(input$select.small)
    filter(mid.code(), 소분류 == input$select.small)
  })
  
  #4. 세분류
  observeEvent(small.code(),{
    choices <- unique(small.code()$세분류)
    updateSelectInput(inputId = "select.se", choices = choices)
  })
  se.code <- reactive({
    req(input$select.se)
    filter(small.code(), 세분류 == input$select.se)
  })
  
  output$industry.table <- DT::renderDataTable(
    datatable(se.code(), options = list(dom = 'tp'))
  )
  
  
  
  #### 개요정보 파트 ####
  selecting.gaeyo <- reactive({
    req(dated())
    dated <- dated()
    
    if(input$select.gaeyo.inform %in% c("주요사업","매출처","상품명")){
      list.colum.gaeyo <- paste(input$select.gaeyo.inform, 1:5, sep = "")
      
      list.colum <- tibble(a = dated[[list.colum.gaeyo[1]]])
      list.colum <- rbind(list.colum, tibble(a = dated[[list.colum.gaeyo[2]]]))
      list.colum <- rbind(list.colum, tibble(a = dated[[list.colum.gaeyo[3]]]))
      list.colum <- rbind(list.colum, tibble(a = dated[[list.colum.gaeyo[4]]]))
      list.colum <- rbind(list.colum, tibble(a = dated[[list.colum.gaeyo[5]]]))
      list.colum <- na.omit(list.colum)
      
      selecting.gaeyo <- list.colum %>% count(list.colum[,1], sort = T) %>% head(20)
      return(selecting.gaeyo)
      
    }else{
      
      selecting.gaeyo <- dated %>% count(dated[,input$select.gaeyo.inform], sort = T)
      selecting.gaeyo <- na.omit(selecting.gaeyo)
      names(selecting.gaeyo)[1] <- "a"
      selecting.gaeyo <- head(selecting.gaeyo, 20) 
      
      return(selecting.gaeyo)
    }
  })
  
  selecting.gaeyo.list <- reactive({
    req(selecting.gaeyo())
    
    selecting.gaeyo <- selecting.gaeyo()
    
    selecting.gaeyo.list <- reorder(selecting.gaeyo$a,selecting.gaeyo$n)
    selecting.gaeyo.list <- levels(selecting.gaeyo.list)
    
    selecting.gaeyo.list <- data.frame(inventory = selecting.gaeyo.list,
                                       num = 1:length(selecting.gaeyo.list), stringsAsFactors = F)
    
    return(selecting.gaeyo.list)
  })
  
  color.gaeyo <- reactiveValues(tohighlight = rep(FALSE, 20),selectedbar = NULL)
  
  observeEvent(eventExpr = input$click.gaeyo,{
    selecting.gaeyo.list <- selecting.gaeyo.list()
    
    color.gaeyo$selectedbar <- selecting.gaeyo.list$inventory[round(input$click.gaeyo$y)]
    color.gaeyo$tohighlight <- selecting.gaeyo.list$inventory %in% color.gaeyo$selectedbar
  })
  
  output$gaeyo.bar <- renderPlot({
    selecting.gaeyo <- selecting.gaeyo()
    color.gaeyo.custom <- color.gaeyo
    color.gaeyo.custom$tohighlight <- color.gaeyo$tohighlight[1:dim(selecting.gaeyo)[1]]
    
    ggplot(selecting.gaeyo, aes(x = reorder(a,n),y = n, label = n,
                                fill = rev(ifelse(color.gaeyo.custom$tohighlight, yes = "yes", no = "no")))) +
      geom_col(position = "dodge") + 
      geom_text(position = position_dodge(width = 1),
                hjust = 0)+
      coord_flip() + xlab(input$select.gaeyo.inform) + ylab("빈도수") +
      scale_fill_manual(values = c("yes" = "blue", no = "grey"), guide = "none")
  },res = 96)
  
  
  selected.infor.gaeyo <- reactive({
    req(color.gaeyo)
    req(input$select.gaeyo.inform)
    req(dated())
    
    dated <- dated()
    selected.infor <- color.gaeyo$selectedbar
    
    if(input$select.gaeyo.inform %in% c("주요사업","매출처","상품명")){
      select.gaeyo.inform.list <- paste(input$select.gaeyo.inform, 1:5, sep = "")
      selected.dat.index <- c()
      selected.dat.index <- c(selected.dat.index, which(dated[[select.gaeyo.inform.list[1]]] %in% selected.infor))
      selected.dat.index <- c(selected.dat.index, which(dated[[select.gaeyo.inform.list[2]]] %in% selected.infor))
      selected.dat.index <- c(selected.dat.index, which(dated[[select.gaeyo.inform.list[3]]] %in% selected.infor))
      selected.dat.index <- c(selected.dat.index, which(dated[[select.gaeyo.inform.list[4]]] %in% selected.infor))
      selected.dat.index <- c(selected.dat.index, which(dated[[select.gaeyo.inform.list[5]]] %in% selected.infor))
      selected.dat.index <- unique(selected.dat.index)
      
      selected.dat.gaeyo <- dated[selected.dat.index,]
      selected.dat.gaeyo <- selected.dat.gaeyo %>% select(ID, 기업명, 사업자번호, `주요사업(사업목적)`, 종업원수, 개인법인구분, 공기업구분,
                                                          `상품명1`, `상품명2`,`상품명3`,`상품명4`,`상품명5`, `매출처1`,
                                                          `매출처2`,`매출처3`,`매출처4`,`매출처5`, 주소)
      return(selected.dat.gaeyo)
      
    }else{
      
      selected.dat.gaeyo <- which(dated[,input$select.gaeyo.inform] == selected.infor)
      selected.dat.gaeyo <- dated[selected.dat.gaeyo,]
      selected.dat.gaeyo <- selected.dat.gaeyo %>% select(ID, 기업명, 사업자번호, `주요사업(사업목적)`, 종업원수, 개인법인구분, 공기업구분,
                                                          `상품명1`, `상품명2`,`상품명3`,`상품명4`,`상품명5`, `매출처1`,
                                                          `매출처2`,`매출처3`,`매출처4`,`매출처5`, 주소)
      return(selected.dat.gaeyo) 
    }
  })
  
  output$gaeyo.table <- DT::renderDataTable({
    req(selected.infor.gaeyo())
    selected.infor.gaeyo <- selected.infor.gaeyo()
    selected.infor.gaeyo <- selected.infor.gaeyo %>% select(-`ID`)
    datatable(selected.infor.gaeyo)
  })
  
  
  #### 재무정보 ####
  observeEvent(input$extracting,{
    dated.f <- dated.f()
    choices <- unique(dated.f$결산일자)
    choices <- na.omit(choices)
    choices <- choices[choices != "2016" & choices != "2022"]
    choices <- as.numeric(choices)
    choices <- as.character(choices[order(choices)])
    updateSelectInput(inputId = "select.jaemu.year", label = "재무년도 선택", choices = choices)
  })
  
  selecting.jaemu <- reactive({
    req(dated.f())
    req(input$select.jaemu.year)
    dated.f <- dated.f()
    
    selecting.jaemu <- dated.f %>% filter(결산일자 %in% input$select.jaemu.year)
    selecting.jaemu <- selecting.jaemu[,c("ID", "결산일자",input$select.jaemu.inform)]
    names(selecting.jaemu)[3] <- "a"
    return(selecting.jaemu)
  })
  
  selecting.jaemu.out <- reactive({
    req(selecting.jaemu())
    req(input$select.jaemu.year)
    selecting.jaemu <- selecting.jaemu()
    
    year.uniq <- unique(selecting.jaemu$결산일자)
    
    #년도 별 이상치 범위를 뽑아내자
    outlier.range <- list()
    for(i in year.uniq){
      wichi <- which(i == year.uniq)
      spe.year.dat <- selecting.jaemu %>% filter(결산일자 == i)
      spe.boxplot <- boxplot(spe.year.dat$a)
      
      f.point <- spe.boxplot$stats[1,1]
      e.point <- spe.boxplot$stats[5,1]
      outlier.range[[wichi]] <- c(f.point, e.point)
    }
    
    selecting.jaemu.out.list <- list()
    for(j in year.uniq){
      wich <- which(j == year.uniq)
      ranging <- outlier.range[[wich]]
      
      dat.out <- selecting.jaemu %>% filter(결산일자 == j)
      dat.out <- dat.out %>% filter(!(a < ranging[1]) & !(a > ranging[2]))
      
      selecting.jaemu.out.list[[wich]] <- dat.out
    }
    
    selecting.jaemu.out <- tibble()
    
    for(m in 1:length(selecting.jaemu.out.list)){
      selecting.jaemu.out <- rbind(selecting.jaemu.out, selecting.jaemu.out.list[[m]])
    }
    
    return(selecting.jaemu.out)
  })
  
  output$jaemu.hist <- renderPlot({
    req(input$select.jaemu.inform)
    req(input$select.jaemu.outlier)
    req(selecting.jaemu())
    req(selecting.jaemu.out())
    
    if(input$select.jaemu.outlier == "포함"){
      selecting.jaemu <- selecting.jaemu()
      
      options(scipen = 7)
      ggplot(selecting.jaemu, aes(x = a, colour = 결산일자)) + 
        geom_density(adjust = 1, alpha = 0.1, fill = "grey") + 
        xlab(paste(input$select.jaemu.inform, "(단위:백만원)")) +
        scale_x_continuous(labels = scales::comma)
    }else{
      selecting.jaemu.out <- selecting.jaemu.out()
      
      options(scipen = 7)
      ggplot(selecting.jaemu.out, aes(x = a, colour = 결산일자)) + 
        geom_density(adjust = 1, alpha = 0.1, fill = "grey") + 
        xlab(paste(input$select.jaemu.inform, "(단위:백만원)")) + 
        scale_x_continuous(labels = scales::comma) 
    }
  },res = 96)
  
  brushing.jaemu <- reactive({
    req(input$brush.jaemu)
    req(input$select.jaemu.outlier)
    req(selecting.jaemu())
    req(selecting.jaemu.out())
    
    if(input$select.jaemu.outlier == "포함"){
      brushing.jaemu <- brushedPoints(selecting.jaemu(), input$brush.jaemu)
    }else{
      brushing.jaemu <- brushedPoints(selecting.jaemu.out(), input$brush.jaemu) 
    }
    
    return(brushing.jaemu)
  })
  
  brushing.data <- reactive({
    req(brushing.jaemu())
    req(dated.f())
    req(input$select.jaemu.year)
    brushing.jaemu <- brushing.jaemu()
    dated.f <- dated.f()
    
    brushing.data <- left_join(brushing.jaemu, dated.f, by = c("ID","결산일자"))
    brushing.data <- brushing.data %>% select(-`a`)
    brushing.data <- left_join(brushing.data, company.name.jaemu, by = "ID")
    brushing.data <- brushing.data %>% select(ID, 결산일자, 기업명, 유동자산:자본총계)
    
    return(brushing.data)
  })
  
  output$data.brush <- renderDataTable({
    req(brushing.data())
    
    brushing.data <- brushing.data()
    brushing.data <- brushing.data %>% select(-`ID`)
    
    datatable(brushing.data)
  })
  
  #### 가설검정 파트 #####
  observeEvent(input$extracting,{
    dated.f <- dated.f()
    choices <- unique(dated.f$결산일자)
    choices <- na.omit(choices)
    choices <- choices[choices != "2016" & choices != "2022"]
    choices <- as.numeric(choices)
    choices <- as.character(choices[order(choices)])
    updateSelectInput(inputId = "g1.s", label = "대상년도1", choices = choices)
    updateSelectInput(inputId = "g2.s", label = "대상년도2", choices = choices)
  })
  
  
  hypo.data <- reactive({
    req(dated.f())
    hypo.data <- dated.f()
    hypo.data <- hypo.data %>% select(ID, 결산일자, input$met)
    
    group1 <- hypo.data %>% filter(결산일자 %in% input$g1.s)
    group2 <- hypo.data %>% filter(결산일자 %in% input$g2.s)
    
    hypo.data <- inner_join(group1, group2, by = "ID")
    names(hypo.data)[2:5] <- c("a.date", "a.value", "b.date", "b.value") 
    
    return(hypo.data)
  })
  
  range <- reactive({
    req(hypo.data())
    hypo.data <- hypo.data()
    
    range.data <- c(hypo.data$a.value, hypo.data$b.value)
    outlier <- boxplot(range.data)
    f.point <- outlier$stats[1,1]
    e.point <- outlier$stats[5,1]
    
    range <- c(f.point, e.point)
    return(range)
  })
  
  output$g1plot <- renderPlot({
    req(range())
    req(hypo.data())
    
    range <- range()
    hypo.data <- hypo.data()
    
    g1data <- hypo.data %>% select(ID, a.date, a.value)
    
    ggplot(g1data, aes(a.value)) + 
      geom_density(adjust = 1, alpha = 0.1, color = "red", fill = "grey") + 
      xlab(paste(input$met, "(단위:백만원)")) + labs(title = "대상년도1") + 
      scale_x_continuous(labels = scales::comma, limits = c(range[1], range[2]))
  })
  
  output$g2plot <- renderPlot({
    req(range())
    req(hypo.data())
    
    range <- range()
    hypo.data <- hypo.data()
    
    g2data <- hypo.data %>% select(ID, b.date, b.value)
    
    ggplot(g2data, aes(b.value)) + 
      geom_density(adjust = 1, alpha = 0.1, color = "blue", fill = "grey") + 
      xlab(paste(input$met, "(단위:백만원)")) + labs(title = "대상년도2") + 
      scale_x_continuous(labels = scales::comma, limits = c(range[1], range[2]))
  })
  
  g1.summary <- reactive({
    req(hypo.data())
    hypo.data <- hypo.data()
    
    g1.summary <- tibble(표본수 = dim(hypo.data)[1],
                         최소값 = min(hypo.data$a.value),
                         중앙값 = median(hypo.data$a.value),
                         평균 = round(mean(hypo.data$a.value),1),
                         최대값 = max(hypo.data$a.value),
                         표준편차 = round(sd(hypo.data$a.value),1))
    return(g1.summary)
  })
  
  g2.summary <- reactive({
    req(hypo.data())
    hypo.data <- hypo.data()
    
    g2.summary <- tibble(표본수 = dim(hypo.data)[1],
                         최소값 = min(hypo.data$b.value),
                         중앙값 = median(hypo.data$b.value),
                         평균 = round(mean(hypo.data$b.value),1),
                         최대값 = max(hypo.data$b.value),
                         표준편차 = round(sd(hypo.data$b.value),1))
    return(g2.summary)
  })
  
  output$g1summary <- DT::renderDataTable({
    req(g1.summary())
    datatable(g1.summary(),options = list(dom = 't'))
  })
  
  output$g2summary <- DT::renderDataTable({
    req(g2.summary())
    datatable(g2.summary(),options = list(dom = 't'))
  })
  
  output$result.test <- renderPrint({
    req(hypo.data())
    hypo.data <- hypo.data()
    wilcox.test(hypo.data$a.value, hypo.data$b.value, paired = T, alternative = input$altern)
  })
  
  #### 다운로드 버튼 ####
  #1. 데이터 추출 파트 : input$download.basic
  
  shinyjs::disable("download.basic")
  
  observe({
    shinyjs::toggleState("download.basic", condition = req(dated()))
  })
  
  output$download.basic <- downloadHandler(
    filename = function(){
      "extraction.xlsx"
    },
    
    content = function(file){
      dated <- dated()
      export.dat <- raw.data %>% filter(ID %in% dated$ID)
      write.xlsx(export.dat, file)
    }
  )
  
  #2. 개요 정보 파트
  shinyjs::disable("download.gaeyo")
  
  observe({
    shinyjs::toggleState("download.gaeyo", condition = (dim(selected.infor.gaeyo())[1] > 0))
  })
  
  output$download.gaeyo <- downloadHandler(
    filename = function(){
      "summary.xlsx"
    },
    
    content = function(file){
      selected.infor.gaeyo <- selected.infor.gaeyo()
      export.dat <- raw.data %>% filter(ID %in% selected.infor.gaeyo$ID)
      export.dat <- export.dat %>% select(-`ID`)
      write.xlsx(export.dat, file)
    }
  )
  
  #3. 재무 정보 파트
  shinyjs::disable("download.jaemu")
  
  observe({
    shinyjs::toggleState("download.jaemu", condition = !is.null(input$brush.jaemu))
  })
  
  output$download.jaemu <- downloadHandler(
    filename = function(){
      "finance.xlsx"
    },
    
    content = function(file){
      brushing.data <- brushing.data()
      export.dat <- raw.data %>% filter(ID %in% brushing.data$ID)
      export.dat <- export.dat %>% select(-`ID`)
      write.xlsx(export.dat, file)
    }
  )
  
  #4. AI 파트
  # AI 정보 파트
  output$ai.infor <- renderText({
    req(input$ai.selecting)
    paste("◎ 정보 : 선택하신 AI는 ", input$ai.selecting, " 기업들의 재무정보를 코로나 전후로 예측합니다.", sep ="")
  })
  
  #(1). 입력한 데이터를 프레임으로 만든다.
  predicting.dat <- eventReactive(input$start.pred,{
    predicting.dat <- tibble(var1 = input$ai1*0.01,
                             var2 = input$ai2*0.01,
                             var3 = input$ai3*0.01,
                             var4 = input$ai4*0.01,
                             var5 = input$ai5*0.01,
                             var6 = input$ai6*0.01,
                             var7 = input$ai7*0.01,
                             var8 = input$ai8*0.01,
                             var9 = input$ai9*0.01,
                             var10 = input$ai10*0.01,
                             var11 = input$ai11*0.01,
                             var12 = input$ai12*0.01,
                             var13 = input$ai13*0.01,
                             var14 = input$ai14*0.01,
                             var15 = input$ai15*0.01,
                             var16 = input$ai16*0.01,
                             var17 = input$ai17*0.01,
                             var18 = input$ai18*0.01,
                             var19 = input$ai19*0.01,
                             var20 = input$ai20*0.01,
                             var21 = input$ai21*0.01,
                             var22 = input$ai22*0.01)
    names(predicting.dat) <- naming.ai.var
    return(predicting.dat)
  })
  
  ##곁가지로 데이터 정보 테이블을 만들어준다.
  output$now.predict.data <- renderDataTable({
    req(predicting.dat())
    predicting.dat <- predicting.dat()
    
    show.dat <- tibble(재무정보 = names(predicting.dat),
                       입력값 = paste(round(as.vector(as.matrix(predicting.dat)) * 100, 2), "%", sep = "")
    )
    datatable(show.dat, options = list(dom = 'tp'))
  })
  
  output$index.informing <- renderDataTable({
    datatable(index.infor)
  })
  
  #(2). 해당 데이터 대상 예측 시작
  predicting.result <- reactive({
    req(predicting.dat())
    req(input$ai.selecting)
    predicting.dat <- predicting.dat()
    
    
    #사용할 AI 선택!
    if(input$ai.selecting == "전체대상"){
      ai.now <- ai.list[[1]]
    }
    
    if(input$ai.selecting == "도매 및 상품 중개업"){
      ai.now <- ai.list[[2]]
    }
    
    if(input$ai.selecting == "소매업; 자동차 제외"){
      ai.now <- ai.list[[3]]
    }
    
    if(input$ai.selecting == "의복, 의복 액세서리 및 모피제품 제조업"){
      ai.now <- ai.list[[4]]
    }
    
    if(input$ai.selecting == "섬유제품 제조업; 의복 제외"){
      ai.now <- ai.list[[5]]
    }
    
    predicting.result <- predict(ai.now, predicting.dat, type = "prob")
    return(predicting.result)
  })
  
  before.result <- reactive({
    req(predicting.result())
    predicting.result <- predicting.result()
    
    before.result <- predicting.result[["이전"]]
    return(before.result)
  })
  
  after.result <- reactive({
    req(predicting.result())
    predicting.result <- predicting.result()
    
    after.result <- predicting.result[["이후"]]
    return(after.result)
  })
  
  output$before.resulting <- renderText({
    req(before.result())
    paste("△ 해당 재무정보가 코로나 이전의 재무일 확률은 ", round(before.result()*100,2), "%로 예측됩니다.", sep = "")
  })
  
  output$after.resulting <- renderText({
    req(after.result())
    paste("△ 해당 재무정보가 코로나 이후의 재무일 확률은 ", round(after.result()*100,2), "%로 예측됩니다.", sep = "")
  })
  
  # AI의 학습정보
  output$ai.performance <- renderPrint({
    req(input$ai.selecting)
    #사용할 AI 선택!
    if(input$ai.selecting == "전체대상"){
      ai.now <- ai.list[[1]]
    }
    
    if(input$ai.selecting == "도매 및 상품 중개업"){
      ai.now <- ai.list[[2]]
    }
    
    if(input$ai.selecting == "소매업; 자동차 제외"){
      ai.now <- ai.list[[3]]
    }
    
    if(input$ai.selecting == "의복, 의복 액세서리 및 모피제품 제조업"){
      ai.now <- ai.list[[4]]
    }
    
    if(input$ai.selecting == "섬유제품 제조업; 의복 제외"){
      ai.now <- ai.list[[5]]
    }
    
    training.dat <- ai.now$trainingData
    
    pred.training.data <- predict(ai.now, training.dat)
    confusionMatrix(pred.training.data, as.factor(training.dat$.outcome))
  })
  
  #AI의 변수중요도
  output$ai.variable.importance <- renderPlot({
    req(input$ai.selecting)
    #사용할 AI 선택!
    if(input$ai.selecting == "전체대상"){
      ai.now <- ai.list[[1]]
    }
    
    if(input$ai.selecting == "도매 및 상품 중개업"){
      ai.now <- ai.list[[2]]
    }
    
    if(input$ai.selecting == "소매업; 자동차 제외"){
      ai.now <- ai.list[[3]]
    }
    
    if(input$ai.selecting == "의복, 의복 액세서리 및 모피제품 제조업"){
      ai.now <- ai.list[[4]]
    }
    
    if(input$ai.selecting == "섬유제품 제조업; 의복 제외"){
      ai.now <- ai.list[[5]]
    }
    
    var_imp <- varImp(ai.now, scale = T)$importance
    var_imp <- data.frame(variables=row.names(var_imp),
                          importance=var_imp$Overall)
    
    var_imp %>%
      arrange(importance) %>%
      ggplot(aes(x=reorder(variables, importance), y=importance)) + 
      geom_bar(stat='identity') + 
      coord_flip() + 
      xlab('재무정보') + ylab('중요도') + 
      labs(title='AI가 생각하는 변수 중요도') + 
      theme_minimal() 
  }, res = 96)
}


#### 실행 ####
shinyApp(ui, server)

