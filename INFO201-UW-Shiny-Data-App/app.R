#install.packages("rsconnect")
library(rsconnect)

source("ui.R")
source("server.R")

#shinyapp.io account:
rsconnect::setAccountInfo(name='ngotandai',
                          token='FC5BB928F172A24328BCF9CD7B8E3E85',
                          secret='<SECRET>')
uiapp <- ui
serverapp <- server

shinyApp(uiapp = ui, serverapp = server)