#install.packages("shiny")
#install.packages("ggplot2")
#install.packages("dplyr")
#install.packages("DT")

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

#creating the UI layout with filter widgets of sliderinputs of the intervals (ranges) 
#of eviction rate and median household income, checkbox of trendline for the 
#scatter plot, and with select widget of select input of choice of year
ui <- fluidPage(
  titlePanel("Relationship between US States Eviction Rates and Median Household 
             Incomes by Year"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("eviction_rates_us_states_choice", label = "Eviction rates in 
                  each of the US states", min = eviction_rates_us_states_range[1],
                  max = eviction_rates_us_states_range[2], 
                  value = eviction_rates_us_states_range),
      sliderInput("median_household_income_choice", 
                  label = "Median household income in each of the US states", 
                  min = median_household_income_range[1], 
                  max = median_household_income_range[2], 
                  value = median_household_income_range),
      checkboxInput("smooth", label = strong("Show Trendline"), value = TRUE),
      selectInput("year_choice", label = "Year", choices = c(2000:2016))
    ),
    
    #output layout divide into three sections. First section is either a scatter
    #plot or table depending which tabs the user clicks on. The second section is
    #a data table on demand for user to select the specific data of interest. It
    #is for extra credit. The third section is for the reference of the data, which 
    #I used for this app. All of them separated with headings, vertical brakes, and 
    #summary paraghraphs
    mainPanel(
      h1("Graph/Table Visualization"),
      tabsetPanel(type = "tabs",
                  tabPanel("Plot", plotOutput("plot", click = "plot_click"),
                           br(),
                           verbatimTextOutput("state"),
                           textOutput("year", inline = TRUE)),
                  tabPanel("Table", tableOutput("table"),
                           br(),
                           p("The table above shows all of the US. States with 
                             their respective median household incomes in dollars
                             and eviction rates which falls within the user's 
                             selected range in the sliders and his or her choice 
                             of year from 2000 to 2016"))
    ),
    h2("Data Table on Demand"),
    DTOutput("original"),
    br(),
    p("The data table above show the",em("original data table"),"with only
                the name of the state and its repective median household income
                and eviction rate from the",strong("EvictionLabs website."),"The user can 
                specifically search for the interested information using the 
                data table on demand above. Notice that some information about
                eviction rate are missing."),
    h3("Citation of work"),
    p(strong("Reference:"),"This research uses data from The Eviction Lab at Princeton 
      University, a project directed by Matthew Desmond and designed by Ashley 
      Gromis, Lavar Edmonds, James Hendrickson, Katie Krywokulski, Lillian Leung,
      and Adam Porton. The Eviction Lab is funded by the JPB, Gates, and Ford 
      Foundations as well as the Chan Zuckerberg Initiative. More information is
      found at", a(href="https://evictionlab.org", "evictionlab.org"))
  )
)
)

shinyUI(ui)