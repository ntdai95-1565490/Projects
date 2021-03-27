#Load the necessary libraries:
library(shiny)
library(ggplot2)
library(dplyr)
library(DT)

#read the csv file, not letting strings as factors
eviction_rates_us_states <- read.csv("data/evictionlab-us-states.csv", 
                                     stringsAsFactors = FALSE)

#creating the intervals for eviction rate and median household income, lefting out
#NA values
eviction_rates_us_states_range <- range(eviction_rates_us_states$eviction.rate, 
                                        na.rm = TRUE)
median_household_income_range <- range(eviction_rates_us_states$median.household.income,
                                       na.rm = TRUE)

#definning the server function which filters out the dataset depending, the user's
#choice of intervals of eviction rate and median household income as well as his or
#her choice of year.
server <- function(input, output){
  filtered <- reactive({
    data <- eviction_rates_us_states %>%
      filter(eviction.rate > input$eviction_rates_us_states_choice[1] &
             eviction.rate < input$eviction_rates_us_states_choice[2]) %>%
      filter(median.household.income > input$median_household_income_choice[1] & 
             median.household.income < input$median_household_income_choice[2]) %>%
      filter(year == input$year_choice)
    
    return(data)
  })
  
  #creating the scatterplot with eviction rate on the x-axis and median household income
  #on the y-axis.Include the Trendline if the trendline checkbox is selected
  output$plot <- renderPlot({
    graph <- ggplot(data = filtered(), mapping = aes(x = eviction.rate, 
                                                     y = median.household.income),
                    color = "blue") +
      geom_point() +
      labs(title = "US states eviction rate compared to median household income",
           x = "Eviction rates", y = "Median Houshold Incomes of each states in 
           dollars")
    if(input$smooth) {
      graph <- graph + geom_smooth(se = FALSE)
    }
    return(graph)
  })
  
  #supporting the above scatterplot with the click option, when the user click on
  #one of the point on the graph the selected eviction rate on the x value and 
  #median household income in dollars on the y value will appear below the graph
  output$state <- renderText({
    paste0("x = ", input$plot_click$x, "\ny = ", input$plot_click$y)
  })
  
  #creating the output summary paragraph for the above scatterplot using the year
  #as a reactive expression as well as the intervals of eviction rate and median 
  #household income
  output$year <- renderText({
    return(paste("The graph above shows the data, with an option of showing the 
                 trendline, for",input$year_choice,"within the selected range of
                 median household income between",
                 input$median_household_income_choice[1],"and",
                 input$median_household_income_choice[2],"and eviction rate
                 between",input$eviction_rates_us_states_choice[1],"and",
                 input$eviction_rates_us_states_choice[2],"for each of the US. 
                 states. In addition, the user can click on the specific point on
                 the graph to see the related eviction rate on the x value and
                 median houshole income of that state on the y value below the 
                 graph."))
  })
  
  #creating and formatting the output filtered table according to the widgets of eviction rate,
  #median household income, and year of choice. Selecting and renaming the column names
  #of state, median household income in dollars, and eviction rate
  output$table <- renderTable({
    filtered_table <- select(filtered(),name,median.household.income,
                             eviction.rate)
    colnames(filtered_table)[1:3] <- c("US. State","Median Houeshold Income in 
                                       dollars","Eviction rate")
    return(filtered_table)
  })
  
  #creating the data table option for extra credit with the columns of the state
  #name, median household income in dollars, and eviction rate
  output$original = renderDT(
    select(eviction_rates_us_states,name,median.household.income,eviction.rate),
    options = list(lengthChange = FALSE)
  )
}

shinyServer(server)