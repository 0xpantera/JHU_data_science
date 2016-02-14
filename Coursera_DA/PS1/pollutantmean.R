setwd("~/Documents/data_science/Coursera_DA/PS1/")

pollutantmean <- function(directory, pollutant, id = 1:332) {
    readPollutant <- function(directory, id) {
        read.csv(paste(directory, "/", sprintf("%03d", id), ".csv", sep=''))
    }
    
    data <- NA
    
    for(i in id) {
        csv <- readPollutant(directory, i)
        data <- rbind(data, csv)
    }
    
    mean(data[[pollutant]], na.rm = TRUE)
}

#Tests
pollutantmean("specdata", "sulfate", 1:10) == 4.064
pollutantmean("specdata", "nitrate", 70:72) == 1.706
pollutantmean("specdata", "nitrate", 23) == 1.281

