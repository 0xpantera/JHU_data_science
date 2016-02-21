
corr <- function(directory, threshold = 0) {
    readPollutant <- function(directory, id) {
        read.csv(paste(directory, "/", sprintf("%03d", id), ".csv", sep=''))
    }
    source("complete.R")
    
    com <- complete(directory)
    
    # subset the data.frame according to the threshold for the nobs
    data <- com[com$nobs > threshold, ]
    
    # result is a numeric vector
    result <- numeric(0)
    
    # for each data point, read CSV, calculate the cor and append to the result
    for(id in data$id) {
        csv <- readPollutant(directory, id)
        
        # logical vector of valid rows
        tf <- !is.na(csv$sulfate) & !is.na(csv$nitrate)
        
        # subset of valid rows
        x <- csv[tf, ]  
        
        result <- c(result, cor(x$sulfate, x$nitrate))
    }
    
    result
}

cr <- corr("specdata", 150)
head(cr)