library(ggplot2)
library(dplyr)
library(shiny)
library(markdown)

national <- read.csv("data/arrests_national.csv", stringsAsFactors = FALSE)
state_and_national <- read.csv("data/estimated_crimes.csv",
  stringsAsFactors = FALSE
)
state <- state_and_national[23:1144, ]

state_abbreviations <- unique(state$state_abbr, incomparables = FALSE)

juvenile_data <- read.csv("data/arrests_national_juvenile.csv",
  stringsAsFactors = FALSE
)
juvenile_data <- filter(juvenile_data, year == 2016) %>%
  filter(offense_name != "Curfew and Loitering Law Violations" & offense_name != "Runaway")

# UI of the app 
my_ui <-
  
  # Navbar Pages style for the app
  navbarPage(
    "Crimes in United States",
    tabPanel("Introduction", includeMarkdown("intro.md")),
    
    tabPanel(
      "Type of crimes by state",
      selectInput("state_choice",
        label = "Selected State",
        choices = state_abbreviations
      ),
      plotOutput("plot1", click = "plot_click"), br(),
      verbatimTextOutput("click1"), br(),
      htmlOutput("explanation", inline = TRUE)
    ),
    
    tabPanel(
      "Comparison in Juvenile and Adults Crime", br(),
      textOutput("intro_viz"), br(),
      selectInput("crimes",
        label = "Select Crimes",
        choices = juvenile_data["offense_name"]
      ),
      br(), textOutput("intro_to_graph")
      , br(),
      plotOutput("plot2"), br(),
      textOutput("conclusion_to_grph"), br(),
      sliderInput("year",
                  label = "Select Year",
                  min = 1994, 
                  max = 2016,
                  value = c(1994, 2016)
      ),
      br(),
      dataTableOutput("table_2")
    ),
    
    tabPanel(
      "National Arrests Data", textOutput("plot_info"),
      br(), plotOutput("plot3"), br(),
      selectInput("select_year", h3("Select Year"),
        choices = list(
          "1995" = 1995, "1996" = 1996, "1997" = 1997,
          "1998" = 1998,
          "1999" = 1999, "2000" = 2000,
          "2001" = 2001, "2002" = 2002, "2003" = 2003,
          "2004" = 2004, "2005" = 2005, "2006" = 2006,
          "2007" = 2007, "2008" = 2008, "2009" = 2009,
          "2010" = 2010, "2011" = 2011, "2012" = 2012,
          "2013" = 2013, "2014" = 2014,
          "2015" = 2015, "2016" = 2016, selected = 2000
        )
      ),
      br(), dataTableOutput("table_3")
    ),
    
    tabPanel(
      "DUI Against Various Theft Types",
      plotOutput("plot4"),
      textOutput("analysis_plot_4")
    ),
    
    tabPanel("Conclusion", includeMarkdown("conclusion.md"))
  )

shinyUI(my_ui)

